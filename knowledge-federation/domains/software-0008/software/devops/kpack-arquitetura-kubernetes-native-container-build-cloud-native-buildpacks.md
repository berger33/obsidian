---
id: software.devops.tranche19.001891
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

# kpack: arquitetura do serviço Kubernetes-native de build e rebase contínuo de imagens OCI com Cloud Native Buildpacks

## Em uma frase
O **kpack** (`kpack.io/v1alpha2`, mantido pela comunidade Cloud Native Buildpacks sob licença Apache 2.0) estende o Kubernetes utilizando primitivas **não privilegiadas** para construir e manter imagens de container OCI automaticamente a partir de código-fonte, implementando a especificação **Cloud Native Buildpacks (CNB)** como plataforma declarativa.

## Por que importa
Construir imagens com Dockerfiles manuais espalhados por centenas de repositórios obriga cada equipe de produto a abrir Pull Requests e reexecutar pipelines de CI inteiros sempre que sai uma correção de CVE na imagem base do SO (Ubuntu/Debian) ou no runtime do Java/Node.js.

## Como funciona
No kpack, você declara recursos **`ClusterStack`**, **`ClusterStore`**, **`Builder`/`ClusterBuilder`** e **`Image`**. O controlador do kpack monitora continuamente três entradas — 1) commits no repositório Git/Blob/Registry de código-fonte, 2) novas versões de Buildpacks no Store e 3) atualizações de segurança na Stack do SO — agendando novos objetos **`Build`** ou executando **Rebase** rápido de camadas OCI sem recompilar a aplicação.

## Exemplo
```bash
# Listando os recursos declarativos do kpack no cluster com kubectl ou kp CLI:
kubectl get clusterstacks,clusterstores,clusterbuilders,images,builds -A
```

## Limites e trade-offs
Como os Pods de `Build` gerados pelo kpack executam o *CNB Lifecycle* (`detect`, `analyze`, `restore`, `build`, `export` ou `rebase`) em containers sem privilégios de root/Docker daemon, eles operam com segurança em clusters multi-tenant.

## Como verificar
Verifique o controlador e o webhook do kpack em execução com `kubectl get pods -n kpack`.

## Conexões
- [[kpack-crd-image-spec-tag-additionaltags-cache-history-limits]] — Veja também: kpack `Image` CRD: configuração declarativa de `tag`, `additionalTags`, `cache` (Volume vs Registry) e limites de histórico.

## Fontes
- [kpack GitHub — README.md (Kubernetes Native Container Build Service with Cloud Native Buildpacks)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/README.md) — README oficial do buildpacks-community/kpack apresentando builds OCI não privilegiados no Kubernetes e recursos declarativos Image, Builder e ClusterStack; consultado em 2026-10-03.
- [kpack Official Documentation — Image Resources (docs/image.md: Tags, Cache Volume/Registry, Git/Blob/Registry Sources, SubPath & Build Config)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/image.md) — Documentação oficial do recurso Image do kpack detalhando tag, additionalTags, cache, source (git/blob/registry com subPath) e configuração de build/Cosign; consultado em 2026-10-03.
- [kpack Official Documentation — Builders (docs/builders.md: Builder, ClusterBuilder, Detection Order, Resolving Buildpack IDs & Status Conditions)](https://raw.githubusercontent.com/buildpacks-community/kpack/main/docs/builders.md) — Documentação oficial dos recursos Builder e ClusterBuilder do kpack explicando spec.order, resolução de buildpacks e condições Ready/UpToDate; consultado em 2026-10-03.
