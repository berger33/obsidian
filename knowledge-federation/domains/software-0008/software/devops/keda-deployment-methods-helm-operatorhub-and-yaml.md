---
id: software.devops.tranche03.000254
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

# Métodos oficiais de implantação do KEDA: Helm, Operator Hub e manifestos YAML

## Em uma frase
A subseção `Deploying KEDA` no README oficial aponta para a documentação de implantação (`keda.sh/docs/latest/deploy/`), destacando os métodos suportados para instalar o KEDA no cluster: **Helm** (com chart publicado no Artifact Hub sob `packages/helm/kedacore/keda`), **Operator Hub** e arquivos **YAML** diretos.

## Por que importa
Oferecer instalação tanto via Helm Chart quanto via Operator Hub (OLM, muito usado em ambientes Red Hat OpenShift) e manifestos YAML puros permite encaixar o KEDA em qualquer fluxo declarativo de GitOps (Argo CD, Flux ou Kustomize).

## Como funciona
Escolha o método de deploy alinhado ao padrão da sua plataforma — por exemplo, o Helm chart oficial `kedacore/keda` ou o pacote do Operator Hub — e mantenha a versão sincronizada com as CRDs instaladas.

## Exemplo
Uma equipe gerencia a instalação do KEDA em múltiplos clusters Kubernetes usando o Helm chart oficial `kedacore/keda` reconciliado pelo Argo CD.

## Limites e trade-offs
Durante upgrades de versão do KEDA via Helm, verifique se as CustomResourceDefinitions (CRDs) atualizadas da nova versão também são aplicadas no cluster, já que o Helm não atualiza CRDs automaticamente por padrão sem configuração ou passo explícito.

## Como verificar
Conferi os badges de topo e a subseção Deploying KEDA no README oficial de kedacore/keda.

## Conexões
- [[keda-quickstarts-rabbitmq-azure-kafka-and-scaledjob]] — Veja também: Exemplos oficiais de QuickStart: RabbitMQ, Azure Functions, Kafka e ScaledJob.
- [[keda-operator-sdk-build-and-goproxy-gosumdb]] — Veja também: Construção sobre o Operator SDK, dev containers e variáveis GOPROXY e GOSUMDB.

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
