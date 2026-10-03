---
id: software.devops.tranche02.000116
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte a ambientes IPv4, IPv6 e dual-stack no Velero

## Em uma frase
O README oficial registra na seção de compatibilidade que o Velero suporta ambientes IPv4, IPv6 e dual-stack, observando que o suporte para essas topologias foi testado a partir do Velero `v1.8`.

## Por que importa
Clusters Kubernetes modernos em telecomunicações, borda e nuvens públicas frequentemente operam em IPv6 puro ou dual-stack para evitar exaustão de endereços IPv4, exigindo que o agente de backup e os pods auxiliares de movimentação de dados funcionem sem assumir IPv4 fixo.

## Como funciona
Ao implantar o Velero em clusters IPv6 ou dual-stack, certifique-se de que os endpoints do Object Storage e os plugins de provedor também suportem resolução e tráfego na família de endereços utilizada pelo cluster.

## Exemplo
Um cluster Kubernetes dual-stack executa o servidor do Velero e restaura serviços mantendo a configuração de famílias de IP dos manifests.

## Limites e trade-offs
Ao migrar recursos de um cluster dual-stack para um cluster somente IPv4, revise os campos `ipFamilies` e `ipFamilyPolicy` dos objetos `Service` durante a restauração.

## Como verificar
Conferi a nota de suporte a IPv4, IPv6 e dual-stack (testado desde a `v1.8`) logo abaixo da tabela em Velero compatibility matrix no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-n-minus-2-upgrade-restore-guarantee]] — Veja também: Garantia de restauração de backups entre versões N-2 menores do Velero.
- [[velero-design-proposals-and-implemented-archive]] — Veja também: Processo de propostas de design em design/ e histórico em design/Implemented/.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
