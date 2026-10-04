---
id: software.devops.tranche06.000572
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md", "https://www.vagrantup.com/docs/getting-started", "https://github.com/hashicorp/vagrant"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura multi-provedor do Vagrant: VirtualBox, VMware, AWS, OpenStack, Docker e LXC

## Em uma frase
O README oficial destaca que os ambientes de desenvolvimento gerenciados pelo Vagrant não estão presos a um único hipervisor: eles podem rodar em plataformas de virtualização locais como **VirtualBox** ou **VMware**, na nuvem via **AWS** ou **OpenStack**, ou diretamente em contêineres como **Docker** ou **LXC puro (raw LXC)** (além de provedores comunitários como `libvirt`/KVM e Hyper-V). Enquanto o guia de início rápido utiliza o VirtualBox por ser gratuito e multiplataforma, o mesmo fluxo de trabalho (`vagrant up`, `vagrant ssh`, `vagrant destroy`) permanece idêntico em qualquer provedor.

## Por que importa
Em uma equipe distribuída onde alguns engenheiros usam Linux com KVM/`libvirt` ou Docker, outros usam macOS/Windows com VMware/VirtualBox e testes pesados rodam em instâncias temporárias na AWS ou OpenStack, abstrair o provedor sob o mesmo `Vagrantfile` evita reescrever scripts de laboratório para cada plataforma.

## Como funciona
Configure blocos específicos de provedor (`config.vm.provider`) no `Vagrantfile` quando precisar ajustar memória, CPUs ou flags nativas de VirtualBox, VMware, Docker ou nuvem, mantendo o provisionamento pós-boot compartilhado entre todos.

## Exemplo
Um desenvolvedor local executa `vagrant up` usando VirtualBox em sua estação de trabalho para validar uma receita de infraestrutura e, para um teste de carga maior, executa `vagrant up --provider=aws` reutilizando o mesmo provisionador.

## Limites e trade-offs
Ao compartilhar um `Vagrantfile` entre desenvolvedores em arquiteturas de CPU diferentes (`x86_64` vs `arm64`), escolha *boxes* multi-arquitetura ou parametrize o provedor compatível com a arquitetura do host.

## Como verificar
Execute `vagrant up` especificando (ou validando o padrão de) `--provider` e confirme com `vagrant status` que a máquina subiu no provedor esperado.

## Conexões
- [[vagrant-portable-development-environments-and-vagrantfile]] — Veja também: Vagrant e o Vagrantfile para construção de ambientes de desenvolvimento portáteis e reproduzíveis.
- [[vagrant-quickstart-workflow-vagrant-init-and-vagrant-up-boxes]] — Veja também: Fluxo rápido com vagrant init, vagrant up e download sob demanda de Boxes.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
