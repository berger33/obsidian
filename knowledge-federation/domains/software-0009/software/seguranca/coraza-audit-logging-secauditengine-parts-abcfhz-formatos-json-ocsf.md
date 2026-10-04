---
id: software.seguranca.tranche02.000104
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

# Coraza Audit Logging (`SecAuditEngine`, `SecAuditLogParts` e `SecAuditLogFormat`): saída estruturada em `JSON`, `OCSF` e `Native`

## Em uma frase
Conforme a documentação oficial de diretivas do Coraza, o subsistema de auditoria é configurado por **`SecAuditEngine`** (`On`, `Off`, **`RelevantOnly`**), **`SecAuditLogRelevantStatus`** (regex de status HTTP, ex.: `^(?:5|4(?!04))`), **`SecAuditLogParts`** (padrão `ABCFHZ`, mais `J` para uploads multipart a partir da v3.7.0 e `K` para regras casadas) e **`SecAuditLogFormat`** (**`JSON`**, **`OCSF`**, `JsonLegacy` ou `Native`).

## Por que importa
Habilitar `SecAuditEngine On` (que grava cabeçalhos e corpos de 100% das requisições HTTP 200 normais em disco) esgota o armazenamento e degrada o throughput de I/O em minutos.

## Como funciona
A configuração recomendada para produção é **`SecAuditEngine RelevantOnly`** combinada com **`SecAuditLogFormat JSON`** ou **`OCSF`** (*Open Cybersecurity Schema Framework*): assim, o Coraza grava logs de auditoria apenas quando uma regra de segurança dispara alerta ou quando o código HTTP casa com `SecAuditLogRelevantStatus`.

## Exemplo
```apache
SecAuditEngine RelevantOnly
SecAuditLogRelevantStatus "^(?:5|40[1235])"
SecAuditLogParts ABCFHJKZ
SecAuditLogType Serial
SecAuditLogFormat OCSF
SecAuditLog /var/log/coraza/audit.log
```

## Limites e trade-offs
Como alerta a documentação oficial de `SecAuditLogParts`, não inclua a parte `C` (Request Body bruto) sem filtro em rotas de login se os campos de senha não forem mascarados antes de enviar os logs ao SIEM.

## Como verificar
Envie uma requisição de teste que acione uma regra e valide o objeto JSON/OCSF gravado em `/var/log/coraza/audit.log`.

## Conexões
- [[coraza-diretivas-seclang-secruleengine-request-response-body-access]] — Veja também: Coraza Diretivas Essenciais `SecLang`: `SecRuleEngine`, `SecRequestBodyAccess`, `SecResponseBodyAccess` e limites de memória.
- [[coraza-integracoes-cloud-native-proxy-wasm-envoy-istio-caddy-traefik]] — Veja também: Coraza em Proxies Cloud-Native: `coraza-proxy-wasm` (Envoy / Istio), `coraza-caddy`, Traefik e HAProxy SPOA.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://www.coraza.io/docs/seclang/directives/) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
