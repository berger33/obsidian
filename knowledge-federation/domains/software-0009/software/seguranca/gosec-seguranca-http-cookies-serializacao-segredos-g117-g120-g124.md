---
id: software.seguranca.tranche03.000274
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

# `gosec` Hardening de Serviços Web e Serialização: exposição de segredos em JSON/YAML (`G117`), `ParseMultipartForm` (`G120`) e Cookies (`G124`)

## Em uma frase
As regras modernas da série `G1xx` documentadas em `RULES.md` protegem aplicações web Go contra quatro falhas frequentes em APIs: **`G116`** (*Trojan Source* com caracteres Unicode bidirecionais), **`G117`** (exposição acidental de campos sensíveis `Password`/`Secret`/`Token` durante serialização `json.Marshal` / `yaml.Marshal`), **`G120`** (`ParseMultipartForm` sem limite razoável causando exaustão de memória) e **`G124`** (configuração insegura de `http.Cookie` faltando `Secure`, `HttpOnly` ou `SameSite`).

## Por que importa
Em Go, se uma struct `User` tiver um campo exportado `PasswordHash string` ou `APIToken string` e você esquecer de colocar a tag **`json:"-"`** (e `yaml:"-"`), qualquer chamada `json.NewEncoder(w).Encode(user)` enviará o hash da senha ou o token secreto na resposta JSON da API!

## Como funciona
A regra **`G117`** inspeciona structs passadas para funções de marshaling (JSON, YAML, XML, TOML) e alerta sempre que campos cujos nomes casam com `(?i)secret|token|password` não estão explicitamente omitidos ou protegidos!

## Exemplo
```go
package auth

import "net/http"

type Account struct {
	ID           string `json:"id"`
	Email        string `json:"email"`
	PasswordHash string `json:"-" yaml:"-"` // Aprovado pela G117: nunca serializado em JSON/YAML
}

func SetSessionCookie(w http.ResponseWriter, token string) {
	// Aprovado pela G124: define explicitamente Secure, HttpOnly e SameSiteStrictMode
	http.SetCookie(w, &http.Cookie{
		Name:     "__Host-session",
		Value:    token,
		Path:     "/",
		Secure:   true,
		HttpOnly: true,
		SameSite: http.SameSiteStrictMode,
	})
}
```

## Limites e trade-offs
Você pode customizar a expressão regular de nomes de campos sensíveis da regra `G117` no arquivo JSON de configuração do `gosec` (`{"G117": {"pattern": "(?i)secret|token|password|api_key|cpf"}}`).

## Como verificar
Execute `gosec -include=G117,G120,G124 ./...` para auditar serialização de structs e emissão de cookies.

## Conexões
- [[gosec-analisadores-ssa-g113-http-smuggling-g115-integer-overflow-g118-context]] — Veja também: `gosec` Analisadores `SSA`: detecção de *HTTP Smuggling* (`G113`), *Integer Overflow* (`G115`), *Context Leak* (`G118`) e *TOCTOU* (`G122`).
- [[gosec-seguranca-filesystem-permissoes-zip-slip-decompression-bomb-g110-g301-g307]] — Veja também: `gosec` Segurança de Sistema de Arquivos (`G110` *Decompression Bomb*, `G301`–`G307` Permissões Octais e `G305` *Zip Slip*).

## Fontes
- [Securego gosec Official Rules Documentation — RULES.md (Complete Catalog of G1xx-G7xx Rules, AST/SSA/Taint Implementations & Per-Rule JSON Config)](https://raw.githubusercontent.com/securego/gosec/master/RULES.md) — Catálogo oficial RULES.md detalhando todas as regras G1xx a G7xx, distinção entre motores AST, SSA e Taint Analysis e configuração JSON; consultado em 2026-10-03.
- [Securego gosec GitHub — README.md (Go Security Checker, CLI Flags, SARIF Code Scanning, Private Modules GOPRIVATE & Bazel nogo)](https://raw.githubusercontent.com/securego/gosec/master/README.md) — README oficial do securego/gosec documentando instalação, códigos de saída, seleção de regras, supressões e integração em pipelines CI/CD; consultado em 2026-10-03.
- [Securego gosec — Official GitHub Repository](https://github.com/securego/gosec) — Repositório oficial Apache-2.0 do Securego gosec; consultado em 2026-10-03.
