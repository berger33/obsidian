---
id: software.devops.tranche13.001280
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

# Lefthook: Execução de lefthook run no Pipeline de CI/CD para Paridade Total com Hooks Locais

## Em uma frase
Como o comando `lefthook run <hook-name>` pode ser invocado diretamente sem depender de um evento interativo do Git, o mesmo arquivo `lefthook.yml` usado nos laptops dos desenvolvedores pode ser executado dentro do pipeline de CI/CD (`lefthook run pre-commit --all-files`).

## Por que importa
Como hooks locais do Git residem na máquina do cliente e podem ser pulados com `--no-verify` ou `LEFTHOOK=0`, o pipeline de CI precisa validar exatamente as mesmas regras sem duplicar a lista de comandos e filtros `glob` no YAML do GitHub Actions.

## Como funciona
No job de CI, instala-se o binário `lefthook` (ou via `mise`/`devbox`) e executa-se `lefthook validate` seguido de `lefthook run pre-push` ou `lefthook run pre-commit --all-files`, garantindo uma única fonte da verdade para os linters do repositório.

## Exemplo
```bash
lefthook validate
lefthook run pre-commit --all-files --no-tty
```

## Limites e trade-offs
Executar `lefthook run pre-commit` simples (sem `--all-files` ou `--files-from-command`) em um runner de CI onde o índice de staging do Git está vazio (`{staged_files}` vazio) faz o Lefthook pular todos os jobs que dependem de `{staged_files}`.

## Como verificar
Em pipelines de CI, passe `--all-files` (ou configure um job/hook dedicado como `pre-push` que compara o diff do Pull Request) para que todos os arquivos relevantes sejam verificados.

## Conexões
- [[lefthook-seguranca-shift-left-gitleaks-trivy-kubeconform-tflint]] — Veja também: Lefthook: Prevenção Shift-Left de Vazamento de Segredos e Erros IaC no pre-commit DevOps.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://lefthook.dev/usage/) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/configuration/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
