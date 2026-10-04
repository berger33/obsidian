---
id: software.devops.tranche04.000307
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

# Verificação de saúde HEALTH_OK com Rook Toolbox e plugin kubectl rook-ceph

## Em uma frase
Para verificar a saúde interna do cluster Ceph e executar comandos administrativos `ceph`, a documentação oficial do Rook orienta implantar o pod `rook-ceph-tools` (Rook toolbox) ou utilizar o plugin oficial `kubectl rook-ceph` (`github.com/rook/kubectl-rook-ceph`). Dentro do toolbox, o comando `ceph status` deve reportar `health: HEALTH_OK`, todos os monitores em quórum (`mon: 3 daemons, quorum a,b,c`), um gerenciador ativo com standby (`mgr: a(active), standbys: b`) e pelo menos três OSDs com status `up` e `in` (`3 osds: 3 up, 3 in`).

## Por que importa
Apenas observar pods `Running` no Kubernetes não garante que o cluster Ceph formou quórum de placement groups (PGs) ou que não há degradação de replicação. O comando `ceph status` via toolbox ou plugin `kubectl rook-ceph` inspeciona diretamente o plano de controle nativo do Ceph.

## Como funciona
Implante o manifesto `toolbox.yaml` no namespace `rook-ceph` (ou instale o plugin `kubectl-rook-ceph`) e incorpore a checagem de `ceph status` aos runbooks de validação de mudança e resposta a incidentes de armazenamento.

## Exemplo
Antes de liberar o cluster para criação de bancos de dados produtivos, o SRE acessa o toolbox e executa `ceph status`, confirmando `health: HEALTH_OK`, quórum `a,b,c` e `3 osds: 3 up, 3 in`.

## Limites e trade-offs
Qualquer estado diferente de `HEALTH_OK` (como `HEALTH_WARN` ou `HEALTH_ERR`) exige investigação imediata dos avisos reportados por `ceph health detail` antes de prosseguir com upgrades de versão ou manutenção de nós.

## Como verificar
Execute `ceph status` a partir do toolbox do Rook e verifique explicitamente `health: HEALTH_OK`, quórum completo de `mon`, `mgr` ativo e no mínimo três OSDs `up` e `in`.

## Conexões
- [[rook-mon-mgr-osd-and-csi-pods-architecture]] — Veja também: Arquitetura de pods mon, mgr, osd e plugins CSI no namespace rook-ceph.
- [[rook-block-rbd-shared-filesystem-cephfs-and-object-rgw]] — Veja também: Consumo de armazenamento Block (RBD RWO), Shared Filesystem (CephFS RWX) e Object (RGW S3) no Rook.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
