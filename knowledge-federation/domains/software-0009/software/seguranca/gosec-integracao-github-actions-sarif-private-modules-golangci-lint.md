---
id: software.seguranca.tranche03.000280
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/securego/gosec/master/README.md", "https://raw.githubusercontent.com/securego/gosec/master/RULES.md", "https://github.com/securego/gosec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `gosec` em Pipelines CI/CD: GitHub Actions com `SARIF`, módulos privados (`GOPRIVATE`) e integração com `golangci-lint` / Bazel `nogo`

## Em uma frase
Conforme detalhado na seção *Installation / GitHub Action* do README oficial (`securego/gosec`), o `gosec` integra-se nativamente ao **GitHub Code Scanning** exportando arquivos **SARIF (`-fmt sarif -out results.sarif`)**, suporta repositórios com módulos Go privados via variáveis **`GOPRIVATE`** e **`GITHUB_AUTHENTICATION_TOKEN`**, e pode rodar embutido no **`golangci-lint`** ou no **`nogo` do Bazel**.

## Por que importa
Se o seu serviço Go importa pacotes internos privados da sua organização (`github.com/sua-org/pkg-interno`) e o runner do `gosec` não tiver `GOPRIVATE` e `GITHUB_AUTHENTICATION_TOKEN` configurados, o `go/packages` falhará ao baixar os tipos das dependências e a análise SSA/Taint ficará incompleta!

## Como funciona
Ao usar o workflow com upload SARIF para o GitHub Code Scanning, o README oficial recomenda passar **`-no-fail -fmt sarif -out results.sarif ./...`** na etapa do `gosec` para que o step seguinte (`github/codeql-action/upload-sarif`) sempre receba e publique o relatório SARIF antes de o GitHub aplicar o bloqueio da PR.

## Exemplo
```yaml
# Exemplo baseado no README oficial do securego/gosec para projetos com módulos Go privados e upload SARIF:
jobs:
  security-scan:
    runs-on: ubuntu-latest
    env:
      GO111MODULE: on
      GOPRIVATE: github.com/minha-org/*
      GITHUB_AUTHENTICATION_TOKEN: ${{ secrets.PRIVATE_REPO_TOKEN }}
    steps:
      - name: Checkout Source
        uses: actions/checkout@v4
      - name: Run Gosec Security Scanner
        uses: securego/gosec@master
        with:
          args: '-no-fail -fmt sarif -out results.sarif ./...'
      - name: Upload SARIF file
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif
```

## Limites e trade-offs
Quando habilitar o linter `gosec` dentro do `.golangci.yml`, lembre-se de atualizar regularmente a versão do `golangci-lint` para receber as novas regras de *Taint Analysis* (`G701`–`G710`) e *SSA* (`G113`–`G124`).

## Como verificar
Execute `gosec -fmt sarif -out results.sarif ./...` localmente e valide o schema SARIF gerado com `jq '.runs[0].tool.driver.name' results.sarif`.

## Conexões
- [[gosec-filtragem-severity-confidence-include-exclude-tests-build-tags]] — Veja também: `gosec` Seleção de Escopo na CLI: `-severity`, `-confidence`, `-include`/`-exclude`, `-tests` e `-tags` de compilação.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
