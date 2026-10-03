---
id: software.seguranca.tranche04.000355
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

# ProjectDiscovery `httpx`: Triagem Visual em Escala com Screenshots Headless (`-ss`, `-system-chrome` e `-jsc`)

## Em uma frase
O modo Headless do `httpx` (`-ss` / `-screenshot`) utiliza uma instância do Chromium/Chrome para renderizar cada página web descoberta, capturar *screenshots* para triagem visual rápida e opcionalmente executar código JavaScript após a navegação (`-jsc`).

## Por que importa
Em superfícies externas com centenas de hosts respondendo `200 OK`, a inspeção visual de *screenshots* permite identificar em segundos painéis de login expostos (Grafana, Jenkins, Kibana, Argo CD), páginas de erro com *stack traces* e ambientes de homologação esquecidos.

## Como funciona
O `httpx` salva as capturas de tela e o corpo DOM renderizado em disco (`output/screenshot/`) e gera um relatório visual navegável. As flags `-st 10s` (`-screenshot-timeout`) e `-sid 1s` (`-screenshot-idle`) controlam o tempo de espera pela renderização de SPAs, enquanto `-esb` (`-exclude-screenshot-bytes`) evita inflar o arquivo JSONL com imagens em Base64.

## Exemplo
```bash
# Capturar screenshots usando o Chrome local sem embutir os bytes Base64 no JSONL
httpx -l live-web-assets.txt \
  -ss -system-chrome \
  -st 15s -sid 2s -esb \
  -json -o visual-recon.jsonl
```

## Limites e trade-offs
Executar dezenas de abas do Headless Chrome simultaneamente consome grande quantidade de CPU e memória RAM (`/dev/shm` em containers Docker); monte `--shm-size=2g` no Docker e reduza `-threads` durante varreduras com `-ss`.

## Como verificar
Verifique o diretório `output/screenshot/` gerado e confirme que os caminhos das imagens constam no campo `screenshot_path` do arquivo `visual-recon.jsonl`.

## Conexões
- [[httpxpd-inspecao-certificados-tls-csp-extract-fqdn-san]] — Veja também: ProjectDiscovery `httpx`: Inspeção de Certificados TLS (`tls-grab`), Header CSP (`-csp-probe`) e Extração de FQDNs (`-efqdn`).
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — Veja também: ProjectDiscovery `httpx`: Filtragem Avançada com Matchers (`-mc`, `-ms`, `-mr`, `-mfc`) e Filters (`-fc`, `-fs`, `-fr`, `-fcdn`).
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.
- [[httpxpd-armazenamento-respostas-srd-irh-csv-sqlite-dbs]] — Referência cruzada direta com httpxpd-armazenamento-respostas-srd-irh-csv-sqlite-dbs.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
