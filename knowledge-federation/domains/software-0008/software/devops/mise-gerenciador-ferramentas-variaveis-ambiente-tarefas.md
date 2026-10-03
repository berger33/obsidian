---
id: software.devops.tranche11.001091
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

# mise (mise-en-place): CLI unificada em Rust para gerenciar ferramentas de desenvolvimento, variáveis de ambiente e tarefas

## Em uma frase
O **mise** (`jdx/mise`, *mise-en-place*, licenciado sob MIT e escrito em Rust) é uma ferramenta de linha de comando que unifica em um único arquivo declarativo (`mise.toml`) o gerenciamento de versões de ferramentas de desenvolvimento (Node.js, Python, Go, Rust, Terraform, kubectl e centenas de outras), variáveis de ambiente por projeto (`.env` e `[env]`) e execução de tarefas (`[tasks]`), além de bootstrap de máquinas.

## Por que importa
Tradicionalmente, equipes de engenharia precisavam combinar três ou quatro utilitários distintos com sintaxes incompatíveis — `asdf` ou `nvm`/`pyenv` para versões de linguagens, `direnv` para variáveis de ambiente por diretório e `make` ou scripts shell para tarefas de build/teste. O `mise` consolida essas três funções com alta performance (sem shims lentos em shell script) e funciona de forma idêntica no terminal do desenvolvedor, na IDE e no pipeline de CI/CD.

## Como funciona
Conforme descrevem o README oficial (`jdx/mise`) e o guia *Getting started* (`mise.jdx.dev/getting-started.html`), o instalador oficial (`curl https://mise.run | sh`, ou pacotes via Homebrew, apt, dnf, Nix e `winget install jdx.mise`) posiciona o binário em `~/.local/bin/mise`. Em cada repositório, o arquivo **`mise.toml`** declara as seções `[tools]`, `[env]` e `[tasks.<nome>]`. Ao executar `mise install`, `mise exec` ou `mise run`, ou ao navegar até o diretório com o shell ativado (`mise activate`), o `mise` resolve e disponibiliza exatamente as versões de ferramentas e variáveis configuradas para aquele projeto.

## Exemplo
```bash
# Instalar o mise no Linux/macOS e executar um comando com Node.js 24 sem alterar o ambiente global
curl https://mise.run | sh
~/.local/bin/mise --version
mise exec node@24 -- node --version
```

## Limites e trade-offs
Conforme destaca a documentação oficial, uma especificação de série como `node = "24"` em `mise.toml` seleciona uma release dentro da série 24 do Node.js, não um pino imutável exato; quando toda a equipe e o CI precisam usar exatamente a mesma versão patch resolvida, utilize pinos exatos (ex.: `24.0.0`) ou o recurso de lockfile (`mise.lock`) do `mise`.

## Como verificar
Execute `mise config ls`, `mise ls --current` e `mise doctor` dentro do diretório do projeto para verificar quais arquivos `mise.toml` estão ativos e se as ferramentas selecionadas estão íntegras.

## Conexões
- [[mise-configuracao-projeto-mise-toml-tools-env-tasks]] — Veja também: Estrutura declarativa do mise.toml: seções [tools], [env] e [tasks] versionadas no Git.
- [[mise-comandos-operacionais-use-install-exec-run-global]] — Referência cruzada direta com mise-comandos-operacionais-use-install-exec-run-global.
- [[mise-ativacao-shell-activate-vs-shims-matriz-shells]] — Referência cruzada direta com mise-ativacao-shell-activate-vs-shims-matriz-shells.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://mise.jdx.dev/getting-started.html) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
