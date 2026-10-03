---
id: software.devops.tranche04.000314
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

# Componentes Longhorn Manager, Instance Manager, Share Manager e Backing Image Manager

## Em uma frase
O código-fonte do Longhorn é modularizado em componentes especializados documentados na tabela oficial do projeto: **Longhorn Manager** (`longhorn/longhorn-manager`), responsável pela orquestração geral e pelo driver CSI para Kubernetes; **Longhorn Instance Manager** (`longhorn/longhorn-instance-manager`), que gerencia o ciclo de vida das instâncias de controladores e réplicas nos nós; **Longhorn Share Manager** (`longhorn/longhorn-share-manager`), um provisionador NFS que expõe volumes de bloco do Longhorn como volumes `ReadWriteMany` (RWX); **Longhorn Backing Image Manager** (`longhorn/backing-image-manager`), que baixa, sincroniza e remove imagens base nos discos; além do **Longhorn UI** (`longhorn/longhorn-ui`) e **Longhorn CLI** (`longhorn/cli`).

## Por que importa
Compreender a divisão de responsabilidades entre `longhorn-manager` (plano de controle e CSI), `instance-manager` (execução de processos de engine/réplica por nó) e `share-manager` (exportação NFS para RWX) acelera o diagnóstico de incidentes em clusters multi-nó.

## Como funciona
Ao depurar problemas de anexação de volume RWO, inspecione os pods `longhorn-manager` e `instance-manager`; ao investigar compartilhamento de arquivos RWX entre múltiplos pods, verifique também o pod do `share-manager` associado ao volume.

## Exemplo
Quando uma aplicação web escalada horizontalmente exige um diretório compartilhado `ReadWriteMany`, o Longhorn instancia automaticamente um pod gerenciado pelo `longhorn-share-manager` que monta o volume de bloco subjacente e o exporta via servidor NFS interno para os pods consumidores.

## Limites e trade-offs
Não exclua nem reinicie abruptamente pods `instance-manager` em múltiplos nós ao mesmo tempo, pois cada `instance-manager` hospeda os processos de controlador e réplica dos volumes ativos naquele nó.

## Como verificar
Execute `kubectl -n longhorn-system get pods` e confirme a saúde dos DaemonSets `longhorn-manager`, pods `instance-manager-*` e `csi-*` em todos os nós de armazenamento.

## Conexões
- [[longhorn-automated-non-disruptive-software-upgrades]] — Veja também: Upgrade automatizado e não disruptivo da pilha de software do Longhorn.
- [[longhorn-v1-engine-iscsi-and-v2-spdk-data-engines]] — Veja também: Motores de dados Longhorn Engine V1 (iSCSI) e Longhorn SPDK Engine V2 (SPDK).

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
