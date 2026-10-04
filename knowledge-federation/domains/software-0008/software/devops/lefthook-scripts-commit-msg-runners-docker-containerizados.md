---
id: software.devops.tranche13.001275
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

# Lefthook: Execução de Scripts Dedicados (script e runner) e Hooks em Ambientes Docker

## Em uma frase
Além de comandos inline (`run`), o Lefthook permite executar scripts armazenados em `.lefthook/<hook-name>/` usando a chave `script` combinada com um `runner` customizado (como `bash`, `python3` ou `docker run -it --rm <container> {cmd}`).

## Por que importa
Regras complexas de validação de mensagens de commit (`commit-msg` para Conventional Commits ou vínculo obrigatório de ticket Jira) ou verificações que rodam dentro de containers de desenvolvimento ficam ilegíveis se escritas em uma única linha de shell no YAML.

## Como funciona
Colocando o arquivo executável ou script em `.lefthook/commit-msg/template_checker` e declarando `script: "template_checker"` com `runner: bash` (ou um `runner` Docker que substitui `{cmd}`), o Lefthook repassa os argumentos nativos do Git (como `$1` apontando para `.git/COMMIT_EDITMSG`) ao script.

## Exemplo
```yaml
commit-msg:
  jobs:
    - script: "check_conventional_commit.sh"
      runner: bash
```

## Limites e trade-offs
Usar `docker run -it` (com flag `-t` de TTY obrigatório) em um `runner` do Lefthook quando o commit é feito por uma interface gráfica de IDE ou em CI sem terminal interativo falha com erro `the input device is not a TTY`.

## Como verificar
Remova a flag `-t` (use `docker run --rm -i`) nos runners Docker do `lefthook.yml` para garantir compatibilidade tanto no terminal quanto em IDEs (VS Code, JetBrains) e pipelines de CI.

## Conexões
- [[lefthook-local-yml-overrides-pessoais-skip-tags-docker]] — Veja também: Lefthook: Customização Pessoal sem Poluir o Git com lefthook-local.yml, tags e exclude_tags.
- [[lefthook-custom-tasks-fixer-stage-fixed-autofix]] — Veja também: Lefthook: Grupos de Tarefas Customizadas (lefthook run <grupo>) e Auto-Correção com stage_fixed.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
