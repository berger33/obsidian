---
id: software.devops.tranche03.000251
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

# Escalonamento automático fino orientado a eventos — inclusive para e a partir de zero — graduado na CNCF

## Em uma frase
O README oficial no repositório kedacore/keda define o KEDA (Kubernetes-based Event Driven Autoscaling) como o projeto graduado da Cloud Native Computing Foundation (CNCF) que permite escalonamento automático fino — incluindo escalar para zero e a partir de zero (`to/from zero`) — para cargas de trabalho Kubernetes orientadas a eventos, atuando como um Kubernetes Metrics Server e permitindo definir regras de autoscaling por meio de Custom Resource Definitions (CRDs) dedicadas.

## Por que importa
O Horizontal Pod Autoscaler (HPA) nativo do Kubernetes escala tradicionalmente por CPU/memória e não reduz um Deployment ocioso a zero réplicas por padrão quando não há mensagens na fila; o KEDA conecta diretamente o tamanho das filas e fluxos de eventos ao escalonamento dos pods, economizando recursos quando o sistema está ocioso.

## Como funciona
Implante o KEDA no cluster para escalar consumidores de filas, streams e jobs sob demanda até zero réplicas quando não houver eventos pendentes e despertá-los automaticamente quando novos eventos chegarem.

## Exemplo
Um serviço de processamento de pedidos em segundo plano escala para 0 pods durante a madrugada sem tráfego e sobe para 20 réplicas em segundos quando mensagens entram na fila.

## Limites e trade-offs
Escalar para zero (`scale to zero`) é ideal para workers assíncronos e consumidores de filas; para APIs HTTP síncronas sem um interceptor de tráfego na frente, zerar réplicas causaria erro de conexão na primeira requisição até o pod subir.

## Como verificar
Conferi a abertura do README oficial de kedacore/keda.

## Conexões
- [[keda-hpa-native-integration-cloud-and-edge]] — Veja também: Integração nativa com o Horizontal Pod Autoscaler na nuvem ou na borda sem dependências externas.

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
