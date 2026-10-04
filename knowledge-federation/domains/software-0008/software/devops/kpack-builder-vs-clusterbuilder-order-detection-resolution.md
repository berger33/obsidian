---
id: software.devops.tranche19.001894
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
fontes: ["https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md", "https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md", "https://github.com/buildpacks-community/kpack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kpack `Builder` e `ClusterBuilder`: definição da ordem de detecção (`spec.order`) e resolução de IDs de Buildpacks

## Em uma frase
Os recursos **`Builder`** (escopo de namespace) e **`ClusterBuilder`** (escopo de cluster) combinam uma **`ClusterStack`**, uma **`ClusterStore`** opcional e uma lista ordenada de grupos de detecção (**`spec.order`**) para construir e publicar no registry uma imagem de *CNB Builder* pronta para uso pelas `Images`.

## Por que importa
Permitir que cada desenvolvedor escolha versões arbitrárias ou não homologadas de compiladores perde a governança; com um `ClusterBuilder`, a equipe de plataforma define centralmente quais buildpacks (ex.: Paketo Java, Node.js, Go, Python) e versões são testados na fase de `detection`.

## Como funciona
Durante o build de uma aplicação, o CNB Lifecycle testa os grupos de `spec.order` sequencialmente, um grupo por vez: o **primeiro grupo** cujos buildpacks não-opcionais (`optional: false`) passarem todos na detecção é selecionado para compilar a aplicação. Enquanto o `Builder` usa `spec.serviceAccountName` do próprio namespace, o `ClusterBuilder` usa `spec.serviceAccountRef` (`name` e `namespace`).

## Exemplo
```yaml
apiVersion: kpack.io/v1alpha2
kind: ClusterBuilder
metadata:
  name: default-cluster-builder
spec:
  tag: ghcr.io/org/kpack-cluster-builder:latest
  serviceAccountRef:
    name: kpack-registry-sa
    namespace: kpack
  stack:
    name: noble-base-stack
    kind: ClusterStack
  store:
    name: paketo-cluster-store
    kind: ClusterStore
  order:
    - group:
        - id: paketo-buildpacks/java
    - group:
        - id: paketo-buildpacks/nodejs
    - group:
        - id: paketo-buildpacks/go
```

## Limites e trade-offs
Um `ClusterBuilder` expõe duas condições de status importantes: **`Ready`** (indicando se pode ser usado em Builds) e **`UpToDate`** (indicando se a reconciliação mais recente com a Stack e Buildpacks mais novos teve sucesso).

## Como verificar
Execute `kubectl get clusterbuilders` e `kubectl describe clusterbuilder default-cluster-builder` para verificar as condições `Ready` e `UpToDate` e a lista de buildpacks resolvidos.

## Conexões
- [[kpack-source-configuration-git-blob-registry-subpath-monorepo]] — Veja também: kpack Fontes de Código (`spec.source`): monitoramento de repositórios `git`, arquivos `blob` e imagens `registry` com `subPath`.
- [[kpack-clusterstack-build-image-run-image-rebase-automatico-cve]] — Veja também: kpack `ClusterStack` e Operação de `Rebase`: atualização instantânea da camada de SO (`runImage`) sem recompilar o código.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
