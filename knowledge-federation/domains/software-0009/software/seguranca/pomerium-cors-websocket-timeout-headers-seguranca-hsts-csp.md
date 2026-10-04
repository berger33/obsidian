---
id: software.seguranca.tranche03.000249
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
fontes: ["https://www.pomerium.com/docs", "https://raw.githubusercontent.com/pomerium/pomerium/main/README.md", "https://github.com/pomerium/pomerium"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pomerium Controles de Tráfego HTTP/WebSockets (`allow_websockets`, `timeout`, `idle_timeout`) e Cabeçalhos de Segurança (`set_response_headers`)

## Em uma frase
Por ser construído sobre o **Envoy Proxy**, o Pomerium oferece controle granular de protocolo por rota: suporte explícito a **WebSockets (`allow_websockets: true`)**, **SPDY (`allow_spdy: true`)** — essencial para `kubectl exec` e `kubectl port-forward` —, configuração de **`timeout`** e **`idle_timeout`** para streams longos, reescrita de caminho (`prefix_rewrite` / `regex_rewrite`) e injeção de cabeçalhos HTTP de segurança na resposta (`set_response_headers`).

## Por que importa
Aplicações interativas modernas (como terminais web no Rancher/Argo CD, JupyterHub, VS Code Server / coder) dependem de conexões WebSocket persistentes; se o proxy reverso não habilitar o upgrade WebSocket explicitamente ou cortar a conexão após 30 segundos, o terminal web cairá constantemente.

## Como funciona
Ativando `allow_websockets: true` na rota específica, o Pomerium autentica e autoriza o handshake HTTP inicial contra a política PPL antes de estabelecer o túnel WebSocket bidirecional.

## Exemplo
```yaml
routes:
  - from: https://vscode.internal.corp
    to: http://code-server.dev.svc.cluster.local:8080
    allow_websockets: true
    idle_timeout: 1h
    set_response_headers:
      Strict-Transport-Security: "max-age=31536000; includeSubDomains; preload"
      X-Frame-Options: "DENY"
      X-Content-Type-Options: "nosniff"
    policy:
      - allow:
          and:
            - claim/groups:
                has: engineering
```

## Limites e trade-offs
Habilite `allow_websockets: true` e `allow_spdy: true` apenas nas rotas de aplicações que realmente utilizam esses protocolos, mantendo a superfície de protocolo mínima nas demais rotas.

## Como verificar
Verifique os cabeçalhos HTTP retornados na rota com `curl -I https://vscode.internal.corp`.

## Conexões
- [[pomerium-integracao-kubernetes-dashboard-api-impersonation-serviceaccount]] — Veja também: Pomerium para Acesso Zero-Trust a `Kubernetes API` e Dashboards Internos: injeção de credenciais upstream e cabeçalhos `Impersonate-*`.
- [[pomerium-auditoria-continua-authorize-logs-otel-metricas-prometheus]] — Veja também: Pomerium Verificação Contínua e Observabilidade (`authorize_log`, `access_log`, `Prometheus` e `OpenTelemetry` Tracing).

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
