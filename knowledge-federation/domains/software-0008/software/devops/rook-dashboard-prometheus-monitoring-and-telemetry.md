---
id: software.devops.tranche04.000309
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

# Ceph Dashboard, coletores Prometheus nativos e telemetria anônima no Rook

## Em uma frase
Cada cluster Rook inclui um painel visual integrado (Ceph Dashboard) para visualização do estado do cluster e coletores/exporters nativos de métricas (`rook-ceph-exporter` e módulo Prometheus do `mgr`) para monitoramento com Prometheus. Além disso, os mantenedores do Rook disponibilizam o recurso de telemetria anônima do Ceph — ativável dentro do toolbox com `ceph telemetry on` — que envia relatórios estatísticos sem informações de identificação pessoal conforme a documentação de privacidade do Ceph.

## Por que importa
Sem coleta contínua de métricas de latência de OSD, utilização de capacidade do pool e estado de Placement Groups no Prometheus, problemas de disco lento ou enchimento assimétrico de OSDs só são percebidos quando os volumes entram em modo somente-leitura.

## Como funciona
Habilite o monitoramento Prometheus na especificação do `CephCluster` aplicando os `ServiceMonitors` e regras de alerta recomendados no guia de monitoramento do Rook, e exponha o Ceph Dashboard apenas através de ingress autenticado ou port-forward administrativo seguro.

## Exemplo
A equipe de observabilidade integra o `rook-ceph-exporter` e o endpoint de métricas do `rook-ceph-mgr` ao stack Prometheus/Alertmanager do cluster, disparando alertas preventivos quando qualquer OSD ultrapassa 75% de ocupação ou apresenta PGs inconsistentes.

## Limites e trade-offs
Evite expor o serviço do Ceph Dashboard publicamente sem TLS e autenticação forte, pois o painel administrativo permite visualizar e alterar configurações sensíveis de pools e clientes do cluster Ceph.

## Como verificar
Consulte os alvos do Prometheus para `rook-ceph` e acesse o Ceph Dashboard confirmando a exibição em tempo real de capacidade, IOPS, throughput e saúde `HEALTH_OK` do cluster.

## Conexões
- [[rook-block-rbd-shared-filesystem-cephfs-and-object-rgw]] — Veja também: Consumo de armazenamento Block (RBD RWO), Shared Filesystem (CephFS RWX) e Object (RGW S3) no Rook.
- [[rook-cluster-teardown-and-disk-cleanup-safety]] — Veja também: Desmontagem limpa (teardown) de clusters Rook e limpeza de metadados nos discos dos hosts.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
