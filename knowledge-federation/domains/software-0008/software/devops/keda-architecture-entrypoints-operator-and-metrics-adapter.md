---
id: software.devops.tranche03.000258
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
fontes: ["https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md", "https://raw.githubusercontent.com/kedacore/keda/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pontos de entrada em Go: cmd/operator/main.go e cmd/adapter/main.go

## Em uma frase
A seção `Debugging with VS Code` de `BUILD.md` expõe os dois pontos de entrada em Go e as variáveis de ambiente de escopo da arquitetura do KEDA: o operador principal em `cmd/operator/main.go` e o servidor de métricas em `cmd/adapter/main.go`, ambos recebendo `WATCH_NAMESPACE` (vazio `""` para observar todos os namespaces) e `KEDA_CLUSTER_OBJECT_NAMESPACE` (definido como `"keda"`), sendo que a depuração local de `cmd/adapter/main.go` aceita flags como `--secure-port=6443`, `--v=5` e permite consultar métricas manualmente sem substituir o KEDA Metrics Server implantado no cluster.

## Por que importa
Compreender que `WATCH_NAMESPACE` controla se o KEDA opera em modo global no cluster (vazio) ou restrito a um namespace específico e que `KEDA_CLUSTER_OBJECT_NAMESPACE` define onde residem objetos globais (como `ClusterTriggerAuthentication`) ajuda a configurar instalações multi-tenant seguras.

## Como funciona
Configure `WATCH_NAMESPACE` e `KEDA_CLUSTER_OBJECT_NAMESPACE` de acordo com o modelo de isolamento do seu cluster e utilize os perfis de debug de `cmd/operator/main.go` e `cmd/adapter/main.go` ao investigar problemas no código Go.

## Exemplo
Em um cluster compartilhado onde o KEDA deve atuar apenas em um namespace específico, o administrador preenche `WATCH_NAMESPACE` na configuração do operador.

## Limites e trade-offs
Lembre-se da nota explícita de `BUILD.md`: rodar `cmd/adapter/main.go` localmente no VS Code permite consultar métricas manualmente contra a instância local, mas não substitui o Metrics Server registrado no API Server do cluster.

## Como verificar
Conferi as subseções Operator e Metrics server em Debugging with VS Code no arquivo `BUILD.md` de kedacore/keda.

## Conexões
- [[keda-custom-images-publish-and-pod-log-verification]] — Veja também: Publicação de imagens customizadas (IMAGE_REGISTRY e IMAGE_REPO) e verificação dos pods do KEDA.
- [[keda-ci-workflows-and-testing-strategy]] — Veja também: Workflows de build principal e testes end-to-end noturnos (TESTING.md).

## Fontes
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
