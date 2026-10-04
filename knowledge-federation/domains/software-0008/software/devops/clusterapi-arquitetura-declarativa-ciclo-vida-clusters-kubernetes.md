---
id: software.devops.tranche09.000821
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md", "https://cluster-api.sigs.k8s.io/user/concepts.html", "https://github.com/kubernetes-sigs/cluster-api"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes Cluster API (CAPI): gerenciamento declarativo do ciclo de vida de clusters usando APIs estilo Kubernetes

## Em uma frase
O Cluster API (`kubernetes-sigs/cluster-api`, subprojeto do Kubernetes SIG Cluster Lifecycle) fornece APIs declarativas (Custom Resource Definitions) e controladores para automatizar o provisionamento, atualização e operação de múltiplos clusters Kubernetes.

## Por que importa
Provisionar e atualizar dezenas de clusters Kubernetes em diferentes nuvens (AWS, Azure, GCP) e data centers (vSphere, bare-metal) usando scripts imperativos separados para cada ambiente torna a gestão de frotas lenta e inconsistente. Segundo o README oficial e o `The Cluster API Book`, o Cluster API permite que operadores de plataforma definam máquinas virtuais, redes, balanceadores de carga e a configuração do cluster Kubernetes exatamente da mesma maneira declarativa que desenvolvedores usam `Deployments` para gerenciar Pods.

## Como funciona
A arquitetura do Cluster API baseia-se em um **Management Cluster** (um cluster Kubernetes onde rodam os controladores do Cluster API e um ou mais provedores de infraestrutura/bootstrap/control-plane). Dentro do Management Cluster, o operador cria Custom Resources declarativos no grupo de API `cluster.x-k8s.io` (como `Cluster`, `Machine`, `MachineSet`, `MachineDeployment`, `MachinePool`, `KubeadmControlPlane` e `MachineHealthCheck`). Os controladores reconciliam continuamente esses objetos comunicando-se com as APIs da nuvem/hipervisor para criar e manter os **Workload Clusters** (os clusters finais onde rodam as cargas de trabalho dos usuários).

## Exemplo
```bash
# Inicializar um Management Cluster do Cluster API usando a CLI oficial clusterctl (ex.: com o provider Docker/CAPD para testes)
clusterctl init --infrastructure docker
kubectl get providers -A
```

## Limites e trade-offs
Como o **Management Cluster** armazena o estado declarativo, os certificados PKI e as credenciais de provedores de todos os Workload Clusters gerenciados, a perda ou comprometimento do Management Cluster afeta a capacidade de escalar, atualizar ou recuperar toda a frota de clusters (embora os Workload Clusters existentes continuem rodando suas aplicações de forma autônoma enquanto o Management Cluster estiver indisponível).

## Como verificar
Em um Management Cluster inicializado com `clusterctl init`, execute `kubectl get crds | grep cluster.x-k8s.io` e `kubectl get pods -n capi-system` para verificar que os controladores centrais estão em execução.

## Conexões
- [[clusterapi-recursos-cluster-machine-imutabilidade]] — Veja também: Kubernetes Cluster API: Custom Resources Cluster e Machine e o princípio de imutabilidade de máquinas.
- [[clusterapi-machinedeployment-machineset-machinepool-rollout]] — Referência cruzada direta com clusterapi-machinedeployment-machineset-machinepool-rollout.
- [[clusterapi-provedores-infraestrutura-bootstrap-control-plane]] — Referência cruzada direta com clusterapi-provedores-infraestrutura-bootstrap-control-plane.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
