---
id: software.seguranca.tranche04.000356
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md", "https://docs.projectdiscovery.io/opensource/httpx/overview", "https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ProjectDiscovery `httpx`: Filtragem Avançada com Matchers (`-mc`, `-ms`, `-mr`, `-mfc`) e Filters (`-fc`, `-fs`, `-fr`, `-fcdn`)

## Em uma frase
O `httpx` dispõe de um motor completo de *Matchers* e *Filters* para selecionar ou descartar respostas HTTP por código de status (`-mc`/`-fc`), comprimento (`-ml`/`-fl`), contagem de linhas/palavras (`-mlc`/`-mwc`), substring (`-ms`/`-fs`), expressão regular (`-mr`/`-fr`), hash de favicon (`-mfc`/`-ffc`), provedor CDN (`-mcdn`/`-fcdn`) e tempo de resposta (`-mrt`/`-frt`).

## Por que importa
Permite isolar diretamente no pipeline os ativos de alto risco (ex.: páginas contendo `"Swagger UI"` ou `"GraphiQL"`, ou servidores retornando `401`/`403`/`500` fora de CDN) sem pós-processamento complexo.

## Como funciona
Além das flags individuais, as opções `-filter-condition` e `-match-condition` aceitam expressões DSL booleanas completas sobre os atributos da resposta (como `status_code==200 && contains(body, "openapi")` ou `!cdn && status_code!=404`), avaliando múltiplos critérios simultaneamente em tempo de execução.

## Exemplo
```bash
# Localizar especificações OpenAPI/Swagger ou GraphQL expostas diretamente na origem
httpx -l subdomains.txt \
  -path /swagger/index.html,/v3/api-docs,/graphql \
  -mc 200 \
  -mr "Swagger UI|openapi|__schema" \
  -json -o exposed-api-schemas.jsonl
```

## Limites e trade-offs
Combinar `-path` com uma lista de 50 caminhos em uma entrada de 10.000 subdomínios gera 500.000 requisições; use `-path` no `httpx` apenas para sondas cirúrgicas de poucos caminhos de alto valor e reserve wordlists grandes para o `ffuf`.

## Como verificar
Execute o comando e confirme com `jq -r '.url' exposed-api-schemas.jsonl` que todas as URLs retornadas satisfazem tanto `-mc 200` quanto a expressão regular `-mr`.

## Conexões
- [[httpxpd-captura-screenshots-headless-chrome-system-chrome-js]] — Veja também: ProjectDiscovery `httpx`: Triagem Visual em Escala com Screenshots Headless (`-ss`, `-system-chrome` e `-jsc`).
- [[httpxpd-extratores-customizados-er-ep-body-preview-redirect-chain]] — Veja também: ProjectDiscovery `httpx`: Extratores Regex (`-er`, `-ep`), Body Preview (`-bp`) e Cadeia de Redirecionamento (`-fr` / `- follow-redirects`).
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — Referência cruzada direta com ffuf-matchers-filters-status-size-words-lines-regex-time.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
