---
id: software.devops.tranche03.000252
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kedacore/keda/main/README.md", "https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração nativa com o Horizontal Pod Autoscaler na nuvem ou na borda sem dependências externas

## Em uma frase
O segundo parágrafo do README oficial destaca três qualidades arquiteturais do KEDA: ele pode rodar tanto na nuvem (`cloud`) quanto na borda (`edge`), integra-se nativamente com componentes do próprio Kubernetes como o **Horizontal Pod Autoscaler (HPA)** e não possui dependências externas (`has no external dependencies`).

## Por que importa
Em vez de reimplementar um motor paralelo de controle de réplicas que conflite com o HPA nativo do Kubernetes, o KEDA gerencia a ativação `0 <-> 1` e alimenta o HPA padrão com as métricas externas dos eventos para escalar `1 <-> N`.

## Como funciona
Utilize o KEDA sem precisar instalar bancos de dados ou barramentos extras para o próprio autoscaler, deixando que ele crie e alimente os objetos HPA nativos do Kubernetes para as suas cargas.

## Exemplo
Um cluster Kubernetes leve na borda (edge) executa o KEDA sem dependências externas para escalar processadores locais de telemetria conforme o tamanho da fila local.

## Limites e trade-offs
Não crie manualmente um segundo objeto HPA separado apontando para o mesmo Deployment que já está sendo gerenciado por um `ScaledObject` do KEDA, pois ambos disputariam o controle do número de réplicas.

## Como verificar
Conferi o segundo parágrafo da abertura do README oficial de kedacore/keda.

## Conexões
- [[keda-event-driven-autoscaling-and-scale-to-zero]] — Veja também: Escalonamento automático fino orientado a eventos — inclusive para e a partir de zero — graduado na CNCF.
- [[keda-quickstarts-rabbitmq-azure-kafka-and-scaledjob]] — Veja também: Exemplos oficiais de QuickStart: RabbitMQ, Azure Functions, Kafka e ScaledJob.

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
