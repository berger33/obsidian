---
id: software.devops.tranche07.000653
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

# OpenCost: precificação dinâmica via APIs de Cloud Billing (AWS, Azure, GCP), custos de carbono e CSV on-premises

## Em uma frase
O OpenCost obtém preços dinâmicos de ativos Kubernetes integrando-se às APIs de faturamento de AWS, Azure e GCP, suporta precificação customizada via CSV para clusters on-premises e calcula custos externos de nuvem e de carbono.

## Por que importa
Estimar custos de Kubernetes usando tabelas estáticas de preços públicos de lista (on-demand) distorce a realidade financeira de empresas que utilizam instâncias spot/preemptible, Savings Plans, Reserved Instances, descontos corporativos negociados (EDP) ou servidores bare-metal próprios no data center local. Segundo o README oficial do OpenCost, a plataforma suporta tanto integração direta com billing de nuvem quanto tabelas CSV customizadas para ambientes on-premises.

## Como funciona
Para clusters em nuvem pública, o OpenCost consulta as APIs de preços e exportações de faturamento (AWS Cost and Usage Report / Pricing API, Azure Billing / RateCard, GCP Cloud Billing export no BigQuery) para precificar com exatidão os ativos do cluster (`Node`, `Disk`, `LoadBalancer`, `Network`, `ClusterManagement`) e também monitorar gastos de todos os serviços de nuvem fora do cluster (`Cloud Costs`, como bancos gerenciados RDS/CloudSQL e buckets S3) com crédito e filtragem por provedor, serviço, categoria, região e conta. Além de valores monetários, o OpenCost estima custos de emissões de carbono dos recursos em nuvem. Em data centers on-premises, o administrador fornece um arquivo CSV definindo o custo horário por core de CPU, GB de RAM, GPU e armazenamento por classe/rótulo de nó.

## Exemplo
```yaml
# Trecho de configuração de variáveis de ambiente para habilitar ingestão de Cloud Costs no OpenCost
opencost:
  exporter:
    extraEnv:
      CLOUD_COST_ENABLED: "true"
      CLOUD_COST_CONFIG_PATH: "/var/cloud-integration/cloud-integration.json"
```

## Limites e trade-offs
As exportações detalhadas de faturamento dos provedores de nuvem (como AWS CUR no S3 ou GCP Billing no BigQuery) possuem atraso natural de processamento pelo provedor (frequentemente de várias horas até 24–48 horas para reconciliação de descontos e créditos); por isso, o OpenCost exibe estimativas sob demanda em tempo real para o dia corrente e reconcilia os valores exatos faturados à medida que os dados de billing consolidados são ingeridos.

## Como verificar
Consulte a API de ativos e de custos de nuvem do OpenCost (`/assets` e `/cloudCost`) para confirmar se os preços dos nós refletem a região e o tipo de instância corretos do provedor ou a tabela CSV configurada.

## Conexões
- [[opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus]] — Veja também: OpenCost: modelo de alocação de custos in-cluster para CPU, GPU, memória, PersistentVolumes e recursos ociosos.
- [[opencost-rastreamento-custos-inferencia-ia-vllm-tokens-kv-cache]] — Veja também: OpenCost: rastreamento de custos de inferência de IA para vLLM e llm-d por milhão de tokens e KV cache.
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-plugins-custos-externos-datadog-saas]] — Referência cruzada direta com opencost-plugins-custos-externos-datadog-saas.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
