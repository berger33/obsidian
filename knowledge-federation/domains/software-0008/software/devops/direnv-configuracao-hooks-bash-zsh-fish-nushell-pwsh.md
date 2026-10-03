---
id: software.devops.tranche12.001133
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md", "https://raw.githubusercontent.com/direnv/direnv/master/README.md", "https://github.com/direnv/direnv"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# direnv: Configuração de Hooks em Bash, Zsh, Fish, Nushell e PowerShell

## Em uma frase
Para interceptar mudanças de diretório com latência imperceptível, o `direnv` se integra ao mecanismo nativo de hook de prompt de cada shell (`eval "$(direnv hook bash)"`, `eval "$(direnv hook zsh)"`, `direnv hook fish | source` ou hooks JSON no Nushell).

## Por que importa
Se o hook do `direnv` for posicionado antes de extensões que reescrevem `PROMPT_COMMAND` ou `precmd` (como `rvm`, `git-prompt` ou temas customizados), o gatilho de atualização de ambiente pode ser sobrescrito e parar de funcionar.

## Como funciona
No Bash (`~/.bashrc`) e no Zsh (`~/.zshrc`), a linha `eval "$(direnv hook <shell>)"` deve ser adicionada ao final do arquivo de inicialização. No Fish (`~/.config/fish/config.fish`), usa-se `direnv hook fish | source` com suporte à variável `direnv_fish_mode` (`eval_on_arrow`, `eval_after_arrow` ou `disable_arrow`). No Nushell, o hook em `$env.config.hooks.env_change.PWD` consome `direnv export json | from json | default {} | load-env`.

## Exemplo
```bash
# No final do ~/.bashrc:
eval "$(direnv hook bash)"

# No final do ~/.zshrc:
eval "$(direnv hook zsh)"

# Inspecionar o codigo gerado pelo hook:
direnv hook bash
```

## Limites e trade-offs
Esquecer de reiniciar o shell após adicionar o hook ou posicionar `eval "$(direnv hook bash)"` no topo do `~/.bashrc` antes de manipuladores de prompt impede que o `direnv` detecte a navegação entre pastas.

## Como verificar
Execute `direnv hook <seu-shell>` para verificar a saída do hook e teste a ativação entrando em um diretório com `.envrc` permitido.

## Conexões
- [[direnv-seguranca-allow-deny-bloqueio-execucao-envrc]] — Veja também: direnv: Mecanismo de Segurança com direnv allow, direnv deny e Hash de Autorização.
- [[direnv-stdlib-path-add-source-up-dotenv-watch-file]] — Veja também: direnv: Biblioteca Padrão (stdlib) com PATH_add, dotenv, source_up e watch_file.

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
