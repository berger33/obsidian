---
id: software.devops.tranche01.000044
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

# Modelo de branches do repositório: `devel` ativa, linhas `stable-2.X` e ciclo de manutenção

## Em uma frase
A seção Branch Info do README oficial documenta a estrutura de ramificações do repositório `ansible/ansible`: a branch `devel` corresponde à versão ativamente em desenvolvimento; as branches `stable-2.X` correspondem às releases estáveis mantidas; quem deseja abrir um Pull Request deve criar sua branch a partir de `devel` e configurar o ambiente de desenvolvimento conforme o guia oficial; e a página `release_and_maintenance.html` detalha quais branches estão ativas e seu ciclo de suporte.

## Por que importa
Saber que todo Pull Request novo entra sempre em `devel` (e nunca diretamente numa branch `stable-2.X` sem passar pelo fluxo do projeto) e onde consultar a tabela de manutenção das séries `stable-2.X` evita PRs abertos contra a branch errada e ajuda a planejar upgrades de `ansible-core`.

## Como funciona
Ao desenvolver uma correção ou melhoria para o `ansible-core`, ramifique a partir de `devel` (`git checkout -b minha-feature devel`), configure o ambiente descrito em `developing_modules_general.html#common-environment-setup` e consulte `release_and_maintenance.html` para checar as versões `stable-2.X` suportadas.

## Exemplo
As branches de manutenção seguem o padrão de nomenclatura `stable-2.X` no repositório, enquanto o pipeline de CI em Azure Pipelines valida continuamente a branch `devel`.

## Limites e trade-offs
Antes de iniciar uma alteração grande para a branch `devel`, a seção Contribute to Ansible recomenda conversar previamente com a equipe para evitar esforço duplicado.

## Como verificar
Conferi as seções Branch Info e Contribute to Ansible no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-installation-pip-pkg-and-devel-branch]] — Veja também: Instalação de versões lançadas via `pip` ou gerenciador de pacotes do sistema versus uso da branch `devel`.
- [[ansible-module-development-guidelines-and-context]] — Veja também: Diretrizes de desenvolvimento de módulos: diretório `context/`, checklist e boas práticas.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Repositório oficial ansible/ansible](https://github.com/ansible/ansible) — Repositório oficial do ansible-core no GitHub com diretório context/, COPYING (GPL v3.0+) e .github/CONTRIBUTING.md.; consultado em 2026-10-03.
