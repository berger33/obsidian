---
id: software.devops.tranche19.001896
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

# kpack `ClusterStore`, `Buildpack` e `ClusterBuildpack`: catálogo e resolução de versões de Cloud Native Buildpacks

## Em uma frase
Para alimentar `Builders` e `ClusterBuilders`, o kpack oferece três recursos que referenciam pacotes de buildpacks distribuídos como imagens OCI (*buildpackages*): **`ClusterStore`**, **`Buildpack`** (namespaced) e **`ClusterBuildpack`** (cluster-scoped).

## Por que importa
Entender a ordem exata em que o kpack resolve um `id` de buildpack (e sua `version`) declarado em `spec.order` evita surpresas quando múltiplas versões do mesmo buildpack coexistem no cluster.

## Como funciona
Conforme documentado em `docs/builders.md`, quando um `Builder` referencia apenas `{ id: "paketo-buildpacks/gradle" }` (sem `version` explícita, escolhendo a maior versão SemVer), o kpack procura o buildpack nesta ordem: 1º como sub-buildpack de qualquer `Buildpack` no mesmo namespace do Builder; 2º como sub-buildpack de qualquer `ClusterBuildpack`; e 3º dentro do `ClusterStore` especificado em `spec.store`.

## Exemplo
```yaml
apiVersion: kpack.io/v1alpha2
kind: ClusterStore
metadata:
  name: paketo-cluster-store
spec:
  sources:
    - image: paketobuildpacks/java:latest
    - image: paketobuildpacks/nodejs:latest
    - image: paketobuildpacks/go:latest
```

## Limites e trade-offs
Um mesmo ID de buildpack pode aparecer em múltiplos grupos (`group`) diferentes de `spec.order`, mas nunca duas vezes dentro do mesmo `group`.

## Como verificar
Inspecione todos os buildpacks e sub-buildpacks indexados pelo store com `kubectl describe clusterstore paketo-cluster-store`.

## Conexões
- [[kpack-clusterstack-build-image-run-image-rebase-automatico-cve]] — Veja também: kpack `ClusterStack` e Operação de `Rebase`: atualização instantânea da camada de SO (`runImage`) sem recompilar o código.
- [[kpack-build-configuration-env-resources-project-toml-cosign]] — Veja também: kpack Configuração Avançada de Build (`spec.build` e `spec.cosign`): variáveis `BP_*`, limites de CPU/RAM, `project.toml` e assinatura Cosign.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
