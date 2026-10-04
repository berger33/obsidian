---
id: software.seguranca.tranche04.000366
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

# Katana: Extração Estruturada de Campos (`-f`, `-sf`, `-em`, `-ef`) e `field-config.yaml` (`-flc`)

## Em uma frase
O motor de *Field Extraction* do `katana` permite formatar a saída ou filtrar os resultados por componentes específicos da URL (`url`, `path`, `fqdn`, `rdn`, `rurl`, `qurl`, `qpath`, `file`, `ufile`, `key`, `value`, `kv`, `dir`, `udir`) e por campos customizados baseados em regex (`-flc`).

## Por que importa
Permite extrair diretamente uma wordlist limpa de nomes de parâmetros (`-f key`), caminhos únicos de diretórios (`-f udir`) ou apenas URLs que possuem parâmetros de query (`-f qurl`) para alimentar fuzzers como `ffuf` ou scanners de injeção.

## Como funciona
Além dos campos nativos selecionados com `-f`, o analista pode definir extratores customizados em `~/.config/katana/field-config.yaml` (ou `-flc`) para capturar chaves de API, endereços de e-mail ou cabeçalhos específicos durante o crawl, enquanto `-ef png,jpg,css,ico` exclui extensões estáticas irrelevantes e `-em php,jsp,json` restringe a extensões de interesse.

## Exemplo
```bash
# Extrair apenas URLs que contêm query parameters (qurl) e gerar wordlist de chaves de parâmetros
katana -u https://app.staging.corp \
  -d 3 -jc -silent \
  -f qurl -o urls-with-params.txt

katana -u https://app.staging.corp \
  -d 3 -jc -silent \
  -f key | sort -u > custom-param-wordlist.txt
```

## Limites e trade-offs
Ao usar `-f key` ou `-f ufile`, linhas vazias são omitidas automaticamente, mas quando combinado com `-jsonl`, todos os campos extraídos permanecem aninhados no objeto JSON de cada requisição.

## Como verificar
Verifique `custom-param-wordlist.txt` e confirme que contém apenas identificadores de parâmetros únicos prontos para uso em `ffuf -w custom-param-wordlist.txt:PARAM`.

## Conexões
- [[katana-deduplicacao-similaridade-fsu-pcs-simhash-tfidf-bm25]] — Veja também: Katana: Deduplicação de URLs Paramétricas (`-fsu`, `-iqp`) e Similaridade de Conteúdo (`-pcs` SimHash/TF-IDF/BM25).
- [[katana-knowledge-base-classificacao-endpoints-segredos-kb]] — Veja também: Katana: Knowledge Base (`-kb`), Classificação de Endpoints REST/GraphQL (`-kb-endpoints`) e Detecção de Segredos (`-kb-secrets`).
- [[katana-analise-javascript-jc-jsluice-known-files-endpoints]] — Referência cruzada direta com katana-analise-javascript-jc-jsluice-known-files-endpoints.
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Referência cruzada direta com ffuf-fuzzing-parametros-get-post-json-headers-raw-request.
- [[httpxpd-extratores-customizados-er-ep-body-preview-redirect-chain]] — Referência cruzada direta com httpxpd-extratores-customizados-er-ep-body-preview-redirect-chain.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
