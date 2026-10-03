---
id: software.devops.tranche11.001094
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

# Ativação de shell no mise (mise activate vs Shims) e matriz de compatibilidade entre Bash, Zsh, Fish, Nushell, Elvish, Xonsh e PowerShell

## Em uma frase
Para disponibilizar ferramentas e variáveis de ambiente automaticamente no `PATH`, o `mise` oferece duas abordagens — **`mise activate`** (hook de prompt recomendado para shells interativos) e **Shims** (executáveis intermediários úteis para IDEs e processos que não carregam o rc do shell) — além da opção de operar sem nenhum dos dois via `mise exec` / `mise run`.

## Por que importa
Em shells interativos, o `mise activate` atualiza diretamente a variável `PATH` e as variáveis de `[env]` sempre que o prompt é exibido ou o diretório muda (`chpwd`), evitando o overhead de execução de shims a cada chamada de binário. Já editores gráficos (VS Code, IntelliJ, Neovim GUI) e processos background frequentemente não executam `~/.bashrc` ou `~/.zshrc`, tornando os Shims ou `mise exec` a escolha adequada para essas integrações.

## Como funciona
Conforme a seção *4. Activate mise* e a tabela *Shell Feature Compatibility* (`mise.jdx.dev/getting-started.html`): (1) para ativar no Bash (`~/.bashrc`), adiciona-se `eval "$(~/.local/bin/mise activate bash)"`; no Zsh (`~/.zshrc`), `eval "$(~/.local/bin/mise activate zsh)"`; e no Fish (`~/.config/fish/config.fish`), `~/.local/bin/mise activate fish | source`; (2) o `mise` adiciona automaticamente seu próprio diretório `~/.local/bin` ao `PATH` quando ativado; e (3) na matriz de compatibilidade de recursos entre **Bash, Zsh, Fish, Nushell, Elvish, Xonsh e PowerShell**, todos os 7 shells suportam `mise activate`, `mise shell` e o hook `chpwd` (no PowerShell exigindo PowerShell 7+), enquanto aliases de shell (`[shell_alias]`) são suportados em Bash, Zsh e Fish (e não em Nushell, Elvish, Xonsh ou PowerShell).

## Exemplo
```bash
# Adicionar a ativação do mise no Bash ou Zsh (executar apenas uma vez para evitar hooks duplicados)
echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc

# Diagnosticar se a ativação do shell e o PATH estão configurados corretamente
mise doctor
```

## Limites e trade-offs
Conforme alerta a documentação oficial: (1) adicione a linha `mise activate` **apenas uma vez** ao arquivo rc do seu shell, pois repetir o comando `>>` cria hooks duplicados no prompt; e (2) **Shims não suportam todas as funcionalidades do `mise activate`** (por exemplo, um shim intercepta a chamada de um binário, mas não injeta variáveis de ambiente de `[env]` na sessão do shell pai ao entrar em um diretório).

## Como verificar
Se `mise exec -- node --version` funcionar mas `node --version` falhar diretamente no terminal interativo, reinicie a sessão do shell e execute `mise doctor` para verificar o status de ativação.

## Conexões
- [[mise-comandos-operacionais-use-install-exec-run-global]] — Veja também: Diferença semântica entre os comandos do mise: mise use, mise use --global, mise install, mise exec e mise run.
- [[mise-seguranca-confianca-mise-trust-paranoid-mode]] — Veja também: Segurança de configuração no mise: mise trust e operação em Paranoid Mode.
- [[mise-gerenciador-ferramentas-variaveis-ambiente-tarefas]] — Referência cruzada direta com mise-gerenciador-ferramentas-variaveis-ambiente-tarefas.
- [[mise-diagnostico-doctor-rate-limit-github-token-ci]] — Referência cruzada direta com mise-diagnostico-doctor-rate-limit-github-token-ci.

## Fontes
- [mise GitHub — README.md (Dev Tools, Env Vars & Tasks in mise.toml, Quickstart & Shell Activation)](https://mise.jdx.dev/getting-started.html) — README oficial do jdx/mise (MIT) apresentando gerenciamento unificado de tools, env vars, tasks e bootstrap em mise.toml; consultado em 2026-10-03.
- [mise Official Documentation — Getting Started (mise use/install/exec/run, mise trust, Paranoid Mode, Activate vs Shims, Backends & Shell Compatibility Matrix)](https://raw.githubusercontent.com/jdx/mise/main/README.md) — Guia oficial Getting Started do mise detalhando comandos operacionais, confiança de arquivos (mise trust e paranoid mode), mise activate vs shims, matriz de 7 shells, registry/backends (github:), mise doctor e lockfiles; consultado em 2026-10-03.
- [mise — Official GitHub Repository](https://github.com/jdx/mise) — Repositório oficial do mise (jdx/mise); consultado em 2026-10-03.
