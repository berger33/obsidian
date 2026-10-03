---
id: software.seguranca.tranche09.000866
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

# Wapiti: Módulos de Postura Defensiva (`csp`, `http_headers`, `cookieflags`, `csrf`, `https_redirect`, `methods` e `ssl`)

## Em uma frase
Além dos módulos ofensivos de injeção, o Wapiti possui sete módulos rápidos e não-intrusivos focados na **Postura de Segurança HTTP e Criptográfica** da aplicação: **`csp`**, **`http_headers`**, **`cookieflags`**, **`csrf`**, **`https_redirect`**, **`methods`** e **`ssl`**!

## Por que importa
O módulo **`csp` (*CSP Evaluator*)** analisa a política **Content-Security-Policy** em busca de diretivas inseguras como `'unsafe-inline'`, `'unsafe-eval'`, wildcards `*` em `script-src` ou ausência de `object-src`/`base-uri`; **`http_headers`** audita `Strict-Transport-Security`, `X-Frame-Options` e `X-Content-Type-Options`; e **`cookieflags`** verifica se todos os cookies possuem as flags `Secure`, `HttpOnly` e `SameSite`!

## Como funciona
Por sua vez, o módulo **`csrf`** analisa se os formulários HTML possuem tokens anti-CSRF imprevisíveis, e o módulo **`methods`** verifica se métodos HTTP perigosos (`PUT`, `DELETE`, `TRACE`, `CONNECT`) estão habilitados nas rotas.

## Exemplo
```bash
# Executar uma auditoria nao-intrusiva de postura HTTP (CSP, Security Headers, Cookies, CSRF e Redirecionamento HTTPS)
wapiti -u https://app.internal.corp/ \
  --scope domain --depth 3 \
  -m "csp,http_headers,cookieflags,csrf,https_redirect,methods" \
  -f json -o /cases/pentest/wapiti_posture_headers.json
```

## Limites e trade-offs
Esses 6 módulos (`csp,http_headers,cookieflags,csrf,https_redirect,methods`) não enviam payloads destrutivos de banco de dados e rodam em poucos segundos, sendo ideais como **Smoke Test de Segurança em todos os deploys de CI/CD**!

## Como verificar
Inspecione no JSON os alertas detalhados do avaliador `csp` para refinar a política Content-Security-Policy da aplicação.

## Conexões
- [[wapiti-varredura-apis-rest-openapi-swagger-json-payloads]] — Veja também: Wapiti para **APIs REST (`--swagger`)**: Auditoria Direta de Contratos **OpenAPI / Swagger** e Injeção de Payloads dentro de **Corpos JSON**.
- [[wapiti-modulos-cves-cms-wappalyzer-log4shell-spring4shell-takeover]] — Veja também: Wapiti: Módulos de Reconhecimento e CVEs Críticas (`wapp`, `cms`, `wp_enum`, `nikto`, `backup`, `buster`, `takeover`, `log4shell` e `spring4shell`).
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
