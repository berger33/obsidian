---
id: software.devops.tranche12.001139
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

# direnv: Configuração Global no direnv.toml (load_dotenv, strict_env e warn_timeout)

## Em uma frase
O arquivo de configuração global `~/.config/direnv/direnv.toml` controla comportamentos de segurança, performance e compatibilidade do `direnv`, como carregamento automático de `.env` (`load_dotenv`), modo estrito de execução (`strict_env`) e limite de alerta de lentidão (`warn_timeout`).

## Por que importa
Scripts `.envrc` que ignoram erros silenciosos de comandos intermediários ou demoram vários segundos bloqueando o prompt degradam a experiência de terminal sem deixar claro qual comando travou.

## Como funciona
Em `~/.config/direnv/direnv.toml`, habilitar `strict_env = true` na seção `[global]` faz com que todo `.envrc` seja avaliado com `set -euo pipefail`, interrompendo imediatamente o carregamento se qualquer comando falhar ou referenciar variável não definida. O parâmetro `warn_timeout` (padrão `5s`) emite aviso quando a avaliação do `.envrc` demora demais.

## Exemplo
```toml
# ~/.config/direnv/direnv.toml
[global]
strict_env = true
warn_timeout = "3s"
load_dotenv = false
hide_env_diff = false

[whitelist]
exact = []
```

## Limites e trade-offs
Habilitar `load_dotenv = true` globalmente sem revisar projetos legados pode fazer o `direnv` solicitar autorização ou carregar arquivos `.env` de exemplo que não deveriam sobrescrever o ambiente do shell interativo.

## Como verificar
Prefira usar `dotenv` ou `dotenv_if_exists` explicitamente dentro do `.envrc` de cada projeto e mantenha `strict_env = true` ativo no `direnv.toml` para detectar falhas cedo.

## Conexões
- [[direnv-isolamento-multi-cluster-kubeconfig-aws-profile-terraform]] — Veja também: direnv: Isolamento de Contexto Multi-Cluster e Multi-Cloud (KUBECONFIG, AWS_PROFILE e TF_WORKSPACE).
- [[direnv-exec-export-ci-cd-editors-vscode-headless]] — Veja também: direnv: Execução Não Interativa com direnv exec e direnv export em IDEs e CI/CD.

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
