---
id: software.devops.tranche12.001198
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

# just: Atributos de Receita ([confirm], [private], [no-cd], [linux], [macos]) para Segurança Operacional

## Em uma frase
O `just` suporta atributos declarativos entre colchetes acima de cada receita — como `[confirm]` (que exige confirmação interativa antes de rodar), `[private]` (que oculta receitas auxiliares de `just --list`), `[no-cd]` (que mantém o diretório atual em vez de mudar para a raiz do `justfile`), `[doc(...)]` e `[linux]`/`[macos]`/`[windows]`.

## Por que importa
Receitas destrutivas como `terraform destroy`, `k8s-delete-namespace` ou reset de banco de dados podem ser disparadas acidentalmente no histórico do terminal se não exigirem uma barreira explícita de confirmação.

## Como funciona
Ao anotar uma receita com `[confirm("Tem certeza que deseja destruir o ambiente? (y/N)")]`, o `just` bloqueia a execução até que o operador confirme explicitamente (ou passe `--yes` em automação consciente). Atributos de sistema (`[macos]`, `[linux]`) permitem definir implementações diferentes para o mesmo nome de receita conforme o SO.

## Exemplo
```just
[private]
check-auth:
  kubectl auth can-i '*' '*'

[confirm("Confirma o rollout restart em producao?")]
restart-prod deployment: check-auth
  kubectl -n production rollout restart deployment/{{deployment}}
```

## Limites e trade-offs
Acionar uma receita anotada com `[confirm]` dentro de um pipeline de CI/CD não-interativo sem passar a flag `--yes` (`just --yes <receita>`) faz o job falhar ao aguardar entrada do `stdin`.

## Como verificar
Proteja todas as receitas destrutivas ou de produção com `[confirm("...")]` para operadores humanos e passe `--yes` apenas em jobs de pipeline que já passaram por aprovação de ambiente.

## Conexões
- [[just-modulos-imports-organizacao-monorepos-devops]] — Veja também: just: Organização de Monorepos e Plataformas com import e Módulos (mod).
- [[just-descoberta-interativa-choose-list-summary-completions]] — Veja também: just: Descoberta Interativa de Tarefas (--list, --summary, --choose com fzf e Shell Completions).

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
