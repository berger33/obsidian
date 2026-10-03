---
id: software.devops.tranche04.000302
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

# Versões do Kubernetes v1.31 a v1.37 e arquiteturas amd64 e arm64 suportadas pelo Rook

## Em uma frase
A documentação oficial de Quickstart do Rook especifica suporte às versões do Kubernetes de `v1.31` até `v1.37` na release atual, disponibilizando artefatos oficiais compilados para as arquiteturas de CPU `amd64 / x86_64` e `arm64`. Esse recorte de compatibilidade garante que o operador Rook, o `csi-operator` e os daemons do Ceph interajam corretamente com as APIs de armazenamento (CSI, StorageClasses, PersistentVolumeClaims) e de agendamento das versões suportadas do Kubernetes.

## Por que importa
Operar um orquestrador de armazenamento fora da matriz de versões suportadas do Kubernetes ou em arquiteturas não homologadas pode introduzir falhas silenciosas no provisionamento de volumes CSI ou durante upgrades de versão do cluster. Validar a matriz de versão e arquitetura antes do deploy é requisito básico de prontidão operacional.

## Como funciona
Verifique a versão dos nós e do control plane (`kubectl version`) e a arquitetura dos nós (`amd64` ou `arm64`) antes de instalar ou atualizar os manifestos `crds.yaml`, `common.yaml`, `csi-operator.yaml` e `operator.yaml` ou os Helm Charts equivalentes do Rook.

## Exemplo
Ao planejar a atualização de um cluster Kubernetes corporativo que executa nós mistos `x86_64` e `arm64`, a equipe de plataforma consulta a faixa suportada (`v1.31`–`v1.37`) do Quickstart do Rook para alinhar a versão do operador Ceph antes de avançar o control plane.

## Limites e trade-offs
Não atualize o Kubernetes para uma versão fora da janela suportada pela release instalada do Rook sem antes validar as notas de versão e atualizar o operador Rook conforme o guia oficial de upgrade.

## Como verificar
Verifique na saída de `kubectl get nodes -o wide` que todos os nós de armazenamento executam versão do Kubernetes entre `v1.31` e `v1.37` sobre arquitetura `amd64` ou `arm64`.

## Conexões
- [[rook-orchestrator-for-ceph-on-kubernetes]] — Veja também: Rook como orquestrador cloud-native de armazenamento Ceph no Kubernetes.
- [[rook-raw-devices-lvm-and-block-pvc-prerequisites]] — Veja também: Pré-requisitos de dispositivos brutos, partições, LVM e PVs em modo block para OSDs no Rook.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
