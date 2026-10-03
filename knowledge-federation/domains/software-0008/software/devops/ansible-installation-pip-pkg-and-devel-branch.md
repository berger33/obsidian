---
id: software.devops.tranche01.000043
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

# Instalação de versões lançadas via `pip` ou gerenciador de pacotes do sistema versus uso da branch `devel`

## Em uma frase
A seção Use Ansible do README oficial orienta que qualquer usuário pode instalar uma versão lançada do Ansible com `pip` ou com um gerenciador de pacotes do sistema (remetendo ao guia oficial `https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html`), enquanto usuários avançados e desenvolvedores podem rodar diretamente a branch `devel`, que contém as funcionalidades e correções mais recentes.

## Por que importa
Separar claramente o caminho de produção (pacotes estáveis instalados via `pip` ou gerenciador do sistema operacional) do caminho de experimentação e desenvolvimento (rodar a branch `devel` diretamente) evita que equipes de operação sofram com quebras inesperadas em playbooks críticos.

## Como funciona
Em ambientes de produção e CI/CD corporativo, instale uma versão lançada seguindo `intro_installation.html`; reserve a execução direta da branch `devel` para testar recursos novos, validar correções ou contribuir com a comunidade.

## Exemplo
O próprio README faz a ressalva honesta sobre a branch `devel`: embora ela seja razoavelmente estável, você tem maior probabilidade de encontrar mudanças incompatíveis (breaking changes) ao rodá-la diretamente.

## Limites e trade-offs
Ao instalar via `pip`, observe no badge oficial do repositório que o pacote do motor principal no PyPI é publicado sob o nome `ansible-core`.

## Como verificar
Conferi a seção Use Ansible e o badge do PyPI no README oficial de `ansible/ansible`.

## Conexões
- [[ansible-agentless-ssh-and-nine-design-principles]] — Veja também: Arquitetura sem agentes sobre SSH e os nove princípios de design do Ansible.
- [[ansible-branch-model-devel-vs-stable-2x]] — Veja também: Modelo de branches do repositório: `devel` ativa, linhas `stable-2.X` e ciclo de manutenção.

## Fontes
- [Ansible — README oficial (branch devel)](https://raw.githubusercontent.com/ansible/ansible/devel/README.md) — README oficial do Ansible com seis frentes de automação, nove princípios de design (agentless sobre SSH, zero bootstrap, non-root), instalação via pip/package manager, branches devel vs stable-2.X, Ansible Forum/Matrix/Bullhorn, context/, criador e licença GPL v3.0+.; consultado em 2026-10-03.
- [Ansible — Installation Guide oficial](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) — Guia oficial de instalação do Ansible em múltiplas plataformas via pip e gerenciadores de pacotes.; consultado em 2026-10-03.
