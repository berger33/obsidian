---
id: software.seguranca.tranche03.000250
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

# Pomerium Verificação Contínua e Observabilidade (`authorize_log`, `access_log`, `Prometheus` e `OpenTelemetry` Tracing)

## Em uma frase
Conforme destacado no README oficial (*"every single action is verified before allowed to execute"*), o Pomerium emite logs estruturados em JSON para cada decisão de autorização (**`authorize-log`**) e para cada requisição HTTP/TCP encaminhada (**`http-access`**), além de exportar métricas **Prometheus (`metrics_address`)** e traces distribuídos **OpenTelemetry (`tracing_provider`)**.

## Por que importa
Em uma VPN tradicional, os logs de segurança mostram apenas "Alice conectou na VPN às 09:00 e desconectou às 18:00", sem visibilidade de quais endpoints internos ela acessou nem quais requisições foram negadas por política.

## Como funciona
Nos logs de decisão `authorize-log` do Pomerium, cada linha JSON registra o `request-id`, `user`, `email`, `ip`, `http-host`, `http-method`, `http-path`, **`allow: true|false`**, **`deny: true|false`** e as razões exatas da política avaliada, fornecendo trilha de auditoria completa para SOC 2, ISO 27001 e PCI-DSS!

## Exemplo
```yaml
# Habilitando logs JSON detalhados e métricas Prometheus no config.yaml do Pomerium:
log_level: info
proxy_log_level: info
metrics_address: 0.0.0.0:9090
authorize_log_fields:
  - request-id
  - ip
  - user
  - email
  - http-method
  - http-host
  - http-path
  - allow
  - deny
```

## Limites e trade-offs
Ative a coleta do endpoint Prometheus `:9090/metrics` do Pomerium e crie alertas para picos na métrica de requisições negadas por política (`403 Forbidden`) ou erros de comunicação com o IdP upstream.

## Como verificar
Filtre os eventos de autorização nos logs do Pomerium com `jq 'select(.service == "authorize")'`.

## Conexões
- [[pomerium-cors-websocket-timeout-headers-seguranca-hsts-csp]] — Veja também: Pomerium Controles de Tráfego HTTP/WebSockets (`allow_websockets`, `timeout`, `idle_timeout`) e Cabeçalhos de Segurança (`set_response_headers`).

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
