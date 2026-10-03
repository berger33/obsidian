---
id: software.devops.tranche03.000261
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md", "https://github.com/kubernetes-sigs/karpenter"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ciclo de quatro etapas do Karpenter: Watching, Evaluating, Provisioning e Removing

## Em uma frase
O README oficial no repositório kubernetes-sigs/karpenter explica que o Karpenter melhora a eficiência e o custo de executar cargas de trabalho em clusters Kubernetes por meio de quatro ações contínuas: **Watching** (observar pods que o agendador do Kubernetes marcou como não agendáveis — `unschedulable`), **Evaluating** (avaliar todas as restrições de agendamento solicitadas pelos pods), **Provisioning** (provisionar nós que atendam exatamente aos requisitos dos pods) e **Removing** (remover os nós quando eles não são mais necessários).

## Por que importa
Diferentemente do Cluster Autoscaler tradicional baseado em grupos estáticos de nós pré-configurados (Node Groups / Auto Scaling Groups), o Karpenter provisiona diretamente a capacidade de computação sob medida para os pods pendentes e consolida/remove nós ociosos sem ficar preso a templates fixos de grupo.

## Como funciona
Implante o Karpenter no cluster Kubernetes para automatizar o ciclo completo de criação e remoção de nós diretamente a partir da fila de pods `Pending`/`Unschedulable`.

## Exemplo
Quando um pico de tráfego dispara dezenas de novas réplicas via HPA ou KEDA que não cabem nos nós atuais, o Karpenter observa os pods não agendáveis, calcula a capacidade ideal, provisiona os novos nós em segundos e os remove assim que o pico passa.

## Limites e trade-offs
Para que a etapa `Removing` desaloje pods e consolide nós sem interromper serviços críticos, configure `PodDisruptionBudgets` (PDBs) adequados nas aplicações.

## Como verificar
Conferi a seção inicial Karpenter no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-evaluating-five-pod-scheduling-constraints]] — Veja também: Avaliação conjunta das cinco restrições de agendamento de pods pelo Karpenter.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
