---
id: software.devops.tranche06.000579
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

# Ciclo de vida completo do ambiente Vagrant: ssh, suspend, resume, halt, reload e destroy

## Em uma frase
O guia `vagrantup.com/docs/getting-started` documenta os comandos que controlam todo o ciclo de vida diário de um ambiente Vagrant após o `vagrant up`: **`vagrant ssh`** (abre uma sessão SSH autenticada automaticamente com chave gerenciada pelo Vagrant dentro da máquina convidada), **`vagrant suspend`** (salva o estado exato em memória da VM em disco para retomada rápida com **`vagrant resume`**), **`vagrant halt`** (realiza o desligamento gracioso — graceful shutdown — do sistema operacional convidado liberando RAM e CPU do host, mas preservando o disco da VM), **`vagrant reload`** (equivale a um `halt` seguido de `up`, aplicando alterações feitas no `Vagrantfile` como portas de rede ou pastas sincronizadas) e **`vagrant destroy`** (desliga e apaga completamente os discos e recursos da máquina virtual do computador).

## Por que importa
Saber quando usar `vagrant suspend` (pausa rápida para o almoço), `vagrant halt` (fim do expediente liberando RAM mas mantendo o banco populado), `vagrant reload` (após editar `config.vm.network` no `Vagrantfile`) ou `vagrant destroy && vagrant up` (reconstruir do zero limpo) otimiza o uso de recursos da estação de trabalho.

## Como funciona
Sempre que alterar configurações de hardware, rede ou pastas sincronizadas no `Vagrantfile`, execute **`vagrant reload`** (ou `vagrant reload --provision`) para que o hipervisor recrie os adaptadores e aplique as novas configurações na VM.

## Exemplo
Ao terminar os testes de um laboratório pesado de 3 VMs, o engenheiro executa `vagrant destroy -f` para liberar imediatamente dezenas de gigabytes de disco e gigabytes de memória RAM da sua máquina de trabalho, sabendo que poderá recriar tudo a qualquer momento com `vagrant up`.

## Limites e trade-offs
Lembre-se de que `vagrant destroy` apaga tudo o que estava apenas dentro do disco virtual da VM, mas **preserva intactos** os arquivos do seu projeto no diretório do host sincronizado em `/vagrant`.

## Como verificar
Teste a sequência `vagrant up`, `vagrant ssh -c "uname -a"`, `vagrant halt` e `vagrant destroy -f` em um ambiente de teste confirmando a limpeza completa em `vagrant status`.

## Conexões
- [[vagrant-networking-port-forwarding-private-and-public-networks]] — Veja também: Configuração de rede no Vagrant: Port Forwarding, Private Network (Host-Only) e Public Network (Bridged).
- [[vagrant-multi-machine-environments-for-devops-and-sre-labs]] — Veja também: Modelagem de ambientes multi-máquina (Multi-Machine) no Vagrantfile para laboratórios de DevOps e SRE.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
