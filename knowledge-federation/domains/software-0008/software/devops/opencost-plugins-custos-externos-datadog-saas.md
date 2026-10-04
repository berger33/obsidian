---
id: software.devops.tranche07.000655
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

# OpenCost: arquitetura de OpenCost Plugins para monitorar custos externos de SaaS e observabilidade (Datadog)

## Em uma frase
Por meio do sistema de OpenCost Plugins (`opencost/opencost-plugins`), o OpenCost estende o monitoramento financeiro para incluir custos externos de plataformas SaaS e ferramentas de terceiros, como o Datadog.

## Por que importa
A conta total de operação de uma plataforma cloud-native não se resume à infraestrutura Kubernetes e aos serviços de IaaS da nuvem: licenças e consumo de serviços SaaS externos (como ingestão de logs, métricas customizadas, hosts e APM no Datadog) frequentemente representam uma fatia expressiva do orçamento de engenharia. Segundo o README oficial do OpenCost, o suporte a custos externos via plugins unifica gastos de Kubernetes, nuvem e SaaS na mesma visão.

## Como funciona
Os plugins do OpenCost (mantidos no repositório oficial `github.com/opencost/opencost-plugins`) são executáveis que implementam a interface de custos customizados do OpenCost (comunicando-se via gRPC/protobuf com o core do OpenCost). O plugin consulta a API de faturamento e uso do fornecedor externo (como a API do Datadog), normaliza os dados de consumo e custo por janela de tempo, serviço ou categoria e entrega esses registros ao OpenCost para armazenamento e exibição junto aos custos de cluster e de nuvem.

## Exemplo
```bash
# Inspecionar os logs do container do OpenCost para confirmar o carregamento de plugins de custos customizados
kubectl logs -n opencost deploy/opencost -c opencost | grep -i "plugin"
```

## Limites e trade-offs
Cada plugin externo exige credenciais de leitura de faturamento/uso da respectiva plataforma SaaS (como `DD_API_KEY` e `DD_APP_KEY` com escopo de billing no Datadog) montadas com segurança via Kubernetes Secrets, além de estar sujeito aos limites de taxa (rate limits) e à granularidade temporal de agregação da API do fornecedor SaaS.

## Como verificar
Após habilitar e configurar o plugin de custos externos no OpenCost, consulte a API de custos customizados para confirmar que as despesas do serviço SaaS (como Datadog) estão sendo ingeridas e listadas por janela temporal.

## Conexões
- [[opencost-rastreamento-custos-inferencia-ia-vllm-tokens-kv-cache]] — Veja também: OpenCost: rastreamento de custos de inferência de IA para vLLM e llm-d por milhão de tokens e KV cache.
- [[opencost-mcp-server-agentes-ia-ferramentas-custos]] — Veja também: OpenCost: servidor MCP (Model Context Protocol) opt-in na porta 8081 para agentes de IA.
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-precificacao-dinamica-cloud-billing-csv-on-prem]] — Referência cruzada direta com opencost-precificacao-dinamica-cloud-billing-csv-on-prem.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
