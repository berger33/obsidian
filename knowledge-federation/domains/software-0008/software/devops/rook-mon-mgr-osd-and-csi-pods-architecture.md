---
id: software.devops.tranche04.000306
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

# Arquitetura de pods mon, mgr, osd e plugins CSI no namespace rook-ceph

## Em uma frase
Após aplicar `cluster.yaml`, o Rook provisiona no namespace `rook-ceph` a topologia completa de daemons do Ceph e drivers CSI: três monitores de quórum (`rook-ceph-mon-a`, `b`, `c`), gerenciadores ativo e standby (`rook-ceph-mgr-a`, `rook-ceph-mgr-b`), um pod `rook-ceph-osd-<n>` para cada dispositivo elegível preparado pelos jobs `rook-ceph-osd-prepare-<node>`, coletores `rook-ceph-crashcollector` e `rook-ceph-exporter`, além dos controladores e DaemonSets de nó do Ceph CSI para CephFS (`rook-ceph.cephfs.csi.ceph.com-ctrlplugin` e `nodeplugin`) e RBD (`rook-ceph.rbd.csi.ceph.com-ctrlplugin` e `nodeplugin`).

## Por que importa
Conhecer a função de cada família de pods permite diagnosticar rapidamente se uma falha de armazenamento está no quórum de controle (`mon`), na camada de gerenciamento e métricas (`mgr`), na preparação ou saúde dos discos de dados (`osd-prepare` / `osd`) ou na montagem CSI no kubelet (`nodeplugin`).

## Como funciona
Monitore a convergência inicial com `kubectl -n rook-ceph get pod`, verificando que os jobs `rook-ceph-osd-prepare-*` mudam para `Completed` e dão lugar aos pods `rook-ceph-osd-0`, `1`, `2` em estado `Running`.

## Exemplo
Durante a validação pós-instalação em um cluster de 3 nós com 1 disco bruto por nó, o engenheiro confirma a presença de 3 pods `mon`, 2 pods `mgr`, 3 pods `osd` e os pares `ctrlplugin`/`nodeplugin` para `cephfs` e `rbd`.

## Limites e trade-offs
Se os pods `rook-ceph-mon`, `rook-ceph-mgr` ou `rook-ceph-osd` não forem criados, não tente criar os Deployment/Pods manualmente; o Rook reconcilia esses recursos a partir do CRD `CephCluster`, devendo-se investigar os logs do `rook-ceph-operator` e dos jobs `osd-prepare`.

## Como verificar
Liste os pods com `kubectl -n rook-ceph get pod` e valide que todos os daemons `mon`, `mgr`, `osd` e plugins `csi` estão `Running` sem loop de reinicialização.

## Conexões
- [[rook-cluster-manifests-bare-metal-on-pvc-and-test]] — Veja também: Manifestos de cluster Rook para bare-metal (cluster.yaml), nuvem dinâmica (cluster-on-pvc.yaml) e teste (cluster-test.yaml).
- [[rook-ceph-toolbox-and-kubectl-plugin-verification]] — Veja também: Verificação de saúde HEALTH_OK com Rook Toolbox e plugin kubectl rook-ceph.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
