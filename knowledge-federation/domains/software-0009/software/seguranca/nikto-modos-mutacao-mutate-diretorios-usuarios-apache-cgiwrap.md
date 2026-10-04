---
id: software.seguranca.tranche09.000853
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

# Nikto **`-mutate` e `-Cgidirs`**: Descoberta Cruzada de Diretórios/Arquivos (`-mutate 1`), Enumeração Apache `/~user` (`-mutate 3`) e Diretórios CGI

## Em uma frase
Além dos testes estáticos de `db_tests`, o Nikto possui um motor de **Mutação Combinatória (`-mutate <1..6>`)** e controle de diretórios CGI (**`-Cgidirs`**) que expandem a busca quando o servidor utiliza estruturas legadas.

## Por que importa
Conforme documentado no `README.md` oficial, os seis modos de `-mutate` são: **`1`** (testa todos os arquivos combinados com todos os diretórios raiz), **`2`** (adivinha nomes de arquivos de senhas), **`3`** (enumera nomes de usuários Unix do sistema via **`Apache UserDir /~usuario`**!), **`4`** (enumera usuários via `/cgi-bin/cgiwrap/~usuario`), **`5`** (tenta força bruta de subdomínios) e **`6`** (adivinha nomes de diretórios a partir de um arquivo de dicionário passado em **`-mutate-options`**).

## Como funciona
Por sua vez, a flag **`-Cgidirs`** aceita **`none`** (para pular completamente os milhares de testes `/cgi-bin/` em servidores modernos Node.js/Go/Python que não usam CGI!), **`all`** ou uma lista customizada (`-Cgidirs "/cgi/ /scripts/"`)!

## Exemplo
```bash
# Executar o Nikto em uma API moderna desativando testes de CGI legados (-Cgidirs none) para acelerar a varredura em 5x
nikto -h https://api.internal.corp \
  -Cgidirs none \
  -Tuning 23ab \
  -ask no -nointeractive -nocheck \
  -o /cases/pentest/nikto_modern_api.json
```

## Limites e trade-offs
Dica de ouro de performance: ao auditar aplicações modernas (React/Next.js, FastAPI, Spring Boot, Go, .NET Core), passar **`-Cgidirs none`** elimina milhares de requisições inúteis para `/cgi-bin/*.cgi` dos anos 2000 e reduz o tempo do Nikto de 15 minutos para menos de 1 minuto!

## Como verificar
Verifique no servidor Apache se o módulo `mod_userdir` (`/~root`, `/~www-data`) está desativado para mitigar o `-mutate 3`.

## Conexões
- [[nikto-filtragem-categorias-testes-tuning-reverso-x-escopo]] — Veja também: Nikto **`-Tuning`**: Seleção Cirúrgica de Categorias de Testes (`1`–`9`, `0`, `a`–`e`) e Operador de **Exclusão Reversa (`x`)**.
- [[nikto-tecnicas-evasao-ids-waf-libwhisker-evasion-deteccao]] — Veja também: Nikto **`-evasion`**: As 10 Técnicas de Codificação HTTP **LibWhisker** (`1`–`8`, `A`, `B`) para Teste de Regras de Normalização de **IDS / WAF**.
- [[nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins]] — Referência cruzada direta com nikto-arquitetura-web-server-scanner-libwhisker-databases-plugins.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
