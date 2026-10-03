---
id: software.seguranca.tranche04.000367
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

# Katana: Knowledge Base (`-kb`), Classificação de Endpoints REST/GraphQL (`-kb-endpoints`) e Detecção de Segredos (`-kb-secrets`)

## Em uma frase
O módulo *Knowledge Base* do `katana` (`-kb`) utiliza classificadores embarcados e extratores semânticos para categorizar tipos de páginas e formulários, classificar endpoints de API (`-kb-endpoints`: REST, GraphQL, SOAP, XHR) e detectar segredos expostos no código cliente (`-kb-secrets`).

## Por que importa
Acelera a triagem de segurança ao separar automaticamente páginas estáticas institucionais de formulários de autenticação, endpoints GraphQL e bundles JavaScript contendo tokens de API vazados.

## Como funciona
Quando `-kb -kb-endpoints -kb-secrets` é habilitado com `-jsonl`, cada registro emitido pelo `katana` recebe metadados de classificação indicando a natureza da rota e quaisquer credenciais candidatas encontradas no corpo ou nos scripts da página.

## Exemplo
```bash
# Executar crawl com classificação de endpoints de API e detecção passiva de segredos em JSONL
katana -u https://app.staging.corp \
  -d 3 -jc -kb -kb-endpoints -kb-secrets \
  -jsonl -o kb-classified-crawl.jsonl
```

## Limites e trade-offs
A flag experimental `-kb-validate-secrets` envia chamadas de API ativas para os provedores externos a fim de testar se um segredo encontrado é válido; **não** habilite `-kb-validate-secrets` sem autorização explícita no ROE, pois gera tráfego externo usando credenciais de terceiros.

## Como verificar
Filtre o arquivo gerado com `jq -c 'select(.knowledge_base != null)' kb-classified-crawl.jsonl` para revisar os endpoints classificados e alertas de segredos.

## Conexões
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Veja também: Katana: Extração Estruturada de Campos (`-f`, `-sf`, `-em`, `-ef`) e `field-config.yaml` (`-flc`).
- [[katana-crawling-autenticado-headers-cookies-chrome-ws-url]] — Veja também: Katana: Crawling Autenticado com Headers/Cookies (`-H`), Sessão de Navegador (`-cdd`) e Chrome DevTools (`-cwu`).
- [[katana-analise-javascript-jc-jsluice-known-files-endpoints]] — Referência cruzada direta com katana-analise-javascript-jc-jsluice-known-files-endpoints.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
