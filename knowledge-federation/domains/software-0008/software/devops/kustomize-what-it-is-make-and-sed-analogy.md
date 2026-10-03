---
id: software.devops.tranche01.000061
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

# Kustomize: customização de YAML bruto e livre de templates com a semântica de `make` e `sed`

## Em uma frase
O README oficial no repositório kubernetes-sigs/kustomize explica que o `kustomize` permite customizar arquivos YAML brutos e livres de templates (template-free) para múltiplos propósitos, deixando o YAML original intocado e utilizável tal como está; voltado ao Kubernetes, ele entende e aplica patches em objetos de API no estilo Kubernetes, sendo comparado pelo próprio README ao `make` (porque o que ele faz é declarado em um arquivo) e ao `sed` (porque ele emite texto editado).

## Por que importa
Ferramentas baseadas em motores de template de texto substituem trechos do YAML por marcadores `{{ ... }}`, tornando o arquivo base inválido como YAML puro e difícil de atualizar com `git rebase` quando vem de um repositório externo; ao manter o YAML original intacto e válido, o Kustomize permite aplicar o manifesto base diretamente ou transformá-lo por composição declarativa.

## Como funciona
Mantenha os manifestos Kubernetes como arquivos YAML válidos sem placeholders de template e declare todas as transformações (labels, geradores, patches) em um arquivo `kustomization.yaml`.

## Exemplo
O projeto é patrocinado pelo grupo de interesse especial `sig-cli` do Kubernetes (formalizado no KEP-2377), com documentação geral em `https://kubectl.docs.kubernetes.io/references/kustomize/`.

## Limites e trade-offs
Como o Kustomize conhece a estrutura dos objetos de API do Kubernetes (`apiVersion`, `kind`, `metadata`, `spec`), suas edições operam sobre a árvore semântica dos recursos e não como substituição cega de strings.

## Como verificar
Conferi os três parágrafos de abertura do README oficial em `kubernetes-sigs/kustomize`.

## Conexões
- [[kustomize-embedded-in-kubectl-version-matrix]] — Veja também: Integração nativa no `kubectl`: histórico de versões embutidas e verificação com `kubectl version --client`.

## Fontes
- [Kustomize — README oficial](https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/README.md) — README oficial do Kustomize com customização YAML template-free (analogia make/sed), matriz de versões embutidas no kubectl, kustomization.yaml com labels/includeSelectors/configMapGenerator, kustomize build e overlays com patches.; consultado em 2026-10-03.
- [Kustomize — documentação oficial de referência](https://kubectl.docs.kubernetes.io/references/kustomize/) — Documentação oficial de referência e glossário do Kustomize mantida pelo sig-cli do Kubernetes.; consultado em 2026-10-03.
