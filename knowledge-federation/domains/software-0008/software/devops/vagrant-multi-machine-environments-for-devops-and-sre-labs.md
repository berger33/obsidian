---
id: software.devops.tranche06.000580
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

# Modelagem de ambientes multi-máquina (Multi-Machine) no Vagrantfile para laboratórios de DevOps e SRE

## Em uma frase
Como o `Vagrantfile` utiliza sintaxe Ruby declarativa sob `Vagrant.configure("2") do |config|`, um único `Vagrantfile` pode definir e orquestrar **múltiplas máquinas virtuais independentes (`config.vm.define`)** ao mesmo tempo — por exemplo, um servidor de banco de dados, dois servidores de aplicação e um balanceador de carga, ou múltiplos nós de um cluster Nomad, Consul ou Kubernetes. Com ambientes multi-máquina, todos os comandos do CLI (`vagrant up`, `vagrant ssh <nome>`, `vagrant halt <nome>`, `vagrant destroy`) aceitam opcionalmente o nome ou expressão regular de uma máquina específica ou operam sobre todo o conjunto.

## Por que importa
Para engenheiros de plataforma e SREs, testar failover de cluster (Consul Raft, Nomad, MetalLB L2/BGP, Rook Ceph) exige simular a queda abrupta de um nó específico (`vagrant halt node2`) e observar como os nós restantes (`node1` e `node3`) reagem na mesma rede privada.

## Como funciona
Utilize blocos `config.vm.define "nome" do |node|` dentro do seu `Vagrantfile` para construir topologias multi-nó completas e teste cenários de falha controlando nós individuais pelo nome (`vagrant halt node-2`, `vagrant up node-2`).

## Exemplo
Em um laboratório de alta disponibilidade do HashiCorp Consul e Nomad, o `Vagrantfile` define 3 servidores e 2 clientes; o engenheiro sobe toda a topologia com `vagrant up`, conecta no primeiro servidor com `vagrant ssh server-1` e simula a perda de um nó com `vagrant halt server-2`.

## Limites e trade-offs
Ao definir um ambiente multi-máquina no `Vagrantfile`, dimensionar cada VM com a memória mínima necessária (ex.: `vb.memory = "1024"` ou `"2048"`) evita esgotar a RAM física do laptop quando todas as VMs sobem juntas no `vagrant up`.

## Como verificar
Execute `vagrant status` em um `Vagrantfile` multi-máquina e confirme a listagem individual do estado de cada máquina definida.

## Conexões
- [[vagrant-vm-lifecycle-commands-ssh-suspend-halt-reload-and-destroy]] — Veja também: Ciclo de vida completo do ambiente Vagrant: ssh, suspend, resume, halt, reload e destroy.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
