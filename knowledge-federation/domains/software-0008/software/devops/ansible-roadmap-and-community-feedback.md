---
id: software.devops.tranche01.000047
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
fontes: ["https://raw.githubusercontent.com/ansible/ansible/devel/README.md", "https://github.com/ansible/ansible"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Planejamento público por versão no Ansible Roadmap e influência da comunidade

## Em uma frase
A seção Roadmap do README oficial explica que, com base no feedback da equipe e da comunidade, um roadmap inicial é publicado para cada versão maior ou menor (exemplificando com `2.7`, `2.8`, etc.), e que a página oficial `https://docs.ansible.com/ansible/devel/roadmap/` detalha tanto o que está planejado quanto como a comunidade pode influenciar o roadmap.

## Por que importa
Quando uma organização depende de recursos futuros do `ansible-core` ou precisa antecipar mudanças planejadas para o próximo ciclo de release, consultar a página oficial de Roadmap mostra o escopo planejado para cada versão antes do fechamento da branch `stable-2.X`.

## Como funciona
Acesse `https://docs.ansible.com/ansible/devel/roadmap/` para verificar o cronograma e os itens planejados para a versão em desenvolvimento na branch `devel` e use os canais comunitários indicados na página para enviar feedback.

## Exemplo
O próprio README destaca que o roadmap inicial de cada versão nasce da combinação entre o planejamento do time e o feedback recebido da comunidade.

## Limites e trade-offs
Itens listados em um roadmap inicial para a branch `devel` representam o plano de trabalho e podem sofrer ajustes até o corte final da release estável correspondente.

## Como verificar
Conferi a seção Roadmap no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-forum-matrix-and-bullhorn-newsletter]] — Veja também: Canais oficiais de comunicação: Ansible Forum (tags `ansible`, `ansible-core`, `playbook`), Matrix e newsletter The Bullhorn.
- [[ansible-security-auditability-and-nonroot-operation]] — Veja também: Segurança e auditabilidade nos princípios do Ansible: leitura humana e execução não-root.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Repositório oficial ansible/ansible](https://github.com/ansible/ansible) — Repositório oficial do ansible-core no GitHub com diretório context/, COPYING (GPL v3.0+) e .github/CONTRIBUTING.md.; consultado em 2026-10-03.
