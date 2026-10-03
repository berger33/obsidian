---
id: software.devops.tranche05.000437
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

# Matriz de compatibilidade KubeVirt vs Kubernetes e governança do repositório kubevirt/sig-release

## Em uma frase
A seção *Useful links* do README oficial destaca que o repositório **KubeVirt SIG-release** (`github.com/kubevirt/sig-release`) mantém a documentação oficial sobre versões atuais, anteriores e futuras do projeto, incluindo especificamente a **KubeVirt to Kubernetes version support matrix** (`releases/k8s-support-matrix.md`), as mudanças relevantes da próxima versão (`upcoming-changes.md`) e o cronograma de lançamentos (`releases/`).

## Por que importa
Como o KubeVirt interage intimamente com APIs do Kubelet, dispositivos de nó, CNI, CSI e validação de CRDs, executar uma versão do KubeVirt fora da matriz de versões do Kubernetes testadas e suportadas pelo `sig-release` pode causar falhas em migrações ao vivo (live migration) ou no agendamento de `VMIs`.

## Como funciona
Antes de atualizar a versão minor do Kubernetes ou do KubeVirt em produção, consulte obrigatoriamente `k8s-support-matrix.md` e `upcoming-changes.md` no repositório `kubevirt/sig-release` para confirmar o pareamento suportado.

## Exemplo
Ao planejar o upgrade anual dos clusters bare-metal que hospedam VMs e contêineres, a equipe de plataforma verifica a matriz em `kubevirt/sig-release` e atualiza o operador do KubeVirt em sincronia com a janela homologada do Kubernetes.

## Limites e trade-offs
Não atualize o Kubernetes para uma versão recém-lançada sem antes confirmar na matriz do `kubevirt/sig-release` se a versão instalada do KubeVirt já foi compilada e validada contra aquela release do Kubernetes.

## Como verificar
Verifique a versão do operador KubeVirt (`kubectl get kubevirt -n kubevirt -o yaml`) e a versão dos nós Kubernetes confirmando que o par consta na matriz oficial de suporte.

## Conexões
- [[kubevirt-security-model-no-privilege-escalation-for-operators]] — Veja também: Modelo de segurança do KubeVirt: coexistência com cargas nativas sem elevação de privilégios.
- [[kubevirt-ecosystem-integrations-libvirt-cockpit-and-ansible]] — Veja também: Integrações do ecossistema KubeVirt: Libvirt, Cockpit e coleção Ansible kubevirt.core.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
