---
id: software.devops.tranche09.000822
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

# Kubernetes Cluster API: Custom Resources Cluster e Machine e o princípio de imutabilidade de máquinas

## Em uma frase
No Cluster API (`cluster.x-k8s.io/v1beta2`), o recurso `Cluster` representa o cluster de workload inteiro (rede e referências `infrastructureRef` e `controlPlaneRef`), enquanto o recurso `Machine` representa declarativamente o host que executa um `Node` Kubernetes sob o princípio de imutabilidade.

## Por que importa
Em ferramentas tradicionais de gerência de configuração, quando se deseja atualizar a versão do Kubernetes ou do SO de um servidor, scripts tentam mutar a máquina existente; se falharem, o nó vira um "floco de neve" irreproduzível. A página `Concepts` do `Cluster API Book` explica como os recursos `Cluster` e `Machine` separam propriedades portáveis de detalhes específicos de provedor e tratam cada `Machine` como imutável.

## Como funciona
(1) **`Cluster`**: define propriedades comuns como blocos CIDR de pods/services (`spec.clusterNetwork.pods.cidrBlocks`) e delega detalhes específicos da nuvem para os objetos apontados em `spec.infrastructureRef` (ex.: `VSphereCluster`, `AWSCluster`) e `spec.controlPlaneRef` (ex.: `KubeadmControlPlane`); e (2) **`Machine`**: define a especificação declarativa de um servidor individual (como `spec.clusterName`, `spec.version: v1.35.0`, `spec.infrastructureRef` e `spec.bootstrap.configRef`). Quando uma `Machine` é criada, o controlador provisiona um novo host que se registra como `Node` (`status.nodeRef`); quando a `Machine` é deletada, o host subjacente e o `Node` são destruídos. **Sob a perspectiva do Cluster API, todas as `Machines` são imutáveis**: uma vez criadas, nunca são atualizadas in-place por padrão (exceto labels, annotations e status), sendo substituídas por novas máquinas durante upgrades.

## Exemplo
```yaml
# Exemplo oficial do Cluster API Book (v1beta2) declarando um objeto Cluster e suas referências
apiVersion: cluster.x-k8s.io/v1beta2
kind: Cluster
metadata:
  name: my-cluster
spec:
  clusterNetwork:
    pods:
      cidrBlocks:
        - 192.168.0.0/16
  infrastructureRef:
    apiGroup: infrastructure.cluster.x-k8s.io
    kind: VSphereCluster
    name: my-cluster-infrastructure
  controlPlaneRef:
    apiGroup: controlplane.cluster.x-k8s.io
    kind: KubeadmControlPlane
    name: my-control-plane
```

## Limites e trade-offs
Assim como você não deve criar `Pods` avulsos diretamente no Kubernetes em produção (usando `Deployments` em vez disso), a documentação oficial do Cluster API recomenda **não gerenciar objetos `Machine` individuais diretamente**, mas sim utilizar controladores de nível superior como `KubeadmControlPlane`, `MachineDeployment` ou `MachinePool`, que coordenam a substituição gradual das máquinas imutáveis.

## Como verificar
Execute `kubectl get clusters,machines -A` no Management Cluster e verifique na coluna `PROVIDERID` e `PHASE` (`Running`) o vínculo entre cada `Machine` e seu respectivo `Node` no Workload Cluster.

## Conexões
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Veja também: Kubernetes Cluster API (CAPI): gerenciamento declarativo do ciclo de vida de clusters usando APIs estilo Kubernetes.
- [[clusterapi-machinedeployment-machineset-machinepool-rollout]] — Veja também: Kubernetes Cluster API: gerenciamento de grupos de nós worker com MachineDeployment, MachineSet e MachinePool.
- [[clusterapi-extensoes-atualizacao-in-place-v1-12]] — Referência cruzada direta com clusterapi-extensoes-atualizacao-in-place-v1-12.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
