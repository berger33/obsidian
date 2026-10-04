---
id: software.devops.tranche04.000303
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
fontes: ["https://raw.githubusercontent.com/rook/rook/master/README.md", "https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/", "https://github.com/rook/rook"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pré-requisitos de dispositivos brutos, partições, LVM e PVs em modo block para OSDs no Rook

## Em uma frase
Para configurar um cluster de armazenamento Ceph com o Rook, a documentação oficial exige ao menos uma das seguintes opções de armazenamento local disponível nos nós: dispositivos brutos (`raw devices`, sem partições e sem sistema de arquivos formatado), partições brutas (`raw partitions`, sem sistema de arquivos formatado), volumes lógicos LVM (`LVM Logical Volumes`, sem sistema de arquivos formatado), dispositivos criptografados ou multipath sem sistema de arquivos formatado, ou `Persistent Volumes` dinâmicos fornecidos por uma `StorageClass` em modo `block`.

## Por que importa
Os Object Storage Daemons (`rook-ceph-osd`) do Ceph gerenciam diretamente o layout de bloco via BlueStore e recusam discos que já contenham sistemas de arquivos montados ou formatados para evitar perda catastrófica de dados do sistema operacional host. Compreender esse requisito evita o erro clássico em que os pods `rook-ceph-osd` nunca são criados após aplicar `cluster.yaml`.

## Como funciona
Nos nós dedicados ao Ceph em bare-metal, disponibilize discos ou partições completamente limpos (`wipefs`/`sgdisk --zap-all` quando aplicável em discos novos) ou configure `cluster-on-pvc.yaml` consumindo `PersistentVolumes` em `volumeMode: Block` quando operar em nuvens públicas dinâmicas.

## Exemplo
Em um cluster recém-instalado onde apenas os pods `rook-ceph-mon` e `rook-ceph-mgr` subiram e nenhum `rook-ceph-osd` foi criado, o operador de infraestrutura inspeciona os jobs `rook-ceph-osd-prepare-<node>` e descobre que os discos secundários haviam sido formatados com `ext4` pelo instalador do SO; após limpar o cabeçalho dos discos de dados dedicados, os OSDs entram em estado `Running`.

## Limites e trade-offs
Nunca execute limpeza de disco em dispositivos do sistema operacional e nunca teste o Rook diretamente no host físico de trabalho; conforme alerta em destaque no Quickstart oficial, utilize sempre máquinas virtuais em testes para evitar que dispositivos locais sejam consumidos por engano.

## Como verificar
Inspecione os logs dos pods `rook-ceph-osd-prepare-*` no namespace `rook-ceph` e confirme que cada dispositivo elegível sem filesystem gera um pod `rook-ceph-osd-<id>` em estado `Running`.

## Conexões
- [[rook-kubernetes-versions-and-cpu-architectures]] — Veja também: Versões do Kubernetes v1.31 a v1.37 e arquiteturas amd64 e arm64 suportadas pelo Rook.
- [[rook-operator-deployment-crds-common-and-csi-operator]] — Veja também: Implantação do Rook Operator com crds.yaml, common.yaml, csi-operator.yaml e operator.yaml.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
