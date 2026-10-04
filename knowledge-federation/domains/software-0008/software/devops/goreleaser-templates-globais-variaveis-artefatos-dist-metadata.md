---
id: software.devops.tranche10.000970
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

# GoReleaser: motor de Name Templates ({{.Version}}, {{.Os}}, {{.Arch}}) e metadados em dist/artifacts.json

## Em uma frase
O GoReleaser utiliza um sistema unificado de **Name Templates** (`{{ .ProjectName }}`, `{{ .Version }}`, `{{ .Tag }}`, `{{ .Os }}`, `{{ .Arch }}`, `{{ .Env.VAR }}`) em todas as seções do `.goreleaser.yaml` e grava o inventário estruturado da execução em `dist/artifacts.json` e `dist/metadata.json`.

## Por que importa
Em pipelines corporativos, etapas posteriores do CI (como scripts de notificação, registro em portais internos de desenvolvedor como Backstage ou promoção para repositórios internos) precisam ler um JSON estruturado listando exatamente quais binários, pacotes e digests foram produzidos pelo build sem precisar fazer parsing de logs de texto.

## Como funciona
(1) **Name Templates**: qualquer campo de nome de arquivo, tag de imagem Docker, flag de compilação ou cabeçalho de release no `.goreleaser.yaml` aceita expressões Go template com variáveis de contexto do build — incluindo `{{ .Version }}` (versão sem o prefixo `v`, ex.: `0.1.0`), `{{ .Tag }}` (`v0.1.0`), `{{ .ShortCommit }}`, `{{ .Date }}`, `{{ .Os }}`, `{{ .Arch }}` e `{{ .Env.MINHA_VAR }}`; e (2) **Metadados em `./dist`**: ao final de `goreleaser build` ou `goreleaser release`, o GoReleaser grava na pasta `./dist` os arquivos **`dist/metadata.json`** (informações da versão, tag, commit e data) e **`dist/artifacts.json`** (lista JSON completa de todos os binários, archives, pacotes `.deb`/`.rpm`, SBOMs e checksums gerados com seus caminhos e hashes).

## Exemplo
```bash
# Inspecionar programaticamente com jq todos os artefatos construídos pelo GoReleaser no diretório ./dist
goreleaser release --snapshot --clean
jq '.[] | {name: .name, type: .type, path: .path}' dist/artifacts.json
```

## Limites e trade-offs
Atenção à diferença entre **`{{ .Tag }}`** e **`{{ .Version }}`** nos templates do `.goreleaser.yaml`: se a sua tag Git for `v1.2.3`, `{{ .Tag }}` avalia para `v1.2.3` (com a letra `v`), enquanto `{{ .Version }}` avalia para `1.2.3` (sem a letra `v`, ideal para nomes de pacotes `.deb`/`.rpm` que exigem que a versão comece com um dígito numérico).

## Como verificar
Após executar `goreleaser build --single-target --clean`, leia `cat dist/metadata.json` e `cat dist/artifacts.json` para verificar os metadados gerados.

## Conexões
- [[goreleaser-suporte-rust-zig-node-bun-deno-python]] — Veja também: GoReleaser: uso além do Go com builders nativos para Rust (Cargo), Zig, Node.js, Bun, Deno e Python (uv / Poetry).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.
- [[goreleaser-modos-execucao-snapshot-single-target-skip-publish]] — Referência cruzada direta com goreleaser-modos-execucao-snapshot-single-target-skip-publish.
- [[taskfile-templating-sprig-funcoes-instalacao-cicd]] — Referência cruzada direta com taskfile-templating-sprig-funcoes-instalacao-cicd.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
