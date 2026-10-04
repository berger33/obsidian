---
id: software.devops.tranche12.001132
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

# direnv: Mecanismo de Segurança com direnv allow, direnv deny e Hash de Autorização

## Em uma frase
Por executar código Bash arbitrário contido em `.envrc`, o `direnv` bloqueia por padrão qualquer arquivo `.envrc` novo ou modificado até que o usuário o aprove explicitamente com `direnv allow`, registrando o hash criptográfico do conteúdo permitido.

## Por que importa
Sem esse bloqueio baseado em hash, clonar um repositório Git malicioso ou fazer `git pull` de um commit comprometido e simplesmente executar `cd repo` dispararia execução remota de código imediatamente no terminal do engenheiro.

## Como funciona
Sempre que um `.envrc` é criado ou alterado em um único byte, o `direnv` recusa o carregamento e exibe `.envrc is not allowed`. O operador deve inspecionar o conteúdo do arquivo (`cat .envrc`) e rodar `direnv allow .` para autorizar aquele hash específico, ou `direnv deny .` para revogar a autorização a qualquer momento.

## Exemplo
```bash
echo 'export APP_ENV=staging' > .envrc
# O direnv exibe: direnv: error .envrc is not allowed
cat .envrc
direnv allow .
direnv status
direnv deny .
```

## Limites e trade-offs
Configurar `whitelist` ampla (`prefix = ["/home/user/projects"]`) em `direnv.toml` para pular o `direnv allow` em diretórios onde repositórios externos são clonados expõe a estação de trabalho a execução automática de código não revisado.

## Como verificar
Revise sempre o diff de qualquer `.envrc` antes de executar `direnv allow .` e audite o estado de autorização do diretório atual com `direnv status`.

## Conexões
- [[direnv-arquitetura-shell-hook-subshell-bash-diff-ambiente]] — Veja também: direnv: Arquitetura de Hook de Prompt e Captura de Diff de Ambiente via Sub-Shell Bash.
- [[direnv-configuracao-hooks-bash-zsh-fish-nushell-pwsh]] — Veja também: direnv: Configuração de Hooks em Bash, Zsh, Fish, Nushell e PowerShell.

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
