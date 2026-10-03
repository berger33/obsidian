---
id: software.devops.tranche06.000574
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

# Dependências obrigatórias de sistema do Vagrant no PATH: bsdtar e curl

## Em uma frase
Logo na abertura da seção *Quick Start*, o README oficial documenta um pré-requisito técnico específico que frequentemente causa falhas em instalações mínimas ou a partir do código-fonte: **o Vagrant exige que os utilitários `bsdtar` e `curl` estejam disponíveis no `PATH` do sistema operacional para executar com sucesso** (`Package dependencies: Vagrant requires bsdtar and curl to be available on your system PATH to run successfully`).

## Por que importa
Como uma Vagrant Box é essencialmente um arquivo pacote (`.box`, contendo a imagem de disco virtual, `metadata.json` e `Vagrantfile` base) baixado via HTTP/HTTPS e extraído no sistema local, o Vagrant invoca internamente o **`curl`** para transferências resilientes de rede (com suporte a retomada, proxies e certificados) e o **`bsdtar`** (`libarchive`) para descompactar formatos variados de arquivo com rapidez e portabilidade entre SOs.

## Como funciona
Ao instalar o Vagrant em imagens mínimas de servidores Linux, contêineres de CI ou compilar a partir do código-fonte (`vagrantup.com/docs/installation/source`), verifique sempre que os pacotes que fornecem `bsdtar` (`libarchive-tools` no Debian/Ubuntu, `bsdtar` no RHEL/Fedora) e `curl` estão instalados e acessíveis no `PATH`.

## Exemplo
Em um servidor Linux minimalista recém-instalado para rodar laboratórios automatizados, o comando `vagrant box add` falhava ao tentar extrair a box; instalar o pacote `libarchive-tools` (disponibilizando `bsdtar` no `PATH`) e `curl` resolveu o problema imediatamente.

## Limites e trade-offs
Em redes corporativas que exigem proxy HTTP/HTTPS ou certificados CA internos, lembre-se de que configurar as variáveis padrão reconhecidas pelo `curl` (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`, `CURL_CA_BUNDLE`) afeta diretamente o download de boxes pelo Vagrant.

## Como verificar
Execute `which bsdtar && which curl && vagrant --version` no terminal para comprovar que ambas as dependências obrigatórias estão presentes no `PATH`.

## Conexões
- [[vagrant-quickstart-workflow-vagrant-init-and-vagrant-up-boxes]] — Veja também: Fluxo rápido com vagrant init, vagrant up e download sob demanda de Boxes.
- [[vagrant-hcp-vagrant-deprecation-notice-november-2026-and-cli-continuity]] — Veja também: Aviso oficial de depreciação do HCP Vagrant (novembro de 2026) e continuidade do Vagrant CLI.

## Fontes
- [HashiCorp Vagrant GitHub — README.md (Portable Development Environments, Providers, Quick Start, bsdtar/curl & HCP Vagrant EOL Notice)](https://raw.githubusercontent.com/hashicorp/vagrant/main/README.md) — README oficial do HashiCorp Vagrant detalhando criação e distribuição de ambientes de desenvolvimento portáteis entre Windows, macOS e Linux sobre múltiplos provedores (VirtualBox, VMware, AWS, OpenStack, Docker, LXC), dependências de sistema (bsdtar e curl no PATH), comandos vagrant init hashicorp/bionic64 e vagrant up, e o aviso oficial de depreciação do serviço de nuvem HCP Vagrant em 2 de novembro de 2026 (sem afetar o Vagrant CLI).; consultado em 2026-10-03.
- [HashiCorp Vagrant Official Documentation — Getting Started Guide](https://www.vagrantup.com/docs/getting-started) — Guia oficial de início rápido do Vagrant cobrindo Vagrantfile, boxes, pastas sincronizadas, provisionamento e rede.; consultado em 2026-10-03.
- [HashiCorp Vagrant — Official GitHub Repository](https://github.com/hashicorp/vagrant) — Repositório oficial do HashiCorp Vagrant.; consultado em 2026-10-03.
