---
id: software.devops.tranche01.000050
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

# Origem com Michael DeHaan, mais de 5.000 contribuidores, patrocínio Red Hat e licença GPL v3.0+

## Em uma frase
As seções Authors e License no final do README oficial registram a autoria, o patrocínio e o licenciamento do projeto: o Ansible foi criado por Michael DeHaan (`@mpdehaan`), conta com contribuições de mais de 5.000 usuários (observando expressamente: "This project is substantially coded by humans"), é patrocinado pela Red Hat, Inc. (`redhat.com`) e distribuído sob a licença **GNU General Public License v3.0 or later** (`COPYING`).

## Por que importa
Ao incorporar ferramentas de automação na cadeia de build ou distribuir pacotes derivados, equipes jurídicas e de engenharia precisam distinguir softwares sob licenças permissivas (como Apache-2.0 ou MPL-2.0) do motor `ansible-core`, que é licenciado sob GPL v3.0 ou posterior.

## Como funciona
Consulte o texto integral em `https://github.com/ansible/ansible/blob/devel/COPYING` para revisar os termos da GPL v3.0+ e o guia `.github/CONTRIBUTING.md` ao contribuir código para o repositório.

## Exemplo
O README registra nominalmente o criador Michael DeHaan, a marca de mais de 5.000 contribuidores, a nota de que o projeto é substancialmente codificado por humanos e o patrocínio da Red Hat, Inc.

## Limites e trade-offs
Esta nota fecha o bloco sobre o Ansible consolidando os metadados de autoria, governança e licenciamento publicados no README oficial da branch `devel`.

## Como verificar
Conferi as seções Authors e License no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-parallel-execution-and-zero-bootstrap]] — Veja também: Gerenciamento paralelo de frotas e provisionamento instantâneo sem etapa de bootstrap.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Repositório oficial ansible/ansible](https://github.com/ansible/ansible) — Repositório oficial do ansible-core no GitHub com diretório context/, COPYING (GPL v3.0+) e .github/CONTRIBUTING.md.; consultado em 2026-10-03.
