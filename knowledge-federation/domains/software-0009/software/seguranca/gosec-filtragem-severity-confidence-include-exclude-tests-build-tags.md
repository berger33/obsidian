---
id: software.seguranca.tranche03.000279
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

# `gosec` Seleção de Escopo na CLI: `-severity`, `-confidence`, `-include`/`-exclude`, `-tests` e `-tags` de compilação

## Em uma frase
Para controlar o escopo e a precisão da varredura, a CLI do `gosec` disponibiliza as flags **`-severity`** (`low`, `medium`, `high`), **`-confidence`** (`low`, `medium`, `high`), **`-include=G101,G701`**, **`-exclude=G104`**, **`-exclude-dir`**, **`-tests`** (inclui arquivos `*_test.go` que são ignorados por padrão) e **`-tags`** (passa *build tags* do Go para analisar arquivos condicionais, ex.: `-tags=linux,integration`)!

## Por que importa
Como o `gosec` compila a árvore de tipos e o SSA usando as tags de build ativas, se você tiver código específico de plataforma ou de produção atrás de `//go:build linux && cgo` ou `//go:build prod` e não passar `-tags`, esses arquivos não serão analisados!

## Como funciona
Por padrão, o `gosec` **não analisa arquivos `*_test.go`** para evitar falsos positivos com credenciais fictícias de teste; porém, você pode rodar um segundo passo no CI com `-tests -include=G101` se quiser garantir que ninguém colou uma chave real da AWS dentro de um teste de integração.

## Exemplo
```bash
# Executando o gosec filtrando por severidade e confiança >= medium, excluindo código gerado e passando build tags:
gosec \
  -severity medium \
  -confidence medium \
  -exclude-generated \
  -exclude-dir=vendor \
  -tags=linux \
  ./...
```

## Limites e trade-offs
Use a flag **`-stdout -verbose=text`** junto com `-out=results.json -fmt=json` quando quiser imprimir o resumo legível no log do CI e simultaneamente salvar o arquivo JSON para ingestão automatizada.

## Como verificar
Teste a diferença de cobertura com e sem `-tests` em um módulo Go com testes unitários.

## Conexões
- [[gosec-supressao-anotacoes-nosec-justificativa-tracking-suppressions]] — Veja também: `gosec` Supressões Auditáveis (`// #nosec Gxxx -- justificativa`) e Rastreamento com `-track-suppressions`.
- [[gosec-integracao-github-actions-sarif-private-modules-golangci-lint]] — Veja também: `gosec` em Pipelines CI/CD: GitHub Actions com `SARIF`, módulos privados (`GOPRIVATE`) e integração com `golangci-lint` / Bazel `nogo`.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
