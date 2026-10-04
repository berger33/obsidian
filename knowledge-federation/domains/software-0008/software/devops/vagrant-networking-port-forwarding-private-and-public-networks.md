---
id: software.devops.tranche06.000578
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

# Configuração de rede no Vagrant: Port Forwarding, Private Network (Host-Only) e Public Network (Bridged)

## Em uma frase
O guia oficial `vagrantup.com/docs/getting-started` estrutura as opções de conectividade de rede das máquinas gerenciadas pelo Vagrant em três modos configuráveis no `Vagrantfile` (`config.vm.network`): (1) **Forwarded Ports (`forwarded_port`)** — mapeia uma porta na máquina host (ex.: `host: 8080`) para uma porta dentro da VM convidada (`guest: 80`), permitindo acessar serviços da VM via `localhost:8080`; (2) **Private Network (`private_network`)** — cria uma rede privada isolada (Host-Only) acessível apenas pelo host e por outras VMs na mesma rede privada, ideal para clusters multi-nó; e (3) **Public Network (`public_network`)** — conecta a VM em modo *bridged* diretamente à LAN física como se fosse mais uma máquina independente na rede.

## Por que importa
Para simular um cluster Kubernetes bare-metal (por exemplo, 1 control-plane e 2 workers testando MetalLB ou Strimzi), o mapeamento simples de portas NAT não basta: os nós precisam enxergar uns aos outros por endereços IP fixos em uma mesma sub-rede L2 usando `private_network`.

## Como funciona
Use `forwarded_port` (preferencialmente vinculando `host_ip: "127.0.0.1"`) para acessar uma aplicação web simples da VM no navegador do host, e use `private_network` com IPs estáticos ao construir laboratórios multi-máquina no `Vagrantfile`.

## Exemplo
Um `Vagrantfile` define 3 máquinas virtuais (`node1`, `node2`, `node3`) em loop Ruby atribuindo a cada uma um IP `private_network` sequencial (`192.168.56.11`, `.12`, `.13`), permitindo que elas formem um cluster Kubernetes completo conversando entre si e com o host.

## Limites e trade-offs
Ao usar `forwarded_port` sem especificar `host_ip: "127.0.0.1"`, a porta mapeada no host fica exposta em todas as interfaces (`0.0.0.0`), permitindo que outras máquinas na mesma rede Wi-Fi/LAN alcancem o serviço de desenvolvimento; restrinja sempre a `127.0.0.1` quando o acesso for apenas local.

## Como verificar
Após rodar `vagrant up`, verifique o acesso à porta encaminhada em `127.0.0.1` ou o ping para o IP da `private_network` a partir do host.

## Conexões
- [[vagrant-synced-folders-host-guest-code-sharing]] — Veja também: Compartilhamento de código entre host e convidado com Synced Folders no Vagrant.
- [[vagrant-vm-lifecycle-commands-ssh-suspend-halt-reload-and-destroy]] — Veja também: Ciclo de vida completo do ambiente Vagrant: ssh, suspend, resume, halt, reload e destroy.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
