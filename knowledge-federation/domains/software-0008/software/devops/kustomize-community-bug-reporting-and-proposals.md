---
id: software.devops.tranche01.000070
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://github.com/kubernetes-sigs/kustomize"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Governança no `sig-cli`, testes presubmit no Prow e fluxo para bugs, features e propostas maiores

## Em uma frase
A seção Community e os badges do README oficial detalham onde acompanhar a qualidade e contribuir com o Kustomize: os jobs de presubmit rodam na infraestrutura Prow do Kubernetes (`prow.k8s.io`), e a comunidade divide as contribuições em três caminhos documentados — relatar um bug (`kubectl.docs.kubernetes.io/contributing/kustomize/bugs/`), contribuir uma feature menor (`contributing/kustomize/features/`) ou propor uma melhoria arquitetural maior no diretório `proposals/` do repositório (`github.com/kubernetes-sigs/kustomize/tree/master/proposals`), sob o Kubernetes Code of Conduct.

## Por que importa
Como o Kustomize é embarcado diretamente dentro do binário `kubectl` distribuído para toda a comunidade Kubernetes, mudanças significativas de comportamento exigem passar pelo processo de proposta em `proposals/` e pela bateria de presubmit do `sig-cli` no Prow.

## Como funciona
Siga o guia `contributing/kustomize/bugs/` ao abrir issues com casos mínimos reproduzíveis de `kustomize build`, `contributing/kustomize/features/` para novas funcionalidades pontuais e `proposals/` para alterações estruturais de design.

## Exemplo
O badge do Prow (`kustomize-presubmit-master`) e o Go Report Card no topo do README permitem verificar o status dos testes automatizados da branch principal a qualquer momento.

## Limites e trade-offs
Toda participação nos canais do `sig-cli` e no repositório `kubernetes-sigs/kustomize` segue o `code-of-conduct.md` do Kubernetes.

## Como verificar
Conferi a seção Community e os badges no README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-glossary-declarative-application-management]] — Veja também: Conceitos formais do glossário Kustomize: Declarative Application Management, Base, Overlay, Variant e Resource.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Repositório oficial kubernetes-sigs/kustomize](https://github.com/kubernetes-sigs/kustomize) — Repositório oficial do Kustomize no GitHub (sig-cli) com examples/, proposals/ e releases.; consultado em 2026-10-03.
