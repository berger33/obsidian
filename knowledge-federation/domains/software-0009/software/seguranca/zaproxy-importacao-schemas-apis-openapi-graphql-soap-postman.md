---
id: software.seguranca.tranche01.000044
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://www.zaproxy.org/docs/automate/automation-framework/", "https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md", "https://github.com/zaproxy/zaproxy"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ZAP Segurança de APIs (`openapi`, `graphql`, `soap` e `postman`): importação de contratos para DAST de APIs REST e GraphQL

## Em uma frase
Para testar APIs que não possuem interface HTML navegável por um spider, o Automation Framework do ZAP oferece jobs dedicados de importação de esquemas: **`openapi`** (arquivos ou URLs OpenAPI/Swagger v2 e v3), **`graphql`** (introspecção de endpoint ou arquivo `.graphql`), **`soap`** (arquivos WSDL) e **`postman`** (coleções Postman).

## Por que importa
Se você apontar apenas um spider HTML para um microserviço REST ou GraphQL que retorna JSON, o spider não descobrirá os endpoints `POST /v1/orders`, os parâmetros de query nem os tipos de payload esperados.

## Como funciona
Quando o job `openapi` importa a especificação (`apiFile` ou `apiUrl` com `targetUrl`), o ZAP popula automaticamente a *Sites Tree* com todos os caminhos, verbos HTTP e exemplos de parâmetros definidos no contrato, permitindo que o `activeScan` subsequente injete payloads de teste diretamente nos campos das requisições da API.

## Exemplo
```yaml
jobs:
  - type: openapi
    parameters:
      apiFile: "/zap/wrk/openapi.yaml"
      targetUrl: "https://api-staging.example.com"
      context: "staging-api"
  - type: graphql
    parameters:
      endpoint: "https://api-staging.example.com/graphql"
```

## Limites e trade-offs
Para endpoints GraphQL onde a introspecção está desabilitada em staging/produção por hardening, forneça o arquivo de schema local via parâmetro `schemaFile` no job `graphql`.

## Como verificar
Verifique nos logs de execução do job `openapi` a quantidade de URLs importadas para a *Sites Tree* antes do início do `activeScan`.

## Conexões
- [[zaproxy-descoberta-superficie-spider-spiderajax-spiderclient-spas]] — Veja também: ZAP Crawling e Descoberta (`spider`, `spiderAjax` e `spiderClient`): mapeamento de aplicações tradicionais e SPAs modernas.
- [[zaproxy-autenticacao-browser-auth-autodetect-replacer-bearer-tokens]] — Veja também: ZAP Autenticação no Automation Framework: `browser` auth, `autodetect` de sessão e injeção de tokens com o job `replacer`.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
