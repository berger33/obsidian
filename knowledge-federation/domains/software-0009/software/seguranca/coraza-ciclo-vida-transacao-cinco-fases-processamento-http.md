---
id: software.seguranca.tranche02.000102
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

# Coraza Ciclo de Vida de Transação (`tx`): as 5 fases de avaliação (`Request Headers`, `Request Body`, `Response Headers`, `Response Body`, `Logging`)

## Em uma frase
Toda requisição inspecionada pelo Coraza percorre cinco fases determinísticas de avaliação dentro de uma `Transaction` (`waf.NewTransaction()`): **Fase 1 (`ProcessRequestHeaders`)**, **Fase 2 (`ProcessRequestBody`)**, **Fase 3 (`ProcessResponseHeaders`)**, **Fase 4 (`ProcessResponseBody`)** e **Fase 5 (`ProcessLogging`)**, encerrando obrigatoriamente com `tx.Close()`.

## Por que importa
Se um middleware HTTP integrar o Coraza chamando apenas `ProcessRequestHeaders()` e esquecer de chamar `ProcessRequestBody()` ou `defer tx.Close()`, ataques enviados em payloads JSON/POST passarão sem inspeção e buffers temporários vazarão memória.

## Como funciona
Em cada fase de 1 a 4, o método correspondente retorna um ponteiro `*types.Interruption` (`it != nil`) caso uma regra disruptiva (`deny`, `drop`, `redirect`) tenha sido acionada; o servidor web deve interromper o processamento imediatamente e responder com `it.Status` (ex.: HTTP `403`).

## Exemplo
```go
// Sequência obrigatória de chamadas em um middleware HTTP usando Coraza v3:
tx := waf.NewTransaction()
defer func() {
	tx.ProcessLogging()
	_ = tx.Close()
}()
tx.ProcessURI(req.URL.String(), req.Method, req.Proto)
for k, vals := range req.Header {
	for _, v := range vals {
		tx.AddRequestHeader(k, v)
	}
}
if it := tx.ProcessRequestHeaders(); it != nil {
	w.WriteHeader(it.Status)
	return
}
```

## Limites e trade-offs
Chame sempre `tx.IsRuleEngineOff()` antes de copiar streams grandes se o WAF puder estar desabilitado para rotas específicas.

## Como verificar
Verifique que `tx.Close()` não retorna erro e que todas as 5 fases são invocadas em testes unitários do middleware.

## Conexões
- [[coraza-arquitetura-owasp-waf-go-seclang-compatibilidade-crs-v4]] — Veja também: OWASP Coraza WAF: arquitetura do Web Application Firewall em Go compatível com `SecLang` e OWASP CRS v4.
- [[coraza-diretivas-seclang-secruleengine-request-response-body-access]] — Veja também: Coraza Diretivas Essenciais `SecLang`: `SecRuleEngine`, `SecRequestBodyAccess`, `SecResponseBodyAccess` e limites de memória.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
