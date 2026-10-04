---
id: software.devops.tranche04.000308
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

# Consumo de armazenamento Block (RBD RWO), Shared Filesystem (CephFS RWX) e Object (RGW S3) no Rook

## Em uma frase
Depois que o cluster Ceph gerenciado pelo Rook está saudável, aplicações Kubernetes podem consumir três modalidades nativas de armazenamento documentadas no Quickstart: **Block** via RBD (`Block-Storage-RBD`), fornecendo volumes de bloco de baixa latência montados por um pod por vez (`ReadWriteOnce` — RWO); **Shared Filesystem** via CephFS (`Shared-Filesystem-CephFS`), fornecendo um sistema de arquivos POSIX compartilhado entre múltiplos pods simultaneamente (`ReadWriteMany` — RWX); e **Object** via RADOS Gateway (`Object-Storage-RGW`), expondo um object store compatível com endpoint S3 acessível dentro ou fora do cluster Kubernetes.

## Por que importa
Consolidar bloco RWO, sistema de arquivos compartilhado RWX e armazenamento de objetos S3 sobre um único pool de armazenamento distribuído Ceph elimina a necessidade de operar três soluções distintas de armazenamento persistente no cluster.

## Como funciona
Crie `StorageClasses` específicas associadas aos recursos `CephBlockPool` (para bancos de dados e workloads RWO), `CephFilesystem` (para workloads compartilhados RWX) e `CephObjectStore` / `ObjectBucketClaim` (para aplicações que consomem API S3).

## Exemplo
Em uma plataforma de aprendizado de máquina em Kubernetes, os bancos de metadados usam PVCs RWO sobre RBD, os workers de treinamento distribuído montam datasets compartilhados via PVC RWX sobre CephFS e os artefatos de modelos são gravados em buckets S3 servidos pelo RGW do mesmo cluster Rook.

## Limites e trade-offs
Não utilize armazenamento de bloco RBD em modo de sistema de arquivos compartilhado entre múltiplos escritores sem um cluster filesystem adequado; para compartilhamento de diretórios POSIX entre múltiplos pods, utilize sempre CephFS (`RWX`).

## Como verificar
Provisione um PVC de teste ou `ObjectBucketClaim` para a modalidade utilizada e confirme a vinculação (`Bound`) e a leitura/escrita bem-sucedida a partir de um pod consumidor.

## Conexões
- [[rook-ceph-toolbox-and-kubectl-plugin-verification]] — Veja também: Verificação de saúde HEALTH_OK com Rook Toolbox e plugin kubectl rook-ceph.
- [[rook-dashboard-prometheus-monitoring-and-telemetry]] — Veja também: Ceph Dashboard, coletores Prometheus nativos e telemetria anônima no Rook.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
