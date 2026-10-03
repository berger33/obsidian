---
id: software.devops.tranche13.001277
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://lefthook.dev/usage/", "https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md", "https://lefthook.dev/configuration/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Controle de Verbose (output) e Bypass Consciente em Emergências (LEFTHOOK=0)

## Em uma frase
O Lefthook permite enxugar o ruído visual no terminal configurando a lista `output` no `lefthook.yml` e pode ser desativado pontualmente em um comando Git específico definindo a variável de ambiente `LEFTHOOK=0` (por exemplo, `LEFTHOOK=0 git commit`).

## Por que importa
Durante commits intermediários de trabalho em progresso (`WIP`) em uma branch pessoal ou durante um hotfix crítico onde um linter externo está indisponível, o engenheiro precisa saber como pular a execução local conscientemente sem desinstalar os hooks.

## Como funciona
Definindo `output: [failure, summary]` no `lefthook.yml`, o Lefthook oculta logs extensos de ferramentas que passaram com sucesso e imprime detalhes apenas quando um job falha. Para pular o Lefthook em uma operação específica, precede-se o comando Git com `LEFTHOOK=0`.

## Exemplo
```bash
# Pular a execucao do Lefthook em um commit pontual:
LEFTHOOK=0 git commit -m "wip: checkpoint antes de rebase"

# Executar manualmente todos os hooks pre-push antes de abrir PR:
lefthook run pre-push
```

## Limites e trade-offs
Exportar `export LEFTHOOK=0` permanentemente no `~/.bashrc` ou `~/.zshrc` desativa silenciosamente todas as proteções locais de `pre-commit` e `pre-push` em todos os repositórios da máquina.

## Como verificar
Use `LEFTHOOK=0` apenas inline para um único comando emergencial e execute `lefthook run pre-commit` no pipeline de CI para garantir que commits feitos com `LEFTHOOK=0` ainda sejam validados no Pull Request.

## Conexões
- [[lefthook-custom-tasks-fixer-stage-fixed-autofix]] — Veja também: Lefthook: Grupos de Tarefas Customizadas (lefthook run <grupo>) e Auto-Correção com stage_fixed.
- [[lefthook-extends-remotes-compartilhamento-politicas-organizacao]] — Veja também: Lefthook: Compartilhamento de Políticas entre Repositórios com extends e remotes.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://lefthook.dev/usage/) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/configuration/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
