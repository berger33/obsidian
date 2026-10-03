---
id: software.seguranca.tranche09.000865
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

# Wapiti para **APIs REST (`--swagger`)**: Auditoria Direta de Contratos **OpenAPI / Swagger** e Injeção de Payloads dentro de **Corpos JSON**

## Em uma frase
Aplicações modernas baseadas em microsserviços e SPAs frequentemente expõem APIs REST puras que retornam apenas `application/json` (sem páginas HTML nem tags `<a href>` ou `<form>`): se você apontar um crawler HTML tradicional para `https://api.exemplo.com/v1/`, ele não encontrará nenhuma rota para testar!

## Por que importa
Conforme mostra o `README.rst` e a dependência oficial **`wapiti-swagger`**, o Wapiti resolve a auditoria de APIs REST através da flag **`--swagger <url_ou_arquivo_openapi.json/yaml>`**!

## Como funciona
Quando você fornece o arquivo ou URL do contrato **OpenAPI (v2/v3) / Swagger** via `--swagger`, o Wapiti lê todas as rotas (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`), parâmetros de path/query/header e esquemas de corpo JSON, **e injeta os payloads de SQLi, NoSQLi, XSS, Command Injection, XXE e SSRF diretamente dentro dos atributos do corpo JSON (`application/json`)**!

## Exemplo
```bash
# Auditar uma API REST alimentando o Wapiti diretamente com a especificacao OpenAPI 3.0 (--swagger) e um token Bearer JWT
wapiti -u https://api.internal.corp/ \
  --swagger /cases/iac/api-contracts/openapi.yaml \
  -H "Authorization: Bearer eyJhbGciOiJFUzI1NiIs..." \
  -m "sql,exec,file,ssrf,xxe,http_headers" \
  -f json -o /cases/pentest/wapiti_openapi_dast.json
```

## Limites e trade-offs
Combine a análise estática do contrato OpenAPI no **KICS (`kics scan -t OpenAPI`)** com o teste dinâmico dos endpoints reais no **Wapiti (`wapiti --swagger openapi.yaml`)** para cobrir tanto falhas de especificação quanto vulnerabilidades de injeção na implementação!

## Como verificar
Verifique no log do backend de homologação que o Wapiti enviou requisições `POST`/`PUT` com `Content-Type: application/json` para todas as operações definidas no `openapi.yaml`.

## Conexões
- [[wapiti-varredura-autenticada-getcookie-form-script-cookies-ntlm]] — Veja também: Wapiti: Varredura Autenticada com **`wapiti-getcookie`**, Extração do Navegador (`--cookie`), **`--form-script`** e Autenticação HTTP (`Basic`/`Digest`/`NTLM`).
- [[wapiti-modulos-postura-csp-http-headers-cookieflags-csrf-ssl]] — Veja também: Wapiti: Módulos de Postura Defensiva (`csp`, `http_headers`, `cookieflags`, `csrf`, `https_redirect`, `methods` e `ssl`).
- [[wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos]] — Referência cruzada direta com wapiti-arquitetura-scanner-dast-black-box-httpx-asyncio-modulos.
- [[kics-auditoria-especificacoes-openapi-swagger-grpc-protobuf-apis]] — Referência cruzada direta com kics-auditoria-especificacoes-openapi-swagger-grpc-protobuf-apis.

## Fontes
- [Wapiti Official GitHub — Black-Box Web Vulnerability Scanner & 34 Attack Modules Reference](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/README.rst) — documentação oficial do Wapiti 3 cobrindo os 34 módulos de ataque, escopo de crawling, navegador headless Playwright, OpenAPI/Swagger e OAST; consultado em 2026-10-03.
- [Wapiti Official PyProject Specification — Async Architecture (`httpx`, `aiosqlite`, `playwright`, `mitmproxy`)](https://raw.githubusercontent.com/wapiti-scanner/wapiti/master/pyproject.toml) — especificação técnica oficial do Wapiti 3 (`pyproject.toml`) e seus utilitários `wapiti` e `wapiti-getcookie`; consultado em 2026-10-03.
- [Wapiti Official Project Portal & Documentation](https://wapiti-scanner.github.io/) — portal oficial de documentação do scanner de vulnerabilidades web Wapiti; consultado em 2026-10-03.
