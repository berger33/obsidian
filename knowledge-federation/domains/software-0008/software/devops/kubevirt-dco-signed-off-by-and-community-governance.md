---
id: software.devops.tranche05.000440
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

# Exigência de Developer Certificate of Origin (Signed-off-by: git commit -s) e canais da comunidade KubeVirt

## Em uma frase
As seções *Community* e *Submitting patches* do README oficial estabelecem o protocolo de colaboração do KubeVirt: todo contribuidor que envia patches ao projeto é obrigado a certificar que possui o direito legal de submeter o código adicionando a linha **`Signed-off-by: Real Name <email@address.com>`** ao final de cada mensagem de commit (gerada automaticamente passando a opção **`-s` ao comando `git commit`**), em conformidade com o **Developer's Certificate of Origin 1.1** (`docs/developer-certificate-of-origin`). A coordenação comunitária ocorre no canal `#virtualization` / `@kubernetes/kubevirt-dev` no Slack do Kubernetes, no Google Group `kubevirt-dev` e no repositório `kubevirt/community`.

## Por que importa
Pull requests abertos no repositório `kubevirt/kubevirt` sem a assinatura DCO (`Signed-off-by`) em todos os commits são bloqueados automaticamente pelos verificadores de conformidade de CI, atrasando a revisão e o merge de correções.

## Como funciona
Sempre utilize `git commit -s` ao preparar commits para o repositório `kubevirt/kubevirt` (ou `git commit --amend -s` caso tenha esquecido no último commit) e acompanhe discussões de design no repositório `kubevirt/community` e no grupo `kubevirt-dev`.

## Exemplo
Um engenheiro de plataforma corrige um bug na documentação de arquitetura do KubeVirt, cria o commit com `git commit -s -m "docs: clarify VMI lifecycle"` contendo a linha `Signed-off-by:` e aprova todas as checagens de DCO e Prow CI no pull request.

## Limites e trade-offs
Configure seu nome real e endereço de e-mail válido no Git (`git config user.name` e `git config user.email`) antes de rodar `git commit -s`, pois o DCO exige identificação nominal compatível com o autor do commit.

## Como verificar
Verifique com `git log -1` que a mensagem do commit contém a linha `Signed-off-by: Nome <email>` no formato exigido por `docs/developer-certificate-of-origin`.

## Conexões
- [[kubevirt-prow-ci-coveralls-and-developer-getting-started]] — Veja também: Desenvolvimento, testes contínuos no Prow CI e documentação de componentes do KubeVirt.

## Fontes
- [KubeVirt GitHub — README.md (Virtualization Extension for Kubernetes, CRDs, Support Matrix & DCO)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/README.md) — README oficial do KubeVirt (Apache-2.0) detalhando extensão do Kubernetes via CRDs e controladores para criar, agendar, iniciar, parar e excluir VMs ao lado de Pods, matriz de suporte de versões do Kubernetes em kubevirt/sig-release, recursos relacionados (Libvirt, Cockpit, kubevirt.core Ansible) e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [KubeVirt GitHub — docs/architecture.md (VM, VMI, VMIRS, virt-controller, virt-handler & KubeVirt Razor)](https://raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md) — Documento oficial de arquitetura do KubeVirt detalhando a delegação de agendamento/rede/armazenamento ao Kubernetes, CRDs VirtualMachineInstance (VMI), VirtualMachine (VM) e VirtualMachineInstanceReplicaSet (VMIRS), componentes virt-controller, virt-handler e libvirtd, modelo de segurança sem elevação de privilégios e o princípio The KubeVirt Razor com Multus e CNI.; consultado em 2026-10-03.
- [KubeVirt — Official GitHub Repository](https://github.com/kubevirt/kubevirt) — Repositório oficial Apache-2.0 do KubeVirt na CNCF.; consultado em 2026-10-03.
