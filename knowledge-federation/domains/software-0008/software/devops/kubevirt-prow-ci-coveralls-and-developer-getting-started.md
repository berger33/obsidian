---
id: software.devops.tranche05.000439
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

# Desenvolvimento, testes contínuos no Prow CI e documentação de componentes do KubeVirt

## Em uma frase
O README oficial destaca a infraestrutura de qualidade e desenvolvimento do projeto: integração contínua executada no **KubeVirt Prow CI** (`prow.ci.kubevirt.io/?job=push-kubevirt-main`), monitoramento de cobertura de testes via Coveralls, conformidade CII Best Practices e documentação detalhada para desenvolvedores dividida em `docs/getting-started.md`, `docs/architecture.md`, **`docs/components.md`** (visão detalhada de todos os componentes internos) e a referência completa da API em `kubevirt.io/api-reference/`.

## Por que importa
Para operar o KubeVirt em escala ou contribuir com correções para o projeto, consultar `docs/components.md` e a `API Reference` oficial evita suposições incorretas sobre os campos de especificação de discos, interfaces, probes e estratégias de execução (`runStrategy`) dos CRDs.

## Como funciona
Utilize a referência oficial `kubevirt.io/api-reference/` ao construir manifestos ou Helm charts que geram objetos `VirtualMachine`, e siga `docs/getting-started.md` para levantar ambientes locais de desenvolvimento e teste do KubeVirt.

## Exemplo
Ao parametrizar um template de `VirtualMachine` no Backstage, o engenheiro de plataforma consulta `kubevirt.io/api-reference/` e `docs/components.md` para validar os campos exatos de CPU, dispositivos de disco `virtio` e probes de prontidão da VM.

## Limites e trade-offs
Valide sempre os manifestos de `VirtualMachine` contra o schema OpenAPI instalado pelos CRDs do KubeVirt (`kubectl apply --dry-run=server`) nos pipelines de CI antes de aplicá-los em produção.

## Como verificar
Execute `kubectl explain vm.spec.template.spec` em um cluster com KubeVirt instalado para confirmar a disponibilidade da documentação do schema da API diretamente no cluster.

## Conexões
- [[kubevirt-ecosystem-integrations-libvirt-cockpit-and-ansible]] — Veja também: Integrações do ecossistema KubeVirt: Libvirt, Cockpit e coleção Ansible kubevirt.core.
- [[kubevirt-dco-signed-off-by-and-community-governance]] — Veja também: Exigência de Developer Certificate of Origin (Signed-off-by: git commit -s) e canais da comunidade KubeVirt.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
