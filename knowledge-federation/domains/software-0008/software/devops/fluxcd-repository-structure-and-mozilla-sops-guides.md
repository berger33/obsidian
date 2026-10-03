---
id: software.devops.tranche01.000058
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

# Estruturação de repositórios GitOps e gestão de segredos Kubernetes com Mozilla SOPS

## Em uma frase
Na seção Quickstart and documentation, o README oficial destaca quatro guias práticos essenciais após o `get-started`: `Ways of structuring your repositories` (`fluxcd.io/flux/guides/repository-structure/`), `Manage Helm Releases` (`helmreleases/`), `Automate image updates to Git` (`image-update/`) e `Manage Kubernetes secrets with Flux and SOPS` (`fluxcd.io/flux/guides/mozilla-sops/`).

## Por que importa
Dois dos maiores bloqueios ao adotar GitOps em produção são decidir como organizar diretórios/repositórios entre equipes e ambientes e como versionar `Secrets` do Kubernetes no Git sem expor dados sensíveis em texto claro; os guias oficiais de estrutura de repositórios e integração com Mozilla SOPS endereçam exatamente essas duas decisões.

## Como funciona
Consulte `https://fluxcd.io/flux/guides/repository-structure/` antes de definir o layout de pastas para múltiplos clusters ou equipes, e siga `https://fluxcd.io/flux/guides/mozilla-sops/` para criptografar Secrets no Git de forma que o Flux os descriptografe dentro do cluster.

## Exemplo
Com o suporte a SOPS documentado no guia oficial, os manifestos criptografados convivem no mesmo repositório Git junto aos demais recursos da aplicação, preservando o fluxo declarativo único.

## Limites e trade-offs
Jamais faça commit de objetos `Secret` do Kubernetes não criptografados em repositórios Git; configure a chave de descriptografia no controlador do Flux seguindo o guia `mozilla-sops`.

## Como verificar
Conferi a lista de quatro guias na seção Quickstart and documentation do README oficial de `fluxcd/flux2`.

## Conexões
- [[fluxcd-image-automation-controllers-three-crds]] — Veja também: Automação de atualização de imagens no Git: `ImageRepository`, `ImagePolicy` e `ImageUpdateAutomation`.
- [[fluxcd-multi-tenancy-prometheus-and-slsa3]] — Veja também: Multi-tenancy, integração nativa com Prometheus e avaliação de segurança SLSA Level 3.

## Fontes
- [Flux v2 — README oficial](https://raw.githubusercontent.com/fluxcd/flux2/main/README.md) — README oficial do Flux v2 com sincronização Git/OCI, integração Prometheus, multi-tenancy, GitOps Toolkit, as cinco famílias de controladores e todos os seus CRDs, quatro guias práticos e diretrizes de suporte.; consultado em 2026-10-03.
- [Flux — Get Started e documentação oficial](https://fluxcd.io/flux/get-started/) — Guia oficial Get Started do Flux v2 para bootstrap em clusters Kubernetes e entrega contínua GitOps.; consultado em 2026-10-03.
