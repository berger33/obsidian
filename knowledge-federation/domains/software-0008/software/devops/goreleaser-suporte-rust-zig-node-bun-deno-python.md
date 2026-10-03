---
id: software.devops.tranche10.000969
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

# GoReleaser: uso além do Go com builders nativos para Rust (Cargo), Zig, Node.js, Bun, Deno e Python (uv / Poetry)

## Em uma frase
Conforme demonstra o guia oficial `Quick Start` (`goreleaser.com/getting-started/quick-start/`), o GoReleaser v2 deixou de ser exclusivo para Go e possui builders nativos para projetos **Rust (`cargo`)**, **Zig**, **Node.js**, **Bun**, **Deno**, **Python (`uv`)** e **Python (`poetry`)**.

## Por que importa
Muitas organizações poliglotas que já usavam o GoReleaser para empacotar, assinar (Cosign), gerar SBOMs (Syft), criar pacotes `.deb`/`.rpm` (nFPM) e publicar no Homebrew suas ferramentas em Go queriam exatamente o mesmo pipeline declarativo para seus novos projetos escritos em **Rust**, **Zig**, **TypeScript (Bun/Deno/Node)** ou **Python (`uv`/`poetry`)**.

## Como funciona
No `.goreleaser.yaml`, cada item de `builds:` declara `builder: <linguagem>` (ou `goreleaser init` detecta a linguagem inicializada no diretório): (1) **Rust (`builder: rust`)**: compila usando `cargo` para targets como `TARGET="aarch64-unknown-linux-gnu" goreleaser build --single-target --clean`; (2) **Zig (`builder: zig`)**: usa o poderoso cross-compiler nativo do Zig para targets como `TARGET="aarch64-linux"`; (3) **Bun (`builder: bun`) e Deno (`builder: deno`)**: compilam projetos TypeScript/JavaScript em executáveis standalone (`TARGET="bun-linux-arm64"`, `TARGET="aarch64-unknown-linux-gnu"`); e (4) **Python (`uv` e `poetry`)**: constroem distribuições wheel/sdist (`TARGET="none-any"`). Todos os passos posteriores do GoReleaser (archives, nFPM, SBOM, Cosign, GitHub Release, Homebrew) funcionam de maneira idêntica!

## Exemplo
```bash
# Compilar um único alvo em um projeto Rust, Zig ou Bun usando o GoReleaser conforme documentado no Quick Start
TARGET="aarch64-unknown-linux-gnu" goreleaser build --single-target --clean
TARGET="aarch64-linux" goreleaser build --single-target --clean
TARGET="bun-linux-arm64" goreleaser build --single-target --clean
```

## Limites e trade-offs
Enquanto o compilador Go e o compilador Zig realizam cross-compilation nativa para múltiplos sistemas operacionais sem dependências extras, compilar projetos **Rust** para múltiplos targets Linux/macOS/Windows na seção `builds:` do GoReleaser exige que os targets do `rustup` e os linkers de cross-compilation (ou `cargo-zigbuild` / `cross`) estejam instalados no ambiente de build.

## Como verificar
Em um diretório de teste inicializado com `cargo init --bin` ou `zig init`, execute `goreleaser init` e `goreleaser release --snapshot --clean` para verificar a geração dos artefatos em `./dist`.

## Conexões
- [[goreleaser-changelog-automatico-conventional-commits-filtros]] — Veja também: GoReleaser: geração automática de Changelog categorizado com Conventional Commits, grupos e filtros.
- [[goreleaser-templates-globais-variaveis-artefatos-dist-metadata]] — Veja também: GoReleaser: motor de Name Templates ({{.Version}}, {{.Os}}, {{.Arch}}) e metadados em dist/artifacts.json.
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[goreleaser-modos-execucao-snapshot-single-target-skip-publish]] — Referência cruzada direta com goreleaser-modos-execucao-snapshot-single-target-skip-publish.
- [[goreleaser-configuracao-builds-matriz-ldflags-env-hooks]] — Referência cruzada direta com goreleaser-configuracao-builds-matriz-ldflags-env-hooks.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
