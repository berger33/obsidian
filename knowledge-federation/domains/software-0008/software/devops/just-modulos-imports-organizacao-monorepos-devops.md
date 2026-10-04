---
id: software.devops.tranche12.001197
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

# just: Organização de Monorepos e Plataformas com import e Módulos (mod)

## Em uma frase
Para repositórios grandes e monorepos de infraestrutura, o `just` oferece duas primitivas de composição: `import 'caminho.just'` (que mescla receitas e variáveis no mesmo namespace) e `mod <nome>` (que cria submódulos isolados invocáveis via `just <modulo> <receita>` ou `just <modulo>::<receita>`).

## Por que importa
Concentrar centenas de receitas de Terraform, Kubernetes, observabilidade, banco de dados e CI dentro de um único `justfile` monolítico na raiz do repositório torna o arquivo difícil de manter e gera colisões de nomes de variáveis.

## Como funciona
Com `mod k8s 'scripts/k8s.just'` e `mod tf 'scripts/terraform.just'` no `justfile` raiz (e `import? 'local.just'` opcional para overrides locais), cada domínio mantém seu próprio arquivo e diretório de trabalho, enquanto o operador descobre e executa tudo a partir de `just --list` e `just k8s deploy`.

## Exemplo
```just
# No justfile da raiz do monorepo:
import? 'local.just'
mod k8s 'ops/k8s.just'
mod tf 'ops/terraform.just'

# Listando submodulos e receitas:
# just --list
# just k8s apply
```

## Limites e trade-offs
Usar `import` (sem o modificador opcional `?`) apontando para um arquivo de customização local ignorado pelo Git (`local.just`) quebra a execução do `just` para qualquer desenvolvedor que acabou de clonar o repositório.

## Como verificar
Use sempre `import? 'local.just'` (com ponto de interrogação) para arquivos opcionais não versionados e prefira `mod` para isolar escopos de variáveis entre equipes.

## Conexões
- [[just-dependencias-receitas-pre-post-argumentos-encadeamento]] — Veja também: just: Grafo de Dependências de Receitas (Pré-Dependências, Pós-Dependências e Passagem de Argumentos).
- [[just-atributos-confirm-private-no-cd-os-specific-safety]] — Veja também: just: Atributos de Receita ([confirm], [private], [no-cd], [linux], [macos]) para Segurança Operacional.

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
