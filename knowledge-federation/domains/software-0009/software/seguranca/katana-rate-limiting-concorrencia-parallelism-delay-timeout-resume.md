---
id: software.seguranca.tranche04.000369
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

# Katana: Controle de Concorrência (`-c`, `-p`), Rate-Limiting (`-rl`, `-rlm`, `-rd`), TLS Impersonation (`-tlsi`) e `-resume`

## Em uma frase
O `katana` separa a concorrência de URLs por alvo (`-c` / `-concurrency`, padrão 10) do paralelismo de alvos simultâneos (`-p` / `-parallelism`, padrão 10), controlando a cadência com `-rl` (req/s), `-rlm` (req/min), `-rd` (atraso em segundos entre requisições) e retomada de estado via `-resume resume.cfg`.

## Por que importa
Impede a sobrecarga de servidores de aplicação durante *crawls* profundos e permite pausar e retomar varreduras longas sem repetir o trabalho já executado.

## Como funciona
Quando o processo é interrompido (`SIGINT`), o `katana` salva o estado atual em `resume.cfg`. Adicionalmente, a flag `-tlsi` (`-tls-impersonate`) randomiza a impressão digital TLS `ClientHello` (JA3) para evitar que WAFs bloqueiem o crawler simplesmente por reconhecerem o fingerprint TLS padrão da biblioteca `crypto/tls` do Go.

## Exemplo
```bash
# Executar crawl controlado a 20 req/s com atraso de 1s e armazenamento de respostas brutas
katana -list staging-apps.txt \
  -c 5 -p 2 -rl 20 -rd 1 -timeout 15 \
  -srd /var/lib/dast/katana-responses \
  -jsonl -o controlled-crawl.jsonl
```

## Limites e trade-offs
Definir `-c 20` e `-p 20` simultaneamente sem limitar `-rl` pode disparar centenas de requisições concorrentes caso a lista de entrada possua múltiplos subdomínios apontando para o mesmo cluster de backend.

## Como verificar
Interrompa um teste longo e reinicie com `katana -resume resume.cfg`, verificando nos logs a retomada a partir do checkpoint salvo.

## Conexões
- [[katana-crawling-autenticado-headers-cookies-chrome-ws-url]] — Veja também: Katana: Crawling Autenticado com Headers/Cookies (`-H`), Sessão de Navegador (`-cdd`) e Chrome DevTools (`-cwu`).
- [[katana-integracao-pipelines-dast-nuclei-ffuf-zap-proxy]] — Veja também: Katana: Integração em Pipelines DAST com Proxy de Auditoria (`-proxy`), `nuclei` e `ffuf`.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[katana-deduplicacao-similaridade-fsu-pcs-simhash-tfidf-bm25]] — Referência cruzada direta com katana-deduplicacao-similaridade-fsu-pcs-simhash-tfidf-bm25.
- [[httpxpd-otimizacao-rate-limit-threads-retries-timeout-waf-bypass]] — Referência cruzada direta com httpxpd-otimizacao-rate-limit-threads-retries-timeout-waf-bypass.

## Fontes
- [ProjectDiscovery Katana GitHub — README.md (Next-Generation Crawling and Spidering Framework, Standard/Headless Modes, JS Crawl, Scope & Similarity Filtering)](https://raw.githubusercontent.com/projectdiscovery/katana/main/README.md) — README oficial do projectdiscovery/katana detalhando todas as flags de configuração, deduplicação SimHash/TF-IDF/BM25, Knowledge Base e extração de campos; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Katana Overview (SPA Headless Crawling, JavaScript Parsing & Field Extraction)](https://docs.projectdiscovery.io/opensource/katana/overview) — Visão geral oficial da documentação do Katana cobrindo o rastreamento de Single-Page Applications (React/Angular/Vue) e automação em pipelines; consultado em 2026-10-03.
- [ProjectDiscovery Katana — Official GitHub Releases & Documentation](https://github.com/projectdiscovery/katana/releases) — Repositório oficial MIT do ProjectDiscovery Katana; consultado em 2026-10-03.
