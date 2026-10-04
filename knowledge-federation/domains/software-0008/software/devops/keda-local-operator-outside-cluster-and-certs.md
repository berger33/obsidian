---
id: software.devops.tranche03.000256
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

# Execução local do operador fora do cluster, geração de certificados em /certs e --zap-log-level

## Em uma frase
A subseção `Custom KEDA locally outside cluster` em `BUILD.md` mostra que o Operator SDK permite rodar o controlador do KEDA localmente fora do cluster (em Linux ou macOS) para depurar o operador ou scalers sem precisar construir imagens a cada mudança: como o KEDA exige certificados TLS para criptografar qualquer comunicação HTTP e inspeciona por padrão a pasta `/certs` (customizável via `--cert-dir`), o guia fornece os comandos `openssl req -newkey rsa:2048` para criar `/certs/tls.key`, `/certs/tls.crt` e `/certs/ca.crt`, implantar o Metrics Server no cluster (`make deploy`), escalar o `deployment/keda-operator` para `0` réplicas no namespace `keda` e rodar localmente `make run ARGS="--zap-log-level=debug"`.

## Por que importa
Rodar o `keda-operator` na máquina local conectado ao cluster via `$HOME/.kube/config` permite testar um novo scaler em segundos, desde que o `deployment/keda-operator` dentro do cluster seja zerado para não concorrer com o processo local.

## Como funciona
Para depurar o operador localmente fora do cluster, gere os certificados locais em `/certs` (ou aponte `--cert-dir`), execute `kubectl scale deployment/keda-operator --replicas=0 -n keda` e inicie `make run ARGS="--zap-log-level=debug"`.

## Exemplo
O desenvolvedor zera o deployment `keda-operator` no cluster de desenvolvimento e executa o operador localmente em modo debug para inspecionar um novo scaler.

## Limites e trade-offs
Se você esquecer de escalar `deployment/keda-operator` para `--replicas=0` no cluster antes de rodar `make run` localmente, duas instâncias do operador reconciliarão os mesmos recursos simultaneamente.

## Como verificar
Conferi a subseção Custom KEDA locally outside cluster em `BUILD.md` de kedacore/keda.

## Conexões
- [[keda-operator-sdk-build-and-goproxy-gosumdb]] — Veja também: Construção sobre o Operator SDK, dev containers e variáveis GOPROXY e GOSUMDB.
- [[keda-custom-images-publish-and-pod-log-verification]] — Veja também: Publicação de imagens customizadas (IMAGE_REGISTRY e IMAGE_REPO) e verificação dos pods do KEDA.

## Fontes
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
