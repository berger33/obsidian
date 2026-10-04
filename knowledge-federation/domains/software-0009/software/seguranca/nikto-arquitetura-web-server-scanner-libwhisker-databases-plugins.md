---
id: software.seguranca.tranche09.000851
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

# **Nikto Web Server Scanner (`sullo/nikto`)**: Arquitetura de Plugins (`program/plugins/`), Bancos de Testes (`db_tests`, `udb_tests`) e `nikto.conf`

## Em uma frase
**Nikto** (`sullo/nikto`, licença GPLv2, mantido por Chris Sullo / CIRT.net) é o scanner open-source clássico de auditoria de servidores web, projetado para identificar rapidamente mais de **7.000 arquivos/programas CGI potencialmente perigosos**, versões desatualizadas de mais de 1.250 servidores HTTP (Apache, Nginx, IIS, Tomcat, Jetty, Lighttpd) e problemas de configuração de segurança e cabeçalhos.

## Por que importa
A arquitetura do Nikto é dividida entre o motor HTTP (baseado em **LibWhisker2 / `LW2.pm`** e `Net::SSLeay` com reutilização de conexão `SSLKEEPALIVE`), o diretório de **Plugins (`program/plugins/`)** e os bancos de dados tabulares em **`program/databases/`** (`db_tests`, `db_headers`, `db_outdated`, `db_variables`, `db_404_strings`).

## Como funciona
Para adicionar verificações exclusivas da sua organização sem correr o risco de perdê-las em uma atualização do Git, o Nikto suporta **Bancos de Dados de Usuário (`udb_tests`, `udb_variables`)** e a flag **`-dbcheck`**, que valida a sintaxe de todas as tabelas de testes antes do scan!

## Exemplo
```bash
# Verificar a versao do Nikto, listar os plugins carregados e checar a integridade sintatica dos bancos de testes (-dbcheck)
nikto -Version
nikto -dbcheck
```

## Limites e trade-offs
Conforme instrui o arquivo oficial `nikto.conf.default`, defina **`UPDATES=no`** e **`PROMPTS=no`** (ou passe **`-ask no -nointeractive -nocheck`** na linha de comando) em ambientes corporativos para que o Nikto nunca faça prompts interativos nem envie strings de versão desconhecidas para servidores externos!

## Como verificar
Execute `nikto -list-plugins` para inspecionar todos os plugins e macros (`@@DEFAULT`, `@@EXTRAS`) disponíveis na sua instalação.

## Conexões
- [[nikto-filtragem-categorias-testes-tuning-reverso-x-escopo]] — Veja também: Nikto **`-Tuning`**: Seleção Cirúrgica de Categorias de Testes (`1`–`9`, `0`, `a`–`e`) e Operador de **Exclusão Reversa (`x`)**.
- [[nikto-modos-mutacao-mutate-diretorios-usuarios-apache-cgiwrap]] — Referência cruzada direta com nikto-modos-mutacao-mutate-diretorios-usuarios-apache-cgiwrap.
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.

## Fontes
- [Nikto Official GitHub — Web Server Scanner CLI Reference, Tuning & Mutate Modes](https://raw.githubusercontent.com/sullo/nikto/master/README.md) — documentação oficial do Nikto cobrindo categorias `-Tuning` (incluindo exclusão `x`), modos `-mutate`, técnicas `-evasion` e formatos de saída; consultado em 2026-10-03.
- [Nikto Official Default Configuration Reference (`nikto.conf.default`)](https://raw.githubusercontent.com/sullo/nikto/master/program/nikto.conf.default) — arquivo oficial de configuração `nikto.conf.default` cobrindo macros `@@DEFAULT`, `STATIC-COOKIE`, `SKIPIDS`, banco SQL e opções LibWhisker; consultado em 2026-10-03.
- [Nikto Official Project Wiki — Plugins, Databases & Reporting](https://github.com/sullo/nikto/wiki) — wiki oficial do projeto Nikto cobrindo estrutura dos bancos `db_tests`/`udb_tests` e plugins; consultado em 2026-10-03.
