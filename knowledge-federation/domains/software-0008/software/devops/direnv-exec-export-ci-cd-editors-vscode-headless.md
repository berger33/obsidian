---
id: software.devops.tranche12.001140
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
fontes: ["https://raw.githubusercontent.com/direnv/direnv/master/README.md", "https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md", "https://github.com/direnv/direnv"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# direnv: Execução Não Interativa com direnv exec e direnv export em IDEs e CI/CD

## Em uma frase
Em ambientes onde não há prompt interativo (como tasks de IDEs, scripts de automação ou steps de GitHub Actions), os subcomandos `direnv exec <dir> <comando>` e `direnv export <shell|json>` carregam o `.envrc` autorizado e executam processos com o ambiente completo.

## Por que importa
Como o hook padrão do `direnv` é acionado apenas antes da renderização do prompt interativo (`PROMPT_COMMAND` / `precmd`), scripts executados em background, runners de CI ou extensões de editor que invocam binários diretamente não recebem as variáveis do `.envrc` automaticamente.

## Como funciona
O comando `direnv allow . && direnv exec . <comando>` avalia o `.envrc` do diretório indicado, aplica o diff de variáveis de ambiente ao processo filho e executa o comando imediatamente. Já `direnv export json` emite um objeto JSON com as variáveis calculadas, sendo consumido por extensões de VS Code, Neovim, Emacs e pelo hook do Nushell.

## Exemplo
```bash
direnv allow .
direnv exec . env | grep -E '^(AWS_PROFILE|KUBECONFIG)='
direnv export json
```

## Limites e trade-offs
Invocar `direnv exec . <comando>` em um runner de CI sem antes executar `direnv allow .` falha imediatamente com `error .envrc is not allowed` porque a autorização não é persistida no repositório Git.

## Como verificar
Em pipelines de CI ou containers efêmeros, execute `direnv allow .` após o checkout do código revisado antes de chamar `direnv exec . <comando>`.

## Conexões
- [[direnv-toml-configuracao-global-load-dotenv-strict-env]] — Veja também: direnv: Configuração Global no direnv.toml (load_dotenv, strict_env e warn_timeout).

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
