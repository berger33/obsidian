---
id: software.devops.tranche04.000312
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

# Snapshots incrementais e backups para NFSv4 ou S3 com detecção eficiente de blocos alterados

## Em uma frase
Entre os recursos centrais destacados no README oficial do Longhorn estão a geração de snapshots incrementais do armazenamento de bloco, o agendamento recorrente de snapshots e backups, e o envio de backups para armazenamento secundário externo — suportando servidores **NFSv4** ou **object storage compatível com S3** — construído sobre detecção eficiente de blocos alterados (change block detection) através da biblioteca `longhorn/backupstore`.

## Por que importa
Snapshots locais no cluster protegem contra erros lógicos imediatos, mas não sobrevivem à perda total do cluster Kubernetes. O backup incremental baseado em blocos alterados para S3 ou NFSv4 transfere apenas os deltas modificados, reduzindo consumo de rede e armazenamento externo enquanto garante recuperação de desastres (DR) entre clusters.

## Como funciona
Configure um Backup Target (bucket S3 ou export NFSv4) no Longhorn e defina políticas de `RecurringJob` para criar snapshots locais frequentes e exportar backups incrementais periódicos para os volumes críticos de produção.

## Exemplo
Uma equipe de plataforma configura um bucket S3 externo como Backup Target no Longhorn e agenda snapshots a cada 4 horas com backup diário; durante um exercício de DR em um cluster secundário, os volumes são restaurados diretamente do bucket S3 com perda mínima de RPO.

## Limites e trade-offs
Não confunda snapshots dentro do cluster com backups externos: snapshots residem junto às réplicas nos discos dos nós do próprio cluster e não substituem um Backup Target NFSv4 ou S3 externo.

## Como verificar
Dispare um backup manual ou via `RecurringJob` para o alvo S3/NFSv4 configurado e valide a conclusão do snapshot e a listagem do backup disponível para restauração na UI ou via CRD `backups.longhorn.io`.

## Conexões
- [[longhorn-distributed-block-storage-microservice-controller]] — Veja também: Longhorn e arquitetura de controlador dedicado por volume com replicação síncrona.
- [[longhorn-automated-non-disruptive-software-upgrades]] — Veja também: Upgrade automatizado e não disruptivo da pilha de software do Longhorn.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
