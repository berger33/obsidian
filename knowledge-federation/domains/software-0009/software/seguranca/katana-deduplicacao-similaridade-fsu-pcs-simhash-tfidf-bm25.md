---
id: software.seguranca.tranche04.000365
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

# Katana: Deduplicação de URLs Paramétricas (`-fsu`, `-iqp`) e Similaridade de Conteúdo (`-pcs` SimHash/TF-IDF/BM25)

## Em uma frase
Para evitar *spider traps* (calendários infinitos, catálogos com milhares de produtos `/items/1` a `/items/99999` ou paginações redundantes), o `katana` combina filtragem de URLs estruturalmente similares (`-fsu`), descarte de query params repetidos (`-iqp`) e deduplicação por similaridade de conteúdo (`-pcs`).

## Por que importa
Sem deduplicação de similaridade, um crawler gasta 99% do seu orçamento de tempo (`-ct`) visitando milhares de páginas de produtos ou artigos que possuem exatamente o mesmo template de código no servidor.

## Como funciona
A flag `-fsu` (`-filter-similar`) detecta quando uma posição do caminho de URL recebe mais de `-fst 10` valores distintos (ex.: `/users/101`, `/users/102`...) e passa a tratá-la como parâmetro já coberto. Já `-pcs` (`-page-content-similar`) calcula *fingerprints* do conteúdo HTML via `simhash` (distância de Hamming `-pcsd 3`), `tfidf` ou `bm25` (`-pcst 0.85`), processando apenas `-pcsn 1` página por cluster de similaridade.

## Exemplo
```bash
# Evitar spider traps de catálogo filtrando URLs parametrizadas e páginas com SimHash similar
katana -u https://ecommerce.staging.corp \
  -d 4 -iqp \
  -fsu -fst 5 \
  -pcs -pcsm simhash -pcsd 3 -pcsn 1 \
  -mdp 1000 -o deduplicated-routes.txt
```

## Limites e trade-offs
Definir `-fst` muito baixo (ex.: `2`) em APIs onde o primeiro segmento de rota define módulos distintos (`/users`, `/orders`, `/billing`) pode fazer o filtro inferir erroneamente que o primeiro segmento é um ID dinâmico.

## Como verificar
Compare o tempo de execução e a contagem de linhas geradas com e sem `-fsu -pcs` em um portal com paginação extensa, confirmando a eliminação de rotas `/items/<id>` duplicadas.

## Conexões
- [[katana-preenchimento-formularios-aff-form-config-estrategias-visita]] — Veja também: Katana: Preenchimento Automático de Formulários (`-aff`, `-fc`), Extração (`-fx`) e Estratégias de Visita (`-s`).
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Veja também: Katana: Extração Estruturada de Campos (`-f`, `-sf`, `-em`, `-ef`) e `field-config.yaml` (`-flc`).
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Referência cruzada direta com katana-controle-escopo-field-scope-crawl-scope-out-of-scope.
- [[katana-rate-limiting-concorrencia-parallelism-delay-timeout-resume]] — Referência cruzada direta com katana-rate-limiting-concorrencia-parallelism-delay-timeout-resume.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
