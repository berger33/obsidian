---
id: software.devops.tranche13.001274
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
fontes: ["https://lefthook.dev/configuration/", "https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md", "https://lefthook.dev/usage/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Customização Pessoal sem Poluir o Git com lefthook-local.yml, tags e exclude_tags

## Em uma frase
O Lefthook mescla automaticamente um arquivo complementar chamado `lefthook-local.yml` (ou `.lefthook-local.yml`, seguindo o mesmo prefixo/formato do arquivo principal) sobre a configuração principal, permitindo que cada desenvolvedor pule tags específicas (`exclude_tags`), altere o `runner` para Docker ou adicione hooks próprios sem alterar o `lefthook.yml` versionado.

## Por que importa
Em equipes multidisciplinares, um engenheiro de infraestrutura que nunca edita o frontend ou que roda todas as ferramentas dentro de containers Docker precisa ajustar a execução local sem quebrar o `lefthook.yml` compartilhado pelo restante do time.

## Como funciona
No `lefthook.yml` principal, os jobs recebem `tags: [frontend, linters]` ou `[backend, security]`. Na máquina local, o desenvolvedor cria um `lefthook-local.yml` (ignorado no `.gitignore`) com `exclude_tags: [frontend]` ou `skip: true` em jobs específicos, e verifica o resultado mesclado com `lefthook dump`.

## Exemplo
```yaml
# lefthook-local.yml (ignorado no Git):
pre-push:
  exclude_tags:
    - frontend
  jobs:
    - name: audit-gems
      skip: true
```

## Limites e trade-offs
Esquecer de adicionar `lefthook-local.yml` (e `.lefthook-local.*`) ao `.gitignore` do repositório faz com que overrides pessoais de um desenvolvedor sejam commitados acidentalmente e desativem verificações para toda a equipe.

## Como verificar
Inclua `*lefthook-local*` no `.gitignore` do projeto e use `lefthook dump` para inspecionar como o arquivo local foi mesclado à configuração base.

## Conexões
- [[lefthook-filtros-glob-exclude-root-monorepos]] — Veja também: Lefthook: Filtros de Arquivos (glob, exclude, files) e Escopo de Subdiretório (root) em Monorepos.
- [[lefthook-scripts-commit-msg-runners-docker-containerizados]] — Veja também: Lefthook: Execução de Scripts Dedicados (script e runner) e Hooks em Ambientes Docker.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://lefthook.dev/configuration/) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
