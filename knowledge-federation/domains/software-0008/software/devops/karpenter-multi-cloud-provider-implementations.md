---
id: software.devops.tranche03.000264
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

# Arquitetura multi-cloud e as 16 implementações de provedores de nuvem e infraestrutura

## Em uma frase
A seção `Karpenter Implementations` do README documenta que o Karpenter é um projeto multi-cloud com implementações para 16 plataformas e provedores: **AWS** (`aws/karpenter-provider-aws`), **Azure** (`Azure/karpenter-provider-azure`), **AlibabaCloud**, **Bizfly Cloud**, **Clever Cloud**, **Cluster API** (`kubernetes-sigs/karpenter-provider-cluster-api`), **Exoscale**, **GCP**, **Hetzner**, **Huawei Cloud**, **IBM Cloud** (`kubernetes-sigs/karpenter-provider-ibm-cloud`), **Proxmox** (`sergelogvinov/karpenter-provider-proxmox`), **Oracle Cloud Infrastructure (OCI)** (repositório oficial mantido pela Oracle e variante mantida pela Zoom), **Akamai/Linode** (Alpha) e **UpCloud** (variantes Alpha e Beta).

## Por que importa
Separar a lógica central de agendamento, bin-packing e ciclo de vida de nós (`kubernetes-sigs/karpenter`) dos provedores específicos de infraestrutura permite aplicar o mesmo modelo operacional desde grandes nuvens públicas (AWS, Azure, GCP, OCI, IBM) até ambientes Cluster API e virtualização Proxmox.

## Como funciona
Instale o provedor específico da sua infraestrutura (por exemplo, `aws/karpenter-provider-aws`, `Azure/karpenter-provider-azure` ou `kubernetes-sigs/karpenter-provider-cluster-api`) mantendo a versão alinhada ao núcleo do Karpenter.

## Exemplo
Uma empresa opera clusters na AWS com `karpenter-provider-aws` e clusters on-premises gerenciados via Cluster API com `karpenter-provider-cluster-api`.

## Limites e trade-offs
Observe o estágio de maturidade de cada provedor listado no README (por exemplo, provedores marcados como `Alpha` ou `Beta` como Linode e UpCloud) antes de adotá-los em ambientes produtivos críticos.

## Como verificar
Conferi a seção Karpenter Implementations no README oficial de kubernetes-sigs/karpenter.

## Conexões
- [[karpenter-groupless-provisioning-versus-cluster-autoscaler]] — Veja também: Provisionamento sem grupos de nós (Groupless Autoscaling) e consolidação de cargas.
- [[karpenter-oci-and-upcloud-dual-provider-variants]] — Veja também: Distinção entre implementações oficiais e comunitárias em provedores como OCI e UpCloud.

## Fontes
- [Karpenter — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/karpenter/main/README.md) — Visão geral do Karpenter em kubernetes-sigs (ciclo Watching, Evaluating, Provisioning e Removing, 5 restrições de agendamento de pods, 16 implementações multi-cloud de provedores, canais Slack e reuniões do Working Group e Issue Triage).; consultado em 2026-10-03.
- [Karpenter — Repositório Oficial no GitHub](https://github.com/kubernetes-sigs/karpenter) — Repositório oficial do núcleo do Karpenter em kubernetes-sigs com código-fonte, CONTRIBUTING.md e code-of-conduct.md.; consultado em 2026-10-03.
