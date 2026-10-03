---
id: software.devops.tranche06.000575
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

# Aviso oficial de depreciação do HCP Vagrant (novembro de 2026) e continuidade do Vagrant CLI

## Em uma frase
No topo do README oficial (`> [!IMPORTANT]`), a HashiCorp publica um comunicado importante sobre o serviço de nuvem associado: o **HCP Vagrant** está em processo de depreciação e recursos limitados estarão disponíveis a partir da edição comunitária com efeito em **2 de novembro de 2026** (detalhado em `developer.hashicorp.com/hcp/docs/vagrant/hcp-vagrant-eol`). O comunicado ressalta em negrito: **"This change is only for HCP Vagrant and does not apply to Vagrant CLI"** — isto é, a mudança refere-se exclusivamente ao serviço hospedado HCP Vagrant Registry/Cloud e **não se aplica à ferramenta de linha de comando Vagrant CLI**.

## Por que importa
Equipes de infraestrutura que armazenam ou consomem boxes privadas hospedadas no serviço de nuvem HCP Vagrant precisam conhecer o marco de **2 de novembro de 2026** para planejar o armazenamento de seus artefatos `.box` em registros internos (como Artifactory, Nexus, buckets S3/GCS com URLs versionadas ou servidores HTTP internos), sabendo ao mesmo tempo que o **Vagrant CLI** continua operando normalmente.

## Como funciona
Para ambientes corporativos de longo prazo, hospede suas Vagrant Boxes internas em seu próprio repositório de artefatos ou bucket de objetos corporativo (apontando `config.vm.box_url` para o catálogo JSON/URL interna) em vez de depender exclusivamente de recursos depreciados do HCP Vagrant.

## Exemplo
Ao revisar o aviso oficial no README do repositório `hashicorp/vagrant`, a equipe de plataforma configura seu servidor de artefatos interno para hospedar as boxes geradas pelo Packer e atualiza `config.vm.box_url` nos templates internos antes de novembro de 2026.

## Limites e trade-offs
Não confunda a depreciação de funcionalidades do portal de nuvem **HCP Vagrant** com o fim do **Vagrant CLI**: o Vagrant CLI suporta nativamente carregar boxes diretamente de arquivos locais, servidores HTTP/HTTPS próprios e múltiplos repositórios sem depender do HCP.

## Como verificar
Verifique nos `Vagrantfiles` da organização de onde as boxes estão sendo baixadas (`config.vm.box` / `config.vm.box_url`) e valide o acesso direto ao artefato `.box`.

## Conexões
- [[vagrant-system-path-dependencies-bsdtar-and-curl]] — Veja também: Dependências obrigatórias de sistema do Vagrant no PATH: bsdtar e curl.
- [[vagrant-automated-provisioning-shell-ansible-docker-and-file]] — Veja também: Provisionamento automatizado de máquinas com Shell, Ansible, File e Docker no Vagrant.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
