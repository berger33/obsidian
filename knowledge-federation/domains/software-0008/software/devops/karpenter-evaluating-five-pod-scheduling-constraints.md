---
id: software.devops.tranche03.000262
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

# Avaliação conjunta das cinco restrições de agendamento de pods pelo Karpenter

## Em uma frase
No segundo item da abertura do README (`Evaluating`), o projeto especifica as cinco categorias de restrições de agendamento solicitadas pelos pods que o Karpenter avalia antes de escolher e provisionar um nó: **resource requests** (CPU, memória, armazenamento efêmero, GPUs), **nodeselectors**, **affinities** (node affinity e pod affinity/anti-affinity), **tolerations** e **topology spread constraints**.

## Por que importa
Em grupos de nós tradicionais, combinar múltiplas zonas de disponibilidade, arquiteturas (AMD64 vs ARM64), GPUs e regras de `topologySpreadConstraints` exige criar dezenas de Node Groups separados; o Karpenter resolve a equação de restrições diretamente a partir da especificação do Pod.

## Como funciona
Declare nos manifestos dos seus Pods exatamente os `requests` de recursos, `nodeSelector`, `affinity`, `tolerations` e `topologySpreadConstraints` necessários para que o Karpenter selecione o tipo de instância, zona e arquitetura compatíveis.

## Exemplo
Um lote de pods exige GPU, tolera um taint dedicado e pede distribuição uniforme entre três zonas via `topologySpreadConstraints`; o Karpenter avalia todas as cinco dimensões e provisiona os nós nas zonas corretas.

## Limites e trade-offs
Pods sem `resources.requests` definidos impedem o dimensionamento preciso da capacidade necessária; imponha requests obrigatórios com políticas do Kyverno ou Gatekeeper.

## Como verificar
Conferi o item Evaluating na abertura do README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-four-step-node-lifecycle-optimization]] — Veja também: Ciclo de quatro etapas do Karpenter: Watching, Evaluating, Provisioning e Removing.
- [[karpenter-groupless-provisioning-versus-cluster-autoscaler]] — Veja também: Provisionamento sem grupos de nós (Groupless Autoscaling) e consolidação de cargas.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
