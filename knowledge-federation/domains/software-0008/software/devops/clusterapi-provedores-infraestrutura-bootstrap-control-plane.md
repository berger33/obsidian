---
id: software.devops.tranche09.000824
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

# Kubernetes Cluster API: arquitetura extensível de Providers (Infrastructure, Bootstrap e Control Plane)

## Em uma frase
A extensibilidade do Cluster API divide responsabilidades em três tipos de provedores plugáveis: **Infrastructure Provider** (VMs, rede, variantes EC2/EKS), **Bootstrap Provider** (geração de `BootstrapData`/cloud-init e join de nós) e **Control Plane Provider** (self-provisioned, pod-based ou managed).

## Por que importa
Desacoplar "onde a máquina virtual roda" (AWS, Azure, GCP, vSphere, Metal3,MAAS) de "como um servidor vira um nó Kubernetes" (`kubeadm`, Talos, K3s, MicroK8s) permite combinar qualquer infraestrutura com qualquer distribuição Kubernetes sem reescrever a lógica de ciclo de vida. A página `Concepts` do `Cluster API Book` detalha o papel de cada um dos três tipos de provedores.

## Como funciona
(1) **Infrastructure Provider**: provisiona os recursos computacionais e de rede exigidos pelo `Cluster` ou pelas `Machines` (em nuvem como AWS, Azure, Google; ou bare-metal como VMware, MAAS, `metal3.io`). Quando um mesmo provedor oferece mais de uma maneira de obter recursos (como a AWS oferecendo tanto VMs EC2 quanto clusters gerenciados EKS), cada maneira é chamada de **variant**; (2) **Bootstrap Provider**: transforma um servidor em um nó Kubernetes gerando o `BootstrapData` (geralmente `cloud-init`), gerando certificados do cluster (se não especificados), inicializando o control plane e coordenando o join de nós; e (3) **Control Plane Provider**: gerencia o control plane em três abordagens possíveis: **Self-provisioned** (ex.: `KubeadmControlPlane` usando static pods em `Machines`), **Pod-based** (control plane rodando como `Deployment`/`StatefulSet` em um cluster hospedeiro externo) ou **External/Managed** (GKE, AKS, EKS, IKS).

## Exemplo
```bash
# Listar todos os providers (Core, Bootstrap, ControlPlane e Infrastructure) instalados no Management Cluster
kubectl get providers.clusterctl.cluster.x-k8s.io -A
```

## Limites e trade-offs
Ao utilizar uma variante **External/Managed** de Control Plane (como `AWSManagedControlPlane` para Amazon EKS ou `AzureManagedControlPlane` para AKS), o plano de controle é gerenciado pela nuvem pública (portanto você não gerencia `Machines` individuais de control plane nem o `etcd` diretamente via `KubeadmControlPlane`), gerenciando pelo CAPI a configuração do cluster gerenciado e os `MachinePools` / `MachineDeployments` dos workers.

## Como verificar
Consulte `kubectl get pods -A | grep -E "capi-|cap"` para confirmar que os três controladores (Infrastructure, Bootstrap e Control Plane) mais o Core Provider estão saudáveis no Management Cluster.

## Conexões
- [[clusterapi-machinedeployment-machineset-machinepool-rollout]] — Veja também: Kubernetes Cluster API: gerenciamento de grupos de nós worker com MachineDeployment, MachineSet e MachinePool.
- [[clusterapi-control-plane-kubeadmcontrolplane-etcd-upgrade]] — Veja também: Kubernetes Cluster API: gerenciamento declarativo do Control Plane com KubeadmControlPlane (KCP).
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-recursos-cluster-machine-imutabilidade]] — Referência cruzada direta com clusterapi-recursos-cluster-machine-imutabilidade.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
