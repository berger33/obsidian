---
id: software.devops.tranche13.001271
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

# Lefthook: Gerenciador Poliglota e Paralelo de Git Hooks em Go (lefthook.yml)

## Em uma frase
O **Lefthook** (`evilmartians/lefthook`, criado pela Evil Martians) é um gerenciador rápido de Git hooks escrito em Go, distribuído como um único binário sem dependências de runtime, que orquestra verificações de `pre-commit`, `pre-push` e `commit-msg` em paralelo para projetos de qualquer linguagem.

## Por que importa
Ferramentas de Git hooks acopladas a um único ecossistema (como Husky em Node.js, Overcommit em Ruby ou ambientes Python pesados) obrigam equipes de plataforma/infraestrutura (que usam Go, Rust, Terraform e YAML) a instalar runtimes desnecessários apenas para rodar linters antes do commit.

## Como funciona
O Lefthook lê a configuração do projeto (`lefthook.yml`, `lefthook.toml` ou `lefthook.json`), instala os hooks nativos em `.git/hooks/` com `lefthook install` e permite validar e inspecionar a configuração consolidada com `lefthook validate` e `lefthook dump`.

## Exemplo
```bash
lefthook install
lefthook validate
lefthook dump
lefthook run pre-commit
```

## Limites e trade-offs
Manter múltiplos arquivos de configuração (por exemplo, `lefthook.yml` e `lefthook.toml`) no mesmo repositório causa comportamento não-determinístico, pois a documentação oficial alerta que apenas um arquivo será lido sem ordem garantida.

## Como verificar
Padronize um único formato de arquivo (preferencialmente `lefthook.yml` na raiz do repositório) e valide-o no CI com `lefthook validate`.

## Conexões
- [[lefthook-execucao-paralela-jobs-staged-files-push-files]] — Veja também: Lefthook: Execução Paralela (parallel: true) e Placeholders de Arquivos ({staged_files}, {push_files}, {all_files}).

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
