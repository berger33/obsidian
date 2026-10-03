---
id: software.devops.tranche13.001272
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

# Lefthook: Execução Paralela (parallel: true) e Placeholders de Arquivos ({staged_files}, {push_files}, {all_files})

## Em uma frase
O Lefthook acelera os hooks do Git executando múltiplos `jobs` concorrentemente quando `parallel: true` está habilitado e injetando automaticamente apenas os arquivos relevantes no comando por meio de templates como `{staged_files}`, `{push_files}`, `{all_files}` e `{files}`.

## Por que importa
Executar `golangci-lint`, `shellcheck`, `kubeconform` e `tflint` sequencialmente sobre todos os milhares de arquivos de um repositório a cada `git commit` demora dezenas de segundos e leva desenvolvedores a desativarem os hooks.

## Como funciona
Definindo `parallel: true` em `pre-commit` ou `pre-push`, o Lefthook dispara todos os jobs em goroutines paralelas e substitui `{staged_files}` apenas pelos arquivos preparados no índice do Git (filtrados por `glob` e `exclude`), pulando automaticamente qualquer job cuja lista de arquivos filtrados seja vazia.

## Exemplo
```yaml
pre-commit:
  parallel: true
  jobs:
    - name: shellcheck-scripts
      glob: "*.sh"
      run: shellcheck {staged_files}
    - name: kubeconform-manifests
      glob: "k8s/**/*.yaml"
      run: kubeconform -strict {staged_files}
```

## Limites e trade-offs
Usar `{all_files}` em vez de `{staged_files}` em hooks `pre-commit` para linters lentos faz com que cada pequeno commit reescaneie todo o repositório desnecessariamente.

## Como verificar
Utilize `{staged_files}` em `pre-commit` para feedback sub-segundo e reserve varreduras mais amplas (`{push_files}` ou `{all_files}`) para o hook `pre-push` e para o pipeline de CI.

## Conexões
- [[lefthook-gerenciador-git-hooks-poliglota-go-lefthook-yml]] — Veja também: Lefthook: Gerenciador Poliglota e Paralelo de Git Hooks em Go (lefthook.yml).
- [[lefthook-filtros-glob-exclude-root-monorepos]] — Veja também: Lefthook: Filtros de Arquivos (glob, exclude, files) e Escopo de Subdiretório (root) em Monorepos.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
