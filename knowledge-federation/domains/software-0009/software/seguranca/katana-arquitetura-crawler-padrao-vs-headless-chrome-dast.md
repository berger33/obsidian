---
id: software.seguranca.tranche04.000361
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md", "https://docs.projectdiscovery.io/opensource/katana/overview", "https://github.com/projectdiscovery/katana/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Katana: Arquitetura de Web Crawling e Spidering (Modo Standard HTTP vs Modo Headless Chrome `-hl`)

## Em uma frase
`katana` (ProjectDiscovery, MIT) é um framework de *web crawling* e *spidering* escrito em Go que opera tanto em modo **Standard** (análise rápida de respostas HTTP brutas) quanto em modo **Headless Híbrido** (`-hl` / `-headless`, instrumentando um navegador Chromium real via DevTools Protocol).

## Por que importa
Aplicações *Single-Page Application* (SPAs em React, Angular, Vue, Next.js) constroem o DOM e disparam chamadas XHR/Fetch dinamicamente no navegador; crawlers tradicionais sem motor JavaScript veem apenas uma página HTML vazia (`<div id="root"></div>`).

## Como funciona
No modo Standard, o `katana` analisa tags HTML (`href`, `src`, `form`, `action`), cabeçalhos e sitemaps com altíssima velocidade e baixo uso de CPU. Quando `-hl` (e `-system-chrome`) é ativado, o `katana` renderiza cada página no Chrome Headless, intercepta chamadas de rede geradas pelo frontend e segue eventos de navegação DOM até a profundidade máxima configurada (`-d`, padrão 3).

## Exemplo
```bash
# Executar crawling híbrido com Headless Chrome até profundidade 3 e limite de 5 minutos
katana -u https://app.staging.corp \
  -hl -system-chrome \
  -d 3 -ct 5m \
  -silent -o spa-endpoints.txt
```

## Limites e trade-offs
Em containers Docker ou Kubernetes sem privilégios de namespace de usuário, o Chrome Headless pode falhar ao iniciar o sandbox interno; utilize `-system-chrome` com perfil dedicado ou `-nos` (`--no-sandbox`) apenas em containers efêmeros estritamente isolados.

## Como verificar
Compare o número de rotas descobertas na SPA com e sem `-hl` e confirme a captura das chamadas de API `/api/v1/*` disparadas pelo bundle JavaScript.

## Conexões
- [[katana-analise-javascript-jc-jsluice-known-files-endpoints]] — Veja também: Katana: Parsing Estático de Arquivos JavaScript (`-jc` e `-jsl`) e Descoberta de `known-files` (`-kf`).
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Referência cruzada direta com katana-controle-escopo-field-scope-crawl-scope-out-of-scope.
- [[httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei]] — Referência cruzada direta com httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
