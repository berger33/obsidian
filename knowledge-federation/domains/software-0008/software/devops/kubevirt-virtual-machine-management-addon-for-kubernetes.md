---
id: software.devops.tranche05.000431
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

# KubeVirt como add-on de gerenciamento declarativo de máquinas virtuais no Kubernetes

## Em uma frase
O KubeVirt (`kubevirt.io`), licenciado sob Apache-2.0, é um add-on de gerenciamento de máquinas virtuais para o Kubernetes cujo objetivo é fornecer uma base comum para soluções de virtualização rodando sobre o Kubernetes. Em vez de modificar o código-fonte do Kubernetes em si, o KubeVirt estende um cluster existente adicionando novos tipos de recursos via **Custom Resource Definitions (CRDs)** — especialmente `VirtualMachine` (`VM`) e `VirtualMachineInstance` (`VMI`) — acompanhados de controladores e agentes executados como Pods sobre o próprio cluster, permitindo declarativamente **criar, agendar, iniciar, parar e excluir máquinas virtuais** lado a lado com cargas nativas em contêineres.

## Por que importa
Organizações em modernização de infraestrutura frequentemente possuem cargas legadas ou especializadas (sistemas operacionais Windows, kernels customizados ou appliances virtuais) que não podem ser containerizadas imediatamente. Operar uma plataforma separada de hipervisores apenas para essas VMs duplica ferramentas de rede, armazenamento, RBAC e GitOps; o KubeVirt unifica VMs e Pods na mesma API do Kubernetes.

## Como funciona
Instale o KubeVirt sobre clusters Kubernetes com suporte a virtualização por hardware (KVM) nos nós trabalhadores para gerenciar máquinas virtuais usando os mesmos fluxos `kubectl`, Helm, Argo CD e Prometheus já adotados para contêineres.

## Exemplo
Uma equipe de infraestrutura migra servidores virtuais legados para o mesmo cluster Kubernetes bare-metal onde já rodam os novos microsserviços, declarando cada VM em YAML versionado no Git e provisionando seus discos via PVCs CSI (como Rook Ceph RBD ou Longhorn).

## Limites e trade-offs
Certifique-se de que os nós do cluster onde as VMs serão agendadas possuam extensões de virtualização de CPU (`vmx` ou `svm`, `/dev/kvm`) habilitadas na BIOS/hipervisor antes de implantar cargas produtivas no KubeVirt.

## Como verificar
Aplique um manifesto de `VirtualMachine` de teste e confirme seu agendamento e inicialização via `kubectl get vm,vmi`.

## Conexões
- [[kubevirt-vmi-vm-and-vmirs-custom-resources-hierarchy]] — Veja também: Hierarquia de Custom Resources no KubeVirt: VMI (efêmero), VM (stateful) e VMIRS (escala horizontal).

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
