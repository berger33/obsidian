---
id: software.devops.tranche12.001193
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
fontes: ["https://just.systems/man/en/", "https://raw.githubusercontent.com/casey/just/master/README.md", "https://github.com/casey/just"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# just: Configurações de Comportamento no justfile (set shell, dotenv-load, export e positional-arguments)

## Em uma frase
O comportamento de execução de um `justfile` é controlado por diretivas declarativas `set <opção> := <valor>` no topo do arquivo, permitindo customizar o shell interpretador (`set shell`), carregar arquivos `.env` automaticamente (`set dotenv-load`), exportar todas as variáveis (`set export`) e habilitar `$1`, `$@` (`set positional-arguments`).

## Por que importa
Por padrão, o `just` executa cada linha de uma receita usando `sh -cu`, que não possui `set -o pipefail` do Bash nem carrega variáveis de arquivos `.env` se isso não for declarado nas configurações do `justfile`.

## Como funciona
Definir `set shell := ["bash", "-euo", "pipefail", "-c"]` garante que qualquer falha em pipelines com `|` interrompa imediatamente a receita; `set dotenv-load := true` (ou `set dotenv-filename := ".env.local"`) popula o ambiente das receitas a partir do `.env`; e `set export := true` exporta todas as variáveis definidas no `justfile` para os processos filhos.

## Exemplo
```just
set shell := ["bash", "-euo", "pipefail", "-c"]
set dotenv-load := true
set export := true
set positional-arguments := true

tf-plan env="staging":
  terraform -chdir=envs/$1 init -backend=false
  terraform -chdir=envs/$1 plan
```

## Limites e trade-offs
Manter o `set shell` padrão (`sh -cu`) ao escrever receitas que usam sintaxe exclusiva do Bash (como arrays associativos, condicionais estendidas ou `set -o pipefail`) causa falha em sistemas Debian/Ubuntu onde `/bin/sh` aponta para `dash`.

## Como verificar
Declare explicitamente `set shell := ["bash", "-euo", "pipefail", "-c"]` no topo de todo `justfile` que utilize construções Bash modernas.

## Conexões
- [[just-parametros-receitas-valores-padrao-variadic-flags]] — Veja também: just: Parâmetros de Receitas, Valores Padrão, Argumentos Variádicos e Flags no justfile.
- [[just-shebang-recipes-execucao-bloco-unico-python-bash-node]] — Veja também: just: Receitas Shebang (#!/usr/bin/env) para Execução em Bloco Único e Múltiplas Linguagens.

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
