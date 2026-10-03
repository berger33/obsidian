---
id: software.seguranca.tranche02.000106
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

# Coraza Otimização de Performance e Build Tags: memoização de regex/Aho-Corasick, `WAF.Close()`, `SecRxPreFilter` e `no_regex_multiline`

## Em uma frase
Conforme detalhado na seção *Build tags* do README oficial do Coraza, o motor utiliza **memoização global por padrão** para reutilizar padrões compilados de expressões regulares (`@rx`) e autômatos Aho-Corasick (`@pm`) entre múltiplas instâncias WAF, além de oferecer otimizações como `SecRxPreFilter` e `coraza.rule.no_regex_multiline`.

## Por que importa
Em um Ingress Controller multi-tenant que instancia 500 objetos `coraza.WAF` (um por VirtualHost carregando o OWASP CRS v4), compilar 500 vezes as mesmas centenas de expressões regulares esgotaria gigabytes de RAM sem memoização compartilhada.

## Como funciona
Em processos de longa duração que recarregam configurações WAF dinamicamente (*live reload*), chame **`WAF.Close()`** (via interface `experimental.WAFCloser`) ao descartar uma instância antiga do WAF para liberar as entradas cacheadas, ou utilize a build tag `coraza.no_memoize` se preferir desativar o cache global.

## Exemplo
```bash
# Compilando binário Go com Coraza alinhado ao comportamento CRS sem multiline por padrão em @rx:
go build -tags="coraza.rule.no_regex_multiline,coraza.rule.case_sensitive_args_keys" ./cmd/waf-proxy
```

## Limites e trade-offs
Como documenta o README oficial, a build tag `coraza.rule.no_regex_multiline` desativa o modificador multiline padrão no operador `@rx`, alinhando o comportamento ao esperado pelo CRS, reduzindo falsos positivos e melhorando a performance.

## Como verificar
Monitore o uso de memória heap (`go tool pprof`) durante reloads sucessivos de instâncias WAF confirmando a chamada a `WAF.Close()`.

## Conexões
- [[coraza-integracoes-cloud-native-proxy-wasm-envoy-istio-caddy-traefik]] — Veja também: Coraza em Proxies Cloud-Native: `coraza-proxy-wasm` (Envoy / Istio), `coraza-caddy`, Traefik e HAProxy SPOA.
- [[coraza-modo-fips-140-3-restricao-transformacoes-md5-sha1]] — Veja também: Coraza em Modo `FIPS 140-3` (`GODEBUG=fips140=on`): detecção em tempo de execução e restrição automática de `t:md5` e `t:sha1`.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
