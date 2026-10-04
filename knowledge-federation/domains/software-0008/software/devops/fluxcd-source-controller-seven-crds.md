---
id: software.devops.tranche01.000053
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/fluxcd/flux2/main/README.md", "https://fluxcd.io/flux/get-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Source Controller e seus sete CRDs de origem: de `GitRepository` e `OCIRepository` a `ArtifactGenerator`

## Em uma frase
Na subseção Components do README oficial, o grupo **Source Controllers** (`fluxcd.io/flux/components/source/`) abrange sete Custom Resource Definitions (CRDs) para obtenção de artefatos: `GitRepository`, `OCIRepository`, `HelmRepository`, `HelmChart`, `Bucket`, `ExternalArtifact` e `ArtifactGenerator`.

## Por que importa
Unificar a busca, verificação, autenticação e armazenamento em cache de artefatos em um controlador de fontes dedicado evita que os controladores de aplicação (Kustomize e Helm) precisem reimplementar lógica de clone Git, pull de registro OCI, download de buckets S3-compatíveis ou índices de repositórios Helm.

## Como funciona
Declare a origem dos seus manifestos ou pacotes usando o CRD apropriado do Source Controller (`GitRepository`, `OCIRepository`, `HelmRepository`, `HelmChart`, `Bucket`, `ExternalArtifact` ou `ArtifactGenerator`) e referencie essa fonte nos controladores consumidores.

## Exemplo
Com `OCIRepository` e `Bucket` ao lado de `GitRepository`, equipes podem distribuir manifestos empacotados como artefatos OCI assinados no registry sem exigir que o cluster de produção tenha acesso direto ao servidor Git interno.

## Limites e trade-offs
O Source Controller apenas busca e disponibiliza o artefato internamente no cluster; para aplicar os manifestos resultantes na API do Kubernetes, é preciso vincular um `Kustomization` ou `HelmRelease` a essa fonte.

## Como verificar
Conferi a lista de Source Controllers na subseção Components do README oficial de `fluxcd/flux2`.

## Conexões
- [[fluxcd-gitops-toolkit-composable-apis]] — Veja também: O GitOps Toolkit: conjunto de APIs componíveis e controladores especializados em Kubernetes.
- [[fluxcd-kustomize-controller-and-crd]] — Veja também: Kustomize Controller e o CRD `Kustomization` para reconciliação de manifestos e overlays.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Flux — Get Started e documentação oficial](https://fluxcd.io/flux/get-started/) — Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.; consultado em 2026-10-03.
