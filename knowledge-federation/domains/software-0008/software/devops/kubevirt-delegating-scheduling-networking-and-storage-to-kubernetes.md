---
id: software.devops.tranche05.000434
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

# Delegação de agendamento, rede e armazenamento ao Kubernetes na pilha do KubeVirt

## Em uma frase
O diagrama de pilha (*Stack*) em `docs/architecture.md` deixa claro o papel exato de cada camada: os usuários falam com a API de Virtualização no Kubernetes API Server, e **agendamento (scheduling), rede (networking) e armazenamento (storage) são todos delegados ao próprio Kubernetes**, enquanto o KubeVirt fornece especificamente a funcionalidade de virtualização. Na prática, cada `VMI` é materializado em um Pod gerenciado pelo KubeVirt (`virt-launcher`), que consome CPUs, memória, `PersistentVolumeClaims` e interfaces CNI exatamente como qualquer outro Pod do cluster.

## Por que importa
Essa decisão arquitetural permite que o KubeVirt aproveite imediatamente afinidades de nó, taints/tolerations, ResourceQuotas, NetworkPolicies, Service Meshes e drivers CSI de armazenamento em bloco (como Rook Ceph e Longhorn) sem reinventar um agendador ou gerenciador de volumes paralelo.

## Como funciona
Dimensione `requests` e `limits` de CPU e memória, afinidades de nó e `PersistentVolumeClaims` (preferencialmente em `volumeMode: Block` ou com *Backing Images* para alta performance de disco) diretamente na especificação do template da `VirtualMachine`.

## Exemplo
Uma VM de banco de dados declarada no KubeVirt utiliza `nodeSelector` e `topologySpreadConstraints` nativos do Kubernetes para agendar seu pod `virt-launcher` em nós com SSD NVMe dedicado e consome um PVC ReadWriteOnce provisionado via CSI.

## Limites e trade-offs
Lembre-se de contabilizar a pequena sobrecarga adicional de memória do processo QEMU/`libvirtd` dentro do pod `virt-launcher` ao definir os limites (`limits.memory`) do namespace e do nó no Kubernetes.

## Como verificar
Verifique o pod `virt-launcher-<vmi>` associado à máquina virtual em execução e confirme que os volumes PVC e recursos de CPU/memória foram alocados pelo `kubelet`.

## Conexões
- [[kubevirt-virt-controller-virt-handler-and-libvirtd-choreography]] — Veja também: Arquitetura orientada a serviços e coreografia entre virt-controller, virt-handler e libvirtd.
- [[kubevirt-the-kubevirt-razor-design-principle-and-multus-cni]] — Veja também: O princípio de design The KubeVirt Razor e a integração de rede com Multus e CNI.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
