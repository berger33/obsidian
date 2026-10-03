---
id: software.devops.tranche05.000490
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/dapr/dapr/master/README.md", "https://docs.dapr.io/getting-started/", "https://github.com/dapr/dapr"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Observabilidade integrada no Dapr: métricas, rastreamento distribuído automático e diagnósticos

## Em uma frase
O README oficial destaca que todas as APIs do Dapr já oferecem **observabilidade embutida (built-in observability)** documentada em `docs.dapr.io/concepts/observability-concept/`. Como todas as chamadas de invocação de serviço, publicação/consumo de eventos, leitura/escrita de estado e execução de workflows passam pelo sidecar `daprd`, o Dapr gera automaticamente spans de rastreamento distribuído (propagando contexto W3C Trace Context via OpenTelemetry/Zipkin), métricas Prometheus de latência/erro/throughput e logs estruturados sem exigir instrumentação manual de cada chamada de infraestrutura na aplicação.

## Por que importa
Quando uma requisição atravessa cinco microsserviços e três filas de mensagens em linguagens diferentes, manter a propagação consistente de cabeçalhos `traceparent` e métricas uniformes manualmente em cada serviço é difícil; o sidecar `daprd` instrumenta toda a malha de comunicação e acesso a componentes de forma uniforme.

## Como funciona
Configure a seção `tracing` e `metric` no recurso `kind: Configuration` do Dapr apontando o exportador OpenTelemetry/Zipkin para o coletor de observabilidade (como OpenTelemetry Collector + Grafana Tempo) e colete as métricas Prometheus dos sidecars `daprd` e do plano de controle.

## Exemplo
Ao habilitar o tracing na `Configuration` do Dapr apontando para o OpenTelemetry Collector e Grafana Tempo, a equipe passa a visualizar no Grafana o trace completo de ponta a ponta cobrindo `Service Invocation`, `Pub/Sub` e etapas de `Dapr Workflows` entre serviços Go, Python e .NET.

## Limites e trade-offs
Garanta que o código da aplicação repasse os cabeçalhos de contexto de trace recebidos nas requisições de entrada ao fazer novas chamadas HTTP/gRPC para o sidecar local, preservando o vínculo pai-filho completo entre spans internos e spans de rede.

## Como verificar
Consulte o endpoint de métricas Prometheus do sidecar `daprd` (por padrão porta `9090/metrics`) e verifique a exportação das métricas de runtime e chamadas de componentes.

## Conexões
- [[dapr-dapr-cli-local-and-kubernetes-lifecycle-management]] — Veja também: Gerenciamento de desenvolvimento local e clusters Kubernetes com Dapr CLI (dapr/cli).

## Fontes
- [Dapr GitHub — README.md (Durable Execution, AI Agents, Zero-Trust mTLS, 12 Building Block APIs & Sidecar Architecture)](https://raw.githubusercontent.com/dapr/dapr/master/README.md) — README oficial do Dapr (projeto graduado na CNCF sob Apache-2.0) detalhando execução durável com Dapr Workflows, primitivas para agentes de IA e Conversation API, segurança por padrão com mTLS e Configuration accessControl, execução verificável, tabela das 12 APIs de blocos de construção sobre HTTP/gRPC (binário de ~58MB usando ~4MB de RAM) e repositórios de SDKs e components-contrib.; consultado em 2026-10-03.
- [Dapr Official Documentation — Getting Started & Concepts](https://docs.dapr.io/getting-started/) — Documentação oficial do Dapr cobrindo inicialização com Dapr CLI local e em Kubernetes, sidecar daprd, componentes plugáveis e observabilidade.; consultado em 2026-10-03.
- [Dapr — Official GitHub Repository](https://github.com/dapr/dapr) — Repositório principal Apache-2.0 do Dapr na CNCF.; consultado em 2026-10-03.
