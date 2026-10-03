---
id: software.devops.tranche10.000968
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

# GoReleaser: geração automática de Changelog categorizado com Conventional Commits, grupos e filtros

## Em uma frase
Durante o `goreleaser release`, a seção **`changelog:`** do `.goreleaser.yaml` analisa os commits Git entre a tag anterior e a tag atual, filtrando commits irrelevantes (`docs:`, `test:`, `chore:`) e agrupando as notas de lançamento em categorias baseadas em **Conventional Commits** (`feat:`, `fix:`, `perf:`).

## Por que importa
Escrever notas de versão manualmente a cada release é demorado e sujeito a esquecimentos, enquanto despejar a saída bruta de `git log` na página de Releases mistura refatorações internas e ajustes de CI com novas funcionalidades importantes para o usuário.

## Como funciona
Na seção **`changelog:`** do `.goreleaser.yaml`, o engenheiro configura: (1) **`sort: asc`** (ou `desc`); (2) **`use: github`** (ou `git`, `gitlab`, `github-native`), onde `github` enriquece cada linha com o `@username` do autor no GitHub; (3) **`filters.exclude`**: lista de expressões regulares de mensagens de commit que não devem aparecer nas notas de release (ex.: `^docs:`, `^test:`, `^chore:`, `Merge pull request`); e (4) **`groups:`**: lista de grupos com `title` (ex.: `Features`, `Bug Fixes`, `Security`) e `regexp` (ex.: `^.*?feat(\(\w+\))??!?:.+$`) que organizam as mudanças em seções Markdown limpas no corpo da GitHub/GitLab Release.

## Exemplo
```yaml
# Exemplo de seção changelog no .goreleaser.yaml agrupando Conventional Commits e excluindo commits de docs/testes
changelog:
  sort: asc
  use: github
  filters:
    exclude:
      - "^docs:"
      - "^test:"
      - "^chore:"
  groups:
    - title: "Novas Funcionalidades"
      regexp: '^.*?feat(\(\w+\))??!?:.+$'
      order: 0
    - title: "Correções de Bugs"
      regexp: '^.*?fix(\(\w+\))??!?:.+$'
      order: 1
```

## Limites e trade-offs
Se a sua equipe já utiliza as notas geradas pelo próprio GitHub (`Release Drafter` ou `.github/release.yml` nativo do GitHub), você pode configurar `changelog: { use: github-native }` ou `disable: true` no `.goreleaser.yaml` para delegar a formatação das notas de release à API nativa do GitHub.

## Como verificar
Execute `goreleaser release --skip=publish --clean` em um repositório com tags e inspecione o arquivo `./dist/CHANGELOG.md` gerado para pré-visualizar exatamente como as notas da release ficarão formatadas.

## Conexões
- [[goreleaser-integracao-github-actions-permissoes-token-ci]] — Veja também: GoReleaser: publicação em CI/CD (GITHUB_TOKEN, escopos write:packages e contents:write e goreleaser-action).
- [[goreleaser-suporte-rust-zig-node-bun-deno-python]] — Veja também: GoReleaser: uso além do Go com builders nativos para Rust (Cargo), Zig, Node.js, Bun, Deno e Python (uv / Poetry).
- [[goreleaser-automacao-release-engineering-multilinguagem]] — Referência cruzada direta com goreleaser-automacao-release-engineering-multilinguagem.

## Fontes
- [GoReleaser Official Documentation — Quick Start (goreleaser init, check, healthcheck, build --single-target, release --snapshot & GITHUB_TOKEN)](https://raw.githubusercontent.com/goreleaser/goreleaser/main/README.md) — Guia oficial Quick Start do GoReleaser (v2.18+) demonstrando inicialização, builders para Go/Rust/Node.js/Zig/Bun/Deno/uv/Poetry, --snapshot, --single-target, check, healthcheck, --skip=publish e permissões GITHUB_TOKEN; consultado em 2026-10-03.
- [GoReleaser GitHub — README.md (Release Engineering Automation & Multi-Language Support)](https://goreleaser.com/getting-started/quick-start/) — README oficial do projeto goreleaser/goreleaser (MIT); consultado em 2026-10-03.
- [GoReleaser — Official GitHub Repository](https://github.com/goreleaser/goreleaser) — Repositório oficial do GoReleaser; consultado em 2026-10-03.
