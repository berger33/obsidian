---
id: software.devops.tranche02.000113
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
fontes: ["https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Movimentação de dados de volumes: file-system backup, data mover CSI e plugins de provedor

## Em uma frase
A seção `How Velero works` de `ARCHITECTURE.md` detalha que os dados de volumes são movidos pelo mecanismo embutido de `file-system backup` (`velero.io/docs/main/file-system-backup/`) e pelo `data mover` para snapshots CSI (`velero.io/docs/main/csi-snapshot-data-movement/`), enquanto as operações de armazenamento de objetos e de snapshots de volumes são tratadas por meio de plugins de provedor (`provider plugins`).

## Por que importa
Nem todo armazenamento possui suporte nativo a snapshots de bloco na nuvem; combinar plugins de provedor, snapshots CSI com movimentação de dados e backup no nível do sistema de arquivos permite proteger volumes tanto em nuvens públicas quanto em ambientes on-premises.

## Como funciona
Escolha a estratégia de proteção de volumes adequada a cada StorageClass: plugins nativos de snapshot do provedor, CSI snapshot data movement ou file-system backup para volumes sem suporte a snapshot.

## Exemplo
Em um cluster híbrido, bancos de dados usam snapshots CSI com data mover para object storage, enquanto volumes NFS usam file-system backup.

## Limites e trade-offs
Realizar backup de volumes ativos sem congelar ou coordenar a escrita da aplicação pode gerar snapshots apenas crash-consistent; configure hooks de pré e pós-backup quando necessário.

## Como verificar
Conferi a seção How Velero works em `ARCHITECTURE.md` no repositório `vmware-tanzu/velero`.

## Conexões
- [[velero-server-controllers-and-local-cli]] — Veja também: Arquitetura cliente-servidor: controladores em réplica única no cluster e CLI local.
- [[velero-kubernetes-compatibility-matrix]] — Veja também: Matriz de compatibilidade do Velero 1.14 a 1.18 com versões do Kubernetes.

## Fontes
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
