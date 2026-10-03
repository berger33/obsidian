---
id: software.devops.tranche05.000436
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

# Modelo de segurança do KubeVirt: coexistência com cargas nativas sem elevação de privilégios

## Em uma frase
A seção *Native Workloads* de `docs/architecture.md` estabelece duas garantias arquiteturais e de segurança para clusters que executam KubeVirt ao lado de contêineres nativos: (1) operadores de aplicação não devem precisar de permissões adicionais para usar recursos do cluster com VMs em comparação ao uso dos mesmos recursos com um Pod comum; e (2) **do ponto de vista de segurança, instalar e usar o KubeVirt jamais deve conceder aos usuários qualquer permissão que eles já não possuam em relação a cargas nativas** — por exemplo, um operador de aplicação não privilegiado nunca deve conseguir acesso a um Pod privilegiado ou ao host por meio de uma funcionalidade do KubeVirt.

## Por que importa
Executar um hipervisor QEMU/KVM exige acesso a dispositivos de virtualização do kernel, mas se a API do KubeVirt permitisse que um usuário comum montasse caminhos arbitrários do host (`hostPath`) ou elevasse privilégios do pod lançador, o KubeVirt abriria uma brecha crítica de escalação de privilégio em clusters multi-tenant.

## Como funciona
Utilize as `ClusterRoles` padrão agregadas pelo KubeVirt ao RBAC do Kubernetes (`view`, `edit`, `admin`) para conceder permissões de gerenciamento de `VM`/`VMI` restritas ao namespace de cada equipe, sem jamás conceder permissão de criar pods `privileged` diretamente aos usuários finais.

## Exemplo
Em um cluster compartilhado entre múltiplas equipes de produto, os desenvolvedores têm permissão RBAC no seu namespace para criar `Pods`, `PVCs` e `VirtualMachines`, podendo subir tanto contêineres quanto VMs sem qualquer acesso administrativo aos nós trabalhadores.

## Limites e trade-offs
Nunca conceda permissões de edição direta sobre o DaemonSet `virt-handler` ou sobre o namespace `kubevirt` a contas de usuários de aplicação, mantendo o plano de controle do KubeVirt isolado sob administração da plataforma.

## Como verificar
Valide com `kubectl auth can-i` que a conta de serviço ou papel de operador da aplicação consegue criar objetos `virtualmachines.kubevirt.io` no seu namespace, mas continua impedida de criar pods privilegiados ou recursos de cluster.

## Conexões
- [[kubevirt-the-kubevirt-razor-design-principle-and-multus-cni]] — Veja também: O princípio de design The KubeVirt Razor e a integração de rede com Multus e CNI.
- [[kubevirt-kubernetes-version-support-matrix-and-sig-release]] — Veja também: Matriz de compatibilidade KubeVirt vs Kubernetes e governança do repositório kubevirt/sig-release.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
