---
id: software.seguranca.tranche09.000868
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

# Wapiti **Out-of-Band (OAST / `--external-endpoint`)**: Detecção de **Blind SSRF**, **Blind XXE** e **Log4Shell** com Endpoint Externo Próprio

## Em uma frase
Vulnerabilidades **Cegas (*Blind*)** — como **Blind SSRF** (onde o backend faz uma requisição HTTP interna ou DNS sem devolver o corpo da resposta ao usuário), **Blind XXE** e **Log4Shell (`${jndi:ldap://...}`)** — não podem ser detectadas apenas olhando a resposta HTTP imediata: o scanner precisa injetar uma URL apontando para um **Servidor Externo de Callback (*Out-of-Band Endpoint*)** e verificar depois se o servidor alvo conectou naquele endpoint!

## Por que importa
Por padrão, os módulos `ssrf`, `xxe` e `log4shell` do Wapiti utilizam um endpoint externo do projeto Wapiti; porém, em **pentests corporativos confidenciais ou em redes internas isoladas sem saída para a internet**, você **não** deve usar um endpoint público externo (quer por confidencialidade dos IPs/URLs internas, quer porque o servidor alvo interno não alcança a internet!).

## Como funciona
Para manter 100% do tráfego dentro do seu controle, o Wapiti permite configurar seu próprio servidor de callback usando as flags **`--external-endpoint <URL>`** e **`--internal-endpoint <URL>`**!

## Exemplo
```bash
# Executar os modulos de SSRF e XXE apontando para um endpoint de callback interno controlado pela equipe de Pentest
wapiti -u https://app.internal.corp/ \
  -m "ssrf,xxe" \
  --external-endpoint http://oast.pentest.internal.corp/ \
  --internal-endpoint http://oast.pentest.internal.corp/ \
  -f json -o /cases/pentest/wapiti_oast_results.json
```

## Limites e trade-offs
Nunca execute os módulos `ssrf`, `xxe` ou `log4shell` em engajamentos confidenciais de clientes sem antes apontar `--external-endpoint` para uma infraestrutura de callback privada da sua equipe de segurança (ou desativá-los se não houver servidor OAST autorizado no ROE).

## Como verificar
Verifique nos logs do seu servidor OAST interno quais parâmetros da aplicação dispararam lookups DNS ou requisições HTTP.

## Conexões
- [[wapiti-modulos-cves-cms-wappalyzer-log4shell-spring4shell-takeover]] — Veja também: Wapiti: Módulos de Reconhecimento e CVEs Críticas (`wapp`, `cms`, `wp_enum`, `nikto`, `backup`, `buster`, `takeover`, `log4shell` e `spring4shell`).
- [[wapiti-performance-tasks-concorrentes-timeouts-persistencia-sqlite]] — Veja também: Wapiti: Ajuste de Concorrência Assíncrona (**`--tasks`**), Timeouts (`-t`, `--max-scan-time`, `--max-attack-time`) e Sessões SQLite (`--store-session`).
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.
- [[wapiti-modulos-injecao-sql-timesql-xss-permanentxss-xxe-exec-file]] — Referência cruzada direta com wapiti-modulos-injecao-sql-timesql-xss-permanentxss-xxe-exec-file.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
