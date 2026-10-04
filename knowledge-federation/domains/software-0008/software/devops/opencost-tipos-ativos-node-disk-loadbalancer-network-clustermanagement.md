---
id: software.devops.tranche07.000658
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/opencost/opencost/develop/README.md", "https://www.opencost.io/docs/installation/prometheus", "https://github.com/opencost/opencost"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenCost: contabilidade detalhada por tipos de ativos (Node, Disk, LoadBalancer, Network, Cloud e ClusterManagement)

## Em uma frase
O modelo de ativos do OpenCost (`get_asset_costs` / API `/assets`) classifica e contabiliza individualmente os custos de infraestrutura em seis categorias: `Node`, `Disk`, `LoadBalancer`, `Network`, `Cloud` e `ClusterManagement`.

## Por que importa
Se uma ferramenta de custos Kubernetes contabilizar apenas o preço das máquinas virtuais (`Node`), ela deixará de fora parcelas substanciais da fatura real do cluster: dezenas de volumes EBS/Persistent Disks anexados (`Disk`), balanceadores de carga provisionados por Services do tipo `LoadBalancer`, tráfego de rede cross-AZ/egress (`Network`) e a taxa horária cobrada pelo provedor por cada control plane EKS/AKS/GKE (`ClusterManagement`). O README oficial do OpenCost detalha o suporte completo a todos esses tipos de ativos.

## Como funciona
O motor de ativos do OpenCost inventaria continuamente os recursos provisionados pelo cluster Kubernetes e pela conta de nuvem em cada janela (`window`): (1) **`Node`** registra instâncias de computação com discriminação de custo de CPU, RAM e GPU; (2) **`Disk`** rastreia volumes de armazenamento com detalhamento de bytes usados versus capacidade provisionada; (3) **`LoadBalancer`** contabiliza instâncias de balanceadores de carga com IP e status público/privado; (4) **`Network`** agrega custos e uso de tráfego de rede; (5) **`Cloud`** consolida custos de serviços de nuvem com informações de créditos; e (6) **`ClusterManagement`** registra a taxa de gerenciamento do próprio cluster Kubernetes.

## Exemplo
```bash
# Consultar a API de ativos do OpenCost para as últimas 24 horas (1d)
curl -s "http://localhost:9003/assets?window=1d" | jq .
```

## Limites e trade-offs
Enquanto os custos de `Node` e `Disk` (PVCs montados) podem ser atribuídos diretamente aos pods agendados naqueles nós e volumes, custos de ativos compartilhados como `ClusterManagement` ou `LoadBalancer` compartilhados por um Ingress Controller exigem políticas claras de rateio organizacional para decidir se serão absorvidos pela equipe de plataforma ou distribuídos entre os tenants.

## Como verificar
Invoque o endpoint `/assets?window=1d` ou a ferramenta MCP `get_asset_costs` com `window: "1d"` e confirme a presença dos ativos `Node`, `Disk`, `LoadBalancer` e `ClusterManagement` com seus respectivos custos horários e totais.

## Conexões
- [[opencost-eficiencia-recursos-rightsizing-buffer-multiplier]] — Veja também: OpenCost: métricas de eficiência de recursos e recomendações de rightsizing com buffer_multiplier.
- [[opencost-integracao-prometheus-ha-thanos-mimir-cortex]] — Veja também: OpenCost: integração com Prometheus e requisitos de consulta global em topologias HA (Thanos, Mimir, Cortex).
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-precificacao-dinamica-cloud-billing-csv-on-prem]] — Referência cruzada direta com opencost-precificacao-dinamica-cloud-billing-csv-on-prem.
- [[opencost-mcp-server-agentes-ia-ferramentas-custos]] — Referência cruzada direta com opencost-mcp-server-agentes-ia-ferramentas-custos.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
