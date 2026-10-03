---
id: software.devops.tranche10.000974
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md", "https://www.vcluster.com/docs/vcluster/introduction/architecture/", "https://github.com/loft-sh/vcluster"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# vCluster in Docker (vind): execução de Tenant Clusters diretamente em containers Docker sem Kubernetes prévio

## Em uma frase
Introduzido na v0.32+, o **vind (vCluster in Docker)** permite criar um Tenant Cluster completo diretamente em containers Docker na máquina local ou em runners de CI via `vcluster create <nome> --driver docker`, sem exigir nenhum cluster Kubernetes existente.

## Por que importa
Desenvolvedores locais e pipelines de CI/CD frequentemente usam o `kind` para subir um cluster em Docker, mas sofrem porque o `kind` não possui *sleep/wake* (exigindo deletar e recriar o cluster para liberar recursos), exige configuração manual de MetalLB para `LoadBalancer` e exige rodar `kind load docker-image` a cada build. A seção `vind (vCluster in Docker)` da documentação oficial de arquitetura compara diretamente o `vind` ao `KinD`.

## Como funciona
Ao executar **`vcluster create my-vcluster --driver docker`**, a CLI provisiona o control plane e os worker nodes como containers em um único host Docker utilizando a arquitetura de **Private Nodes** por baixo dos panos. Conforme a tabela comparativa oficial (`vind` vs `KinD` em `vcluster.com/docs/vcluster/introduction/architecture/`), o `vind` oferece cinco diferenciais nativos: (1) **Sleep and wake**: pausa o cluster para liberar recursos e o retoma instantaneamente sem deletar; (2) **Load balancers out of the box**: `Services` do tipo `LoadBalancer` funcionam automaticamente sem setup extra; (3) **Pull-through image cache**: usa o cache de imagens do daemon Docker do host diretamente sem precisar de `kind load`; (4) **External nodes**: instâncias de nuvem podem se juntar a um cluster `vind` local via VPN para desenvolvimento híbrido; e (5) escolha livre de CNI/CSI.

## Exemplo
```bash
# Criar um Tenant Cluster completo rodando diretamente em containers Docker usando o driver vind (sem Kubernetes prévio)
vcluster create my-vcluster --driver docker
kubectl get namespaces
vcluster pause my-vcluster
vcluster resume my-vcluster
```

## Limites e trade-offs
Conforme observa o README oficial do vCluster na seção `vind`, a implantação em Docker é conduzida diretamente pela CLI (`vcluster create --driver docker`) em vez de ser gerenciada por um operador dentro de um Control Plane Cluster; portanto, ele é voltado para desenvolvimento local, pipelines de CI/CD e cenários híbridos de estação de trabalho.

## Como verificar
Execute `vcluster list` após criar um cluster com `--driver docker` para visualizar o status do cluster local e teste criar um `Service` do tipo `LoadBalancer` verificando a atribuição automática de IP.

## Conexões
- [[vcluster-modos-nos-shared-dedicated-private-nodes-standalone]] — Veja também: vCluster: comparação arquitetural entre Shared Nodes, Dedicated Nodes, Private Nodes e vCluster Standalone.
- [[vcluster-armazenamento-estado-sqlite-etcd-postgres-mysql-ha]] — Veja também: vCluster: opções de Backing Store (SQLite embarcado, etcd embarcado/externo, PostgreSQL e MySQL) e Alta Disponibilidade.
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
