---
id: software.devops.tranche07.000651
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

# OpenCost: especificação aberta e implementação em Go para monitoramento de custos em Kubernetes e nuvem

## Em uma frase
O OpenCost (projeto CNCF Incubating originalmente criado e aberto pela Kubecost, sob licença Apache-2.0) combina uma especificação aberta (`/spec/`) e uma implementação em Golang para monitorar e alocar custos em tempo real e históricos no Kubernetes e em múltiplos provedores de nuvem.

## Por que importa
Em clusters Kubernetes compartilhados por dezenas de aplicações, equipes e departamentos, a fatura mensal consolidada da AWS, Azure ou GCP mostra apenas o custo bruto das máquinas virtuais e discos, sem indicar quanto cada namespace, deployment ou serviço consumiu efetivamente de CPU, RAM, GPU e armazenamento. Segundo o README oficial do OpenCost, o projeto oferece transparência financeira (FinOps) em tempo real tanto para recursos in-cluster quanto para gastos externos de nuvem.

## Como funciona
O OpenCost é instalado e gerenciado exclusivamente por meio do Helm chart oficial (`opencost/opencost`) em qualquer cluster Kubernetes 1.20+ (os manifestos standalone legados foram removidos). Ele coleta métricas de utilização e requisições de recursos via Prometheus, cruza esses dados com os preços dinâmicos sob demanda (ou preços negociados/descontos via APIs de faturamento da AWS, Azure e GCP, ou tabelas CSV customizadas para clusters on-premises) e calcula a alocação de custos por cluster, nó, namespace, controller kind, controller, service ou pod. A interface web oficial é mantida no repositório `opencost/opencost-ui` e o servidor expõe APIs REST de alocação/ativos e um endpoint `/metrics` para o Prometheus.

## Exemplo
```bash
# Instalação oficial do OpenCost em um cluster Kubernetes 1.20+ usando exclusivamente o Helm chart
helm repo add opencost https://opencost.github.io/opencost-helm-chart
helm repo update
helm install opencost opencost/opencost --namespace opencost --create-namespace
```

## Limites e trade-offs
O cálculo de alocação do OpenCost depende diretamente da completude das séries temporais no servidor Prometheus consultado; conforme alerta o README oficial do OpenCost, se o cluster utiliza Prometheus particionado/sharded em alta disponibilidade (HA), a variável `PROMETHEUS_SERVER_ENDPOINT` deve apontar obrigatoriamente para um endpoint de consulta global (como Thanos Query, Cortex ou Grafana Mimir), pois apontar para um único pod Prometheus resultará em dados de custo incompletos ou intermitentes.

## Como verificar
Após instalar o chart `opencost/opencost`, verifique se os pods estão `Running` e consulte a API de alocação ou o endpoint `/metrics` para confirmar a geração de métricas de custo por nó e container.

## Conexões
- [[opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus]] — Veja também: OpenCost: modelo de alocação de custos in-cluster para CPU, GPU, memória, PersistentVolumes e recursos ociosos.
- [[opencost-precificacao-dinamica-cloud-billing-csv-on-prem]] — Referência cruzada direta com opencost-precificacao-dinamica-cloud-billing-csv-on-prem.
- [[opencost-mcp-server-agentes-ia-ferramentas-custos]] — Referência cruzada direta com opencost-mcp-server-agentes-ia-ferramentas-custos.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
