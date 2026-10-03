---
id: software.seguranca.tranche02.000110
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

# Coraza Testes de Regressão de WAF (`go-ftw` e Coraza Playground): validação automatizada de regras SecLang em CI/CD

## Em uma frase
O ecossistema OWASP Coraza / CRS utiliza a ferramenta **[go-ftw](https://github.com/coreruleset/go-ftw)** (*Framework for Testing WAFs*, escrita em Go) e o **[Coraza Playground](https://playground.coraza.io)** para executar suítes de testes automatizados em YAML que enviam requisições HTTP exatas e validam quais IDs de regra foram (ou não foram) acionados.

## Por que importa
Alterar uma expressão regular ou adicionar uma regra de exceção `SecRuleRemoveTargetById` sem testes automatizados de regressão pode desativar acidentalmente a proteção contra SQL Injection em uma rota crítica.

## Como funciona
Em um arquivo YAML de teste do `go-ftw`, cada `test` define o `input` (método, URI, headers, data) e o `output` esperado (`status: 403` ou `expect_error`, `triggered_rules: [942100]`, `non_triggered_rules: [920350]`), rodando no pipeline de CI contra o container de homologação.

## Exemplo
```yaml
meta:
  author: "sec-team"
  description: "Valida bloqueio de SQLi e liberação de payload legítimo do checkout"
tests:
  - test_title: "942100-1"
    stages:
      - input:
          dest_addr: "localhost"
          port: 8080
          uri: "/api/v1/items?id=1'%20OR%20'1'='1"
          headers:
            Host: "localhost"
            User-Agent: "go-ftw-test"
        output:
          status: 403
```

## Limites e trade-offs
Mantenha no repositório casos de teste `go-ftw` tanto para ataques conhecidos (garantindo bloqueio `403`) quanto para payloads complexos reais da sua aplicação (garantindo `status: 200` sem falso positivo).

## Como verificar
Execute `go-ftw run -d ./waf-tests/` no CI após subir o proxy com Coraza.

## Conexões
- [[coraza-extensibilidade-plugins-operators-actions-audit-loggers-go]] — Veja também: Coraza SDK de Extensibilidade (`plugins`): registro de Operadores (`RegisterOperator`), Ações, Transformações e Audit Loggers customizados em Go.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
