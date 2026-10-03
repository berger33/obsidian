---
id: software.seguranca.tranche03.000273
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

# `gosec` Analisadores `SSA`: detecção de *HTTP Smuggling* (`G113`), *Integer Overflow* (`G115`), *Context Leak* (`G118`) e *TOCTOU* (`G122`)

## Em uma frase
Conforme documentado em `RULES.md`, os analisadores baseados em representação **SSA (*Static Single Assignment*)** do `gosec` detectam bugs sutis de segurança e confiabilidade que dependem de tipos e caminhos de execução: **`G113`** (*HTTP Request Smuggling*), **`G115`** (conversão numérica com *Integer Overflow*, ex.: `int64` -> `int32`/`uint`), **`G118`** (falha de propagação/cancelamento de `context.Context` causando vazamento de goroutines — CWE-400), **`G119`** (propagação insegura de cabeçalhos em redirecionamento HTTP), **`G122`** (*TOCTOU race* em `filepath.WalkDir`), **`G123`** (bypass de TLS resumption) e **`G602`** (acesso fora dos limites de slice).

## Por que importa
Em Go, esquecer de chamar a função `cancel` retornada por `context.WithTimeout(ctx, 5*time.Second)` (`G118`) mantém timers e goroutines presos em memória até o timeout expirar, permitindo esgotamento de recursos (DoS); já converter um `int` de 64 bits vindo de uma requisição para `int32` ou `uint16` sem validar os limites (`G115`) pode transformar um número negativo em um tamanho de alocação gigantesco!

## Como funciona
O analisador SSA da regra **`G118`** verifica se `cancel` foi chamado via `defer cancel()`, closure diferida, retornado ao chamador ou armazenado em uma struct com método de limpeza.

## Exemplo
```go
package worker

import (
	"context"
	"math"
	"time"
)

func SafeProcess(ctx context.Context, count int64) (int32, error) {
	// 1. Aprovado pelo G118 (SSA): cancel() é garantido via defer
	childCtx, cancel := context.WithTimeout(ctx, 2*time.Second)
	defer cancel()
	_ = childCtx

	// 2. Aprovado pelo G115 (SSA): verifica limites antes de converter int64 para int32
	if count < math.MinInt32 || count > math.MaxInt32 {
		return 0, context.DeadlineExceeded
	}
	return int32(count), nil
}
```

## Limites e trade-offs
Observe também a regra **`G112`** e **`G114`**: nunca suba um servidor HTTP em Go usando `http.ListenAndServe(":8080", handler)` direto na internet pública, pois a struct padrão não define **`ReadHeaderTimeout`**, deixando o servidor vulnerável a ataques **Slowloris**!

## Como verificar
Rode `gosec -include=G112,G114,G115,G118 ./...` para auditar seus servidores HTTP e conversões numéricas.

## Conexões
- [[gosec-taint-analysis-g701-a-g710-sqli-cmdi-ssrf-xss-path-traversal]] — Veja também: `gosec` Motor de *Taint Analysis* (`G701`–`G710`): rastreamento de fluxo de dados de entradas HTTP até sinks perigosos.
- [[gosec-seguranca-http-cookies-serializacao-segredos-g117-g120-g124]] — Veja também: `gosec` Hardening de Serviços Web e Serialização: exposição de segredos em JSON/YAML (`G117`), `ParseMultipartForm` (`G120`) e Cookies (`G124`).

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
