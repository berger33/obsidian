---
id: software.devops.tranche01.000069
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://kubectl.docs.kubernetes.io/references/kustomize/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Conceitos formais do glossário Kustomize: Declarative Application Management, Base, Overlay, Variant e Resource

## Em uma frase
As referências de rodapé e links ao longo do README oficial conectam os termos usados no guia às definições formais do glossário em `https://kubectl.docs.kubernetes.io/references/kustomize/glossary/`: `declarative-application-management` (DAM), `kustomization`, `resource`, `kubernetes-style-object`, `base`, `overlay`, `variant` e `apply`.

## Por que importa
Em equipes grandes de plataforma, alinhar o vocabulário exato do `sig-cli` — entendendo que um `resource` é um arquivo YAML de entrada descrevendo um objeto Kubernetes, uma `base` é uma kustomization reutilizada por outras, um `overlay` é uma kustomization que depende de uma base e uma `variant` é o resultado da aplicação de um overlay sobre uma base — evita confusão na modelagem de repositórios GitOps.

## Como funciona
Consulte o glossário oficial em `https://kubectl.docs.kubernetes.io/references/kustomize/glossary/` e o diretório `examples/` do repositório ao padronizar a nomenclatura e a arquitetura declarativa dos manifestos da organização.

## Exemplo
O documento de proposta arquitetural original do projeto no Kubernetes (`KEP-2377`) também está linkado no README em `keps/sig-cli/2377-Kustomize/README.md`.

## Limites e trade-offs
Seguir os conceitos de Declarative Application Management permite que ferramentas como `kubectl`, Flux (`Kustomization` CRD) e Argo CD operem sobre a mesma estrutura de diretórios sem adaptações proprietárias.

## Como verificar
Conferi os links de referências e glossário no final do README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-labels-with-include-selectors]] — Veja também: Propagação de rótulos com `labels:` e o efeito de `includeSelectors: true` na base e no overlay.
- [[kustomize-community-bug-reporting-and-proposals]] — Veja também: Governança no `sig-cli`, testes presubmit no Prow e fluxo para bugs, features e propostas maiores.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
