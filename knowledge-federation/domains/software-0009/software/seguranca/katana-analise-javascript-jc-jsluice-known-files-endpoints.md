---
id: software.seguranca.tranche04.000362
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

# Katana: Parsing Estático de Arquivos JavaScript (`-jc` e `-jsl`) e Descoberta de `known-files` (`-kf`)

## Em uma frase
Mesmo sem abrir um navegador Headless, o `katana` extrai rotas de API, parâmetros ocultos e URLs internas analisando estaticamente bundles JavaScript (`.js`, Webpack chunks, sourcemaps) através das flags `-jc` (`-js-crawl`) e `-jsl` (`-jsluice`), combinadas com `-kf all` (`robots.txt` e `sitemap.xml`).

## Por que importa
Bundles JavaScript de frontend frequentemente contêm todas as rotas da API administrativa (`/api/internal/users/export`, mutações GraphQL e flags de feature) mesmo para usuários não autenticados.

## Como funciona
A flag `-jc` aplica analisadores léxicos rápidos sobre todos os arquivos `.js` referenciados pela página, enquanto `-jsl` aciona o motor **jsluice** (baseado em árvore sintática tree-sitter para JavaScript) para resolver concatenações de strings, objetos de configuração e URLs parciais com precisão superior. Já `-kf all` (que requer `-d 3` ou maior) processa automaticamente `/robots.txt` e `/sitemap.xml`.

## Exemplo
```bash
# Extrair rotas de bundles JavaScript com jsluice e processar robots.txt/sitemap.xml
katana -u https://portal.staging.corp \
  -d 3 -jc -jsl -kf all \
  -ef woff,woff2,ttf,png,jpg,svg,css \
  -o js-discovered-routes.txt
```

## Limites e trade-offs
A análise AST do `-jsluice` (`-jsl`) consome significativamente mais memória RAM em bundles JavaScript minificados gigantes (>10 MB); combine com `-mrs 4194304` para limitar o tamanho máximo lido por resposta.

## Como verificar
Inspecione `js-discovered-routes.txt` e confirme a presença de endpoints REST/GraphQL extraídos de dentro dos arquivos `*.chunk.js`.

## Conexões
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Veja também: Katana: Arquitetura de Web Crawling e Spidering (Modo Standard HTTP vs Modo Headless Chrome `-hl`).
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Veja também: Katana: Controle Estrito de Escopo (`-fs`, `-cs`, `-cos`, `-do` e `-e`) para Prevenção de Fuga de Crawl.
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Referência cruzada direta com katana-extracao-campos-field-extraction-custom-regex-jsonl.
- [[katana-knowledge-base-classificacao-endpoints-segredos-kb]] — Referência cruzada direta com katana-knowledge-base-classificacao-endpoints-segredos-kb.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
