---
id: software.devops.tranche01.000042
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/ansible/ansible/devel/README.md", "https://github.com/ansible/ansible"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura sem agentes sobre SSH e os nove princípios de design do Ansible

## Em uma frase
A seção Design Principles do README oficial lista os nove princípios que moldam a arquitetura do Ansible: (1) processo de setup extremamente simples com curva de aprendizado mínima; (2) gerenciar máquinas rapidamente e em paralelo; (3) evitar agentes customizados e portas abertas adicionais, sendo **agentless** ao aproveitar o daemon SSH existente; (4) descrever infraestrutura numa linguagem amigável para máquinas e humanos; (5) focar em segurança e facilidade de auditoria/revisão/reescrita de conteúdo; (6) gerenciar máquinas remotas novas instantaneamente, sem precisar fazer bootstrap de nenhum software; (7) permitir desenvolvimento de módulos em qualquer linguagem dinâmica, não apenas Python; (8) ser utilizável como usuário não-root (`non-root`); e (9) ser o sistema de automação de TI mais fácil de usar.

## Por que importa
Exigir um daemon proprietário instalado previamente em cada servidor ou switch cria um problema de ovo-e-galinha (como instalar e atualizar o agente em máquinas recém-criadas?) e abre novas portas de rede; operar de forma agentless sobre o SSH existente permite gerenciar uma máquina nova no segundo em que ela sobe.

## Como funciona
Conecte o nó de controle às máquinas alvo usando o daemon SSH padrão já presente no sistema operacional, operando com contas não-root e escalonamento controlado de privilégios quando necessário.

## Exemplo
Como destacado nos itens 6, 7 e 8 dos princípios, uma máquina recém-provisionada pode ser gerenciada instantaneamente sem bootstrap prévio, como usuário não-root, e até com módulos escritos em outras linguagens dinâmicas além de Python.

## Limites e trade-offs
Mesmo não exigindo um agente residente do Ansible, a maioria dos módulos padrão em execução no nó remoto utiliza um interpretador disponível na máquina alvo (ou executa comandos raw/script quando este ainda não existe).

## Como verificar
Conferi os nove tópicos da seção Design Principles no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-what-it-is-and-six-domains]] — Veja também: Ansible: sistema de automação de TI para configuração, deploy, nuvem, tarefas ad-hoc, rede e orquestração.
- [[ansible-installation-pip-pkg-and-devel-branch]] — Veja também: Instalação de versões lançadas via `pip` ou gerenciador de pacotes do sistema versus uso da branch `devel`.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Repositório oficial ansible/ansible](https://github.com/ansible/ansible) — Repositório oficial do ansible-core no GitHub com diretório context/, COPYING (GPL v3.0+) e .github/CONTRIBUTING.md.; consultado em 2026-10-03.
