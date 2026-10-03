---
id: software.seguranca.tranche04.000347
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

# Subfinder: Saída Estruturada JSONL (`-oJ`), Atribuição de Fontes (`-cs`) e Diretórios por Domínio (`-oD`)

## Em uma frase
O `subfinder` exporta resultados estruturados em JSON Lines (`-oJ` / `-json`), enriquecidos opcionalmente com a lista completa de todas as fontes passivas que confirmaram cada subdomínio (`-cs` / `-collect-sources`).

## Por que importa
Em programas de gestão contínua de superfície de ataque (EASM), saber se um subdomínio apareceu apenas em um repositório público do GitHub (`source: github`) ou em um certificado TLS recém-emitido (`source: crtsh`) orienta a prioridade da investigação.

## Como funciona
Quando `-cs` é usado sem `-oJ`, apenas a primeira fonte que reportou o host é registrada; combinando `-oJ -cs`, cada linha JSON inclui um array de provedores, o domínio raiz (`input`) e o subdomínio (`host`), facilitando a ingestão em bancos PostgreSQL, OpenSearch ou grafos de ativos.

## Exemplo
```bash
# Exportar inventário enriquecido em JSONL com todas as fontes de descoberta por subdomínio
subfinder -d example.corp -oJ -cs -silent \
  | jq -c 'select(.sources | index("github"))' > leaked-on-github.jsonl
```

## Limites e trade-offs
A flag `-oD <diretório>` só tem efeito quando usada em conjunto com uma lista de domínios de entrada (`-dL domains.txt`), gravando um arquivo individual por domínio raiz dentro do diretório especificado.

## Como verificar
Valide o schema de saída executando `head -n 1 leaked-on-github.jsonl | jq -e '.host and .input and .sources'`.

## Conexões
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Veja também: Subfinder: Controle de Escopo com Match (`-m`), Filter (`-f`) e Exclusão de IPs (`-ei`).
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Veja também: Subfinder: Encadeamento Unix (`stdin`/`stdout`) em Pipelines de Reconhecimento com `httpx`, `katana` e `nuclei`.
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-monitoramento-continuo-diff-novos-subdominios-alertas]] — Referência cruzada direta com subfinder-monitoramento-continuo-diff-novos-subdominios-alertas.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
