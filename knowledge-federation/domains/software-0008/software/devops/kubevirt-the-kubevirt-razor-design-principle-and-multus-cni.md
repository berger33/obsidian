---
id: software.devops.tranche05.000435
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

# O princípio de design The KubeVirt Razor e a integração de rede com Multus e CNI

## Em uma frase
A seção *The Razor* em `docs/architecture.md` documenta o princípio fundamental de engenharia usado pelos mantenedores do projeto para resolver dilemas arquiteturais — o **KubeVirt Razor**: ***"If something is useful for Pods, we should not implement it only for VMs"*** ("Se algo é útil para Pods, não devemos implementá-lo apenas para VMs"). O documento ilustra esse princípio com o caso da conexão de VMs a redes externas: em vez de criar um atalho proprietário do KubeVirt conectando a VM diretamente a uma bridge do host por fora do Kubernetes, o projeto escolheu o caminho modular de integrar e aprimorar o **Multus** (`intel/multus-cni`) e o padrão **CNI** (`containernetworking`), beneficiando tanto Pods quanto VMs.

## Por que importa
Soluções que furam as abstrações do Kubernetes para conectar VMs diretamente à placa de rede física do host quebram a visibilidade do Kubelet, políticas de segurança e portabilidade. Ao seguir o *KubeVirt Razor* sobre CNI e Multus, uma VM pode usar a rede padrão do cluster e múltiplas interfaces secundárias (VLANs, SR-IOV, bridges) usando a mesma especificação de rede de qualquer Pod avançado.

## Como funciona
Quando uma máquina virtual no KubeVirt precisar de múltiplas interfaces de rede ou conexão direta a VLANs corporativas (L2), utilize **Multus CNI** com `NetworkAttachmentDefinitions` anexadas ao template da VM em vez de scripts manuais de rede nos nós.

## Exemplo
Uma appliance virtual de firewall rodando no KubeVirt recebe a interface padrão do pod para gerenciamento e duas interfaces secundárias de alta velocidade conectadas a VLANs distintas via Multus CNI, seguindo o padrão documentado em `docs/architecture.md`.

## Limites e trade-offs
Evite soluções de contorno que manipulem interfaces de rede ou discos diretamente no host Linux fora do modelo CNI/CSI do Kubernetes, pois elas violam o isolamento do pod `virt-launcher` e falham quando a VM é reagendada em outro nó.

## Como verificar
Inspecione as interfaces de rede anexadas ao `VMI` e ao pod `virt-launcher` confirmando o provisionamento limpo via CNI / Multus.

## Conexões
- [[kubevirt-delegating-scheduling-networking-and-storage-to-kubernetes]] — Veja também: Delegação de agendamento, rede e armazenamento ao Kubernetes na pilha do KubeVirt.
- [[kubevirt-security-model-no-privilege-escalation-for-operators]] — Veja também: Modelo de segurança do KubeVirt: coexistência com cargas nativas sem elevação de privilégios.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
