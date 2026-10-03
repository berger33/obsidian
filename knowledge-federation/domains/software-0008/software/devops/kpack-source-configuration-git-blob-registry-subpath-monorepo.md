---
id: software.devops.tranche19.001893
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

# kpack Fontes de Código (`spec.source`): monitoramento de repositórios `git`, arquivos `blob` e imagens `registry` com `subPath`

## Em uma frase
No recurso `Image` do kpack, o bloco **`spec.source`** (reconciliado internamente por um `SourceResolver`) suporta três origens mutuamente exclusivas de código-fonte: **`git`** (repositório Git via HTTPS ou SSH com `revision` e `initializeSubmodules`), **`blob`** (arquivo `.zip`/`.tar.gz`/`.jar` em URL ou bucket com `stripComponents` e `auth`) e **`registry`** (imagem OCI contendo código-fonte), todas compatíveis com **`subPath`**.

## Por que importa
Em arquiteturas de monorepo onde dez microsserviços residem em pastas diferentes (`services/auth`, `services/billing`) do mesmo repositório Git, um commit em `services/auth` não deveria disparar rebuilds desnecessários em `services/billing`.

## Como funciona
Ao configurar `source.git.url`, `source.git.revision: main` e `source.subPath: services/billing` (com a feature flag `GIT_RESOLVER_USE_SHALLOW_CLONE` habilitada), quando `git.revision` é uma branch, o kpack agenda novos builds **somente** se os novos commits modificarem arquivos dentro de `subPath`.

## Exemplo
```yaml
spec:
  source:
    git:
      url: git@github.com:org/platform-monorepo.git
      revision: main
      initializeSubmodules: true
    subPath: services/billing
```

## Limites e trade-offs
Para fontes do tipo `blob` em nuvem privada, o campo `auth` suporta `""` (público), `"secret"` (credenciais via Secret do kpack) ou `"helper"` (Workload Identity da ServiceAccount em Azure AKS e Google GKE).

## Como verificar
Inspecione o objeto `SourceResolver` criado automaticamente para a sua `Image` com `kubectl get sourceresolvers -n builds`.

## Conexões
- [[kpack-crd-image-spec-tag-additionaltags-cache-history-limits]] — Veja também: kpack `Image` CRD: configuração declarativa de `tag`, `additionalTags`, `cache` (Volume vs Registry) e limites de histórico.
- [[kpack-builder-vs-clusterbuilder-order-detection-resolution]] — Veja também: kpack `Builder` e `ClusterBuilder`: definição da ordem de detecção (`spec.order`) e resolução de IDs de Buildpacks.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://github.com/buildpacks-community/kpack) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
