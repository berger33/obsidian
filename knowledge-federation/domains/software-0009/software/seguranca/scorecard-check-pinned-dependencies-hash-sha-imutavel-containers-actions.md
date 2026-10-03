---
id: software.seguranca.tranche01.000095
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md", "https://raw.githubusercontent.com/ossf/scorecard/main/README.md", "https://github.com/ossf/scorecard"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF Scorecard `Pinned-Dependencies`: fixação de GitHub Actions, imagens Docker e downloads por hash criptográfico SHA

## Em uma frase
O check **`Pinned-Dependencies`** (`Risk: Medium`) avalia se todas as dependências externas consumidas nos workflows de CI e `Dockerfiles` — incluindo **GitHub Actions** (`uses:`), **imagens base de container** (`FROM`), pacotes e downloads remotos — estão fixadas por **hash criptográfico imutável (commit SHA de 40 caracteres ou digest SHA-256)** em vez de tags mutáveis.

## Por que importa
Se um workflow usa `uses: terceiros/action@v2` ou `FROM alpine:3.19`, e um atacante compromete o repositório daquela Action de terceiros e move a tag Git `v2` para um commit malicioso (como ocorreu no ataque real à `tj-actions/changed-files`), seu CI executará o código do invasor na próxima execução!

## Como funciona
Quando você fixa a Action pelo hash SHA completo do commit (`uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2`) e a imagem Docker pelo digest (`FROM alpine:3.19@sha256:...`), nem mesmo o comprometimento futuro do repositório upstream pode alterar o código executado pela sua pipeline.

## Exemplo
```dockerfile
# Dockerfile em conformidade com o check Pinned-Dependencies do OpenSSF Scorecard:
FROM golang:1.24-alpine@sha256:4d5f8b9e1c2a3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e AS builder
WORKDIR /src
COPY . .
RUN go build -o /out/app ./cmd/app
```

## Limites e trade-offs
Combine a fixação por hash SHA (`Pinned-Dependencies`) com ferramentas de atualização automatizada como **Renovate** ou **Dependabot** (avaliadas pelo check `Dependency-Update-Tool`) para que os hashes sejam atualizados via Pull Requests auditáveis.

## Como verificar
Execute `scorecard --local=. --checks=Pinned-Dependencies --show-details` para listar todas as referências não fixadas por hash no repositório.

## Conexões
- [[scorecard-checks-token-permissions-dangerous-workflows-github-actions]] — Veja também: OpenSSF Scorecard `Token-Permissions` e `Dangerous-Workflows`: prevenção de escalação de privilégio e injeção em GitHub Actions.
- [[scorecard-checks-signed-releases-packaging-slsa-provenance-cosign]] — Veja também: OpenSSF Scorecard `Signed-Releases` e `Packaging`: assinatura de artefatos, atestados de proveniência SLSA e pacotes oficiais.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
