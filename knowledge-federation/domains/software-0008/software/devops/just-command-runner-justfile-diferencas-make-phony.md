---
id: software.devops.tranche12.001191
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
fontes: ["https://raw.githubusercontent.com/casey/just/master/README.md", "https://just.systems/man/en/", "https://github.com/casey/just"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# just: Command Runner Declarativo (justfile) e Eliminação de Idiossincrasias do Make

## Em uma frase
O `just` (`casey/just`) é um executor de comandos de projeto multiplataforma escrito em Rust que armazena receitas (`recipes`) em um arquivo chamado `justfile`, com sintaxe inspirada no `make`, mas projetado especificamente como command runner em vez de sistema de build baseado em timestamps de arquivos.

## Por que importa
Usar `Makefile` apenas para salvar comandos de projeto (`test`, `lint`, `deploy`, `docker-build`) exige declarar `.PHONY` em todas as tarefas para evitar colisões com arquivos de mesmo nome (como uma pasta `test/` ou `build/`), além de sofrer com erros crípticos quando um editor converte espaços em vez de tabs.

## Como funciona
No `justfile`, toda receita é tratada nativamente como comando a executar (sem necessidade de `.PHONY`), aceita indentação tanto por espaços quanto por tabs (desde que consistente por receita), resolve dependências circulares e receitas inexistentes estaticamente antes de executar qualquer linha e pode ser invocado de qualquer subdiretório do repositório.

## Exemplo
```just
# Exemplo de justfile para automacao DevOps:
set dotenv-load := true

default:
  @just --list

lint:
  golangci-lint run ./...

test: lint
  go test -race ./...
```

## Limites e trade-offs
Misturar espaços e tabulações na indentação dentro do corpo de uma mesma receita no `justfile` gera erro de análise sintática imediato antes da execução.

## Como verificar
Padronize a formatação do `justfile` com `just --fmt --unstable` (ou verifique a sintaxe no CI) e liste as receitas disponíveis com `just --list`.

## Conexões
- [[just-parametros-receitas-valores-padrao-variadic-flags]] — Veja também: just: Parâmetros de Receitas, Valores Padrão, Argumentos Variádicos e Flags no justfile.

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://raw.githubusercontent.com/casey/just/master/README.md) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://just.systems/man/en/) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
