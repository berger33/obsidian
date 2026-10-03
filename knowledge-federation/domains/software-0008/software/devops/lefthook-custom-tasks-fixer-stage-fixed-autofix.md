---
id: software.devops.tranche13.001276
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
fontes: ["https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md", "https://lefthook.dev/usage/", "https://lefthook.dev/configuration/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Grupos de Tarefas Customizadas (lefthook run <grupo>) e Auto-Correção com stage_fixed

## Em uma frase
O Lefthook permite definir grupos de tarefas arbitrários no `lefthook.yml` (além dos nomes de hooks padrão do Git, como um grupo `fixer:` ou `security-audit:`) invocáveis sob demanda via `lefthook run <grupo>`, e suporta `stage_fixed: true` em hooks `pre-commit` para readicionar automaticamente ao `git stage` arquivos formatados por auto-fixers.

## Por que importa
Quando um formatador como `gofmt -w`, `prettier --write` ou `terraform fmt` corrige um arquivo durante o `pre-commit`, sem `stage_fixed: true` a correção fica apenas na working tree e o commit prossegue com o código antigo não formatado.

## Como funciona
Ao configurar `stage_fixed: true` em um job de `pre-commit` que modifica `{staged_files}`, o Lefthook executa o formatador e roda `git add` automaticamente sobre os mesmos `{staged_files}` antes de concluir o hook.

## Exemplo
```yaml
pre-commit:
  jobs:
    - name: terraform-fmt
      glob: "*.tf"
      run: terraform fmt {staged_files}
      stage_fixed: true

fixer:
  jobs:
    - run: golangci-lint run --fix ./...
```

## Limites e trade-offs
Habilitar `stage_fixed: true` em um comando que formata todos os arquivos do diretório (`terraform fmt .`) em vez de apenas `{staged_files}` pode incluir no commit alterações em arquivos que não estavam no stage.

## Como verificar
Combine sempre `stage_fixed: true` com comandos que operam estritamente sobre `{staged_files}`.

## Conexões
- [[lefthook-scripts-commit-msg-runners-docker-containerizados]] — Veja também: Lefthook: Execução de Scripts Dedicados (script e runner) e Hooks em Ambientes Docker.
- [[lefthook-bypass-emergencia-lefthook-0-output-control]] — Veja também: Lefthook: Controle de Verbose (output) e Bypass Consciente em Emergências (LEFTHOOK=0).

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/usage/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/configuration/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
