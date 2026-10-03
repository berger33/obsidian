---
id: software.seguranca.tranche04.000342
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

# Subfinder: Configuração de Chaves de API e Rotação de Credenciais em `provider-config.yaml` (`-pc`)

## Em uma frase
O arquivo `~/.config/subfinder/provider-config.yaml` (ou definido via `-pc` / variável de ambiente `SUBFINDER_PROVIDER_CONFIG`) armazena chaves de API para dezenas de fontes de inteligência (Chaos, SecurityTrails, Censys, Shodan, VirusTotal, GitHub, PassiveTotal).

## Por que importa
Sem chaves de API configuradas, apenas fontes gratuitas públicas são consultadas; adicionar chaves com suporte a rotação automática multiplica a cobertura de ativos descobertos em auditorias de *External Attack Surface Management* (EASM).

## Como funciona
Cada provedor no `provider-config.yaml` aceita uma lista YAML de credenciais. Quando múltiplas chaves são fornecidas para o mesmo provedor (ex.: vários Personal Access Tokens do GitHub ou chaves do Shodan), o `subfinder` seleciona e rotaciona entre elas para distribuir o consumo de cota.

## Exemplo
```yaml
# ~/.config/subfinder/provider-config.yaml (permissão recomendada chmod 600)
chaos:
  - ${PDCP_API_KEY}
securitytrails:
  - ${SECURITYTRAILS_API_KEY}
shodan:
  - ${SHODAN_KEY_PRIMARY}
  - ${SHODAN_KEY_SECONDARY}
censys:
  - ${CENSYS_APP_ID}:${CENSYS_SECRET}
```

## Limites e trade-offs
Nunca versione o arquivo `provider-config.yaml` com chaves reais no repositório Git; injete-o como Secret montado em memória no runner de CI/CD via `SUBFINDER_PROVIDER_CONFIG=/run/secrets/provider-config.yaml`.

## Como verificar
Execute `subfinder -ls` e verifique quais provedores aparecem marcados como configurados e prontos para uso.

## Conexões
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Veja também: Subfinder: Arquitetura de Enumeração Passiva de Subdomínios e Descoberta de Superfície Externa (EASM).
- [[subfinder-selecao-fontes-recursive-all-exclude-sources-max-results]] — Veja também: Subfinder: Seleção Granular de Fontes (`-s`, `-es`, `-all`, `-recursive`) e Paginação (`-mr`).
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Referência cruzada direta com subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
