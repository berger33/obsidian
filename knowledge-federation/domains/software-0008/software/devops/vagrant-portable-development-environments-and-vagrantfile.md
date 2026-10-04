---
id: software.devops.tranche06.000571
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

# Vagrant e o Vagrantfile para construção de ambientes de desenvolvimento portáteis e reproduzíveis

## Em uma frase
O HashiCorp Vagrant (`vagrantup.com` / `github.com/hashicorp/vagrant`) é uma ferramenta para construir e distribuir ambientes de desenvolvimento completos e portáteis. Conforme define o README oficial, o Vagrant fornece o framework e o formato declarativo de configuração (o arquivo **`Vagrantfile`**) para criar e gerenciar ambientes de desenvolvimento que podem viver localmente no computador do engenheiro ou na nuvem, sendo totalmente portáteis entre **Windows, macOS e Linux**.

## Por que importa
Quando projetos exigem kernels específicos, configurações de rede de baixo nível, múltiplos nós simulando um cluster bare-metal (por exemplo, para testar KubeVirt, MetalLB, Rook Ceph ou Ansible) ou sistemas operacionais completos que não cabem em um único contêiner de aplicação, configurar máquinas virtuais manualmente gera deriva entre as máquinas da equipe. O `Vagrantfile` versionado no Git garante que todos subam exatamente a mesma topologia.

## Como funciona
Inclua um `Vagrantfile` na raiz do repositório sempre que o projeto exigir uma máquina virtual Linux completa ou um laboratório multi-nó reproduzível, permitindo que qualquer desenvolvedor inicie o ambiente com um único comando.

## Exemplo
Para testar playbooks Ansible e módulos de kernel Linux em 3 servidores simulados antes de aplicá-los em produção, a equipe de infraestrutura versiona um `Vagrantfile` que define as 3 VMs com IPs privados fixos e discos extras.

## Limites e trade-offs
Não armazene os diretórios de estado local gerados pelo Vagrant (`.vagrant/`) no Git; adicione sempre `.vagrant/` ao arquivo `.gitignore` do repositório, mantendo apenas o `Vagrantfile` e os scripts de provisionamento sob controle de versão.

## Como verificar
Execute `vagrant status` no diretório contendo o `Vagrantfile` para validar a leitura correta da topologia declarada.

## Conexões
- [[vagrant-multi-provider-architecture-virtualbox-vmware-cloud-and-containers]] — Veja também: Arquitetura multi-provedor do Vagrant: VirtualBox, VMware, AWS, OpenStack, Docker e LXC.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
