---
id: software.devops.tranche06.000577
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

# Compartilhamento de código entre host e convidado com Synced Folders no Vagrant

## Em uma frase
Conforme documentado no Getting Started oficial do Vagrant (`vagrantup.com/docs/getting-started`), as **Synced Folders (pastas sincronizadas)** permitem que o desenvolvedor continue editando o código-fonte na sua própria máquina host (usando sua IDE favorita, Git e ferramentas gráficas locais) enquanto compila e executa o código dentro do ambiente isolado da máquina virtual convidada. Por padrão, o Vagrant monta automaticamente o diretório do projeto no host (onde está o `Vagrantfile`) em **`/vagrant`** dentro da máquina convidada.

## Por que importa
Sem pastas sincronizadas, o desenvolvedor teria que editar arquivos pelo terminal via SSH dentro da VM ou copiar arquivos manualmente via `scp` a cada alteração. A pasta `/vagrant` une a ergonomia do sistema operacional host ao isolamento do kernel convidado.

## Como funciona
Utilize a montagem padrão `/vagrant` ou configure pastas sincronizadas adicionais com `config.vm.synced_folder "src/", "/srv/website"` escolhendo o tipo de sincronização mais performático para o seu sistema operacional (`nfs`, `smb`, `rsync` ou `virtiofs`/pastas nativas do provedor).

## Exemplo
Um engenheiro edita o código de um módulo de rede eBPF no VS Code em seu laptop macOS; ao salvar o arquivo, a mudança aparece imediatamente em `/vagrant` dentro da VM Linux do Vagrant onde ele compila e testa o programa no kernel Linux real.

## Limites e trade-offs
Em projetos com dezenas de milhares de arquivos pequenos (como `node_modules` ou diretórios `.git` gigantes), pastas compartilhadas padrão de hipervisor podem apresentar alta latência de I/O; nesses casos, monte o diretório de dependências em um caminho nativo dentro do disco da VM (ex.: `/home/vagrant/node_modules`) ou use `nfs`/`rsync`.

## Como verificar
Entre na máquina com `vagrant ssh`, liste `/vagrant` (`ls -la /vagrant`) e confirme a presença dos arquivos do diretório do projeto no host.

## Conexões
- [[vagrant-automated-provisioning-shell-ansible-docker-and-file]] — Veja também: Provisionamento automatizado de máquinas com Shell, Ansible, File e Docker no Vagrant.
- [[vagrant-networking-port-forwarding-private-and-public-networks]] — Veja também: Configuração de rede no Vagrant: Port Forwarding, Private Network (Host-Only) e Public Network (Bridged).

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
