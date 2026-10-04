---
id: software.seguranca.tranche09.000870
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

# Wapiti: Geração de Relatórios (**`-f html,json,xml,md,csv,txt`**), Encaminhamento via Proxy (**`-p` `mitmproxy` / ZAP**) e Pipelines DevSecOps

## Em uma frase
O Wapiti gera relatórios executivos e técnicos em seis formatos nativos selecionados por **`-f` / `--format`**: **`html`** (relatório visual interativo com gráficos por severidade e abas com a requisição HTTP bruta e o comando `curl` de cada achado), **`json`**, **`xml`**, **`md`** (Markdown pronto para anexar em Issues/Pull Requests do GitHub/GitLab!), **`csv`** e **`txt`**.

## Por que importa
Quando você precisa depurar como a aplicação está respondendo aos payloads do Wapiti ou precisa que um addon Python assine cada requisição em tempo real (ex.: recalculando cabeçalhos HMAC), basta passar **`-p http://127.0.0.1:8080`** (`--proxy`, suportando `http://`, `https://` e `socks5://`) combinado com **`--no-bugreport`** e **`-k`** (`--insecure`, para aceitar a CA do **`mitmproxy`**)!

## Como funciona
Tanto o formato `xml` quanto `json` do Wapiti são importados nativamente pelo **OWASP DefectDojo** (`"Wapiti Scan"`).

## Exemplo
```bash
# Executar o Wapiti encaminhando o trafego pelo mitmproxy local (-p, -k) e gerando relatorio em Markdown (-f md) para PR/Issue
wapiti -u https://app.internal.corp/ \
  --proxy http://127.0.0.1:8080 --insecure \
  --flush-session \
  -m "sql,xss,csp,http_headers,cookieflags" \
  -f md -o /cases/pentest/wapiti_summary.md
```

## Limites e trade-offs
Para que um pipeline de CI/CD falhe automaticamente quando o Wapiti encontrar vulnerabilidades, analise o JSON gerado com `jq '[.vulnerabilities[][] ] | length' relatorio.json` (se `> 0`, retorne exit code `1`).

## Como verificar
Abra o relatório Markdown `/cases/pentest/wapiti_summary.md` ou inspecione os fluxos no `mitmproxy` para reproduzir cada achado com o comando `curl` fornecido pelo Wapiti.

## Conexões
- [[wapiti-performance-tasks-concorrentes-timeouts-persistencia-sqlite]] — Veja também: Wapiti: Ajuste de Concorrência Assíncrona (**`--tasks`**), Timeouts (`-t`, `--max-scan-time`, `--max-attack-time`) e Sessões SQLite (`--store-session`).
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Referência cruzada direta com mitmproxy-automacao-addons-python-request-response-websocket-hooks.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
