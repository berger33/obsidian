---
id: software.devops.tranche19.001892
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
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://github.com/buildpacks-community/kpack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack `Image` CRD: configuração declarativa de `tag`, `additionalTags`, `cache` (Volume vs Registry) e limites de histórico

## Em uma frase
O Custom Resource **`Image`** (`kpack.io/v1alpha2`) define como o kpack deve construir e manter uma imagem OCI ao longo do tempo, especificando o destino no registry (`tag` e `additionalTags`), o `builder`, a fonte de código (`source`), a estratégia de `cache` e os limites de retenção (`successBuildHistoryLimit` e `failedBuildHistoryLimit`).

## Por que importa
Recompilar todas as dependências Maven, Gradle, npm ou Cargo do zero a cada commit demoraria vários minutos; por isso, o kpack preserva as camadas de cache do Cloud Native Buildpacks entre builds consecutivos.

## Como funciona
O campo `spec.tag` é imutável e define o repositório principal da imagem construída, enquanto `spec.additionalTags` é mutável (desde que no mesmo registry). Para o `spec.cache`, o kpack oferece duas variantes: 1) **`cache.volume.size`** (cria um `PersistentVolumeClaim` no cluster para guardar o cache em disco); ou 2) **`cache.registry.tag`** (armazena o cache como uma imagem OCI no registry, ideal para clusters sem ReadWriteMany ou com nós efêmeros).

## Exemplo
```yaml
apiVersion: kpack.io/v1alpha2
kind: Image
metadata:
  name: payment-service-img
  namespace: builds
spec:
  tag: ghcr.io/org/payment-service
  additionalTags:
    - ghcr.io/org/payment-service:latest
  serviceAccountName: kpack-registry-sa
  builder:
    name: default-cluster-builder
    kind: ClusterBuilder
  cache:
    volume:
      size: 2Gi
  failedBuildHistoryLimit: 5
  successBuildHistoryLimit: 5
  imageTaggingStrategy: BuildNumber
  source:
    git:
      url: https://github.com/org/payment-service.git
      revision: main
```

## Limites e trade-offs
Conforme documentado em `docs/image.md`, todas as entradas de `additionalTags` devem residir no **mesmo** registry que o `tag` principal (exportação cruzada entre registries distintos não é suportada).

## Como verificar
Aplique o recurso `Image` e verifique seu status e a última imagem gerada (`LATESTIMAGE`) com `kubectl get images -n builds`.

## Conexões
- [[kpack-arquitetura-kubernetes-native-container-build-cloud-native-buildpacks]] — Veja também: kpack: arquitetura do serviço Kubernetes-native de build e rebase contínuo de imagens OCI com Cloud Native Buildpacks.
- [[kpack-source-configuration-git-blob-registry-subpath-monorepo]] — Veja também: kpack Fontes de Código (`spec.source`): monitoramento de repositórios `git`, arquivos `blob` e imagens `registry` com `subPath`.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
