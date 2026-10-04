---
id: software.seguranca.tranche02.000109
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

# Coraza SDK de Extensibilidade (`plugins`): registro de Operadores (`RegisterOperator`), Ações, Transformações e Audit Loggers customizados em Go

## Em uma frase
Como destaca o README oficial, o Coraza é extensível em seu núcleo por meio do pacote `github.com/corazawaf/coraza/v3/experimental/plugins`, permitindo registrar em Go **Operadores customizados (`plugins.RegisterOperator`)**, **Transformações (`RegisterTransformation`)**, **Body Processors (`RegisterBodyProcessor`)**, **Ações (`RegisterAction`)** e **Audit Loggers (`RegisterAuditLogger`)**.

## Por que importa
Regras puramente baseadas em regex não conseguem consultar um cache local de reputação de IP em memória, validar um token HMAC proprietário ou enviar logs de auditoria diretamente para um stream Kafka/OpenTelemetry.

## Como funciona
Registrando um operador Go customizado (por exemplo `@ipReputationCheck`) via `plugins.RegisterOperator`, suas regras SecLang passam a invocá-lo nativamente (`SecRule REMOTE_ADDR "@ipReputationCheck" "id:501,phase:1,deny"`), combinando a simplicidade declarativa de SecLang com a velocidade de código Go compilado.

## Exemplo
```go
// Exemplo conceitual de uso de WafConfig com filesystem virtual e logger de erros estruturado:
cfg := coraza.NewWAFConfig().
	WithRootFS(customRulesFS).
	WithErrorCallback(func(rule types.MatchedRule) {
		log.Printf("Coraza match rule=%d uri=%s", rule.Rule().ID(), rule.URI())
	})
```

## Limites e trade-offs
Use `WithErrorCallback` na configuração do `WAFConfig` para capturar em tempo real cada regra acionada e exportar contadores Prometheus por `rule_id` e severidade.

## Como verificar
Escreva um teste em Go instanciando `coraza.NewWAF(cfg)` e validando a invocação de `WithErrorCallback`.

## Conexões
- [[coraza-body-processors-json-xml-urlencoded-multipart-inspecao]] — Veja também: Coraza Body Processors (`JSON`, `XML`, `URLENCODED`, `MULTIPART`): parsing estruturado de payloads de APIs modernas na Fase 1 e Fase 2.
- [[coraza-testes-regressao-regras-ftw-go-ftw-playground-ci-cd]] — Veja também: Coraza Testes de Regressão de WAF (`go-ftw` e Coraza Playground): validação automatizada de regras SecLang em CI/CD.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
