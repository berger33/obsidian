---
id: software.seguranca.tranche02.000105
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

# Coraza em Proxies Cloud-Native: `coraza-proxy-wasm` (Envoy / Istio), `coraza-caddy`, Traefik e HAProxy SPOA

## Em uma frase
O projeto Coraza mantém integrações oficiais e comunitárias para embutir o WAF diretamente na camada de Ingress e Service Mesh: **`coraza-caddy`** (módulo nativo para Caddy Server), **`coraza-proxy-wasm`** (filtro WebAssembly ABI Proxy-WASM para **Envoy Proxy** e **Istio Service Mesh**), extensão WASM para **Traefik** e **`coraza-spoa`** (agente SPOE para **HAProxy**).

## Por que importa
Em arquiteturas Kubernetes com Istio ou Envoy Gateway, rotear o tráfego para um appliance WAF externo adiciona saltos de rede e pontos únicos de falha; compilar o Coraza para `Proxy-WASM` executa o WAF dentro do próprio Envoy.

## Como funciona
Quando compilado com TinyGo para o alvo `Proxy-WASM` (onde a build tag `no_fs_access` desativa buffers em disco do SO), o `coraza-proxy-wasm` roda isolado em sandbox WebAssembly dentro dos sidecars ou gateways Envoy/Istio com o OWASP CRS v4 embutido.

## Exemplo
```yaml
# Exemplo de recurso WasmPlugin no Istio carregando o filtro oficial coraza-proxy-wasm:
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: coraza-waf-gateway
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://ghcr.io/corazawaf/coraza-proxy-wasm:latest
  phase: AUTHZ
  pluginConfig:
    rules:
      - "SecRuleEngine On"
      - "Include @owasp_crs/*.conf"
```

## Limites e trade-offs
Em ambientes sem acesso a sistema de arquivos local (como WebAssembly no Envoy), o Coraza usa o filesystem virtual embutido (`io/fs.FS`) para carregar `@owasp_crs/*.conf` diretamente da memória.

## Como verificar
Teste o gateway Istio/Envoy ou Caddy enviando `?id=1'%20OR%20'1'='1` e confirme o retorno HTTP `403 Forbidden`.

## Conexões
- [[coraza-audit-logging-secauditengine-parts-abcfhz-formatos-json-ocsf]] — Veja também: Coraza Audit Logging (`SecAuditEngine`, `SecAuditLogParts` e `SecAuditLogFormat`): saída estruturada em `JSON`, `OCSF` e `Native`.
- [[coraza-build-tags-otimizacao-memoization-multiphase-rx-prefilter]] — Veja também: Coraza Otimização de Performance e Build Tags: memoização de regex/Aho-Corasick, `WAF.Close()`, `SecRxPreFilter` e `no_regex_multiline`.

## Fontes
- [OWASP Coraza GitHub — README.md (Go Enterprise-Grade WAF, ModSecurity SecLang & OWASP CRS v4 Compatibility, Transaction Lifecycle & Integrations)](https://raw.githubusercontent.com/corazawaf/coraza/main/README.md) — README oficial do corazawaf/coraza detalhando a arquitetura do WAF em Go, compatibilidade com SecLang e OWASP CRS v4, extensibilidade e integrações com Caddy, Envoy/Istio, Traefik e HAProxy; consultado em 2026-10-03.
- [OWASP Coraza Official Documentation — SecLang Directives Reference (SecRule, SecAction, SecRuleEngine, Body Access/Limits, Audit Log & Rule Removals)](https://www.coraza.io/docs/seclang/directives/) — Referência oficial das diretivas SecLang implementadas no Coraza WAF, cobrindo controle de motor, limites de body, remoção de regras por ID/Tag e auditoria estruturada; consultado em 2026-10-03.
- [OWASP Coraza WAF — Official GitHub Repository](https://github.com/corazawaf/coraza) — Repositório oficial Apache-2.0 do OWASP Coraza WAF; consultado em 2026-10-03.
