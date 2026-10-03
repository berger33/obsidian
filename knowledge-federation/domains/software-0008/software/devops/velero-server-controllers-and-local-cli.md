---
id: software.devops.tranche02.000112
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

# Arquitetura cliente-servidor: controladores em réplica única no cluster e CLI local

## Em uma frase
O README oficial e a seção `How Velero works` de `ARCHITECTURE.md` explicam que o Velero consiste em dois elementos principais: um servidor (conjunto de controladores) executado como um deployment de réplica única dentro do cluster Kubernetes e um cliente de linha de comando (`velero`) executado localmente, sendo os backups e restaurações dirigidos por Custom Resources do Kubernetes e reconciliados pelo servidor.

## Por que importa
Como as operações são modeladas como Custom Resources nativos do Kubernetes, o estado dos backups pode ser inspecionado tanto pela CLI `velero` quanto por ferramentas padrão do ecossistema Kubernetes e controladores GitOps.

## Como funciona
Instale o servidor do Velero no cluster como deployment de réplica única e utilize a CLI local `velero` (ou manifestos declarativos das CRDs do Velero) para disparar e auditar operações de backup e restore.

## Exemplo
Um operador dispara um backup via CLI local, que cria o Custom Resource correspondente no cluster para ser reconciliado pelo servidor do Velero.

## Limites e trade-offs
Se o próprio cluster sofrer falha catastrófica total, a restauração ocorrerá em um novo cluster apontando o servidor do Velero recém-instalado para o mesmo armazenamento de objetos externo.

## Como verificar
Conferi a seção Overview do README e a seção How Velero works de `ARCHITECTURE.md` em `vmware-tanzu/velero`.

## Conexões
- [[velero-backup-restore-and-cluster-migration]] — Veja também: Visão geral do Velero: backup, restauração, migração e replicação de clusters.
- [[velero-file-system-backup-and-csi-data-mover]] — Veja também: Movimentação de dados de volumes: file-system backup, data mover CSI e plugins de provedor.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
