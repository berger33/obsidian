---
id: software.devops.tranche13.001273
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
fontes: ["https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md", "https://lefthook.dev/configuration/", "https://lefthook.dev/usage/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Filtros de Arquivos (glob, exclude, files) e Escopo de Subdiretório (root) em Monorepos

## Em uma frase
Cada job no `lefthook.yml` pode restringir seu escopo usando padrões `glob`, listas de exclusão `exclude`, comando customizado de descoberta `files` (como `git diff --name-only HEAD @{push}`) e o diretório de trabalho relativo `root` (essencial para monorepos).

## Por que importa
Em um monorepo que contém um serviço Go em `services/api/`, um frontend React em `web/` e módulos Terraform em `infra/`, cada ferramenta exige ser executada dentro de sua respectiva subpasta (onde residem o `go.mod` ou `package.json`).

## Como funciona
Ao configurar `root: "services/api/"` (com barra final conforme recomendado pela documentação), o Lefthook muda o diretório de trabalho para `services/api/` antes de executar o comando `run` e ajusta automaticamente os caminhos em `{staged_files}` para serem relativos àquela subpasta.

## Exemplo
```yaml
pre-commit:
  parallel: true
  jobs:
    - name: go-vet-api
      root: "services/api/"
      glob: "*.go"
      exclude:
        - "*_mock.go"
      run: go vet {staged_files}
```

## Limites e trade-offs
Omitir a barra final em `root: "api/"` ou passar caminhos que duplicam o prefixo do subdiretório no padrão `glob` faz com que o filtro não encontre nenhum arquivo e pule o job silenciosamente.

## Como verificar
Use sempre a barra final em `root: "subpasta/"` e teste quais arquivos estão sendo selecionados com `lefthook run pre-commit -v`.

## Conexões
- [[lefthook-execucao-paralela-jobs-staged-files-push-files]] — Veja também: Lefthook: Execução Paralela (parallel: true) e Placeholders de Arquivos ({staged_files}, {push_files}, {all_files}).
- [[lefthook-local-yml-overrides-pessoais-skip-tags-docker]] — Veja também: Lefthook: Customização Pessoal sem Poluir o Git com lefthook-local.yml, tags e exclude_tags.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
