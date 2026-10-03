---
id: software.devops.tranche06.000573
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

# Fluxo rápido com vagrant init, vagrant up e download sob demanda de Boxes

## Em uma frase
A seção *Quick Start* do README oficial demonstra que construir o primeiro ambiente virtual com o Vagrant exige apenas dois comandos: **`vagrant init hashicorp/bionic64`** (que gera um arquivo `Vagrantfile` inicial configurado para usar a imagem base *box* `hashicorp/bionic64`) seguido de **`vagrant up`** (que provisiona e liga o ambiente). O README destaca um comportamento importante de eficiência: o comando `vagrant up` dispara o download da box especificada **apenas se detectar que aquela box ainda não existe no cache local do sistema** (`~/.vagrant.d/boxes`), reutilizando a imagem base em cache para todas as novas máquinas subsequentes.

## Por que importa
Em vez de instalar um sistema operacional a partir de uma imagem ISO do zero a cada novo projeto (o que leva dezenas de minutos), o conceito de **Vagrant Box** empacota uma imagem base pré-instalada (frequentemente gerada de forma automatizada com o **HashiCorp Packer**) que é clonada em segundos no `vagrant up`.

## Como funciona
Construa suas próprias Vagrant Boxes corporativas padronizadas e endurecidas usando **HashiCorp Packer** e referencie-as em `config.vm.box` com versão fixada (`config.vm.box_version`) nos `Vagrantfiles` das equipes.

## Exemplo
Um engenheiro cria uma pasta de laboratório, roda `vagrant init hashicorp/bionic64` e `vagrant up`; na primeira vez o Vagrant baixa a box, e nos próximos laboratórios que usam a mesma box a máquina virtual já inicia em poucos segundos a partir do cache local.

## Limites e trade-offs
Gerencie periodicamente o cache local de boxes na sua estação de trabalho usando **`vagrant box list`**, **`vagrant box outdated`** e **`vagrant box prune`** para remover versões antigas de boxes que não são mais utilizadas e liberar gigabytes de disco.

## Como verificar
Execute `vagrant box list` para verificar as boxes armazenadas localmente após o primeiro `vagrant up`.

## Conexões
- [[vagrant-multi-provider-architecture-virtualbox-vmware-cloud-and-containers]] — Veja também: Arquitetura multi-provedor do Vagrant: VirtualBox, VMware, AWS, OpenStack, Docker e LXC.
- [[vagrant-system-path-dependencies-bsdtar-and-curl]] — Veja também: Dependências obrigatórias de sistema do Vagrant no PATH: bsdtar e curl.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
