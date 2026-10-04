---
id: software.seguranca.tranche02.000123
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
fontes: ["https://raw.githubusercontent.com/ory/hydra/master/README.md", "https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow", "https://github.com/ory/hydra"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Hydra Gerenciamento de OAuth 2.0 Clients: `token_endpoint_auth_method`, obrigatoriedade de `PKCE` e escopos granulares

## Em uma frase
No Ory Hydra, cada aplicação consumidora é registrada via API Administrativa (`POST /admin/clients` ou CLI `hydra create oauth2-client`) com restrições estritas de `grant_types`, `response_types`, `scope`, `redirect_uris` e método de autenticação (`token_endpoint_auth_method`: `client_secret_basic`, `client_secret_post`, `private_key_jwt` ou `none`).

## Por que importa
Cadastrar clientes OAuth2 com `redirect_uris` genéricas ou permitir fluxos públicos (SPAs e apps mobile) sem exigir **PKCE (`RFC 7636`, `code_challenge_method=S256`)** expõe o código de autorização a interceptação.

## Como funciona
Para aplicações Single-Page (SPA) e aplicativos móveis nativos (clientes públicos que não podem guardar um segredo), configure `token_endpoint_auth_method: "none"` e habilite a exigência estrita de PKCE (`oauth2.pkce.enforced_for_public_clients: true` ou globalmente `oauth2.pkce.enforced: true`). Já para comunicação confidencial backend-a-backend de alta segurança, utilize **`private_key_jwt`** (`RFC 7523`) com chaves assimétricas.

## Exemplo
```bash
# Criando um OAuth2 Client confidencial para Authorization Code + PKCE e Refresh Token via CLI do Hydra:
hydra create oauth2-client \
  --endpoint http://localhost:4445 \
  --name "Portal Web Corporativo" \
  --grant-type authorization_code,refresh_token \
  --response-type code \
  --scope openid,offline_access,profile,email \
  --redirect-uri https://app.example.com/auth/callback
```

## Limites e trade-offs
O escopo `offline_access` (ou `offline`) é obrigatório no Hydra para que o servidor emita um `refresh_token` junto com o `access_token`.

## Como verificar
Liste e audite os clientes registrados com `hydra list oauth2-clients --endpoint http://localhost:4445`.

## Conexões
- [[oryhydra-fluxo-login-consent-challenge-verifier-delegacao-ui]] — Veja também: Ory Hydra Login & Consent Flow: orquestração via `login_challenge`, `consent_challenge` e `skip` com sua própria UI.
- [[oryhydra-estrategias-access-token-opaque-vs-jwt-token-introspection-rfc7662]] — Veja também: Ory Hydra Estratégias de Access Token (`opaque` vs `jwt`) e Token Introspection (`RFC 7662`).

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
