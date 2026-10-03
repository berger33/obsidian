---
id: software.devops.tranche10.000966
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

# GoReleaser: publicação de imagens de container multi-arquitetura (dockers, docker_manifests e integração ko)

## Em uma frase
O GoReleaser pode empacotar os binários pré-compilados em imagens de container OCI usando `docker` / `buildx` (`dockers:` e `docker_manifests:`) ou construir e publicar imagens Go multiplataforma sem daemon Docker usando a integração nativa **`kos:`**.

## Por que importa
Em um`Dockerfile` tradicional multi-arquitetura (`linux/amd64` e `linux/arm64`), rodar `go build` dentro do `docker buildx` usa emulação QEMU lenta para a arquitetura estrangeira; no GoReleaser, os binários já foram compilados nativamente em segundos no estágio `builds` do host e são apenas copiados (`COPY`) para dentro da imagem de cada arquitetura (ou publicados diretamente via `kos:`).

## Como funciona
O `.goreleaser.yaml` oferece dois caminhos para publicar containers: (1) **`dockers:` + `docker_manifests:`** (ou `dockers_v2`): o GoReleaser copia o binário já compilado para o contexto temporário de cada plataforma (`linux/amd64`, `linux/arm64`), constrói e publica as imagens específicas da arquitetura e cria a lista de manifestos multi-arch (`docker_manifests`) sob a tag principal (ex.: `ghcr.io/org/app:v1.0.0` e `:latest`); ou (2) **`kos:`**: integra a biblioteca do projeto **`ko`** diretamente dentro do GoReleaser para construir e publicar imagens multi-arquitetura (`platforms: [linux/amd64, linux/arm64]`) sobre imagens base Chainguard/distroless sem precisar de `Dockerfile` nem de daemon Docker!

## Exemplo
```yaml
# Exemplo de publicação de imagem multi-arquitetura sem Dockerfile usando a seção nativa kos: no .goreleaser.yaml
kos:
  - id: app-ko
    build: cli
    repositories:
      - ghcr.io/minha-org/minha-cli
    platforms:
      - linux/amd64
      - linux/arm64
    tags:
      - "{{.Version}}"
      - latest
    bare: true
```

## Limites e trade-offs
Quando você utiliza `dockers:` com um `Dockerfile` externo no GoReleaser, o `Dockerfile` **não** deve conter uma etapa `RUN go build ...` — ele deve conter apenas **`COPY minha-cli /usr/bin/minha-cli`** (pois o GoReleaser já coloca o binário pré-compilado da arquitetura correta na raiz do contexto de build do Docker).

## Como verificar
Teste a construção local com `goreleaser release --snapshot --clean` e verifique as imagens geradas ou a validação da seção `kos:` / `dockers:` com `goreleaser check`.

## Conexões
- [[goreleaser-seguranca-checksums-sbom-syft-assinatura-cosign]] — Veja também: GoReleaser: segurança de cadeia de suprimentos com checksums SHA-256, geração de SBOM (Syft) e assinatura (Cosign / GPG).
- [[goreleaser-integracao-github-actions-permissoes-token-ci]] — Veja também: GoReleaser: publicação em CI/CD (GITHUB_TOKEN, escopos write:packages e contents:write e goreleaser-action).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
