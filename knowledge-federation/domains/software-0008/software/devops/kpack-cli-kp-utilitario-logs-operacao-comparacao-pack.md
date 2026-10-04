---
id: software.devops.tranche19.001900
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack CLI (`kp`) e Utilitário `logs`: operação de `Images`/`Builders`, streaming de logs de build e comparação `kpack` vs `pack`

## Em uma frase
Para interagir de forma ergonômica com os Custom Resources do kpack no dia a dia e em pipelines de CI/CD, o ecossistema fornece a **CLI oficial `kp`** (`kpack-cli`) e o utilitário **`logs`**, além de documentar quando usar **`kpack`** (in-cluster contínuo) versus **`pack`** (CLI local de desenvolvedor).

## Por que importa
Acompanhar os logs sequenciais de 6 *Init Containers* em um Pod de build usando `kubectl logs -c <init-container>` manualmente um por um é trabalhoso; a CLI `kp build logs` (ou o binário `logs`) encadeia todos os containers automaticamente em tempo real.

## Como funciona
Enquanto a CLI **`pack`** (`pack build`) foi projetada para a máquina local do desenvolvedor (usando um daemon Docker local para construir uma imagem pontual), o **`kpack`** roda dentro do cluster Kubernetes sem Docker daemon e reconstrói/faz rebase automaticamente de toda a frota de imagens ao longo do tempo.

## Exemplo
```bash
# Criando uma Image e acompanhando os logs de todas as fases do build em tempo real com kp:
kp image create payment-service-img \
  --tag ghcr.io/org/payment-service \
  --git https://github.com/org/payment-service.git \
  --git-revision main \
  --cluster-builder default-cluster-builder \
  --namespace builds

kp build list payment-service-img -n builds
kp build logs payment-service-img -n builds
```

## Limites e trade-offs
O comando `kp image status <name> -n <namespace>` resume o estado atual da imagem, o digest completo da última imagem construída, a razão do último build e a referência do Builder utilizado.

## Como verificar
Execute `kp build status payment-service-img -b 1 -n builds` para auditar os buildpacks exatos que participaram do build #1.

## Conexões
- [[kpack-crd-build-fases-cnb-lifecycle-pods-init-containers]] — Veja também: kpack `Build` CRD e Execução em Pod: fases do CNB Lifecycle (`prepare`, `detect`, `analyze`, `restore`, `build`, `export`, `completion`).

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
