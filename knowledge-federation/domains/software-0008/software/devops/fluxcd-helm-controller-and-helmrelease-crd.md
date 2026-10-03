---
id: software.devops.tranche01.000055
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/fluxcd/flux2/main/README.md", "https://fluxcd.io/flux/get-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Helm Controller e o CRD `HelmRelease` para gerenciamento declarativo de charts Helm

## Em uma frase
O terceiro item da subseção Components no README oficial é o **Helm Controller** (`fluxcd.io/flux/components/helm/`), acompanhado do CRD `HelmRelease` (`fluxcd.io/flux/components/helm/helmreleases/`) e do guia dedicado `Manage Helm Releases` (`fluxcd.io/flux/guides/helmreleases/`).

## Por que importa
Executar `helm install` ou `helm upgrade` manualmente da máquina de um operador não deixa rastro declarativo no cluster de quais valores e qual versão de Chart deveriam estar ativos; o CRD `HelmRelease` transforma a instalação, o upgrade e a configuração de valores de um Chart Helm em um objeto declarativo reconciliado pelo Helm Controller.

## Como funciona
Defina um `HelmRepository` (ou `GitRepository` / `OCIRepository`) no Source Controller e crie um objeto `HelmRelease` especificando o chart, a versão e os valores desejados, consultando o guia `https://fluxcd.io/flux/guides/helmreleases/`.

## Exemplo
O Helm Controller observa o `HelmChart` produzido a partir da fonte e executa automaticamente as ações de release do Helm sempre que a versão do chart ou os valores do `HelmRelease` mudam no Git.

## Limites e trade-offs
Toda alteração de valores de um chart gerenciado pelo Flux deve ser feita no manifesto `HelmRelease` versionado no Git, pois edições manuais diretas com a CLI `helm` no cluster serão sobrescritas na próxima reconciliação.

## Como verificar
Conferi as seções Quickstart and documentation e Components no README oficial de `fluxcd/flux2`.

## Conexões
- [[fluxcd-kustomize-controller-and-crd]] — Veja também: Kustomize Controller e o CRD `Kustomization` para reconciliação de manifestos e overlays.
- [[fluxcd-notification-controller-provider-alert-receiver]] — Veja também: Notification Controller: eventos de saída e webhooks de entrada com `Provider`, `Alert` e `Receiver`.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Flux — Get Started e documentação oficial](https://fluxcd.io/flux/get-started/) — Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.; consultado em 2026-10-03.
