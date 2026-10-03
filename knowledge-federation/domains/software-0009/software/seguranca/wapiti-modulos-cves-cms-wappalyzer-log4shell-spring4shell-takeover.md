---
id: software.seguranca.tranche09.000867
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

# Wapiti: Módulos de Reconhecimento e CVEs Críticas (`wapp`, `cms`, `wp_enum`, `nikto`, `backup`, `buster`, `takeover`, `log4shell` e `spring4shell`)

## Em uma frase
Para unir fingerprinting de componentes com detecção de vulnerabilidades conhecidas, o Wapiti inclui módulos especializados de superfície: **`wapp`** (identifica tecnologias, frameworks e versões usando a base **Wappalyzer** e correlaciona com CVEs conhecidas!), **`cms`** (detecta versões e módulos de WordPress, Drupal, Joomla, Magento, SPIP, Typo3), **`wp_enum`** (enumera plugins e temas WordPress), **`backup`** (procura cópias `.bak`, `.old`, `.tar.gz`, `.swp` de scripts) e **`buster`** (enumeração estilo DirBuster).

## Por que importa
Além disso, o Wapiti possui detectores dedicados para vulnerabilidades críticas de infraestrutura e nuvem: **`log4shell`** (`CVE-2021-44228` JNDI injection em cabeçalhos e parâmetros), **`spring4shell`** (`CVE-2022-22965` ClassLoader manipulation), **`shellshock`** (`CVE-2014-6271`) e **`takeover`** (detecção de **Subdomain Takeover**)!

## Como funciona
Você pode atualizar o banco local de assinaturas do Wappalyzer e Nikto usado pelo Wapiti executando **`wapiti --update`**.

## Exemplo
```bash
# Atualizar as bases locais (Wappalyzer/Nikto) do Wapiti e auditar tecnologias, backups de scripts e Subdomain Takeover
wapiti --update
wapiti -u https://app.internal.corp/ \
  -m "wapp,backup,takeover,htaccess,http_headers" \
  -f json -o /cases/pentest/wapiti_tech_backups.json
```

## Limites e trade-offs
Note que o módulo `wapp` é puramente informativo (não envia payloads de ataque): rodá-lo com `-m wapp` sobre uma aplicação mapeia toda a pilha tecnológica (servidor web, framework backend, bibliotecas JavaScript e versões) e lista as CVEs associadas àquelas versões.

## Como verificar
Verifique na seção `infos` e `vulnerabilities` do JSON as tecnologias identificadas pelo módulo `wapp`.

## Conexões
- [[wapiti-modulos-postura-csp-http-headers-cookieflags-csrf-ssl]] — Veja também: Wapiti: Módulos de Postura Defensiva (`csp`, `http_headers`, `cookieflags`, `csrf`, `https_redirect`, `methods` e `ssl`).
- [[wapiti-deteccao-out-of-band-ssrf-xxe-log4shell-endpoint-customizado]] — Veja também: Wapiti **Out-of-Band (OAST / `--external-endpoint`)**: Detecção de **Blind SSRF**, **Blind XXE** e **Log4Shell** com Endpoint Externo Próprio.
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
