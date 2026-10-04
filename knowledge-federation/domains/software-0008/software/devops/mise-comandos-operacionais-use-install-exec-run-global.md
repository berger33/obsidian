---
id: software.devops.tranche11.001093
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

# Diferença semântica entre os comandos do mise: mise use, mise use --global, mise install, mise exec e mise run

## Em uma frase
O `mise` distingue claramente entre comandos que **modificam a configuração** (`mise use <tool>@<ver>` no projeto ou `mise use --global` em `~/.config/mise/config.toml`), comandos que **apenas instalam o que já está declarado** (`mise install`) e comandos que **executam processos no ambiente do projeto** (`mise exec` e `mise run`).

## Por que importa
Uma dúvida recorrente de quem migra de outras ferramentas é a diferença entre `mise install` e `mise use`: rodar `mise use node@24` altera o arquivo `mise.toml` do diretório atual, enquanto em um projeto já existente clonado do Git (ou no pipeline de CI) o comando correto para baixar as ferramentas sem tocar no arquivo de configuração é `mise install` (ou diretamente `mise exec` / `mise run`).

## Como funciona
Conforme a tabela comparativa oficial *Project configuration or global defaults?* (`mise.jdx.dev/getting-started.html`):
1. **`mise use node@24`**: instala o Node.js e grava a requisição de versão no `mise.toml` do diretório do projeto;
2. **`mise use --global node@24`**: instala o Node.js e salva como padrão pessoal global em `~/.config/mise/config.toml` (sendo sobrescrito por configurações de projetos específicos);
3. **`mise install`**: instala todas as ferramentas já declaradas nos arquivos de configuração ativos sem modificar o `mise.toml`;
4. **`mise exec -- <comando>`** (ou `mise exec node@24 -- node --version`): executa um comando avulso com as ferramentas e variáveis do projeto (ou com a ferramenta especificada) sem exigir ativação do shell;
5. **`mise run <tarefa>`**: executa uma tarefa nomeada definida no `mise.toml` com todas as ferramentas e variáveis do projeto carregadas.

## Exemplo
```bash
# Definir um padrão global pessoal, sobrescrever no diretório do projeto e verificar a resolução ativa
mise use --global node@22
mkdir meu-servico && cd meu-servico
mise use node@24
mise config ls
mise ls --current
```

## Limites e trade-offs
Se você rodar `mise exec node@24 -- node --version` fora de um projeto, o `mise` baixa o Node 24 se necessário e executa aquele único comando, mas **não** adiciona o Node 24 ao `mise.toml` nem altera o `PATH` da sua sessão de shell atual.

## Como verificar
Execute `mise ls --current` dentro e fora do diretório `meu-servico` para observar como a configuração de projeto (`node@24`) sobrescreve o padrão global (`node@22`).

## Conexões
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Veja também: Estrutura declarativa do mise.toml: seções [tools], [env] e [tasks] versionadas no Git.
- [[mise-ativacao-shell-activate-vs-shims-matriz-shells]] — Veja também: Ativação de shell no mise (mise activate vs Shims) e matriz de compatibilidade entre Bash, Zsh, Fish, Nushell, Elvish, Xonsh e PowerShell.
- [[mise-gerenciador-ferramentas-variaveis-ambiente-tarefas]] — Referência cruzada direta com mise-gerenciador-ferramentas-variaveis-ambiente-tarefas.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://mise.jdx.dev/getting-started.html) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
