---
id: software.devops.tranche07.000657
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

# OpenCost: métricas de eficiência de recursos e recomendações de rightsizing com buffer_multiplier

## Em uma frase
O OpenCost analisa a eficiência de utilização de recursos (`get_efficiency`) e gera recomendações de redimensionamento (rightsizing) e economia de custos para pods, namespaces e controladores aplicando um multiplicador de folga (`buffer_multiplier`, padrão `1.2`).

## Por que importa
O superprovisionamento de `requests` de CPU e memória em manifestos Kubernetes é uma das maiores fontes de desperdício em nuvem: equipes solicitam 4 CPUs para um container que usa em média 0.2 CPU, bloqueando capacidade nos nós e forçando o Cluster Autoscaler a provisionar máquinas desnecessárias. Segundo o README oficial do OpenCost, a análise de eficiência calcula recomendações práticas de rightsizing com margem de segurança configurável.

## Como funciona
Ao avaliar a eficiência em uma janela temporal (`window`, como `7d`, `1h` ou `30m`) agregada por `pod`, `namespace` ou `controller`, o OpenCost compara os recursos solicitados (`requests`) e pagos com o consumo efetivo observado nas métricas do Prometheus. Para evitar que a recomendação de rightsizing deixe a aplicação sem folga para pequenos picos, o cálculo aplica o parâmetro `buffer_multiplier` (cujo valor padrão é `1.2`, garantindo 20% de headroom acima do uso base). Para janelas longas de consulta, o parâmetro `step` (por exemplo, `1h` ou `6h`) divide a busca em lotes menores para reduzir o pico de uso de memória durante a análise.

## Exemplo
```javascript
// Exemplo oficial de chamada à ferramenta MCP get_efficiency do OpenCost para recomendações de rightsizing
const efficiency = await mcpClient.callTool('get_efficiency', {
  window: '7d',
  aggregate: 'namespace,controller',
  step: '6h',
  buffer_multiplier: 1.2
});
```

## Limites e trade-offs
Conforme documentado nos parâmetros de `get_efficiency` do OpenCost, definir um `step` menor reduz o pico de consumo de memória ao processar janelas longas em lotes, porém pode aumentar o tempo total de consulta e o número de requisições internas; além disso, workloads com picos extremos e curtíssimos de CPU/memória podem exigir um `buffer_multiplier` maior que `1.2` (por exemplo, `1.5`) para evitar throttling de CPU ou OOMKill.

## Como verificar
Execute uma consulta de eficiência para uma janela de `7d` agregada por `namespace,controller` com `buffer_multiplier: 1.2` e verifique as recomendações de redimensionamento e a economia estimada retornadas para cada controlador.

## Conexões
- [[opencost-mcp-server-agentes-ia-ferramentas-custos]] — Veja também: OpenCost: servidor MCP (Model Context Protocol) opt-in na porta 8081 para agentes de IA.
- [[opencost-tipos-ativos-node-disk-loadbalancer-network-clustermanagement]] — Veja também: OpenCost: contabilidade detalhada por tipos de ativos (Node, Disk, LoadBalancer, Network, Cloud e ClusterManagement).
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus]] — Referência cruzada direta com opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
