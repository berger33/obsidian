---
id: software.seguranca.tranche03.000248
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

# Pomerium para Acesso Zero-Trust a `Kubernetes API` e Dashboards Internos: injeção de credenciais upstream e cabeçalhos `Impersonate-*`

## Em uma frase
O Pomerium permite proteger APIs e painéis que possuem seu próprio sistema de autenticação (como o **Kubernetes API Server**, **Grafana**, ** Kibana** ou aplicações legadas) combinando a autenticação do usuário final no Pomerium com a injeção controlada de cabeçalhos de autorização upstream (`set_request_headers`, `remove_request_headers` ou `kubernetes_service_account_token`).

## Por que importa
Quando um painel interno espera receber o usuário autenticado via cabeçalho HTTP (`X-WEBAUTH-USER` no Grafana) ou via *Kubernetes User Impersonation* (`Impersonate-User` e `Impersonate-Group`), permitir que o cliente externo envie esses cabeçalhos diretamente permitiria escalação de privilégio.

## Como funciona
O Pomerium **remove automaticamente** qualquer cabeçalho de identidade enviado pelo cliente externo e injeta os valores verificados da sessão OIDC (ou o token da ServiceAccount do Pomerium configurado na rota) diretamente na chamada ao upstream!

## Exemplo
```yaml
routes:
  - from: https://kibana.internal.corp
    to: http://kibana.logging.svc.cluster.local:5601
    pass_identity_headers: true
    remove_request_headers:
      - X-WEBAUTH-USER
    # O Grafana lê X-Pomerium-Claim-Email (configurado em jwt_claims_headers: ["email"])
    jwt_claims_headers:
      - email
      - groups
    policy:
      - allow:
          and:
            - domain:
                is: internal.corp
```

## Limites e trade-offs
Ao usar `jwt_claims_headers: ["email", "groups"]`, o Pomerium injeta automaticamente os cabeçalhos limpos `X-Pomerium-Claim-Email` e `X-Pomerium-Claim-Groups` (descartando qualquer cabeçalho `X-Pomerium-*` que o navegador externo tente enviar!).

## Como verificar
Teste enviar um cabeçalho forjado `curl -H "X-Pomerium-Claim-Email: admin@internal.corp"` e confirme que o Pomerium o sobrescreve com a identidade real da sessão.

## Conexões
- [[pomerium-arquitetura-distribuida-authenticate-authorize-proxy-databroker]] — Veja também: Pomerium Arquitetura de Serviços Distribuídos (`Authenticate`, `Authorize`, `Proxy` e `Databroker`): isolamento e escalabilidade.
- [[pomerium-cors-websocket-timeout-headers-seguranca-hsts-csp]] — Veja também: Pomerium Controles de Tráfego HTTP/WebSockets (`allow_websockets`, `timeout`, `idle_timeout`) e Cabeçalhos de Segurança (`set_response_headers`).

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
