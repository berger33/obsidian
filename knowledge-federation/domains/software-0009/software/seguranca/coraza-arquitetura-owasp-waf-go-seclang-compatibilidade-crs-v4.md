---
id: software.seguranca.tranche02.000101
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/corazawaf/coraza/main/README.md", "https://www.coraza.io/docs/seclang/directives/", "https://github.com/corazawaf/coraza"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Coraza WAF: arquitetura do Web Application Firewall em Go compatível com `SecLang` e OWASP CRS v4

## Em uma frase
O **OWASP Coraza** (`corazawaf/coraza/v3`, projeto de produção da OWASP licenciado sob Apache 2.0) é um motor de *Web Application Firewall (WAF)* de alta performance escrito 100% em Go, projetado como substituto moderno do motor legado ModSecurity com suporte à linguagem **SecLang** e **100% de compatibilidade com o OWASP Core Rule Set (CRS) v4**.

## Por que importa
Motores WAF tradicionais escritos em C/C++ (`libmodsecurity`) exigem bindings Cgo complexos para integrar com proxies cloud-native em Go (como Caddy, Traefik) ou filtros WebAssembly (`Proxy-WASM` no Envoy/Istio).

## Como funciona
Como o Coraza é uma biblioteca nativa em Go sem dependências Cgo obrigatórias, uma instância `coraza.WAF` compila diretivas `SecRule`/`SecAction` na inicialização e cria objetos leves de transação (`waf.NewTransaction()`) por requisição HTTP, avaliando as 5 fases de inspeção com latência mínima.

## Exemplo
```go
package main

import (
	"fmt"
	"github.com/corazawaf/coraza/v3"
)

func main() {
	waf, err := coraza.NewWAF(coraza.NewWAFConfig().
		WithDirectives(`SecRule REMOTE_ADDR "@rx .*" "id:101,phase:1,deny,status:403"`))
	if err != nil {
		panic(err)
	}
	tx := waf.NewTransaction()
	defer func() {
		tx.ProcessLogging()
		tx.Close()
	}()
	tx.ProcessConnection("127.0.0.1", 8080, "127.0.0.1", 12345)
	if it := tx.ProcessRequestHeaders(); it != nil {
		fmt.Printf("Bloqueado na fase 1 com status %d\n", it.Status)
	}
}
```

## Limites e trade-offs
Conforme documentado no README oficial do Coraza, o motor é **100% compatível com o OWASP CRS v4**, mas versões antigas do CRS (como CRS v3 sem adaptações) não são suportadas diretamente.

## Como verificar
Execute `go test ./...` ou valide suas regras SecLang no [Coraza Playground](https://playground.coraza.io).

## Conexões
- [[coraza-ciclo-vida-transacao-cinco-fases-processamento-http]] — Veja também: Coraza Ciclo de Vida de Transação (`tx`): as 5 fases de avaliação (`Request Headers`, `Request Body`, `Response Headers`, `Response Body`, `Logging`).

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
