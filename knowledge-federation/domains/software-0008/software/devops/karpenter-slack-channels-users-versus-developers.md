---
id: software.devops.tranche03.000268
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

# Canais de suporte e design no Slack do Kubernetes: #karpenter versus #karpenter-dev

## Em uma frase
A seção `Community, discussion, contribution, and support` do README separa claramente os dois canais de comunicação no Slack do Kubernetes (`slack.k8s.io`): **#karpenter** (destinado a quem está usando e implantando o Karpenter, para tirar dúvidas sobre configuração ou troubleshooting) e **#karpenter-dev** (destinado a quem está contribuindo ou desenvolvendo com o Karpenter, para questões aprofundadas de código e discussões de design).

## Por que importa
Separar o suporte operacional de configuração (`#karpenter`) das discussões de arquitetura do controlador e provedores (`#karpenter-dev`) evita que dúvidas urgentes de operadores se percam em debates de implementação Go e vice-versa.

## Como funciona
Direcione dúvidas operacionais, ajustes de NodePool e troubleshooting de agendamento ao canal `#karpenter` e utilize `#karpenter-dev` quando estiver desenvolvendo código para o core ou para um provider.

## Exemplo
Um engenheiro de SRE consulta `#karpenter` para ajustar regras de consolidação, enquanto um desenvolvedor de provedor discute uma interface do core em `#karpenter-dev`.

## Limites e trade-offs
Ao pedir ajuda em `#karpenter`, informe se está usando o provedor da AWS, Azure ou outro, bem como a versão do Karpenter e do Kubernetes.

## Como verificar
Conferi a seção Community, discussion, contribution, and support no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-zero-downtime-node-updates-and-drift]] — Veja também: Automação de atualizações de nós do cluster sem indisponibilidade (Zero Downtime Updates).
- [[karpenter-working-group-and-issue-triage-meetings]] — Veja também: Calendário de reuniões do Working Group (quintas) e Issue Triage (segundas) em dois repositórios.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
