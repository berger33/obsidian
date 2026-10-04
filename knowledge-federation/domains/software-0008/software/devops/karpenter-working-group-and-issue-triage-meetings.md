---
id: software.devops.tranche03.000269
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

# Calendário de reuniões do Working Group (quintas) e Issue Triage (segundas) em dois repositórios

## Em uma frase
As subseções `Working Group Meetings`, `Issue Triage Meetings` e `Meeting Resources` do README documentam a cadência de governança comunitária: as reuniões do **Working Group** ocorrem quinzenalmente às quintas-feiras alternando entre `9:00 PT` e `15:00 PT`, enquanto as reuniões semanais de **Issue Triage** ocorrem às segundas-feiras (alternando mensalmente entre `9:00 PT` e `15:00 PT`) tanto para o repositório core `kubernetes-sigs/karpenter` quanto para o provedor `aws/karpenter-provider-aws`, com link Zoom, Google Calendar e ata pública (`Working Group Log`).

## Por que importa
A alternância entre `9:00 PT` e `15:00 PT` permite a participação tanto de equipes na Europa/Américas quanto na Ásia-Pacífico, e a separação da triagem entre `kubernetes-sigs/karpenter` e `aws/karpenter-provider-aws` reflete a arquitetura desacoplada entre o núcleo agnóstico e o provedor de nuvem.

## Como funciona
Consulte o `Working Group Log` e o calendário público quando acompanhar issues abertas ou propostas de novas funcionalidades no núcleo ou no provedor AWS.

## Exemplo
Um engenheiro acompanha a reunião de segunda-feira de Issue Triage para priorizar a correção de um comportamento de consolidação observado em produção.

## Limites e trade-offs
Verifique no convite do calendário oficial qual repositório (`kubernetes-sigs/karpenter` ou `aws/karpenter-provider-aws`) e qual horário (`9:00 PT` ou `15:00 PT`) correspondem à segunda-feira daquela semana.

## Como verificar
Conferi as subseções Working Group Meetings, Issue Triage Meetings e Meeting Resources no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-slack-channels-users-versus-developers]] — Veja também: Canais de suporte e design no Slack do Kubernetes: #karpenter versus #karpenter-dev.
- [[karpenter-contributing-guide-and-code-of-conduct]] — Veja também: Guia de contribuição, issues para iniciantes e Código de Conduta do Kubernetes.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
