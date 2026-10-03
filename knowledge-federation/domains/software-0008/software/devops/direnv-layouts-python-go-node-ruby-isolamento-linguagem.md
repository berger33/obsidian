---
id: software.devops.tranche12.001135
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

# direnv: Funções de Layout (layout python, layout node, layout go) para Isolamento por Projeto

## Em uma frase
A `stdlib` do `direnv` inclui funções `layout <linguagem>` (como `layout python`, `layout python3`, `layout node`, `layout go` e `layout ruby`) que criam e ativam automaticamente ambientes virtuais e diretórios de dependências isolados dentro de `.direnv/` do projeto.

## Por que importa
Ativar e desativar `source .venv/bin/activate` manualmente a cada troca de repositório Python ou esquecer de adicionar `./node_modules/.bin` ao `PATH` causa instalação de pacotes Python no sistema global ou uso da versão errada de binários JS.

## Como funciona
Ao colocar `layout python3` no `.envrc`, o `direnv` cria automaticamente um virtualenv dentro de `.direnv/python-<versao>` (se ainda não existir), exporta `VIRTUAL_ENV` e adiciona `.direnv/python-<versao>/bin` ao topo do `PATH`. Ao sair do diretório com `cd ..`, o virtualenv é desativado instantaneamente.

## Exemplo
```bash
# Conteudo do .envrc para um projeto Python + Node:
layout python3
layout node

# No terminal apos direnv allow:
which python
which pip
echo "$VIRTUAL_ENV"
```

## Limites e trade-offs
Commitar o diretório `.direnv/` no Git inclui binários locais e caminhos absolutos do virtualenv específicos da máquina do desenvolvedor.

## Como verificar
Adicione `.direnv/` ao `.gitignore` global ou do repositório e confirme com `which python` e `echo $VIRTUAL_ENV` que o ambiente virtual isolado está ativo apenas dentro da pasta do projeto.

## Conexões
- [[direnv-stdlib-path-add-source-up-dotenv-watch-file]] — Veja também: direnv: Biblioteca Padrão (stdlib) com PATH_add, dotenv, source_up e watch_file.
- [[direnv-use-nix-use-flake-integracao-devbox-mise]] — Veja também: direnv: Funções use nix, use flake e Integração com Devbox e mise.

## Fontes
- [direnv GitHub — README.md (Sub-Shell Environment Diff, .envrc Authorization, stdlib & Related Projects)](https://raw.githubusercontent.com/direnv/direnv/master/README.md) — README oficial do direnv/direnv (MIT) explicando a execução do .envrc em sub-processo bash, captura do environment diff, bloqueio de segurança direnv allow, stdlib (PATH_add, dotenv, layout, use) e direnvrc; consultado em 2026-10-03.
- [direnv Official Documentation — Shell Hooks Setup (Bash, Zsh, Fish, Tcsh, Elvish, Nushell, PowerShell & Murex)](https://raw.githubusercontent.com/direnv/direnv/master/docs/hook.md) — Documentação oficial de configuração de hooks do direnv para todos os shells suportados e modos de avaliação; consultado em 2026-10-03.
- [direnv — Official GitHub Repository](https://github.com/direnv/direnv) — Repositório oficial do direnv; consultado em 2026-10-03.
