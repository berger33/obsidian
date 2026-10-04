---
id: software.devops.tranche04.000301
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

# Rook como orquestrador cloud-native de armazenamento Ceph no Kubernetes

## Em uma frase
O Rook é um orquestrador de armazenamento cloud-native de código aberto para Kubernetes, graduado pela CNCF e licenciado sob Apache-2.0, que fornece a plataforma, o framework e o suporte para integrar nativamente o sistema de armazenamento distribuído Ceph ao Kubernetes. Enquanto o Ceph entrega armazenamento de arquivos (CephFS), blocos (RBD) e objetos (RGW) em clusters de produção de larga escala, o operador do Rook automatiza sua implantação e gerenciamento sobre recursos nativos do Kubernetes para prover serviços auto-gerenciáveis, auto-escaláveis e auto-recuperáveis (self-managing, self-scaling e self-healing). O provedor Ceph no Rook possui status oficial Stable, com atualizações entre versões projetadas para preservar compatibilidade retroativa.

## Por que importa
Armazenamento distribuído stateful tradicionalmente exige operação manual complexa fora do plano de controle de contêineres. Ao transformar o ciclo de vida do Ceph em controladores e Custom Resource Definitions nativos do Kubernetes, o Rook permite provisionar, escalar, atualizar e monitorar armazenamento persistente declarativamente junto às cargas de trabalho.

## Como funciona
Adote o Rook quando precisar oferecer armazenamento distribuído de bloco (ReadWriteOnce), sistema de arquivos compartilhado (ReadWriteMany) e armazenamento de objetos compatível com S3 dentro do próprio cluster Kubernetes. Utilize exclusivamente releases oficiais publicadas em `github.com/rook/rook/releases`, evitando builds da branch `master` que sofrem mudanças incompatíveis sem aviso prévio.

## Exemplo
Em um cluster bare-metal de produção com três ou mais nós trabalhadores e discos dedicados sem formatação, a equipe implanta o operador Rook a partir de uma release oficial tagueada (como `v1.20.8`) ou via Helm Chart, provisionando um cluster Ceph unificado para bancos de dados, volumes compartilhados e buckets internos.

## Limites e trade-offs
Não teste nem implante o Rook diretamente em um sistema host compartilhado onde dispositivos locais possam ser consumidos acidentalmente; utilize sempre máquinas virtuais em ambientes de teste e filtre explicitamente os dispositivos elegíveis no manifesto do cluster.

## Como verificar
Confirme no repositório oficial que o provedor Ceph é classificado como Stable, que o projeto é graduado na CNCF sob licença Apache-2.0 e que o uso de releases oficiais é fortemente recomendado em vez da branch `master`.

## Conexões
- [[rook-kubernetes-versions-and-cpu-architectures]] — Veja também: Versões do Kubernetes v1.31 a v1.37 e arquiteturas amd64 e arm64 suportadas pelo Rook.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
