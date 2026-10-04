---
id: software.seguranca.tranche01.000043
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

# ZAP Crawling e Descoberta (`spider`, `spiderAjax` e `spiderClient`): mapeamento de aplicações tradicionais e SPAs modernas

## Em uma frase
No Automation Framework do ZAP, três jobs complementares constroem a árvore de endpoints (*Sites Tree*) da aplicação antes da varredura: **`spider`** (crawler HTTP tradicional ultra-rápido que analisa HTML/links), **`spiderAjax`** (crawler baseado em navegador real headless via Selenium/Firefox/Chrome que clica em elementos DOM) e **`spiderClient`** (integração moderna client-side).

## Por que importa
Em Single-Page Applications (React, Vue, Angular), um crawler HTTP tradicional (`spider`) recebe apenas um `<div id="root"></div>` e um bundle `.js`, não descobrindo nenhuma rota renderizada dinamicamente via JavaScript no navegador.

## Como funciona
Combinar o job `spider` (com `maxDuration: 2` minutos para mapear rapidamente links estáticos, `robots.txt` e `sitemap.xml`) seguido do job `spiderAjax` (para exercitar eventos JavaScript e chamadas `fetch`/`XHR`) garante cobertura completa tanto de páginas SSR quanto de componentes SPA.

## Exemplo
```yaml
jobs:
  - type: spider
    parameters:
      context: "staging-web"
      maxDuration: 2
  - type: spiderAjax
    parameters:
      context: "staging-web"
      maxDuration: 5
      browserId: "firefox-headless"
```

## Limites e trade-offs
Defina sempre `excludePaths` no `context` (por exemplo rotas `/logout` ou `/signout`) antes de rodar o `spider` ou `spiderAjax` autenticado, para evitar que o crawler clique no botão de logout no primeiro segundo e invalide a própria sessão!

## Como verificar
Adicione um teste `stats` no job `spider` validando que `stats.spider.urls.added` encontrou pelo menos o número mínimo esperado de URLs.

## Conexões
- [[zaproxy-automation-framework-yaml-env-jobs-substituicao-packaged-scans]] — Veja também: ZAP Automation Framework (`zap.sh -cmd -autorun`): controle declarativo em arquivo YAML único para CI/CD.
- [[zaproxy-importacao-schemas-apis-openapi-graphql-soap-postman]] — Veja também: ZAP Segurança de APIs (`openapi`, `graphql`, `soap` e `postman`): importação de contratos para DAST de APIs REST e GraphQL.

## Fontes
- [OWASP ZAP Official Documentation — Automation Framework (Declarative YAML Plan, env Contexts, Discovery/Scan/Report Jobs & Job Tests)](https://www.zaproxy.org/docs/automate/automation-framework/) — Documentação oficial do Automation Framework do OWASP ZAP detalhando a estrutura YAML env/jobs, substituição dos Packaged Scans e lista completa de jobs suportados; consultado em 2026-10-03.
- [OWASP ZAP GitHub — README.md (Zed Attack Proxy Architecture, Passive & Active Scanners, Container Images & Add-ons)](https://raw.githubusercontent.com/zaproxy/zaproxy/main/README.md) — README oficial do zaproxy/zaproxy apresentando o projeto DAST open-source, modos de execução headless e ecossistema de extensões; consultado em 2026-10-03.
- [OWASP ZAP — Official GitHub Repository](https://github.com/zaproxy/zaproxy) — Repositório oficial Apache-2.0 do OWASP Zed Attack Proxy; consultado em 2026-10-03.
