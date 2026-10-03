---
id: software.devops.tranche03.000265
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

# Distinção entre implementações oficiais e comunitárias em provedores como OCI e UpCloud

## Em uma frase
Na lista `Karpenter Implementations`, o README faz questão de distinguir quando um provedor possui múltiplas implementações com mantenedores diferentes: para **Oracle Cloud Infrastructure (OCI)**, lista tanto a implementação oficialmente suportada e mantida pela Oracle (`oracle/karpenter-provider-oci`) quanto a mantida pela Zoom (`zoom/karpenter-oci`); e para **UpCloud**, distingue a variante mantida por `kubekanvas` (Alpha) da variante mantida pela comunidade `upcloud-tools` (Beta).

## Por que importa
Escolher por engano um fork ou implementação histórica quando já existe um provedor oficialmente mantido pelo fabricante da nuvem (ou vice-versa) impacta o suporte a novas famílias de instâncias e correções de segurança.

## Como funciona
Antes de instalar um provedor do Karpenter, verifique na seção `Karpenter Implementations` do README oficial qual repositório é mantido oficialmente pelo provedor de nuvem ou pelo SIG e qual o seu nível de maturidade.

## Exemplo
Uma equipe migrando cargas para Oracle Cloud seleciona o repositório oficial `oracle/karpenter-provider-oci` indicado na lista do projeto.

## Limites e trade-offs
Valide sempre a atividade de releases e a matriz de versões do Kubernetes no repositório específico do provedor escolhido.

## Como verificar
Conferi os itens Oracle Cloud Infrastructure (OCI) e UpCloud na seção Karpenter Implementations do README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-multi-cloud-provider-implementations]] — Veja também: Arquitetura multi-cloud e as 16 implementações de provedores de nuvem e infraestrutura.
- [[karpenter-cluster-api-and-proxmox-hybrid-providers]] — Veja também: Extensão do Karpenter para ambientes híbridos e on-premises com Cluster API e Proxmox.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
