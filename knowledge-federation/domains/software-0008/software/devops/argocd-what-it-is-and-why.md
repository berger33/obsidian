---
id: software.devops.tranche01.000011
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
fontes: ["https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md", "https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Argo CD: entrega contínua declarativa GitOps para Kubernetes e seus dois princípios centrais

## Em uma frase
O README oficial no repositório argoproj/argo-cd define o Argo CD como uma ferramenta declarativa de entrega contínua (CD) baseada em GitOps para Kubernetes, fundamentada em duas premissas explícitas na seção Why Argo CD?: (1) definições de aplicações, configurações e ambientes devem ser declarativas e controladas por versão; e (2) a implantação e o gerenciamento do ciclo de vida das aplicações devem ser automatizados, auditáveis e fáceis de entender.

## Por que importa
Quando deploys em Kubernetes são feitos manualmente com comandos imperativos de linha de comando ou scripts de CI que empurram alterações sem reconciliação contínua, o estado real do cluster diverge rapidamente do que está no repositório Git (configuration drift); o modelo GitOps do Argo CD mantém o cluster sincronizado com a fonte declarativa.

## Como funciona
Versione os manifestos Kubernetes (ou charts Helm / overlays Kustomize) no Git e configure o Argo CD no cluster para reconciliar continuamente o estado desejado com o estado vivo da API do Kubernetes.

## Exemplo
O projeto disponibiliza uma demonstração interativa ao vivo em https://cd.apps.argoproj.io/ e a documentação completa em https://argo-cd.readthedocs.io/, além de artefatos assinados com selo SLSA Level 3 no repositório.

## Limites e trade-offs
O guia Getting Started lembra na nota de abertura que o operador deve ter familiaridade prévia com as ferramentas de base sobre as quais o Argo CD opera (Kubernetes, Git e empacotadores de manifestos), remetendo a understand_the_basics.md.

## Como verificar
Conferi as seções What is Argo CD?, Why Argo CD? e Documentation no README oficial de argoproj/argo-cd.

## Conexões
- [[argocd-install-server-side-apply-262kb-limit]] — Veja também: Instalação com `kubectl apply --server-side --force-conflicts` e o limite de 262 KB dos CRDs.

## Fontes
- [Argo CD — README oficial](https://raw.githubusercontent.com/argoproj/argo-cd/master/README.md) — README oficial do Argo CD com definição GitOps para Kubernetes, os dois motivos centrais em Why Argo CD?, USERS.md, documentação, live demo, integrações do ecossistema e canais da comunidade.; consultado em 2026-10-03.
- [Argo CD — Getting Started (docs/getting_started.md)](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/getting_started.md) — Guia oficial Getting Started do Argo CD: instalação com --server-side --force-conflicts (limite de 262 KB), modo core, segredo argocd-redis, LoadBalancer/Ingress/port-forward, argocd-initial-admin-secret e argocd cluster add.; consultado em 2026-10-03.
