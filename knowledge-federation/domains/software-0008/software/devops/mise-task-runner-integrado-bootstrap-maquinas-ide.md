---
id: software.devops.tranche11.001100
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/jdx/mise/main/README.md", "https://mise.jdx.dev/getting-started.html", "https://github.com/jdx/mise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Task Runner integrado ([tasks]), Bootstrap de máquinas e integração com IDEs no mise

## Em uma frase
Além de gerenciar versões de ferramentas e variáveis de ambiente, o `mise` funciona como um **Task Runner** completo (`mise run <task>`, `mise tasks ls`) e suporta **Bootstrap** declarativo de máquinas (pacotes de sistema, dotfiles e serviços) e integração direta com IDEs e pipelines de CI/CD.

## Por que importa
Quando um projeto usa `Makefile` ou scripts Bash avulsos, a tarefa falha se o desenvolvedor esquecer de ativar o ambiente virtual ou instalar a versão correta do linter. No `mise`, toda tarefa executada com `mise run` já garante automaticamente que as ferramentas declaradas em `[tools]` estão instaladas e no `PATH` e que as variáveis de `[env]` estão carregadas antes de iniciar o comando.

## Como funciona
Conforme destacam o README oficial (`jdx/mise`) e o guia *Getting started* (`mise.jdx.dev/getting-started.html`): (1) **`mise tasks ls`** descobre e lista todas as tarefas configuradas no projeto com suas descrições; (2) **`mise run <task>`** instala automaticamente ferramentas ausentes de `[tools]`, aplica `[env]` e executa o script definido em `run`; (3) para uso fora do terminal interativo (como **IDEs** — VS Code, JetBrains, Neovim — ou runners de **CI**), pode-se usar `mise run`, `mise exec` ou o diretório de **Shims** (`~/.local/share/mise/shims`); e (4) o recurso de **Bootstrap** (`mise.jdx.dev/bootstrap.html`) permite declarar a configuração completa da estação de trabalho.

## Exemplo
```toml
# Definir um conjunto de tarefas de plataforma (lint, audit e test) no mise.toml usando as ferramentas do projeto
[tools]
polaris = "latest"
pluto = "latest"

[tasks.audit-k8s]
description = "Auditar manifestos Kubernetes com Polaris e Pluto"
run = '''
pluto detect-files -d ./deploy
polaris audit --audit-path ./deploy --set-exit-code-on-danger
'''
```

## Limites e trade-offs
Para projetos que já possuem dezenas de tarefas complexas em um `Taskfile.yml` (Task) ou `Makefile`, você não precisa reescrever tudo de imediato: pode gerenciar o próprio binário `task` ou `make` na seção `[tools]` do `mise.toml` e migrar tarefas gradualmente para `[tasks]` conforme a conveniência da equipe.

## Como verificar
Execute `mise tasks ls` para confirmar que a tarefa `audit-k8s` aparece documentada na listagem da CLI e invoque `mise run audit-k8s` para validar a execução encadeada.

## Conexões
- [[mise-gerenciamento-ambientes-diretivas-env-dotenv-hierarquia]] — Veja também: Gerenciamento de variáveis de ambiente no mise: seção [env], carregamento de arquivos .env e hierarquia de configuração.
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Referência cruzada direta com mise-configuracao-projeto-mise-toml-tools-env-tasks.
- [[polaris-auditoria-iac-cli-ci-cd-scores-danger-flags]] — Referência cruzada direta com polaris-auditoria-iac-cli-ci-cd-scores-danger-flags.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://mise.jdx.dev/getting-started.html) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
