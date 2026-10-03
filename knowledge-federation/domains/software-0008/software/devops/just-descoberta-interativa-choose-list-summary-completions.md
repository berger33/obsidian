---
id: software.devops.tranche12.001199
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

# just: Descoberta Interativa de Tarefas (--list, --summary, --choose com fzf e Shell Completions)

## Em uma frase
Para melhorar a descoberta de automações por novos membros da equipe, o `just` oferece listagem documentada (`just --list`, `just --summary`), seletor interativo (`just --choose`, integrado ao `fzf`) e scripts nativos de autocompletar (`just --completions <shell>`).

## Por que importa
Em projetos com dezenas de scripts espalhados em pastas `hack/` ou `scripts/`, engenheiros não sabem quais ferramentas já existem e acabam reescrevendo comandos que a equipe de plataforma já havia padronizado.

## Como funciona
Qualquer comentário `#` colocado imediatamente acima de uma receita no `justfile` torna-se automaticamente a documentação exibida ao lado do nome da receita em `just --list`. Além disso, `just --choose` abre um menu fuzzy interativo para selecionar e rodar receitas, e `just --completions zsh` habilita `TAB` completo para nomes de receitas e argumentos.

## Exemplo
```bash
just --list --unsorted
just --summary
just --show test
just --completions bash | head -n 20
```

## Limites e trade-offs
Escrever comentários internos de implementação colados na linha imediatamente acima da assinatura da receita sem usar `[doc("...")]` faz com que notas internas apareçam como descrição pública no `just --list`.

## Como verificar
Use comentários diretos acima da receita para descrições claras ao usuário (ou o atributo `[doc("...")]`) e valide a aparência do catálogo com `just --list`.

## Conexões
- [[just-atributos-confirm-private-no-cd-os-specific-safety]] — Veja também: just: Atributos de Receita ([confirm], [private], [no-cd], [linux], [macos]) para Segurança Operacional.
- [[just-integracao-mise-devbox-direnv-padronizacao-local-ci]] — Veja também: just: Padronização de Workflows entre Laptop e CI Combinando just com mise, Devbox e direnv.

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://raw.githubusercontent.com/casey/just/master/README.md) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://just.systems/man/en/) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
