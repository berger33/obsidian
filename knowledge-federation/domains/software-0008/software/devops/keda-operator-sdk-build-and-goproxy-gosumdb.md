---
id: software.devops.tranche03.000255
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

# Construção sobre o Operator SDK, dev containers e variáveis GOPROXY e GOSUMDB

## Em uma frase
A seção `Building` de `BUILD.md` explica que o KEDA utiliza o framework **Operator SDK** (`operator-framework/operator-sdk`, cuja versão exata usada pelo projeto fica registrada em `RELEASE_VERSION` no arquivo `kedacore/test-tools/blob/main/tools/Dockerfile`), oferece suporte a **Visual Studio Code Dev Containers** para iniciar um ambiente pronto com `make build`, e alerta que, se o build local em Go falhar com erros de `"checksum mismatch"` (comum em algumas instalações Go como no Fedora quando `GOPROXY=direct` e `GOSUMDB=off`), deve-se rodar `go env -w GOPROXY=https://proxy.golang.org,direct GOSUMDB=sum.golang.org`.

## Por que importa
Desenvolvedores que criam novos scalers para o KEDA economizam horas de configuração usando o Dev Container oficial ou alinhando a versão do Operator SDK e as variáveis `GOPROXY`/`GOSUMDB` do ambiente Go.

## Como funciona
Ao compilar o KEDA localmente (`make build`), utilize o VS Code Dev Container ou confira a versão do Operator SDK e configure `GOPROXY` e `GOSUMDB` conforme documentado em `BUILD.md`.

## Exemplo
Um contribuidor corrige um erro de `"checksum mismatch"` no build local executando `go env -w GOPROXY=https://proxy.golang.org,direct GOSUMDB=sum.golang.org` antes de rodar `make build`.

## Limites e trade-offs
Sempre verifique `RELEASE_VERSION` em `kedacore/test-tools` ao instalar o Operator SDK manualmente para evitar diferenças de geração de código e manifestos.

## Como verificar
Conferi a seção Building em `BUILD.md` no repositório kedacore/keda.

## Conexões
- [[keda-deployment-methods-helm-operatorhub-and-yaml]] — Veja também: Métodos oficiais de implantação do KEDA: Helm, Operator Hub e manifestos YAML.
- [[keda-local-operator-outside-cluster-and-certs]] — Veja também: Execução local do operador fora do cluster, geração de certificados em /certs e --zap-log-level.

## Fontes
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
