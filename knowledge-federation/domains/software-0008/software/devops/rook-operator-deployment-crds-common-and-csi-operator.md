---
id: software.devops.tranche04.000304
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

# Implantação do Rook Operator com crds.yaml, common.yaml, csi-operator.yaml e operator.yaml

## Em uma frase
O fluxo padrão de implantação do Rook documentado no Quickstart oficial inicia aplicando quatro manifestos de uma release oficial tagueada (ex.: `git clone --single-branch --branch v1.20.8 https://github.com/rook/rook.git` em `deploy/examples`): `kubectl create -f crds.yaml -f common.yaml -f csi-operator.yaml` seguido de `kubectl create -f operator.yaml` (ou alternativamente via Rook Operator Helm Chart). O administrador deve aguardar o pod `rook-ceph-operator` atingir o estado `Running` no namespace `rook-ceph` antes de criar o recurso `CephCluster`.

## Por que importa
Aplicar o `cluster.yaml` antes de os Custom Resource Definitions (`crds.yaml`), permissões RBAC (`common.yaml`), o operador CSI (`csi-operator.yaml`) e o `rook-ceph-operator` estarem ativos resulta em falhas de validação ou reconciliação incompleta dos controladores CSI de RBD e CephFS.

## Como funciona
Clone sempre uma tag de release estável (como `v1.20.8`), revise as configurações avançadas em `operator.yaml` (já que certas funcionalidades vêm desabilitadas por padrão) e, caso implante em um namespace diferente de `rook-ceph`, siga a documentação específica de namespaces alternativos antes de aplicar os manifestos.

## Exemplo
Automatizando o bootstrap de armazenamento em staging, o pipeline executa `kubectl create -f crds.yaml -f common.yaml -f csi-operator.yaml`, aplica `operator.yaml` e bloqueia em `kubectl -n rook-ceph wait --for=condition=Ready pod -l app=rook-ceph-operator` antes de submeter `cluster.yaml`.

## Limites e trade-offs
Evite usar manifestos diretamente da branch `master` em clusters produtivos e não omita `csi-operator.yaml` nas versões recentes do Rook que delegam o ciclo de vida dos plugins `cephfs.csi.ceph.com` e `rbd.csi.ceph.com` ao operador CSI.

## Como verificar
Execute `kubectl -n rook-ceph get pod` e confirme que `rook-ceph-operator` e `ceph-csi-controller-manager` estão `1/1 Running` antes de criar o cluster Ceph.

## Conexões
- [[rook-raw-devices-lvm-and-block-pvc-prerequisites]] — Veja também: Pré-requisitos de dispositivos brutos, partições, LVM e PVs em modo block para OSDs no Rook.
- [[rook-cluster-manifests-bare-metal-on-pvc-and-test]] — Veja também: Manifestos de cluster Rook para bare-metal (cluster.yaml), nuvem dinâmica (cluster-on-pvc.yaml) e teste (cluster-test.yaml).

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
