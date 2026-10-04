---
id: software.devops.tranche05.000432
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

# Hierarquia de Custom Resources no KubeVirt: VMI (efêmero), VM (stateful) e VMIRS (escala horizontal)

## Em uma frase
O documento oficial `docs/architecture.md` explica a separação entre o bloco básico de execução e os controladores de alto nível do KubeVirt: o **`VirtualMachineInstance` (`VMI`)** é o recurso customizado que representa a instância básica e efêmera de uma máquina virtual em execução (análoga a um `Pod` isolado); na maioria dos cenários produtivos, o usuário não cria o `VMI` diretamente, mas sim recursos de nível superior que o gerenciam: o **`VirtualMachine` (`VM`)**, que representa uma máquina virtual stateful que pode ser parada e iniciada preservando seus dados e estado de configuração, ou o **`VirtualMachineInstanceReplicaSet` (`VMIRS`)**, similar a um `ReplicaSet` de Pods, que mantém um grupo de `VMIs` efêmeros idênticos definidos por um template.

## Por que importa
Se um operador criar apenas um `VMI` avulso e desligá-lo, a instância efêmera encerra seu ciclo de vida assim como um Pod sem controlador. Compreender a diferença entre `VM` (ciclo de vida stateful start/stop) e `VMIRS` (pool escalável de VMs efêmeras) evita perda acidental da definição da máquina ao desligá-la.

## Como funciona
Declare recursos `kind: VirtualMachine` (`VM`) para servidores persistentes que precisam sobreviver a paradas e reinicializações mantendo seus volumes, e utilize `VirtualMachineInstanceReplicaSet` (`VMIRS`) para frotas homogêneas de workers virtuais stateless.

## Exemplo
Para hospedar um servidor Windows de aplicação corporativa que passa por janelas programadas de desligamento e boot, o engenheiro define um objeto `VirtualMachine` com `runStrategy` apropriada, que cria e remove o `VirtualMachineInstance` subjacente conforme o estado desejado.

## Limites e trade-offs
Não edite diretamente o objeto `VirtualMachineInstance` (`VMI`) gerenciado por um `VirtualMachine` (`VM`) esperando que a mudança persista após o próximo ciclo de stop/start; aplique as alterações de especificação no recurso pai `VM`.

## Como verificar
Inspecione a relação de propriedade (`ownerReferences`) entre o recurso `VM` e o `VMI` criado com `kubectl get vm,vmi -o wide`.

## Conexões
- [[kubevirt-virtual-machine-management-addon-for-kubernetes]] — Veja também: KubeVirt como add-on de gerenciamento declarativo de máquinas virtuais no Kubernetes.
- [[kubevirt-virt-controller-virt-handler-and-libvirtd-choreography]] — Veja também: Arquitetura orientada a serviços e coreografia entre virt-controller, virt-handler e libvirtd.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
