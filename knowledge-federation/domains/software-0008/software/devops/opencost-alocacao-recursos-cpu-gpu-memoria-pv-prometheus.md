---
id: software.devops.tranche07.000652
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

# OpenCost: modelo de alocação de custos in-cluster para CPU, GPU, memória, PersistentVolumes e recursos ociosos

## Em uma frase
O modelo de alocação do OpenCost atribui custos de recursos in-cluster (CPU, GPU, memória RAM, PersistentVolumes e rede) agregados por qualquer dimensão do Kubernetes e exporta métricas de preços de volta ao Prometheus em `/metrics`.

## Por que importa
Atribuir custos apenas pelo `requests` declarado no manifesto do Pod ignora casos em que um container sem `requests` consome toda a CPU livre do nó, enquanto atribuir apenas pelo uso real ignora a capacidade reservada que impediu outros pods de serem agendados. De acordo com a especificação e a documentação oficial do OpenCost, o modelo reconcilia uso real e capacidade solicitada (além de distribuir ou isolar recursos ociosos, `idle`) para fornecer chargeback e showback precisos.

## Como funciona
Para cada janela de tempo (`window`), o motor do OpenCost calcula o custo de cada container multiplicando a duração pelo preço horário do ativo subjacente (nó ou disco) e pelo maior valor entre o uso real medido e o `request` configurado para CPU e memória, além de rastrear alocação de GPUs e `PersistentVolumeClaims` (PVCs). Os usuários podem consultar essas alocações via API REST, interface web (`opencost-ui`), plugin `kubectl cost` ou MCP server, agregando por `cluster`, `node`, `namespace`, `controllerKind`, `controller`, `service`, `pod` ou labels, com opções para compartilhar custos ociosos (`share_idle`) ou exibi-los separadamente (`include_idle`). Adicionalmente, o OpenCost expõe métricas de preços unitários em `/metrics` para que consultas PromQL calculem custos diretamente no Prometheus/Grafana.

## Exemplo
```bash
# Consultar a API de alocação do OpenCost agregando custos dos últimos 7 dias por namespace
kubectl port-forward -n opencost svc/opencost 9003:9003 &
curl -s "http://localhost:9003/allocation/compute?window=7d&aggregate=namespace&includeIdle=true" | jq .
```

## Limites e trade-offs
Quando `share_idle=true` é utilizado em relatórios de chargeback corporativo, o custo da capacidade ociosa dos nós Kubernetes (folga mantida para absorver picos de autoscaling) é rateado proporcionalmente entre os namespaces ativos; se um grande namespace for desligado em um cluster com nós fixos, a fatura aparente dos namespaces restantes subirá mesmo sem aumento de consumo próprio, exigindo transparência sobre a parcela `idle`.

## Como verificar
Acesse o endpoint `/metrics` do OpenCost (`curl -s http://localhost:9003/metrics | grep node_cpu_hourly_cost`) e valide que os custos horários de CPU, RAM e GPU por nó estão sendo exportados para o Prometheus.

## Conexões
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Veja também: OpenCost: especificação aberta e implementação em Go para monitoramento de custos em Kubernetes e nuvem.
- [[opencost-precificacao-dinamica-cloud-billing-csv-on-prem]] — Veja também: OpenCost: precificação dinâmica via APIs de Cloud Billing (AWS, Azure, GCP), custos de carbono e CSV on-premises.
- [[mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus]] — Referência cruzada direta com mimir-arquitetura-monolitica-microsservicos-armazenamento-prometheus.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
