---
id: software.seguranca.tranche03.000272
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
fontes: ["https://raw.githubusercontent.com/securego/gosec/master/RULES.md", "https://raw.githubusercontent.com/securego/gosec/master/README.md", "https://github.com/securego/gosec"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `gosec` Motor de *Taint Analysis* (`G701`–`G710`): rastreamento de fluxo de dados de entradas HTTP até sinks perigosos

## Em uma frase
Conforme listado na seção *G7xx: Taint Analysis* do arquivo oficial `RULES.md`, o motor de **Taint Analysis** do `gosec` (`taint.NewGosecAnalyzer`) rastreia o fluxo de dados desde fontes não confiáveis controladas pelo usuário (*Sources*, como `http.Request`, argumentos CLI e variáveis de ambiente) até funções críticas (*Sinks*) através de dez regras dedicadas: **`G701`** (SQL Injection), **`G702`** (Command Injection), **`G703`** (Path Traversal), **`G704`** (SSRF), **`G705`** (XSS), **`G706`** (Log Injection), **`G707`** (SMTP Injection), **`G708`** (SSTI em `text/template`), **`G709`** (Unsafe Deserialization) e **`G710`** (Open Redirect)!

## Por que importa
Nas regras antigas `G201`/`G202` (baseadas apenas em AST), o scanner olhava apenas se a chamada `db.Query` continha um `fmt.Sprintf` ou `+` naquela mesma expressão; se a string contaminada fosse montada em uma função auxiliar e passada por variável, apenas a análise de fluxo **SSA/Taint (`G701`–`G710`)** acompanha a propagação!

## Como funciona
Isso permite identificar vulnerabilidades reais de **SSRF (`G704`)**, **Log Injection (`G706`)** e **Path Traversal (`G703`)** mesmo quando o dado percorre múltiplas atribuições antes de atingir o sink.

## Exemplo
```go
package api

import (
	"database/sql"
	"net/http"
)

func GetUserSafe(db *sql.DB, r *http.Request) (*sql.Row, error) {
	userID := r.URL.Query().Get("id")
	// SEGURO contra G201/G202/G701: utiliza placeholder parametrizado ($1) em vez de concatenar userID:
	return db.QueryRowContext(r.Context(), "SELECT id, email FROM users WHERE id = $1", userID), nil
}
```

## Limites e trade-offs
Para mitigar **`G703` (Path Traversal)** ao ler arquivos baseados em entrada do usuário, use `filepath.Clean` combinado com verificação de prefixo ou a API **`os.Root` (`os.OpenInRoot`)** introduzida no Go moderno para confinar acessos a um diretório base.

## Como verificar
Execute `gosec -include=G701,G702,G703,G704,G705,G706,G707,G708,G709,G710 ./...` para rodar especificamente a suíte de Taint Analysis.

## Conexões
- [[gosec-arquitetura-securego-ast-ssa-taint-analysis-golang]] — Veja também: Securego `gosec`: arquitetura em três motores (`AST`, `SSA` e `Taint Analysis`) para análise estática de segurança em Go.
- [[gosec-analisadores-ssa-g113-http-smuggling-g115-integer-overflow-g118-context]] — Veja também: `gosec` Analisadores `SSA`: detecção de *HTTP Smuggling* (`G113`), *Integer Overflow* (`G115`), *Context Leak* (`G118`) e *TOCTOU* (`G122`).

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
