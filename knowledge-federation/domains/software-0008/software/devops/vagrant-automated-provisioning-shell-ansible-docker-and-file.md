---
id: software.devops.tranche06.000576
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

# Provisionamento automatizado de máquinas com Shell, Ansible, File e Docker no Vagrant

## Em uma frase
O guia oficial `vagrantup.com/docs/getting-started` detalha como o Vagrant transforma uma box base limpa em um ambiente pronto para desenvolvimento sem intervenção manual através dos **Provisioners** (`config.vm.provision`). Durante o primeiro `vagrant up` (ou sempre que solicitado via **`vagrant provision`** ou **`vagrant reload --provision`**), o Vagrant executa automaticamente scripts Shell, playbooks **Ansible** (executados a partir do host via `ansible` ou dentro da própria convidada via `ansible_local`), upload de arquivos (`file`), instalação de contêineres Docker, Puppet ou Chef.

## Por que importa
Se o desenvolvedor precisar entrar via `vagrant ssh` e rodar 20 comandos manuais após o `vagrant up` para instalar pacotes e bancos de dados, o ambiente deixa de ser reproduzível e descartável. O bloco `config.vm.provision` torna a configuração pós-boot 100% determinística.

## Como funciona
Declare toda a instalação de dependências e configuração do sistema em blocos `config.vm.provision` idempotentes (como scripts shell com `set -euo pipefail` ou playbooks Ansible) dentro do `Vagrantfile`.

## Exemplo
Para testar um playbook Ansible localmente mesmo em uma máquina host Windows que não tem Ansible instalado, o desenvolvedor usa o provisionador `ansible_local` no `Vagrantfile`, fazendo com que o Vagrant instale e execute o Ansible diretamente dentro da VM Linux convidada.

## Limites e trade-offs
Escreva scripts de provisionamento **idempotentes** (que possam ser executados múltiplas vezes com `vagrant provision` sem falhar caso o pacote, usuário ou diretório já tenha sido criado na execução anterior).

## Como verificar
Execute `vagrant provision` sobre uma máquina já em execução e confirme que todas as etapas de provisionamento concluem sem erros na segunda passagem.

## Conexões
- [[vagrant-hcp-vagrant-deprecation-notice-november-2026-and-cli-continuity]] — Veja também: Aviso oficial de depreciação do HCP Vagrant (novembro de 2026) e continuidade do Vagrant CLI.
- [[vagrant-synced-folders-host-guest-code-sharing]] — Veja também: Compartilhamento de código entre host e convidado com Synced Folders no Vagrant.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
