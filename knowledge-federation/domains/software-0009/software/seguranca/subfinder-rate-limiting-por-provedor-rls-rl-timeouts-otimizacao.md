---
id: software.seguranca.tranche04.000345
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
fontes: ["https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md", "https://docs.projectdiscovery.io/opensource/subfinder/overview", "https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Subfinder: Rate-Limiting Global (`-rl`) e por Provedor (`-rls`), Timeouts e Limite de Leitura (`-rsr`)

## Em uma frase
O `subfinder` permite impor limites de requisições HTTP por segundo tanto globalmente (`-rl`) quanto individualmente para cada provedor de API (`-rls`), além de limitar o tamanho máximo de corpo lido (`-rsr`) e o tempo total de enumeração (`-max-time`).

## Por que importa
Cada API de Threat Intelligence possui cotas de *rate limit* distintas (ex.: Shodan permite taxas diferentes de HackerTarget ou GitHub); o controle por provedor (`-rls`) evita erros `HTTP 429 Too Many Requests` sem desacelerar os demais provedores.

## Como funciona
A flag `-rls "hackertarget=5/s,shodan=10/s,github=3/m"` aplica *token buckets* independentes por conector. Complementarmente, `-timeout 30` define o tempo máximo por requisição HTTP, `-max-time 10` encerra a enumeração do domínio após 10 minutos e `-rsr 10485760` limita a leitura de respostas gigantes a 10 MiB para proteger a memória RAM do coletor.

## Exemplo
```bash
# Executar subfinder respeitando cotas específicas de cada API e limite de memória de resposta
subfinder -dLroot-domains.txt \
  -rls "shodan=10/s,securitytrails=2/s,github=20/m" \
  -timeout 20 -max-time 5 \
  -rsr 10485760 \
  -oD /var/reports/easm-subdomains/
```

## Limites e trade-offs
Deixar `-rsr 0` (ilimitado) ao consultar fontes de arquivo histórico para domínios com milhões de certificados emitidos pode causar picos elevados de alocação de memória no container.

## Como verificar
Monitore os logs com `-v` durante a execução e confirme a ausência de respostas `429 Too Many Requests` nos provedores configurados em `-rls`.

## Conexões
- [[subfinder-resolucao-ativa-eliminacao-wildcards-nw-resolvers-ip]] — Veja também: Subfinder: Resolução DNS Ativa (`-nW` / `-active`), Eliminação de Wildcards e Extração de IPs (`-oI`).
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Veja também: Subfinder: Controle de Escopo com Match (`-m`), Filter (`-f`) e Exclusão de IPs (`-ei`).
- [[subfinder-configuracao-provedores-api-keys-provider-config-yaml]] — Referência cruzada direta com subfinder-configuracao-provedores-api-keys-provider-config-yaml.
- [[subfinder-selecao-fontes-recursive-all-exclude-sources-max-results]] — Referência cruzada direta com subfinder-selecao-fontes-recursive-all-exclude-sources-max-results.
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Referência cruzada direta com subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
