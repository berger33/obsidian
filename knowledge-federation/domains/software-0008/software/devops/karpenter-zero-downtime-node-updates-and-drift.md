---
id: software.devops.tranche03.000267
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

# Automação de atualizações de nós do cluster sem indisponibilidade (Zero Downtime Updates)

## Em uma frase
Na seção `Talks`, o README destaca a referência técnica de 2025 `"Automating Kubernetes Cluster Updates: Achieving Zero Downtime Effortlessly @ KubeCon"`, conectada ao ciclo de `Provisioning` e `Removing` do Karpenter para renovação contínua de nós.

## Por que importa
Atualizar a versão do Kubernetes ou a imagem base (AMI/OS image) de centenas de nós manualmente com `kubectl cordon` e `kubectl drain` é trabalhoso e arriscado; o Karpenter automatiza a substituição gradual dos nós respeitando a capacidade de agendamento e os orçamentos de disrupção dos pods.

## Como funciona
Utilize o gerenciamento declarativo de ciclo de vida de nós do Karpenter em conjunto com `PodDisruptionBudgets`, `readinessProbes` e `preStop` hooks para realizar upgrades de imagem e versão do Kubernetes sem downtime.

## Exemplo
Quando uma nova imagem de nó com patches de segurança do kernel Linux é publicada, o Karpenter provisiona nós atualizados, migra as cargas gradualmente e remove os nós antigos sem interromper o tráfego.

## Limites e trade-offs
Atualizações de nós sem downtime exigem que os serviços críticos tenham pelo menos duas réplicas distribuídas e tratem graciosamente o sinal `SIGTERM`.

## Como verificar
Conferi o primeiro item da lista Talks (04/03/2025, Automating Kubernetes Cluster Updates) no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-cluster-api-and-proxmox-hybrid-providers]] — Veja também: Extensão do Karpenter para ambientes híbridos e on-premises com Cluster API e Proxmox.
- [[karpenter-slack-channels-users-versus-developers]] — Veja também: Canais de suporte e design no Slack do Kubernetes: #karpenter versus #karpenter-dev.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
