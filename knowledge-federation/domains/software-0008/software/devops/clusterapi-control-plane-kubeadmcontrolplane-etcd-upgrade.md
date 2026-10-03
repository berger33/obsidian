---
id: software.devops.tranche09.000825
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

# Kubernetes Cluster API: gerenciamento declarativo do Control Plane com KubeadmControlPlane (KCP)

## Em uma frase
O recurso `KubeadmControlPlane` (`KCP`), fornecido pelo Kubeadm Control Plane Provider embutido no Cluster API, gerencia declarativamente o conjunto de `Machines` que hospedam os nós de control plane e o `etcd` criados com `kubeadm`.

## Por que importa
Atualizar ou escalar nós de control plane é muito mais delicado do que escalar nós workers comuns: adicionar ou remover uma réplica exige atualizar o quórum de membros do banco de dados `etcd`, transferir liderança do `etcd` antes de desligar um nó, rotacionar certificados PKI e atualizar `kube-apiserver`, `kube-controller-manager`, `kube-scheduler` e `CoreDNS` na sequência correta. O `Cluster API Book` destaca o `KubeadmControlPlane` como o controlador que automatiza todo esse processo.

## Como funciona
Quando o operador declara um objeto **`KubeadmControlPlane`** (por exemplo, com `spec.replicas: 3` e `spec.version: v1.35.0`), o controlador KCP: (1) gera ou carrega as autoridades certificadoras (CAs) do cluster como Secrets no Management Cluster; (2) cria a primeira `Machine` de control plane com configuração `InitConfiguration` do `kubeadm` (que sobe os static pods do `kube-apiserver`, `kube-controller-manager`, `kube-scheduler` e `etcd`); (3) aguarda o plano de controle inicializar antes de liberar a criação das demais `Machines` de control plane (`JoinConfiguration`) e dos workers; e (4) durante upgrades de versão ou alterações de template, executa rolling updates seguros um nó de control plane por vez, verificando a saúde do `etcd` a cada passo.

## Exemplo
```bash
# Inspecionar o estado do KubeadmControlPlane e das réplicas do plano de controle usando clusterctl describe
kubectl get kubeadmcontrolplane -A
clusterctl describe cluster my-cluster
```

## Limites e trade-offs
Como o `KubeadmControlPlane` gerencia o quórum Raft do `etcd` acoplado às `Machines` de control plane (no modo stacked etcd padrão), o campo `spec.replicas` do `KubeadmControlPlane` deve ser sempre configurado com um **número ímpar** (`1` apenas para desenvolvimento/teste, ou `3` e `5` para produção HA) e as atualizações de versão do Kubernetes (`spec.version`) devem respeitar a política oficial de skew do Kubernetes (subindo uma versão minor por vez, ex.: `1.33` -> `1.34` -> `1.35`).

## Como verificar
Execute `clusterctl describe cluster <nome-do-cluster>` para visualizar a árvore hierárquica do `ControlPlane`, a saúde de cada membro do `etcd` e o status das condições `ControlPlaneInitialized` e `Ready`.

## Conexões
- [[clusterapi-provedores-infraestrutura-bootstrap-control-plane]] — Veja também: Kubernetes Cluster API: arquitetura extensível de Providers (Infrastructure, Bootstrap e Control Plane).
- [[clusterapi-auto-remediacao-nos-machinehealthcheck]] — Veja também: Kubernetes Cluster API: detecção de falhas e auto-remediação de nós com MachineHealthCheck.
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
