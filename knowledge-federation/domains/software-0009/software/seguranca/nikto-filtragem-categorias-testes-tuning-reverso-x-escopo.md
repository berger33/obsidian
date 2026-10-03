---
id: software.seguranca.tranche09.000852
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/sullo/nikto/master/README.md", "https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default", "https://github.com/sullo/nikto/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Nikto **`-Tuning`**: Seleção Cirúrgica de Categorias de Testes (`1`–`9`, `0`, `a`–`e`) e Operador de **Exclusão Reversa (`x`)**

## Em uma frase
Executar o Nikto padrão sem filtros dispara milhares de requisições cobrindo todas as categorias de testes, incluindo testes de injeção, *Remote File Retrieval* e até checagens de **Negação de Serviço (`6` — *Denial of Service*)** que não devem ser rodadas contra servidores de produção.

## Por que importa
A flag **`-Tuning <caracteres>`** do Nikto permite escolher exatamente quais classes de vulnerabilidade testar (ou excluir!): **`1`** (Arquivo interessante / visto em logs), **`2`** (Misconfiguration / Arquivo padrão), **`3`** (Information Disclosure), **`4`** (Injeção XSS/Script/HTML), **`5`** (Leitura de arquivo na raiz web), **`6`** (Denial of Service), **`7`** (Leitura de arquivo no servidor), **`8`** (Execução de Comando / Shell), **`9`** (SQL Injection), **`0`** (File Upload), **`a`** (Authentication Bypass), **`b`** (Identificação de Software), **`c`** (Remote Source Inclusion), **`d`** (WebService) e **`e`** (Console Administrativo)!

## Como funciona
Ainda mais útil: incluir a letra **`x` (*Reverse Tuning*)** inverte a lógica e executa **todos os testes EXCETO os caracteres especificados** — por exemplo, **`-Tuning x6`** roda todos os testes exceto *Denial of Service* (`6`)!

## Exemplo
```bash
# Auditar apenas Misconfigurations (2), Information Disclosure (3), Identificacao de Software (b) e Consoles Admin (e)
nikto -h https://app.internal.corp \
  -Tuning 23be \
  -ask no -nointeractive -nocheck \
  -o /cases/pentest/nikto_config_audit.json -Format json
```

## Limites e trade-offs
Em auditorias de homologação e produção onde você quer cobertura ampla sem risco de travar serviços legados, inclua sempre **`-Tuning x6`** para excluir explicitamente os testes da categoria `6` (*Denial of Service*).

## Como verificar
Compare o tempo de execução e o volume de requisições de `-Tuning 23be` (focado em configuração/exposição) frente ao scan completo.

## Conexões
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Veja também: **Nikto Web Server Scanner (`sullo/nikto`)**: Arquitetura de Plugins (`program/plugins/`), Bancos de Testes (`db_tests`, `udb_tests`) e `nikto.conf`.
- [[nikto-modos-mutacao-mutate-diretorios-usuarios-apache-cgiwrap]] — Veja também: Nikto **`-mutate` e `-Cgidirs`**: Descoberta Cruzada de Diretórios/Arquivos (`-mutate 1`), Enumeração Apache `/~user` (`-mutate 3`) e Diretórios CGI.
- [[nikto-selecao-plugins-macros-headers-outdated-robots-put-del]] — Referência cruzada direta com nikto-selecao-plugins-macros-headers-outdated-robots-put-del.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
