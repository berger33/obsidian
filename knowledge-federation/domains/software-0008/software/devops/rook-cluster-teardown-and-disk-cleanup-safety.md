---
id: software.devops.tranche04.000310
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

# Desmontagem limpa (teardown) de clusters Rook e limpeza de metadados nos discos dos hosts

## Em uma frase
O guia oficial de encerramento (`ceph-teardown`) referenciado no Quickstart do Rook destaca que remover apenas os manifestos YAML do Kubernetes não apaga automaticamente os dados e metadados gravados pelo Rook/Ceph no diretório `dataDirHostPath` (como `/var/lib/rook`) nem as assinaturas BlueStore/LVM nos discos brutos dos nós. Para recriar um cluster Rook nos mesmos hosts após um laboratório ou descomissionamento, é necessário remover primeiramente as cargas consumidoras, ativar a política de limpeza ou limpar explicitamente `dataDirHostPath` e zerar as tabelas/assinaturas dos discos de OSD.

## Por que importa
Se o diretório `/var/lib/rook` ou os cabeçalhos LVM/BlueStore permanecerem nos discos de um cluster anterior, uma nova instalação do Rook nos mesmos nós falhará ao inicializar novos monitores devido a conflito de `fsid`/chaves antigas ou ignorará os discos por não estarem mais brutos (`raw`).

## Como funciona
Ao descomissionar um cluster de teste, remova primeiro todos os PVCs, `ObjectBucketClaims`, `CephBlockPools`, `CephFilesystems` e `CephObjectStores`, configure `cleanupPolicy` no `CephCluster` antes de deletá-lo e aguarde a conclusão dos jobs de limpeza nos nós antes de remover o operador e os CRDs.

## Exemplo
Após concluir uma bateria de testes de caos em VMs de homologação, o engenheiro segue o guia `ceph-teardown`, aguarda os jobs `rook-ceph-cleanup` apagarem `/var/lib/rook` e limpa os dispositivos secundários antes de provisionar uma nova versão do cluster.

## Limites e trade-offs
Nunca aplique `cleanupPolicy` destrutiva em um cluster de produção ativo sem dupla verificação e backup externo validado, pois a confirmação dessa política destrói irreversivelmente todos os dados armazenados nos OSDs.

## Como verificar
Após o teardown completo de um ambiente de laboratório, verifique nos nós que `/var/lib/rook` está vazio e que `lsblk -f` nos discos dedicados não exibe sistemas de arquivos ou volumes LVM residuais do Ceph.

## Conexões
- [[rook-dashboard-prometheus-monitoring-and-telemetry]] — Veja também: Ceph Dashboard, coletores Prometheus nativos e telemetria anônima no Rook.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
