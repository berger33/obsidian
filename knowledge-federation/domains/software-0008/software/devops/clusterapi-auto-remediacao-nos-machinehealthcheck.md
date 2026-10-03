---
id: software.devops.tranche09.000826
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

# Kubernetes Cluster API: detecção de falhas e auto-remediação de nós com MachineHealthCheck

## Em uma frase
O recurso `MachineHealthCheck` (`MHC`) define as condições sob as quais um `Node` do Workload Cluster deve ser considerado ausente ou não saudável por um período configurável, iniciando automaticamente a remediação pela substituição da `Machine` correspondente.

## Por que importa
Em uma frota com centenas de servidores ou máquinas virtuais, falhas de hardware, travamentos de kernel, discos cheios ou perda permanente de rede acontecem regularmente; sem auto-remediação, operadores precisam ser acordados de madrugada para deletar manualmente a VM quebrada e provisionar uma nova. A seção `MachineHealthCheck` em `cluster-api.sigs.k8s.io/user/concepts.html` documenta esse mecanismo de autocura.

## Como funciona
Um objeto **`MachineHealthCheck`** criado no Management Cluster seleciona um grupo de `Machines` por labels (`spec.selector`) e define uma lista de `unhealthyConditions` (por exemplo, `type: Ready` com `status: Unknown` ou `status: False` por um `timeout: 300s`, além de `nodeStartupTimeout` para máquinas que nunca conseguem se registrar como `Node`). O controlador monitora continuamente os objetos `Node` dentro do Workload Cluster: se um nó permanecer na condição não saudável além do tempo configurado, o `MachineHealthCheck` marca a `Machine` para remediação e a deleta, fazendo com que o controlador pai (`MachineSet` / `KubeadmControlPlane`) crie automaticamente uma nova `Machine` saudável no seu lugar.

## Exemplo
```yaml
# Exemplo de MachineHealthCheck remediando nós workers que fiquem NotReady ou Unknown por mais de 5 minutos
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: my-cluster-worker-mhc
spec:
  clusterName: my-cluster
  selector:
    matchLabels:
      nodepool: pool-workers
  unhealthyConditions:
    - type: Ready
      status: Unknown
      timeout: 300s
    - type: Ready
      status: "False"
      timeout: 300s
```

## Limites e trade-offs
Conforme destaca explicitamente o `Cluster API Book`, o `MachineHealthCheck` só remedia nós de workers se as respectivas `Machines` forem possuídas por um **`MachineSet`** (ou `MachineDeployment` / `KubeadmControlPlane`) — isso garante que o cluster não perca capacidade ao deletar uma `Machine` avulsa que ninguém recriaria; além disso, deve-se configurar `maxUnhealthy` (disjuntor de circuito) para evitar que uma falha global de rede faça o MHC deletar 100% dos nós do cluster de uma só vez.

## Como verificar
Execute `kubectl get machinehealthchecks -A` e verifique as colunas `EXPECTEDMACHINES` e `CURRENTHEALTHY` para confirmar que o MHC está monitorando ativamente o pool de máquinas.

## Conexões
- [[clusterapi-control-plane-kubeadmcontrolplane-etcd-upgrade]] — Veja também: Kubernetes Cluster API: gerenciamento declarativo do Control Plane com KubeadmControlPlane (KCP).
- [[clusterapi-extensoes-atualizacao-in-place-v1-12]] — Veja também: Kubernetes Cluster API: extensões de atualização In-Place (In-Place Updates a partir do CAPI v1.12) vs substituição imutável.
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-machinedeployment-machineset-machinepool-rollout]] — Referência cruzada direta com clusterapi-machinedeployment-machineset-machinepool-rollout.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
