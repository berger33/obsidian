---
id: software.seguranca.tranche04.000341
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

# Subfinder: Arquitetura de Enumeração Passiva de Subdomínios e Descoberta de Superfície Externa (EASM)

## Em uma frase
`subfinder` (ProjectDiscovery, MIT) é uma ferramenta modular escrita em Go projetada especificamente para enumeração passiva de subdomínios usando dezenas de fontes públicas, transparência de certificados (CT Logs) e APIs de inteligência de ameaças.

## Por que importa
Por operar de forma estritamente passiva por padrão, descobre ativos externos esquecidos (*shadow IT*, ambientes de homologação e subdomínios órfãos) em segundos sem enviar nenhum pacote diretamente para a infraestrutura do domínio investigado.

## Como funciona
O motor consulta paralelamente provedores gratuitos (como `crtsh`, `anubis`, `hackertarget`, `waybackarchive`, `rapiddns`) e provedores autenticados via chave de API, deduplica os resultados em memória e emite a lista consolidada de FQDNs em `stdout`, arquivo (`-o`) ou JSON Lines (`-oJ`).

## Exemplo
```bash
# Listar todas as fontes passivas disponíveis e enumerar subdomínios de um domínio corporativo
subfinder -ls
subfinder -d example.corp -silent -o subdomains-passive.txt
```

## Limites e trade-offs
Como fontes passivas incluem registros históricos de certificados e DNS que podem já ter sido desativados, a lista bruta do `subfinder` deve ser resolvida via DNS (`-nW` ou `dnsx`) antes de acionar scanners ativos.

## Como verificar
Execute `subfinder -d example.corp -cs -oJ | jq -r '. | "\(.host) <- \(.source)"'` para auditar quais fontes passivas retornaram cada subdomínio.

## Conexões
- [[subfinder-configuracao-provedores-api-keys-provider-config-yaml]] — Veja também: Subfinder: Configuração de Chaves de API e Rotação de Credenciais em `provider-config.yaml` (`-pc`).
- [[subfinder-selecao-fontes-recursive-all-exclude-sources-max-results]] — Referência cruzada direta com subfinder-selecao-fontes-recursive-all-exclude-sources-max-results.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
