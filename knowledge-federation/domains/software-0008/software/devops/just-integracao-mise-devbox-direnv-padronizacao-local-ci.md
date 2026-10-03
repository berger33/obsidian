---
id: software.devops.tranche12.001200
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

# just: Padronização de Workflows entre Laptop e CI Combinando just com mise, Devbox e direnv

## Em uma frase
Combinar o `just` como executor universal de receitas (`justfile`) com um gerenciador declarativo de toolchains (`mise.toml` ou `devbox.json`) e ativação automática de diretório (`direnv`) estabelece uma arquitetura onde o desenvolvedor local e o pipeline de CI executam exatamente os mesmos comandos (`just lint`, `just test`, `just build`, `just deploy`).

## Por que importa
Quando o pipeline do GitHub Actions ou GitLab CI contém dezenas de linhas de script shell inline em YAML que não existem localmente, depurar uma falha de CI exige fazer dezenas de commits de tentativa e erro.

## Como funciona
Na arquitetura integrada, o `mise` ou `devbox` instala o próprio binário `just` junto com as versões exatas de Go, Python, Terraform, `kubectl` e `helm`; o `direnv` ativa esse ambiente ao entrar na pasta; e tanto o engenheiro quanto o runner de CI invocam exclusivamente `just check` e `just package`, mantendo a lógica em um único lugar testável localmente.

## Exemplo
```yaml
# No workflow de CI chamando as mesmas receitas do justfile local:
steps:
  - uses: actions/checkout@v4
  - uses: jdx/mise-action@v2
  - name: Executar pipeline padronizado via just
    run: |
      just --list
      just lint
      just test
```

## Limites e trade-offs
Duplicar comandos complexos de build tanto no `justfile` quanto nos passos `run:` do GitHub Actions permite que os dois diverjam silenciosamente ao longo do tempo.

## Como verificar
Faça com que cada etapa do CI invoque diretamente uma receita do `justfile` (`just <receita>`) e teste mudanças de pipeline localmente com `just --dry-run <receita>` antes do push.

## Conexões
- [[just-descoberta-interativa-choose-list-summary-completions]] — Veja também: just: Descoberta Interativa de Tarefas (--list, --summary, --choose com fzf e Shell Completions).

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://raw.githubusercontent.com/casey/just/master/README.md) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://just.systems/man/en/) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
