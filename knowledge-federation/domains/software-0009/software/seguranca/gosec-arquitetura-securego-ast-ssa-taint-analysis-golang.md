---
id: software.seguranca.tranche03.000271
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

# Securego `gosec`: arquitetura em três motores (`AST`, `SSA` e `Taint Analysis`) para análise estática de segurança em Go

## Em uma frase
Conforme documentado no README e em `RULES.md` do repositório oficial (`securego/gosec`, licenciado sob Apache 2.0), o **gosec (Go Security Checker)** inspeciona o código-fonte Go combinando três motores complementares de análise: **1. Regras baseadas em padrões `AST`** (`go/ast` + `go/types`), **2. Analisadores baseados em `SSA` (*Static Single Assignment*)** e **3. Análise de Fluxo de Dados Contaminados (`Taint Analysis`, regras `G701`–`G710`)**!

## Por que importa
Um linter puramente sintático consegue ver se você importou `crypto/md5`, mas não consegue rastrear se um parâmetro lido de `r.URL.Query().Get("id")` passou por três variáveis intermediárias até chegar a um `db.Query(q)` ou se uma função `cancel()` retornada por `context.WithTimeout` deixou de ser chamada em algum caminho de execução.

## Como funciona
No `gosec`, as regras são organizadas em sete categorias oficiais: **`G1xx`** (codificação segura geral, HTTP, cookies, secrets, context), **`G2xx`** (padrões de injeção), **`G3xx`** (filesystem, permissões e Zip Slip), **`G4xx`** (criptografia e TLS), **`G5xx`** (blocklist de imports), **`G6xx`** (segurança de memória/slices em Go) e **`G7xx`** (*Taint Analysis* fim-a-fim)!

## Exemplo
```bash
# Instalando o gosec e escaneando recursivamente todos os pacotes do módulo Go atual:
go install github.com/securego/gosec/v2/cmd/gosec@latest
gosec ./...
```

## Limites e trade-offs
Conforme documentado no README oficial, o `gosec` também exporta o pacote `goanalysis` compatível com a interface padrão `golang.org/x/tools/go/analysis.Analyzer` (usado pelo `golangci-lint` e pelo framework `nogo` do Bazel).

## Como verificar
Execute `gosec -version` e `gosec ./...` verificando o código de saída (`0` sem achados, `1` quando há achados não suprimidos).

## Conexões
- [[gosec-taint-analysis-g701-a-g710-sqli-cmdi-ssrf-xss-path-traversal]] — Veja também: `gosec` Motor de *Taint Analysis* (`G701`–`G710`): rastreamento de fluxo de dados de entradas HTTP até sinks perigosos.

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
