---
id: software.devops.tranche05.000433
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md", "https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md", "https://github.com/kubevirt/kubevirt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura orientada a serviços e coreografia entre virt-controller, virt-handler e libvirtd

## Em uma frase
Conforme detalhado em `docs/architecture.md`, o KubeVirt é construído usando uma arquitetura orientada a serviços e um padrão de coreografia que entrega três elementos ao cluster: (1) os CRDs na API do Kubernetes; (2) controladores de escopo de cluster — como o **`virt-controller`** — que observam objetos `VMI` e criam/gerenciam os Pods correspondentes para que o agendador do Kubernetes escolha um host; e (3) um daemon específico por nó — o **`virt-handler`** — que roda ao lado do `kubelet` em cada host para coordenar, junto ao **`libvirtd`** dentro do pod lançador, a inicialização e configuração da instância virtual até que ela reflita o estado desejado.

## Por que importa
Como tanto os controladores (`virt-controller`) quanto os daemons (`virt-handler`) rodam como Pods sobre o próprio cluster Kubernetes (e o runtime `libvirtd`/QEMU roda encapsulado dentro do Pod da VMI), toda a orquestração de agendamento, limites de CPU/memória, armazenamento e rede é delegada nativamente ao Kubernetes.

## Como funciona
Ao diagnosticar por que uma VM não inicia, siga a cadeia de coreografia: verifique primeiro o objeto `VM`/`VMI`, depois os logs do `virt-controller` (criação do Pod `virt-launcher`), o agendamento do Pod pelo `kube-scheduler` e por fim os logs do `virt-handler` no nó e do contêiner da VMI.

## Exemplo
Quando um `VMI` fica pendente de inicialização, o administrador verifica o pod `virt-launcher` correspondente e os logs do `virt-handler` daquele nó, identificando rapidamente que um volume PVC solicitado pela VM ainda aguardava anexação CSI.

## Limites e trade-offs
Nunca instale um daemon `libvirtd` avulso manualmente no sistema operacional host tentando gerenciar as VMs do KubeVirt por fora do Kubernetes; o ciclo de vida do `libvirtd` pertence exclusivamente aos pods gerenciados pelo KubeVirt.

## Como verificar
Execute `kubectl get pods -n kubevirt` e confirme que as réplicas do `virt-controller`, `virt-api` e o DaemonSet `virt-handler` estão todos `Running` e saudáveis.

## Conexões
- [[kubevirt-vmi-vm-and-vmirs-custom-resources-hierarchy]] — Veja também: Hierarquia de Custom Resources no KubeVirt: VMI (efêmero), VM (stateful) e VMIRS (escala horizontal).
- [[kubevirt-delegating-scheduling-networking-and-storage-to-kubernetes]] — Veja também: Delegação de agendamento, rede e armazenamento ao Kubernetes na pilha do KubeVirt.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
