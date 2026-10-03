---
id: software.devops.tranche03.000263
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

# Provisionamento sem grupos de nós (Groupless Autoscaling) e consolidação de cargas

## Em uma frase
A abertura e a seção `Talks` do README oficial (`Groupless Autoscaling with Karpenter`, `Karpenter vs Kubernetes Cluster Autoscaler` e `Workload Consolidation with Karpenter`) destacam a mudança de paradigma do projeto: substituir o escalonamento preso a grupos de instâncias homogêneas pelo provisionamento **groupless** (sem grupos fixos) combinado à consolidação ativa de cargas de trabalho (`Workload Consolidation`) quando nós ficam subutilizados.

## Por que importa
Manter grupos separados para cada tamanho de VM gera fragmentação severa (capacidade ociosa espalhada em vários grupos); o provisionamento groupless escolhe dinamicamente entre dezenas de tipos de instância permitidos e substitui nós caros por instâncias menores quando a carga diminui.

## Como funciona
Configure seus NodePools/Provisioners do Karpenter com listas amplas de famílias e tamanhos de instâncias compatíveis em vez de restringir a um único tipo fixo de máquina virtual.

## Exemplo
Durante a redução de tráfego noturno, o mecanismo de consolidação do Karpenter drena três nós grandes subutilizados e reagenda os pods restantes em um único nó menor, desligando a capacidade excedente.

## Limites e trade-offs
Cargas que não suportam realocação frequente (como jobs longos sem checkpointing) devem ser marcadas para não sofrer consolidação disruptiva durante sua execução.

## Como verificar
Conferi a abertura e a seção Talks no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-evaluating-five-pod-scheduling-constraints]] — Veja também: Avaliação conjunta das cinco restrições de agendamento de pods pelo Karpenter.
- [[karpenter-multi-cloud-provider-implementations]] — Veja também: Arquitetura multi-cloud e as 16 implementações de provedores de nuvem e infraestrutura.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
