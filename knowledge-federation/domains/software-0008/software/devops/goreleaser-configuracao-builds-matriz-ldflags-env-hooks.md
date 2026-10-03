---
id: software.devops.tranche10.000963
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

# GoReleaser: customização da seção builds (goos, goarch, env, flags, ldflags e hooks de pré/pós-build)

## Em uma frase
Na seção **`builds:`** do `.goreleaser.yaml`, o engenheiro define a matriz de sistemas operacionais (`goos`), arquiteturas (`goarch`/`targets`), variáveis de ambiente (`CGO_ENABLED=0`), injeção de metadados de versão no binário (`ldflags`) e `hooks` de compilação.

## Por que importa
Um binário CLI distribuído para usuários finais precisa responder corretamente ao comando `--version` informando a versão exata da tag Git, o hash do commit e a data do build, além de ser compilado estaticamente (`CGO_ENABLED=0`) e sem símbolos de debug desnecessários (`-s -w`) para reduzir o tamanho do download.

## Como funciona
Por padrão, o GoReleaser injeta automaticamente no `ldflags` do Go as três variáveis padrão **`-s -w -X main.version={{.Version}} -X main.commit={{.Commit}} -X main.date={{.Date}}`**. No bloco `builds:` do `.goreleaser.yaml`, é possível customizar: (1) `main: ./cmd/minha-cli` e `binary: minha-cli`; (2) `env: [CGO_ENABLED=0]`; (3) `goos: [linux, darwin, windows]` e `goarch: [amd64, arm64]` (podendo excluir combinações específicas com `ignore:`); (4) `flags: [-trimpath]` para builds reprodutíveis; e (5) `hooks.pre` / `hooks.post` (ou `before.hooks` global no topo do arquivo, como `go mod tidy` e `go generate ./...`).

## Exemplo
```yaml
# Exemplo de seção builds no .goreleaser.yaml (v2) compilando binários estáticos reprodutíveis para Linux, macOS e Windows
version: 2
before:
  hooks:
    - go mod tidy
builds:
  - id: cli
    main: ./cmd/cli
    binary: minha-cli
    env:
      - CGO_ENABLED=0
    flags:
      - -trimpath
    goos:
      - linux
      - darwin
      - windows
    goarch:
      - amd64
      - arm64
```

## Limites e trade-offs
Se o seu pacote `main` em Go armazena a variável `Version` dentro de um subpacote interno (por exemplo, `internal/version.Version` em vez de `main.version`), o `ldflags` padrão do GoReleaser não preencherá aquela variável a menos que você declare explicitamente `ldflags: ["-s -w -X github.com/org/repo/internal/version.Version={{.Version}}"]` na seção `builds`.

## Como verificar
Execute `goreleaser build --single-target --clean` e rode o binário gerado dentro de `./dist/cli_*/minha-cli --version` para confirmar que `{{.Version}}` e `{{.Commit}}` foram injetados no executável.

## Conexões
- [[goreleaser-modos-execucao-snapshot-single-target-skip-publish]] — Veja também: GoReleaser: modos de validação e dry-run (check, healthcheck, build --single-target, --snapshot e --skip=publish).
- [[goreleaser-empacotamento-archives-nfpm-deb-rpm-apk-homebrew]] — Veja também: GoReleaser: empacotamento em arquivos (.tar.gz/.zip), pacotes Linux via nFPM (.deb, .rpm, .apk) e gerenciadores (Homebrew/Scoop/Winget).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[ko-configuracao-ko-yaml-imagens-base-flags-ldflags]] — Referência cruzada direta com ko-configuracao-ko-yaml-imagens-base-flags-ldflags.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
