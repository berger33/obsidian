---
id: software.devops.tranche11.001095
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
fontes: ["https://mise.jdx.dev/getting-started.html", "https://raw.githubusercontent.com/jdx/mise/main/README.md", "https://github.com/jdx/mise"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Segurança de configuração no mise: mise trust e operação em Paranoid Mode

## Em uma frase
Como arquivos `mise.toml` podem definir tarefas, hooks e diretivas de ambiente capazes de executar código, o `mise` inclui o comando **`mise trust`** e o **modo paranóico (*paranoid mode*)** para controlar quando configurações não globais de projetos são autorizadas a rodar.

## Por que importa
Ao clonar um repositório de terceiros ou fazer checkout de uma branch de um Pull Request externo, um arquivo `mise.toml` malicioso poderia tentar sobrescrever variáveis críticas de ambiente (como `LD_PRELOAD` ou `PATH`) ou executar comandos arbitrários. Revisar o arquivo e gerenciar a confiança protege a estação do desenvolvedor.

## Como funciona
Conforme explica a seção *Trusting config files* do guia oficial (`mise.jdx.dev/getting-started.html`): (1) você deve sempre revisar configurações escritas por outras pessoas antes de executá-las, usando **`mise trust`** para marcar explicitamente como confiável um arquivo de configuração que você já auditou; (2) no **modo normal** (fora de ambientes de CI), comandos que executam explicitamente o comportamento do projeto — incluindo `mise install`, `mise exec` e `mise run` — confiam automaticamente na configuração ativa; porém (3) com o **paranoid mode** habilitado, nenhuma configuração não global é confiável automaticamente, exigindo que o usuário execute explicitamente `mise trust` após revisar cada arquivo `mise.toml`.

## Exemplo
```bash
# Revisar o conteúdo do mise.toml de um repositório recém-clonado e marcá-lo explicitamente como confiável
cat mise.toml
mise trust
mise config ls
```

## Limites e trade-offs
Habilitar o modo paranóico adiciona um passo extra manual (`mise trust`) toda vez que você clona um novo repositório ou quando o arquivo `mise.toml` sofre alterações que invalidam o hash de confiança anterior, trocando conveniência imediata por segurança máxima contra execução acidental ao navegar por diretórios com `mise activate` ativo.

## Como verificar
Execute `mise config ls` no diretório do projeto para verificar os arquivos de configuração detectados e seu estado de carregamento pelo `mise`.

## Conexões
- [[mise-ativacao-shell-activate-vs-shims-matriz-shells]] — Veja também: Ativação de shell no mise (mise activate vs Shims) e matriz de compatibilidade entre Bash, Zsh, Fish, Nushell, Elvish, Xonsh e PowerShell.
- [[mise-registro-ferramentas-backends-github-cargo-npm-core]] — Veja também: Registro de ferramentas e arquitetura de Backends do mise (shorthands vs github:, cargo:, npm:, core:).
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Referência cruzada direta com mise-configuracao-projeto-mise-toml-tools-env-tasks.
- [[mise-gerenciador-ferramentas-variaveis-ambiente-tarefas]] — Referência cruzada direta com mise-gerenciador-ferramentas-variaveis-ambiente-tarefas.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://mise.jdx.dev/getting-started.html) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
