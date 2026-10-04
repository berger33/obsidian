---
id: software.devops.tranche10.000962
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md", "https://goreleaser.com/getting-started/quick-start/", "https://github.com/goreleaser/goreleaser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# GoReleaser: modos de validação e dry-run (check, healthcheck, build --single-target, --snapshot e --skip=publish)

## Em uma frase
Conforme documenta o guia oficial `Quick Start`, o GoReleaser oferece comandos graduais para testar e depurar o pipeline antes de um release real: `goreleaser check`, `goreleaser healthcheck`, `goreleaser build --single-target`, `goreleaser release --snapshot` e `goreleaser release --skip=publish`.

## Por que importa
Descobrir que o `.goreleaser.yaml` tem um erro de sintaxe, que falta uma ferramenta externa no runner ou que a compilação cruzada para `darwin/arm64` quebrou apenas no momento em que você empurra a tag `v1.0.0` de produção gera tags órfãs e atrasos no lançamento.

## Como funciona
Cada modo de execução listado na seção `Dry run` do `Quick Start` atende a uma etapa do fluxo: (1) **`goreleaser check`**: valida se o arquivo `.goreleaser.yaml` é sintaticamente válido e sem opções depreciadas; (2) **`goreleaser healthcheck`**: verifica se todas as ferramentas de terceiros exigidas pela sua configuração atual (ex.: `git`, `go`, `cargo`, `docker`, `cosign`, `syft`) estão instaladas no `$PATH`; (3) **`goreleaser build --single-target --clean`**: compila apenas o binário para o alvo atual (`GOOS`/`GOARCH` ou `TARGET` no Rust/Zig/Bun/Deno) sem empacotar nem publicar, ideal para desenvolvimento local; (4) **`goreleaser build`**: compila todos os alvos da matriz em Pull Requests de CI para garantir que tudo compila sem erros; e (5) **`goreleaser release --skip=publish`** (ou `--snapshot --clean`): executa todo o empacotamento em `./dist` pulando apenas o upload final.

## Exemplo
```bash
# Verificar dependências externas (healthcheck) e compilar rapidamente apenas o binário para linux/arm64 (--single-target)
goreleaser healthcheck
GOOS="linux" GOARCH="arm64" goreleaser build --single-target --clean
```

## Limites e trade-offs
Sempre passe a flag **`--clean`** ao executar `goreleaser build` ou `goreleaser release` em uma máquina local onde você já rodou o GoReleaser anteriormente: sem `--clean`, o GoReleaser falhará caso a pasta `./dist` ainda contenha artefatos residuais de uma execução anterior.

## Como verificar
Execute `goreleaser check` e `goreleaser healthcheck` no repositório e confirme que ambos retornam código de saída `0` sem erros.

## Conexões
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Veja também: GoReleaser: automação completa de engenharia de releases para Go, Rust, Zig, Node.js, Bun, Deno e Python.
- [[goreleaser-configuracao-builds-matriz-ldflags-env-hooks]] — Veja também: GoReleaser: customização da seção builds (goos, goarch, env, flags, ldflags e hooks de pré/pós-build).
- [[taskfile-dependencias-paralelas-sequenciais-loops-matrizes]] — Referência cruzada direta com taskfile-dependencias-paralelas-sequenciais-loops-matrizes.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
