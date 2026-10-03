---
id: software.devops.tranche09.000823
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

# Kubernetes Cluster API: gerenciamento de grupos de nós worker com MachineDeployment, MachineSet e MachinePool

## Em uma frase
De forma análoga a `Deployment` e `ReplicaSet` para Pods no Kubernetes, no Cluster API o `MachineDeployment` gerencia atualizações declarativas rolando alterações entre dois `MachineSets` (o antigo e o novo), enquanto o `MachinePool` usa recursos nativos de grupo de cada provedor de nuvem.

## Por que importa
Para atualizar 50 nós workers de um cluster Kubernetes da versão `v1.34.0` para `v1.35.0` sem derrubar as aplicações em produção, é preciso criar máquinas novas com a versão `v1.35.0`, aguardar que fiquem `Ready`, drenar (`kubectl drain`) as cargas das máquinas antigas respeitando `PodDisruptionBudgets` e remover as máquinas antigas gradualmente. O `Cluster API Book` documenta como o `MachineDeployment` e o `MachineSet` automatizam exatamente esse rollout.

## Como funciona
(1) **`MachineSet`**: tem como propósito manter um conjunto estável de objetos `Machine` rodando a qualquer momento (equivalente a um `ReplicaSet`); não deve ser manipulado diretamente pelo usuário; (2) **`MachineDeployment`**: fica acima do `MachineSet` (equivalente a um `Deployment`); quando o operador altera o template da máquina no `MachineDeployment` (ex.: altera `spec.template.spec.version` ou referencia um novo `InfrastructureMachineTemplate`), o controlador cria um novo `MachineSet` e transfere a capacidade progressivamente do `MachineSet` antigo para o novo; e (3) **`MachinePool`**: similar ao `MachineDeployment`, mas delega o gerenciamento do grupo de máquinas para abstrações nativas do provedor de infraestrutura (como AWS Auto Scaling Groups, Azure VMSS ou GCP Managed Instance Groups).

## Exemplo
```bash
# Escalar declarativamente o número de nós workers de um MachineDeployment e acompanhar o rollout dos MachineSets
kubectl scale machinedeployment my-cluster-md-0 --replicas=5
kubectl get machinedeployments,machinesets,machines
```

## Limites e trade-offs
Como os templates referenciados por um `MachineDeployment` (como `AWSMachineTemplate` ou `VSphereMachineTemplate`) também são tratados como imutáveis para preservar o histórico de rollout entre os dois `MachineSets`, para alterar o tipo de instância (ex.: de `m6i.large` para `m6i.xlarge`) você deve criar um **novo** objeto `*MachineTemplate` com um novo nome e atualizar a referência `infrastructureRef.name` dentro do `MachineDeployment`.

## Como verificar
Inspecione o progresso de uma atualização de versão de nós workers com `kubectl get machinedeployments -o wide` verificando as colunas `REPLICAS`, `AVAILABLE`, `UP-TO-DATE` e `READY`.

## Conexões
- [[clusterapi-recursos-cluster-machine-imutabilidade]] — Veja também: Kubernetes Cluster API: Custom Resources Cluster e Machine e o princípio de imutabilidade de máquinas.
- [[clusterapi-provedores-infraestrutura-bootstrap-control-plane]] — Veja também: Kubernetes Cluster API: arquitetura extensível de Providers (Infrastructure, Bootstrap e Control Plane).
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-auto-remediacao-nos-machinehealthcheck]] — Referência cruzada direta com clusterapi-auto-remediacao-nos-machinehealthcheck.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
