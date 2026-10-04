---
id: software.devops.tranche05.000438
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

# Integrações do ecossistema KubeVirt: Libvirt, Cockpit e coleção Ansible kubevirt.core

## Em uma frase
Na seção *Related resources*, o README oficial referencia as integrações fundamentais do ecossistema KubeVirt: **Kubernetes** (`kubernetes.io`), **Libvirt** (`libvirt.org`, biblioteca e daemon de virtualização utilizados internamente para gerenciar o ciclo de vida das instâncias QEMU/KVM), **Cockpit** (`cockpit-project.org`) e a coleção oficial do **Ansible `kubevirt.core`** (`github.com/kubevirt/kubevirt.core`), que permite automatizar o provisionamento e gerenciamento de máquinas virtuais no KubeVirt usando playbooks Ansible.

## Por que importa
Equipes de infraestrutura que já automatizam o ciclo de vida de máquinas virtuais com Ansible em hipervisores tradicionais podem reutilizar seus playbooks e fluxos de automação apontando a coleção oficial `kubevirt.core` para a API do KubeVirt no Kubernetes.

## Como funciona
Adote a coleção `kubevirt.core` do Ansible quando desejar integrar o provisionamento de recursos `VirtualMachine` do KubeVirt e a configuração pós-boot do sistema operacional convidado dentro do mesmo fluxo de automação Ansible.

## Exemplo
Durante a migração de servidores Linux gerenciados por Ansible para o KubeVirt, a equipe substitui apenas o módulo de criação da VM pelo módulo da coleção `kubevirt.core`, mantendo intactos todos os papéis (roles) Ansible de configuração de pacotes e hardening do SO convidado.

## Limites e trade-offs
Ao usar automação Ansible com KubeVirt, passe configurações iniciais de rede e chaves SSH via `cloud-init` na especificação da `VirtualMachine` para que o Ansible possa conectar-se imediatamente após a VM atingir o estado `Running`.

## Como verificar
Execute um playbook ou manifesto de teste com `cloud-init` em uma `VirtualMachine` do KubeVirt e confirme que a instância inicializa e responde com a configuração injetada.

## Conexões
- [[kubevirt-kubernetes-version-support-matrix-and-sig-release]] — Veja também: Matriz de compatibilidade KubeVirt vs Kubernetes e governança do repositório kubevirt/sig-release.
- [[kubevirt-prow-ci-coveralls-and-developer-getting-started]] — Veja também: Desenvolvimento, testes contínuos no Prow CI e documentação de componentes do KubeVirt.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
