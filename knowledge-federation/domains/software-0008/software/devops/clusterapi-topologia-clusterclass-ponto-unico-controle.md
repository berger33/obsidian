---
id: software.devops.tranche09.000828
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

# Kubernetes Cluster API: reutilização de topologias e ponto único de controle com ClusterClass

## Em uma frase
O recurso `ClusterClass` permite definir um template reutilizável de arquitetura de cluster (control plane, classes de `MachineDeployment`/`MachinePool` e variáveis/patches), transformando o objeto `Cluster` (`spec.topology`) em um ponto único de controle para o cluster inteiro.

## Por que importa
Sem o `ClusterClass`, criar um único Workload Cluster no Cluster API exige instanciar e conectar manualmente 7 a 10 objetos YAML separados (`Cluster`, `AWSCluster`, `KubeadmControlPlane`, `AWSMachineTemplate` do CP, `MachineDeployment`, `AWSMachineTemplate` do worker e `KubeadmConfigTemplate`); multiplicar isso por 50 clusters gera centenas de recursos repetitivos. Conforme destaca o `Cluster API Book`, com `ClusterClass` o objeto `Cluster` torna-se o ponto único de controle.

## Como funciona
A equipe de plataforma define uma vez um objeto **`ClusterClass`** (por exemplo, `ha-eks-standard` ou `vsphere-prod-class`) que amarra os templates de infraestrutura, control plane, workers e variáveis parametrizáveis (como região, tipo de instância, tamanho de disco). A partir daí, para provisionar, escalar ou atualizar qualquer cluster da frota, o usuário cria ou edita **apenas um único objeto `Cluster`** preenchendo o bloco `spec.topology` (`class: vsphere-prod-class`, `version: v1.35.0`, `controlPlane.replicas: 3`, `workers.machineDeployments: ...`). O controlador de topologia do Cluster API gera, atualiza e rotaciona automaticamente todos os templates e objetos subjacentes (`KubeadmControlPlane`, `MachineDeployments` e `*MachineTemplates`).

## Exemplo
```yaml
# Exemplo de objeto Cluster usando ClusterClass (spec.topology) como ponto único de controle do cluster inteiro
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: prod-payment-cluster
spec:
  topology:
    class: corporate-ha-class
    version: v1.35.0
    controlPlane:
      replicas: 3
    workers:
      machineDeployments:
        - class: default-worker
          name: md-general
          replicas: 6
```

## Limites e trade-offs
Quando um `Cluster` é gerenciado por uma `ClusterClass` (`spec.topology`), todos os recursos filhos (`KubeadmControlPlane`, `MachineDeployment`, templates) são reconciliados continuamente pelo controlador de topologia; portanto, você **nunca deve editar manualmente** o `KubeadmControlPlane` ou o `MachineDeployment` gerado, fazendo toda alteração de versão ou escala diretamente em `spec.topology` no objeto `Cluster` (ou na `ClusterClass` para propagar a mudança para todos os clusters que a herdam).

## Como verificar
Execute `kubectl get clusterclasses,clusters -A` e `clusterctl describe cluster <nome>` para verificar a reconciliação da topologia a partir da `ClusterClass`.

## Conexões
- [[clusterapi-extensoes-atualizacao-in-place-v1-12]] — Veja também: Kubernetes Cluster API: extensões de atualização In-Place (In-Place Updates a partir do CAPI v1.12) vs substituição imutável.
- [[clusterapi-cli-clusterctl-init-generate-move-upgrade]] — Veja também: Kubernetes Cluster API: operações de ciclo de vida do Management Cluster com a CLI clusterctl (init, generate, move, upgrade).
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-recursos-cluster-machine-imutabilidade]] — Referência cruzada direta com clusterapi-recursos-cluster-machine-imutabilidade.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
