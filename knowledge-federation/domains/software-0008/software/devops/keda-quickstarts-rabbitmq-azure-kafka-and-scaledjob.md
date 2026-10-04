---
id: software.devops.tranche03.000253
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

# Exemplos oficiais de QuickStart: RabbitMQ, Azure Functions, Kafka e ScaledJob

## Em uma frase
A seção `Getting started` do README lista quatro repositórios de início rápido e o catálogo central `kedacore/samples`: `QuickStart - RabbitMQ and Go` (`sample-go-rabbitmq`), `QuickStart - Azure Functions and Queues` (`sample-hello-world-azure-functions`), `QuickStart - Azure Functions and Kafka on Openshift 4` (`sample-azure-functions-on-ocp4`) e `QuickStart - Azure Storage Queue with ScaledJob` (`sample-go-storage-queue`).

## Por que importa
Esses quatro exemplos mostram os dois modelos principais de carga orientada a eventos no KEDA: serviços contínuos que escalam réplicas de Deployment/StatefulSet (como consumidores RabbitMQ ou Kafka) e execuções em lote por evento modeladas como **ScaledJob** (disparando Jobs do Kubernetes para cada item ou lote na fila).

## Como funciona
Escolha `ScaledObject` ao escalar Deployments ou StatefulSets de longa duração e utilize `ScaledJob` (como no exemplo `sample-go-storage-queue`) quando cada evento exigir um Job isolado de processamento até a conclusão.

## Exemplo
Para processar vídeos pesados enviados a uma fila de armazenamento, a equipe adota o padrão `ScaledJob` de `kedacore/samples`, criando um Job Kubernetes dedicado para cada item da fila.

## Limites e trade-offs
Em cargas com `ScaledJob`, defina limites claros de concorrência máxima e limpeza de Jobs concluídos para não saturar o cluster quando milhares de mensagens chegarem simultaneamente.

## Como verificar
Conferi a seção Getting started no README oficial de kedacore/keda.

## Conexões
- [[keda-hpa-native-integration-cloud-and-edge]] — Veja também: Integração nativa com o Horizontal Pod Autoscaler na nuvem ou na borda sem dependências externas.
- [[keda-deployment-methods-helm-operatorhub-and-yaml]] — Veja também: Métodos oficiais de implantação do KEDA: Helm, Operator Hub e manifestos YAML.

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
