---
id: software.seguranca.tranche04.000370
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

# Katana: Integração em Pipelines DAST com Proxy de Auditoria (`-proxy`), `nuclei` e `ffuf`

## Em uma frase
O `katana` funciona como o motor de descoberta de rotas e parâmetros para scanners de vulnerabilidades e proxies DAST: suas URLs parametrizadas alimentam templates DAST do `nuclei` (`nuclei -dast`) ou o tráfego inteiro do crawl pode ser encaminhado em tempo real por um proxy (`-proxy http://127.0.0.1:8080`) para popular a árvore de sites do OWASP ZAP / Caido.

## Por que importa
Scanners DAST frequentemente têm crawlers lentos ou limitados para SPAs modernas; usar o `katana` (com `-hl -jc -aff`) através da flag `-proxy` popula passivamente 100% das rotas e chamadas XHR dentro do motor de análise do ZAP.

## Como funciona
Em pipelines totalmente automatizados de CI/CD, o `katana` exporta as rotas descobertas com query parameters (`-f qurl`) ou o log JSONL completo (que preserva método HTTP, cabeçalhos e corpo `POST` dos formulários extraídos) para alimentar diretamente os testes ativos de injeção.

## Exemplo
```bash
# Descobrir rotas com parâmetros via katana e alimentar os templates DAST do nuclei
katana -u https://app.staging.corp \
  -hl -system-chrome -jc -aff \
  -fs fqdn -f qurl -silent \
  | nuclei -dast -rl 30 -o dast-findings.txt
```

## Limites e trade-offs
Ao encaminhar o `katana` por um proxy interceptador (`-proxy`), certifique-se de que o modo de interceptação manual (*breakpoint*) do proxy esteja desligado para não travar todas as goroutines do crawler por *timeout*.

## Como verificar
Verifique que o catálogo de rotas no proxy ou a entrada do `nuclei -dast` recebeu os endpoints dinâmicos descobertos pelo `katana`.

## Conexões
- [[katana-rate-limiting-concorrencia-parallelism-delay-timeout-resume]] — Veja também: Katana: Controle de Concorrência (`-c`, `-p`), Rate-Limiting (`-rl`, `-rlm`, `-rd`), TLS Impersonation (`-tlsi`) e `-resume`.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Referência cruzada direta com katana-extracao-campos-field-extraction-custom-regex-jsonl.
- [[httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei]] — Referência cruzada direta com httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
