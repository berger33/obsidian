---
id: software.seguranca.tranche04.000343
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

# Subfinder: Seleção Granular de Fontes (`-s`, `-es`, `-all`, `-recursive`) e Paginação (`-mr`)

## Em uma frase
O `subfinder` permite controlar exatamente quais fontes passivas são acionadas usando inclusão explícita (`-s`), exclusão (`-es`), ativação completa (`-all`) ou filtragem apenas de fontes compatíveis com subdomínios multinível (`-recursive`).

## Por que importa
Ao investigar um subdomínio de terceiro ou quarto nível (ex.: `dev.us-east-1.api.corp.com`), muitas fontes passivas só indexam o domínio raiz (`corp.com`); a flag `-recursive` seleciona apenas provedores capazes de consultar prefixos hierárquicos profundos.

## Como funciona
A flag `-all` habilita todas as fontes suportadas (incluindo provedores mais lentos de arquivo web), enquanto `-es waybackarchive,commoncrawl` exclui fontes lentas quando o tempo de resposta é prioritário. Já `-mr <N>` (`-max-results`) limita o número de resultados buscados em fontes paginadas para evitar esgotar créditos de API em domínios gigantes.

## Exemplo
```bash
# Enumerar apenas fontes rápidas de CT Logs e DNS para subdomínios recursivos com limite de paginação
subfinder -d k8s.us-east.example.corp \
  -recursive \
  -es waybackarchive \
  -mr 5000 \
  -o k8s-subdomains.txt
```

## Limites e trade-offs
Usar `-all` sem configurar `-timeout` e `-max-time` adequados em listas com centenas de domínios (`-dL`) pode atrasar o pipeline de reconhecimento devido a provedores de arquivo histórico que paginam milhões de URLs.

## Como verificar
Execute `subfinder -d example.corp -s crtsh,chaos -v` e confirme nos logs verbosos que exclusivamente os provedores listados em `-s` foram consultados.

## Conexões
- [[subfinder-configuracao-provedores-api-keys-provider-config-yaml]] — Veja também: Subfinder: Configuração de Chaves de API e Rotação de Credenciais em `provider-config.yaml` (`-pc`).
- [[subfinder-resolucao-ativa-eliminacao-wildcards-nw-resolvers-ip]] — Veja também: Subfinder: Resolução DNS Ativa (`-nW` / `-active`), Eliminação de Wildcards e Extração de IPs (`-oI`).
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Referência cruzada direta com subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao.

## Fontes
- [ProjectDiscovery Subfinder GitHub — README.md (Fast Passive Subdomain Enumeration Tool, CLI Flags, Provider Config & Go Library)](https://raw.githubusercontent.com/projectdiscovery/subfinder/dev/README.md) — README oficial do projectdiscovery/subfinder detalhando flags de entrada, seleção de fontes, rate-limit por provedor e saída JSONL; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — Subfinder Overview (Passive Architecture, Curated Sources & Workflow Integration)](https://docs.projectdiscovery.io/opensource/subfinder/overview) — Visão geral oficial da documentação do Subfinder descrevendo o modelo passivo furtivo e integração em pipelines de reconhecimento; consultado em 2026-10-03.
- [ProjectDiscovery Subfinder — Go SDK Example (v2/examples/main.go)](https://github.com/projectdiscovery/subfinder/blob/dev/v2/examples/main.go) — Exemplo oficial de uso programático do Subfinder como biblioteca Go; consultado em 2026-10-03.
