---
id: software.devops.tranche07.000659
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

# OpenCost: integração com Prometheus e requisitos de consulta global em topologias HA (Thanos, Mimir, Cortex)

## Em uma frase
O OpenCost utiliza o Prometheus como fonte primária de telemetria de uso e expõe `/metrics`, exigindo em topologias Prometheus particionadas (sharded/HA) que `PROMETHEUS_SERVER_ENDPOINT` aponte para um endpoint de consulta global como Thanos Query, Cortex ou Grafana Mimir.

## Por que importa
Em clusters Kubernetes de produção, é comum rodar o Prometheus em modo de alta disponibilidade ou com sharding horizontal (`shards > 1`), onde cada pod Prometheus coleta apenas uma fração dos alvos do cluster. Conforme destaca a nota de atenção no README oficial do OpenCost, apontar o OpenCost para um único pod Prometheus em uma configuração sharded causa resultados de exportação e alocação incompletos ou intermitentes.

## Como funciona
O OpenCost executa consultas PromQL periódicas contra o endereço configurado em `PROMETHEUS_SERVER_ENDPOINT` para recuperar métricas do `kube-state-metrics`, `cAdvisor` (kubelet) e do próprio exporter do OpenCost. Quando o ambiente utiliza Prometheus sharded ou múltiplas réplicas HA, o `PROMETHEUS_SERVER_ENDPOINT` deve ser configurado para o componente agregador/global — como o `Thanos Query`, `Cortex` ou o `query-frontend` do `Grafana Mimir` — garantindo que todas as séries de todos os nós e pods estejam visíveis e deduplicadas em um único endpoint compatível com a API HTTP do Prometheus.

## Exemplo
```bash
# Instalar o OpenCost via Helm apontando PROMETHEUS_SERVER_ENDPOINT para o Query-Frontend global do Grafana Mimir
helm install opencost opencost/opencost \
  --namespace opencost --create-namespace \
  --set opencost.prometheus.internal.serviceName=mimir-query-frontend \
  --set opencost.prometheus.internal.namespaceName=mimir \
  --set opencost.prometheus.internal.port=8080
```

## Limites e trade-offs
Quando `PROMETHEUS_SERVER_ENDPOINT` aponta para um backend multi-tenant como o Grafana Mimir ou Cortex que exige o cabeçalho `X-Scope-OrgID`, é necessário configurar os cabeçalhos ou credenciais de autenticação correspondentes no chart do OpenCost para que as consultas PromQL do calculador de custos não recebam erro `401`/`400` por ausência de identificação de tenant.

## Como verificar
Verifique os logs do container `opencost` na inicialização para confirmar que a verificação de conectividade com o `PROMETHEUS_SERVER_ENDPOINT` passou sem avisos de métricas ausentes do `kube-state-metrics` ou `cAdvisor`.

## Conexões
- [[opencost-tipos-ativos-node-disk-loadbalancer-network-clustermanagement]] — Veja também: OpenCost: contabilidade detalhada por tipos de ativos (Node, Disk, LoadBalancer, Network, Cloud e ClusterManagement).
- [[opencost-desenvolvimento-local-tilt-ui-kubectl-cost]] — Veja também: OpenCost: fluxo de desenvolvimento com Tilt, interface web (opencost-ui) e CLI kubectl-cost.
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[mimir-caminho-leitura-query-frontend-scheduler-querier-sharding]] — Referência cruzada direta com mimir-caminho-leitura-query-frontend-scheduler-querier-sharding.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
