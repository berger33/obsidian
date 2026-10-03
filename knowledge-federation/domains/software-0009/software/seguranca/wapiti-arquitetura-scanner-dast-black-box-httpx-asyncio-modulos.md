---
id: software.seguranca.tranche09.000861
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
fontes: ["https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst", "https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml", "https://wapiti-scanner.github.io/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Wapiti 3 (`wapiti-scanner/wapiti`)**: Arquitetura do Scanner **DAST Black-Box** Assíncrono em Python (`httpx`, `aiosqlite`, `Playwright` e `mitmproxy`)

## Em uma frase
**Wapiti** (`wapiti-scanner/wapiti`, pacote PyPI `wapiti3`, licença GPLv2, criado por Nicolas Surribas) é um scanner de vulnerabilidades de aplicações web **Black-Box (DAST)** escrito em Python 3 moderno (`asyncio` sobre **`httpx[brotli,socks]`**, **`aiosqlite`**, **`sqlalchemy`**, **`playwright`** e **`mitmproxy`**).

## Por que importa
Diferente de scanners de infraestrutura como o Nikto (que apenas testam se arquivos estáticos existem no servidor), o Wapiti atua como um **Crawler + Fuzzer de Aplicação**: na **Fase 1 (Crawling/Browsing)** ele navega pela aplicação web extraindo links, formulários HTML5, parâmetros GET/POST/Multipart/JSON e rotas OpenAPI; e na **Fase 2 (Attack)** ele injeta payloads nos parâmetros descobertos para detectar vulnerabilidades reais no código da aplicação!

## Como funciona
Toda sessão de crawling e ataque do Wapiti é persistida automaticamente em um banco de dados **SQLite (`~/.wapiti/scans/`)**, permitindo pausar uma varredura com `Ctrl+C` e retomá-la depois sem refazer o crawling.

## Exemplo
```bash
# Verificar a versao do Wapiti 3 e listar todos os modulos de ataque disponiveis
wapiti --version
wapiti --list-modules
```

## Limites e trade-offs
Se você já realizou a fase de crawling (ou quer repetir apenas os testes de um módulo específico sobre as URLs já mapeadas no banco SQLite sem navegar pelo site tudo de novo), passe a flag **`--skip-crawl`**!

## Como verificar
Inspecione os arquivos de sessão SQLite gerados em `~/.wapiti/scans/` após uma execução de teste.

## Conexões
- [[wapiti-modulos-injecao-sql-timesql-xss-permanentxss-xxe-exec-file]] — Veja também: Wapiti (`-m` / `--module`): Módulos de Injeção Ativa (`sql`, `timesql`, `ldap`, `xss`, `permanentxss`, `exec`, `file`, `xxe`, `crlf` e `ssrf`).
- [[wapiti-controle-escopo-crawler-scope-depth-exclude-headless-playwright]] — Referência cruzada direta com wapiti-controle-escopo-crawler-scope-depth-exclude-headless-playwright.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
