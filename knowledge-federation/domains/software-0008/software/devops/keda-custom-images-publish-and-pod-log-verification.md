---
id: software.devops.tranche03.000257
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

# Publicação de imagens customizadas (IMAGE_REGISTRY e IMAGE_REPO) e verificação dos pods do KEDA

## Em uma frase
A subseção `Custom KEDA as an image` em `BUILD.md` documenta o fluxo de quatro passos para empacotar e implantar imagens customizadas do KEDA: alterar o código, construir e publicar as imagens definindo `IMAGE_REGISTRY` (padrão `ghcr.io`, podendo usar `docker.io`, `quay.io` ou um registro interno) e `IMAGE_REPO` com `IMAGE_REGISTRY=docker.io IMAGE_REPO=johndoe make publish`, implantar no cluster com `IMAGE_REGISTRY=docker.io IMAGE_REPO=johndoe make deploy`, e verificar os logs com `kubectl logs -l app=keda-operator -n keda -f` e `kubectl logs -l app=keda-metrics-apiserver -n keda -f`.

## Por que importa
Esses comandos revelam também os seletores de labels oficiais dos pods de operação do KEDA no namespace `keda` (`app=keda-operator` e `app=keda-metrics-apiserver`), fundamentais tanto para testar builds próprias quanto para diagnosticar o KEDA em produção.

## Como funciona
Utilize as variáveis `IMAGE_REGISTRY` e `IMAGE_REPO` ao espelhar ou publicar builds customizadas do KEDA e monitore os logs de `app=keda-operator` e `app=keda-metrics-apiserver` no namespace `keda`.

## Exemplo
Após implantar uma versão de teste no cluster de homologação, o engenheiro acompanha `kubectl logs -l app=keda-operator -n keda -f` e `kubectl logs -l app=keda-metrics-apiserver -n keda -f` para validar a comunicação com o broker de eventos.

## Limites e trade-offs
Verifique também o terceiro componente de admissão (`admission-webhooks` mencionado no sumário de `BUILD.md`) ao diagnosticar rejeições de manifestos `ScaledObject` ou `ScaledJob`.

## Como verificar
Conferi a subseção Custom KEDA as an image em `BUILD.md` de kedacore/keda.

## Conexões
- [[keda-local-operator-outside-cluster-and-certs]] — Veja também: Execução local do operador fora do cluster, geração de certificados em /certs e --zap-log-level.
- [[keda-architecture-entrypoints-operator-and-metrics-adapter]] — Veja também: Pontos de entrada em Go: cmd/operator/main.go e cmd/adapter/main.go.

## Fontes
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
