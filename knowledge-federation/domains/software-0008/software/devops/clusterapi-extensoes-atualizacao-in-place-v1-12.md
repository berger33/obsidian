---
id: software.devops.tranche09.000827
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

# Kubernetes Cluster API: extensões de atualização In-Place (In-Place Updates a partir do CAPI v1.12) vs substituição imutável

## Em uma frase
A partir do Cluster API v1.12, além do modelo padrão de substituição de máquinas imutáveis (rolling replacement), a arquitetura introduziu pontos de extensão (`update extensions`) que permitem realizar atualizações **in-place** sob circunstâncias bem definidas mantendo a mesma experiência declarativa.

## Por que importa
Embora substituir a máquina virtual inteira a cada mudança seja o padrão ouro para nuvens elásticas, em ambientes de servidores **bare-metal** físicos (onde dar PXE boot e reinstalar um servidor físico leva 20 a 40 minutos) ou quando a mudança é mínima (ou em sistemas operacionais atômicos como Talos/Flatcar), atualizar a máquina existente in-place reduz drasticamente o tempo de rollout e a movimentação de pods. A seção `MachineDeployment` do `Cluster API Book` explica essa evolução introduzida no CAPI v1.12.

## Como funciona
Conforme documenta o `Cluster API Book`, a partir do **Cluster API v1.12**, os usuários podem optar por trocar parte dos benefícios da imutabilidade estrita de `Machine` conectando **pontos de extensão de atualização (Runtime Extensions / In-Place Update extensions)**. Crucialmente, **a experiência do usuário no Cluster API permanece exatamente a mesma** quer as atualizações in-place estejam habilitadas ou não: o operador continua declarando apenas o **estado desejado** no `MachineDeployment` / `KubeadmControlPlane`, e o próprio Cluster API fica responsável por escolher a melhor estratégia (atualizar a máquina existente in-place via extensão quando a mudança for suportada, ou fazer fallback automático para o rollout tradicional de substituição de máquina).

## Exemplo
```bash
# Inspecionar runtime extensions registradas no Management Cluster e o status de rollout de MachineDeployments
kubectl get extensionconfigs.runtime.cluster.x-k8s.io -A
kubectl describe machinedeployment my-cluster-md-0
```

## Limites e trade-offs
Habilitar atualizações in-place via extensões requer que o provedor de bootstrap/SO convidado nos nós possua um agente ou mecanismo capaz de aplicar a mudança solicitada na máquina em execução e reportar sucesso ao Management Cluster; caso a extensão de atualização in-place falhe ou atinja timeout em um nó, a máquina deve ser substituída para evitar desvio de configuração.

## Como verificar
Ao alterar a especificação de um `MachineDeployment`, acompanhe `clusterctl describe cluster <nome>` para observar a estratégia de atualização aplicada pelos controladores às `Machines`.

## Conexões
- [[clusterapi-auto-remediacao-nos-machinehealthcheck]] — Veja também: Kubernetes Cluster API: detecção de falhas e auto-remediação de nós com MachineHealthCheck.
- [[clusterapi-topologia-clusterclass-ponto-unico-controle]] — Veja também: Kubernetes Cluster API: reutilização de topologias e ponto único de controle com ClusterClass.
- [[clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes]] — Referência cruzada direta com clusterapi-arquitetura-declarativa-ciclo-vida-clusters-kubernetes.
- [[clusterapi-recursos-cluster-machine-imutabilidade]] — Referência cruzada direta com clusterapi-recursos-cluster-machine-imutabilidade.
- [[clusterapi-machinedeployment-machineset-machinepool-rollout]] — Referência cruzada direta com clusterapi-machinedeployment-machineset-machinepool-rollout.

## Fontes
- [Cluster API GitHub — README.md (Declarative Kubernetes-style APIs, Goals, Non-Goals & Supported Providers)](https://raw.githubusercontent.com/kubernetes-sigs/cluster-api/main/README.md) — README oficial do Kubernetes Cluster API (CAPI) detalhando objetivos, escopo declarativo e lista de provedores de infraestrutura e bootstrap; consultado em 2026-10-03.
- [Cluster API Book — Concepts & Quick Start (Management/Workload Clusters, clusterctl, MachineDeployment & ClusterClass)](https://cluster-api.sigs.k8s.io/user/concepts.html) — Documentação oficial do Cluster API cobrindo Management Cluster, Workload Cluster, Providers, Machine, MachineSet, MachineDeployment, Bootstrap com cloud-init, ClusterClass e comandos clusterctl; consultado em 2026-10-03.
- [Kubernetes SIGs Cluster API — Official GitHub Repository](https://github.com/kubernetes-sigs/cluster-api) — Repositório oficial Apache-2.0 do projeto kubernetes-sigs/cluster-api; consultado em 2026-10-03.
