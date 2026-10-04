---
id: software.devops.tranche07.000656
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

# OpenCost: servidor MCP (Model Context Protocol) opt-in na porta 8081 para agentes de IA

## Em uma frase
O servidor MCP (Model Context Protocol) do OpenCost — desabilitado por padrão (opt-in) e integrado ao Helm chart oficial na porta `8081` — permite que agentes de IA consultem alocações, ativos, custos de nuvem e eficiência via transporte HTTP.

## Por que importa
Engenheiros e analistas de FinOps frequentemente desejam fazer perguntas analíticas complexas a assistentes de IA (como no Cursor ou agentes internos de plataforma) sobre gastos de infraestrutura e oportunidades de rightsizing sem construir integrações sob medida para a API REST do OpenCost. De acordo com o README oficial do OpenCost, o servidor MCP fornece uma interface padronizada com controle total do usuário e superfície de ataque reduzida por ser opt-in.

## Como funciona
Para minimizar a superfície de ataque, o servidor MCP vem **desabilitado por padrão** em todas as implantações do OpenCost e deve ser explicitamente habilitado no Helm chart com `--set opencost.mcp.enabled=true` (podendo customizar a porta padrão `8081` via `--set opencost.mcp.port=9091` e o nível de log com `--set opencost.mcp.extraEnv.MCP_LOG_LEVEL=debug`). Ele utiliza transporte HTTP (`http://opencost.opencost.svc.cluster.local:8081` ou via `port-forward`) e expõe quatro ferramentas principais para agentes de IA: `get_allocation_costs`, `get_asset_costs`, `get_cloud_costs` e `get_efficiency`.

## Exemplo
```bash
# Implantar o OpenCost via Helm habilitando o servidor MCP opt-in na porta padrão 8081
helm install opencost opencost/opencost \
  --set opencost.mcp.enabled=true

# Expor o servidor MCP localmente para conexão de clientes MCP (como Cursor)
kubectl port-forward svc/opencost 8081:8081
```

## Limites e trade-offs
Como o servidor MCP do OpenCost utiliza transporte HTTP direto e expõe dados financeiros detalhados de todas as contas de nuvem (`accountID`), regiões, nós e namespaces do cluster, quando exposto fora do cluster via `LoadBalancer` ou `Ingress` (`http://your-opencost-domain.com:8081`), ele deve obrigatoriamente ser protegido por autenticação/autorização no gateway ou restrito à rede interna/VPN.

## Como verificar
Com `opencost.mcp.enabled=true`, configure o cliente MCP apontando para `http://localhost:8081` (`"type": "http"`) e valide a listagem das ferramentas `get_allocation_costs`, `get_asset_costs`, `get_cloud_costs` e `get_efficiency`.

## Conexões
- [[opencost-plugins-custos-externos-datadog-saas]] — Veja também: OpenCost: arquitetura de OpenCost Plugins para monitorar custos externos de SaaS e observabilidade (Datadog).
- [[opencost-eficiencia-recursos-rightsizing-buffer-multiplier]] — Veja também: OpenCost: métricas de eficiência de recursos e recomendações de rightsizing com buffer_multiplier.
- [[opencost-monitoramento-custos-kubernetes-multi-cloud-cncf]] — Referência cruzada direta com opencost-monitoramento-custos-kubernetes-multi-cloud-cncf.
- [[kubescape-mcp-server-integracao-agentes-ia]] — Referência cruzada direta com kubescape-mcp-server-integracao-agentes-ia.

## Fontes
- [OpenCost GitHub — README.md (Cost Allocation, Cloud Billing, AI Inference & MCP Server)](https://raw.githubusercontent.com/opencost/opencost/develop/README.md) — README oficial do OpenCost detalhando alocação in-cluster (CPU, GPU, RAM, PV), billing multi-cloud, custos de inferência vLLM/llm-d, OpenCost Plugins e servidor MCP opt-in na porta 8081; consultado em 2026-10-03.
- [OpenCost Official Documentation — Prometheus Integration & Global Query Endpoints](https://www.opencost.io/docs/installation/prometheus) — Documentação oficial de integração do OpenCost com Prometheus e requisitos de endpoint global (Thanos, Cortex, Mimir) em topologias HA/sharded; consultado em 2026-10-03.
- [OpenCost — Official GitHub Repository](https://github.com/opencost/opencost) — Repositório oficial Apache-2.0 do OpenCost (CNCF Incubating); consultado em 2026-10-03.
