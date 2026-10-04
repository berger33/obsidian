---
id: software.seguranca.tranche02.000108
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

# Coraza Body Processors (`JSON`, `XML`, `URLENCODED`, `MULTIPART`): parsing estruturado de payloads de APIs modernas na Fase 1 e Fase 2

## Em uma frase
Para inspecionar APIs REST, GraphQL e SOAP além de formulários HTML tradicionais, o Coraza inclui **Body Processors** nativos (`URLENCODED`, `MULTIPART`, `JSON` e `XML`), ativados dinamicamente na Fase 1 pela ação `ctl:requestBodyProcessor=...` com base no cabeçalho `Content-Type` da requisição.

## Por que importa
Se o WAF tratasse um payload `application/json` complexo apenas como uma string bruta, atacantes poderiam esconder payloads de SQLi/XSS usando sequências de escape Unicode JSON (`\u003cscript\u003e`) ou aninhamento profundo de objetos.

## Como funciona
Quando `ctl:requestBodyProcessor=JSON` é acionado na Fase 1, o parser JSON do Coraza decodifica a árvore de objetos e popula a coleção `ARGS` / `ARGS_NAMES` (ex.: `ARGS:json.user.email`), permitindo que todas as regras da Fase 2 avaliem os valores já decodificados.

## Exemplo
```apache
SecRule REQUEST_HEADERS:Content-Type "^application/(?:[a-z0-9.-]+[+]json|json)" \
    "id:200001,phase:1,t:none,t:lowercase,pass,nolog,ctl:requestBodyProcessor=JSON"
```

## Limites e trade-offs
Caso o corpo da requisição envie um JSON malformado que falhe no parsing, a variável `REQBODY_ERROR` é preenchida (`1`) e pode ser bloqueada imediatamente por uma regra de integridade de protocolo.

## Como verificar
Envie um `POST` com `Content-Type: application/json` e payload malformado `{invalid` para verificar o acionamento de `REQBODY_ERROR`.

## Conexões
- [[coraza-modo-fips-140-3-restricao-transformacoes-md5-sha1]] — Veja também: Coraza em Modo `FIPS 140-3` (`GODEBUG=fips140=on`): detecção em tempo de execução e restrição automática de `t:md5` e `t:sha1`.
- [[coraza-extensibilidade-plugins-operators-actions-audit-loggers-go]] — Veja também: Coraza SDK de Extensibilidade (`plugins`): registro de Operadores (`RegisterOperator`), Ações, Transformações e Audit Loggers customizados em Go.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://www.coraza.io/docs/seclang/directives/) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
