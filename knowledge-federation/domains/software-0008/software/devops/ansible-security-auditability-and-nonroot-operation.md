---
id: software.devops.tranche01.000048
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/ansible/ansible/devel/README.md", "https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Segurança e auditabilidade nos princípios do Ansible: leitura humana e execução não-root

## Em uma frase
Entre os nove itens da seção Design Principles no README oficial, três conectam diretamente automação e segurança operacional: descrever a infraestrutura numa linguagem que seja ao mesmo tempo amigável para máquinas e para humanos; focar em segurança e facilidade de auditoria, revisão e reescrita de conteúdo; e ser utilizável como não-root (`Be usable as non-root`), complementados pela certificação CII Best Practices (projeto 2372) no topo do repositório.

## Por que importa
Scripts imperativos extensos em shell ou agentes que exigem rodar permanentemente como `root` dificultam a revisão de segurança antes da mudança; uma linguagem declarativa legível por humanos que opera sem agentes sobre SSH e suporta usuários não-root reduz o privilégio necessário e torna o código de automação auditável por equipes de segurança.

## Como funciona
Estruture os playbooks e roles de forma clara para revisão humana em Pull Requests e configure a conexão e a execução remota para operar com contas não-root sempre que possível.

## Exemplo
O selo CII Best Practices (`bestpractices.coreinfrastructure.org/projects/2372`) no cabeçalho do README atesta as práticas de engenharia e segurança do próprio projeto upstream.

## Limites e trade-offs
A facilidade de leitura e auditoria do formato do Ansible não dispensa revisar cuidadosamente módulos que executam comandos arbitrários no sistema alvo.

## Como verificar
Conferi a seção Design Principles e os badges do cabeçalho no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-roadmap-and-community-feedback]] — Veja também: Planejamento público por versão no Ansible Roadmap e influência da comunidade.
- [[ansible-parallel-execution-and-zero-bootstrap]] — Veja também: Gerenciamento paralelo de frotas e provisionamento instantâneo sem etapa de bootstrap.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Ansible — Installation Guide oficial](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) — Guia oficial de instalação do Ansible em múltiplas plataformas via pip e gerenciadores de pacotes.; consultado em 2026-10-03.
