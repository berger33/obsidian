---
id: software.devops.tranche10.000967
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

# GoReleaser: publicação em CI/CD (GITHUB_TOKEN, escopos write:packages e contents:write e goreleaser-action)

## Em uma frase
Conforme detalha o guia oficial `Quick Start` (`goreleaser.com/getting-started/quick-start/`), publicar releases no GitHub exige exportar `GITHUB_TOKEN` com permissão **`contents: write`** (ou escopo `repo` em tokens clássicos) e adicionar **`write:packages`** (`packages: write`) quando o pipeline também faz push de imagens Docker para o GitHub Container Registry (`ghcr.io`).

## Por que importa
A falha mais comum ao configurar o GoReleaser pela primeira vez no GitHub Actions é o pipeline compilar todos os binários com sucesso e falhar no último passo com erro `403 Resource not accessible by integration` porque o `GITHUB_TOKEN` padrão do workflow estava com permissão somente-leitura (`contents: read`).

## Como funciona
No GitHub Actions (usando `goreleaser/goreleaser-action`), quando um push de tag `v*` dispara o workflow: (1) o passo `actions/checkout` deve buscar o histórico completo de tags e commits com **`fetch-depth: 0`** para que o GoReleaser possa calcular o changelog entre a tag anterior e a tag atual; (2) o bloco `permissions:` do job deve conceder `contents: write` (para criar a GitHub Release e fazer upload dos `.tar.gz`/`.deb`), `packages: write` (se publicar imagens no `ghcr.io`) e `id-token: write` (se assinar com Cosign keyless); e (3) a variável `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}` é passada ao comando `goreleaser release --clean`.

## Exemplo
```yaml
# Trecho essencial de permissões e checkout (fetch-depth: 0) para rodar o GoReleaser no GitHub Actions
permissions:
  contents: write
  packages: write
  id-token: write

steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  - uses: goreleaser/goreleaser-action@v6
    with:
      version: "~> v2"
      args: release --clean
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Limites e trade-offs
Se você esquecer de configurar `fetch-depth: 0` no `actions/checkout` (que por padrão faz um *shallow clone* buscando apenas 1 commit), o GoReleaser não conseguirá encontrar a tag anterior no histórico Git local e gerará um changelog contendo todos os commits desde o início do repositório ou falhará ao validar o estado da tag.

## Como verificar
Confirme no seu arquivo `.github/workflows/release.yml` a presença de `fetch-depth: 0` no checkout e de `contents: write` no bloco `permissions`.

## Conexões
- [[goreleaser-imagens-containers-dockers-buildx-ko-manifests]] — Veja também: GoReleaser: publicação de imagens de container multi-arquitetura (dockers, docker_manifests e integração ko).
- [[goreleaser-changelog-automatico-conventional-commits-filtros]] — Veja também: GoReleaser: geração automática de Changelog categorizado com Conventional Commits, grupos e filtros.
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[goreleaser-modos-execucao-snapshot-single-target-skip-publish]] — Referência cruzada direta com goreleaser-modos-execucao-snapshot-single-target-skip-publish.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
