---
id: software.devops.tranche01.000057
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

# Automação de atualização de imagens no Git: `ImageRepository`, `ImagePolicy` e `ImageUpdateAutomation`

## Em uma frase
O quinto item da subseção Components (junto ao guia `Automate image updates to Git` em `fluxcd.io/flux/guides/image-update/`) apresenta os **Image Automation Controllers** (`fluxcd.io/flux/components/image/`), estruturados em três CRDs: `ImageRepository`, `ImagePolicy` e `ImageUpdateAutomation`.

## Por que importa
Atualizar manualmente a tag de uma imagem de contêiner no repositório GitOps a cada build de CI é repetitivo, mas alterar a imagem direto no cluster sem passar pelo Git violaria o princípio GitOps; esses três CRDs escaneiam o registry (`ImageRepository`), escolhem a tag mais recente segundo uma regra (`ImagePolicy`) e fazem commit da mudança de volta no repositório Git (`ImageUpdateAutomation`).

## Como funciona
Configure um `ImageRepository` apontando para o registro de contêineres, defina a regra de seleção de versão num `ImagePolicy` (por exemplo SemVer) e use `ImageUpdateAutomation` para gravar a nova tag no repositório Git conforme `https://fluxcd.io/flux/guides/image-update/`.

## Exemplo
Como a atualização é comitada pelo próprio Flux no repositório Git e depois aplicada pelo fluxo normal do `Source Controller` + `Kustomize`/`Helm Controller`, todo o histórico de qual imagem entrou em produção permanece auditável no `git log`.

## Limites e trade-offs
Para que o `ImageUpdateAutomation` consiga fazer push das alterações de tag de volta para o repositório, a credencial configurada para aquele repositório Git precisa ter permissão de escrita.

## Como verificar
Conferi a seção Quickstart and documentation e o item Image Automation Controllers em Components no README oficial.

## Conexões
- [[fluxcd-notification-controller-provider-alert-receiver]] — Veja também: Notification Controller: eventos de saída e webhooks de entrada com `Provider`, `Alert` e `Receiver`.
- [[fluxcd-repository-structure-and-mozilla-sops-guides]] — Veja também: Estruturação de repositórios GitOps e gestão de segredos Kubernetes com Mozilla SOPS.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Flux — Get Started e documentação oficial](https://fluxcd.io/flux/get-started/) — Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.; consultado em 2026-10-03.
