---
id: software.seguranca.tranche02.000103
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
fontes: ["https://www.coraza.io/docs/seclang/directives/", "https://raw.githubusercontent.com/corazawaf/coraza/main/README.md", "https://github.com/corazawaf/coraza"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Coraza Diretivas Essenciais `SecLang`: `SecRuleEngine`, `SecRequestBodyAccess`, `SecResponseBodyAccess` e limites de memória

## Em uma frase
A postura operacional do Coraza é controlada pelas diretivas fundamentais da linguagem SecLang: **`SecRuleEngine`** (`On`, `Off` ou `DetectionOnly`), **`SecRequestBodyAccess`** (`On`/`Off`), **`SecResponseBodyAccess`** (`On`/`Off`), **`SecRequestBodyLimit`**, **`SecRequestBodyInMemoryLimit`** e **`SecRequestBodyLimitAction`** (`Reject` ou `ProcessPartial`).

## Por que importa
Ativar um conjunto novo de regras WAF diretamente com `SecRuleEngine On` em produção sem antes rodar em `DetectionOnly` pode bloquear requisições legítimas de clientes devido a falsos positivos ainda não ajustados.

## Como funciona
Durante o período de *burn-in*, configure `SecRuleEngine DetectionOnly` para que todas as regras das fases 1 a 4 sejam avaliadas e registradas nos logs de auditoria sem interromper o tráfego; após ajustar as exclusões, promova para `SecRuleEngine On` com `SecRequestBodyAccess On`.

## Exemplo
```apache
SecRuleEngine On
SecRequestBodyAccess On
SecRequestBodyLimit 13107200
SecRequestBodyInMemoryLimit 131072
SecRequestBodyLimitAction Reject
SecResponseBodyAccess On
SecResponseBodyMimeType text/plain text/html text/xml application/json
SecArgumentsLimit 1000
```

## Limites e trade-offs
Conforme documentado na referência de diretivas do Coraza, `SecArgumentsLimit` limita por padrão a `1000` o número máximo de parâmetros `ARGS` processados para mitigar ataques de *Hash DoS* / poluição de parâmetros.

## Como verificar
Inspecione uma requisição com mais de 13 MB de body e confirme que `SecRequestBodyLimitAction Reject` retorna HTTP `413` / `403`.

## Conexões
- [[coraza-ciclo-vida-transacao-cinco-fases-processamento-http]] — Veja também: Coraza Ciclo de Vida de Transação (`tx`): as 5 fases de avaliação (`Request Headers`, `Request Body`, `Response Headers`, `Response Body`, `Logging`).
- [[coraza-audit-logging-secauditengine-parts-abcfhz-formatos-json-ocsf]] — Veja também: Coraza Audit Logging (`SecAuditEngine`, `SecAuditLogParts` e `SecAuditLogFormat`): saída estruturada em `JSON`, `OCSF` e `Native`.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://www.coraza.io/docs/seclang/directives/) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
