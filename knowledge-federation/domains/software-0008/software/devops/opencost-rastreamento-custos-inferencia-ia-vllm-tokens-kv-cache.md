---
id: software.devops.tranche07.000654
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

# OpenCost: rastreamento de custos de inferência de IA para vLLM e llm-d por milhão de tokens e KV cache

## Em uma frase
O OpenCost oferece rastreamento nativo de custos de inferência de IA para implantações baseadas em vLLM (como `llm-d` e compatíveis), calculando o custo por milhão de tokens (input/output), preço corrigido por KV cache e atribuição de infraestrutura compartilhada.

## Por que importa
Em plataformas de IA generativa rodando sobre Kubernetes com aceleradores GPU de alto custo, saber apenas que um pod `vllm` custou US$ 40 por hora não responde quanto custa cada requisição de modelo, qual é o custo unitário por milhão de tokens de entrada versus saída ou como atribuir o custo da GPU entre múltiplos clientes que compartilham o mesmo servidor de inferência. De acordo com o README oficial do OpenCost, o recurso de AI inference cost tracking resolve essa atribuição econômica diretamente via APIs REST e métricas Prometheus.

## Como funciona
O OpenCost coleta métricas específicas de telemetria dos servidores de inferência compatíveis com **vLLM** e **llm-d** (como volume de tokens de prompt processados, tokens gerados na decodificação, utilização e hits de KV cache e tempo de ocupação de GPU) e combina esses indicadores com o custo real do ativo de GPU/nó no Kubernetes. O modelo calcula: (1) o custo por milhão de tokens separado entre entrada (`input`) e saída (`output`); (2) a precificação corrigida pelo uso de KV cache (refletindo a economia de computação quando prefixos de prompt são reaproveitados em cache); e (3) a atribuição proporcional de infraestrutura compartilhada, expondo esses resultados tanto em endpoints REST quanto em métricas para o Prometheus.

## Exemplo
```bash
# Verificar métricas de custo e alocação de GPUs e inferência expostas pelo OpenCost para o Prometheus
curl -s http://localhost:9003/metrics | grep -E "gpu|vllm|token|inference"
```

## Limites e trade-offs
Para que o cálculo de custo por milhão de tokens e a correção de KV cache sejam precisos, os pods de inferência vLLM/llm-d precisam estar configurados para expor suas métricas internas ao Prometheus no mesmo intervalo de scrape utilizado pelo OpenCost, e os preços horários das instâncias de GPU (ou partições MIG/time-slicing) devem estar devidamente mapeados no provedor de preços do OpenCost.

## Como verificar
Com um workload vLLM monitorado pelo Prometheus, consulte os endpoints de métricas e APIs de inferência do OpenCost para validar o cálculo do custo unitário por milhão de tokens de input e output.

## Conexões
- [[opencost-precificacao-dinamica-cloud-billing-csv-on-prem]] — Veja também: OpenCost: precificação dinâmica via APIs de Cloud Billing (AWS, Azure, GCP), custos de carbono e CSV on-premises.
- [[opencost-plugins-custos-externos-datadog-saas]] — Veja também: OpenCost: arquitetura de OpenCost Plugins para monitorar custos externos de SaaS e observabilidade (Datadog).
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus]] — Referência cruzada direta com opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
