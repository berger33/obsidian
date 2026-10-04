---
id: software.devops.tranche07.000660
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

# OpenCost: fluxo de desenvolvimento com Tilt, interface web (opencost-ui) e CLI kubectl-cost

## Em uma frase
O ecossistema OpenCost inclui a interface web (`opencost/opencost-ui`), o plugin de linha de comando `kubectl cost` e um ambiente de desenvolvimento local integrado via Tilt (`tilt up` com `tilt-values.yaml`).

## Por que importa
Diferentes perfis de usuários consomem dados de custos de formas distintas: gestores e equipes de FinOps preferem explorar relatórios visuais no navegador (`opencost-ui`), desenvolvedores no terminal preferem inspecionar o custo de seus pods via `kubectl cost`, e contribuidores do projeto precisam subir rapidamente o backend, a UI, o Helm chart e a ingestão de custos de nuvem localmente. O README oficial do OpenCost documenta essas interfaces e o fluxo de desenvolvimento com Tilt.

## Como funciona
Para usuários finais no terminal, o plugin `kubectl cost` (instalável via Krew) consulta a API do OpenCost e exibe tabelas imediatas de custo por namespace, deployment, controller ou pod diretamente na linha de comando. Para visualização web, o container `opencost-ui` serve o painel gráfico que consome as APIs de alocação, ativos e cloud costs. Para desenvolvimento local, ao clonar `opencost` (junto a `opencost-ui` e `opencost-helm-charts` na mesma árvore pai) e executar `tilt up`, o Tilt aplica `tilt-values.yaml` (incluindo `CLOUD_COST_ENABLED: "true"` e `CLOUD_COST_CONFIG_PATH`) para subir o ambiente completo com MCP server e ingestão de cloud costs em minutos.

## Exemplo
```bash
# Consultar custos por namespace diretamente no terminal usando o plugin kubectl cost
kubectl cost namespace --window 7d

# Subir ambiente de desenvolvimento completo do OpenCost localmente com Tilt
git clone https://github.com/opencost/opencost.git
cd opencost
tilt up
```

## Limites e trade-offs
Conforme documentado nas notas de configuração padrão do README do OpenCost, tanto a UI quanto o Prometheus utilizam por padrão a porta `9090` no ambiente local; portanto, ao acessar ambos simultaneamente na máquina de desenvolvimento via `kubectl port-forward`, é necessário mapear um deles para uma porta local não padrão (por exemplo, `9091:9090`).

## Como verificar
Acesse a interface do `opencost-ui` via port-forward ou execute `kubectl cost pod` para validar que as tabelas de alocação renderizam os custos calculados pelo backend do OpenCost.

## Conexões
- [[opencost-integracao-prometheus-ha-thanos-mimir-cortex]] — Veja também: OpenCost: integração com Prometheus e requisitos de consulta global em topologias HA (Thanos, Mimir, Cortex).
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus]] — Referência cruzada direta com opencost-alocacao-recursos-cpu-gpu-memoria-pv-prometheus.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
