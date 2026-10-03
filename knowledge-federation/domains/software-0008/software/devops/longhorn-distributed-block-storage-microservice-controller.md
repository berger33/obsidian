---
id: software.devops.tranche04.000311
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/longhorn/longhorn/master/README.md", "https://longhorn.io/docs/latest/", "https://github.com/longhorn/longhorn"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Longhorn e arquitetura de controlador dedicado por volume com replicação síncrona

## Em uma frase
O Longhorn é um sistema de armazenamento de bloco distribuído para Kubernetes, incubado na CNCF e 100% open-source sob licença Apache-2.0, construído com primitivas de contêineres e microsserviços. Em vez de um controlador monolítico único compartilhado por todo o cluster, o Longhorn cria um controlador de armazenamento dedicado para cada volume de dispositivo de bloco e replica sincronicamente os dados desse volume através de múltiplas réplicas armazenadas em múltiplos nós. Tanto o controlador de armazenamento quanto as réplicas são orquestrados diretamente usando o próprio Kubernetes.

## Por que importa
Ao isolar cada volume em seu próprio controlador e conjunto de processos de réplica independentes, uma falha ou reinicialização no plano de dados de um volume específico não interrompe o I/O dos demais volumes do cluster, eliminando pontos únicos de falha (no single point of failure).

## Como funciona
Instale o Longhorn em um cluster Kubernetes existente via comando único `kubectl apply`, Helm chart ou catálogo do Rancher para adicionar suporte a `PersistentVolumes` distribuídos sem necessidade de appliances externos de armazenamento.

## Exemplo
Em um cluster de borda de três nós executando bancos de dados relacionais em StatefulSets, cada PVC provisionado pelo Longhorn recebe seu próprio controlador dedicado e três réplicas distribuídas entre os discos locais dos três nós, mantendo disponibilidade caso um nó falhe.

## Limites e trade-offs
Evite agendar todas as réplicas de um volume no mesmo nó físico ou disco subjacente; mantenha políticas de anti-afinidade de nó e zona para que a replicação síncrona proteja efetivamente contra perda de host.

## Como verificar
Inspecione o volume no painel do Longhorn ou via recurso `volumes.longhorn.io` no namespace `longhorn-system` e confirme o estado `attached` e `healthy` com réplicas ativas em nós distintos.

## Conexões
- [[longhorn-incremental-snapshots-and-change-block-backups]] — Veja também: Snapshots incrementais e backups para NFSv4 ou S3 com detecção eficiente de blocos alterados.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
