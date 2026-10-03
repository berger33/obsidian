---
id: software.devops.tranche01.000056
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
fontes: ["https://raw.githubusercontent.com/fluxcd/flux2/main/README.md", "https://github.com/fluxcd/flux2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Notification Controller: eventos de saída e webhooks de entrada com `Provider`, `Alert` e `Receiver`

## Em uma frase
O quarto item da subseção Components no README oficial é o **Notification Controller** (`fluxcd.io/flux/components/notification/`), composto por três CRDs: `Provider` (`providers/`), `Alert` (`alerts/`) e `Receiver` (`receivers/`).

## Por que importa
Um sistema GitOps que opera de forma assíncrona dentro do cluster precisa de comunicação bidirecional: avisar a equipe quando uma reconciliação de `Kustomization` ou `HelmRelease` falha (via `Provider` e `Alert`) e receber webhooks de servidores Git ou registries para disparar a sincronização imediatamente sem esperar o intervalo de polling (via `Receiver`).

## Como funciona
Configure um `Provider` (indicando o destino de notificação) e um `Alert` (selecionando quais eventos de quais recursos do Flux devem ser enviados), e crie um `Receiver` quando quiser acionar reconciliações imediatas por webhook externo.

## Exemplo
Com os três CRDs separados (`Provider`, `Alert` e `Receiver`), várias equipes no mesmo cluster multi-tenant podem definir seus próprios alertas e webhooks sem alterar a configuração global do controlador.

## Limites e trade-offs
Ao expor o endpoint de um `Receiver` para webhooks externos de Git ou registry, utilize os mecanismos de segredo e validação documentados em `fluxcd.io/flux/components/notification/receivers/`.

## Como verificar
Conferi o bloco Notification Controller na subseção Components do README oficial de `fluxcd/flux2`.

## Conexões
- [[fluxcd-helm-controller-and-helmrelease-crd]] — Veja também: Helm Controller e o CRD `HelmRelease` para gerenciamento declarativo de charts Helm.
- [[fluxcd-image-automation-controllers-three-crds]] — Veja também: Automação de atualização de imagens no Git: `ImageRepository`, `ImagePolicy` e `ImageUpdateAutomation`.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Repositório oficial fluxcd/flux2](https://github.com/fluxcd/flux2) — Repositório oficial do Flux v2 no GitHub com código-fonte, diagramas de arquitetura, CONTRIBUTING.md e releases SLSA 3.; consultado em 2026-10-03.
