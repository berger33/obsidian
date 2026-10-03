---
id: software.devops.tranche01.000068
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
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md", "https://kubectl.docs.kubernetes.io/references/kustomize/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Propagação de rótulos com `labels:` e o efeito de `includeSelectors: true` na base e no overlay

## Em uma frase
Tanto no exemplo da base (`pairs: app: myapp`) quanto no exemplo do overlay (`pairs: variant: prod`) do README oficial, o bloco `labels:` do `kustomization.yaml` utiliza a configuração `- includeSelectors: true`.

## Por que importa
No Kubernetes, objetos como `Deployment` e `Service` conectam-se aos `Pods` por meio de campos de seletor (`spec.selector.matchLabels` e `spec.selector`); configurar `includeSelectors: true` instrui o Kustomize a injetar o rótulo não apenas nos metadados (`metadata.labels`), mas também nos seletores e no template dos Pods, mantendo o pareamento consistente entre Service, Deployment e Pods daquela variante.

## Como funciona
Use a seção `labels:` com `includeSelectors: true` quando quiser que o par chave-valor identifique e isole tanto os recursos quanto os seletores de tráfego e de réplicas daquela base ou variante.

## Exemplo
No overlay de produção do README, adicionar `variant: prod` com `includeSelectors: true` garante que o Deployment e o Service de produção selecionem especificamente os Pods rotulados com `variant: prod`.

## Limites e trade-offs
Em recursos `Deployment` já existentes no cluster, lembre-se de que o Kubernetes trata `spec.selector.matchLabels` como imutável após a criação; portanto, defina `includeSelectors: true` desde a criação inicial do recurso ou gerencie a transição com cuidado.

## Como verificar
Conferi os blocos `labels:` nos dois exemplos de `kustomization.yaml` (base e overlay) do README oficial de `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-git-workflow-sibling-repos-without-submodules]] — Veja também: Fluxo Git com repositórios irmãos em disco: consumindo bases upstream sem precisar de Git submodules.
- [[kustomize-glossary-declarative-application-management]] — Veja também: Conceitos formais do glossário Kustomize: Declarative Application Management, Base, Overlay, Variant e Resource.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
