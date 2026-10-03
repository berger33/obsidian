---
id: software.seguranca.tranche02.000124
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

# Ory Hydra Estratégias de Access Token (`opaque` vs `jwt`) e Token Introspection (`RFC 7662`)

## Em uma frase
O Ory Hydra suporta duas estratégias para emissão de `access_token` (`strategies.access_token`): **Opaque Tokens** (padrão recomendado: strings aleatórias de alta entropia sem carga útil legível, validadas via endpoint de **Token Introspection `RFC 7662`**) e **JSON Web Tokens (`jwt`)** (assinados criptograficamente com as chaves JWKS do Hydra).

## Por que importa
Tokens JWT podem ser validados localmente pelos microsserviços sem chamada de rede ao Hydra, mas **não podem ser revogados instantaneamente** antes da expiração (`exp`) sem uma blocklist distribuída e expõem metadados internos ao cliente se decodificados.

## Como funciona
Um padrão arquitetural consagrado com o Ory Hydra (frequentemente combinado com um API Gateway ou Ory Oathkeeper) é emitir **Opaque Tokens** para a internet externa e, na borda do cluster (API Gateway), chamar `POST /admin/oauth2/introspect` no Hydra — que valida revogação imediata em sub-milissegundos — convertendo o resultado em um JWT interno de curta duração para os microsserviços!

## Exemplo
```bash
# Inspecionando e validando um Access Token (Opaque ou JWT) no endpoint de Introspecção RFC 7662 do Hydra:
curl -sS -X POST "http://localhost:4445/admin/oauth2/introspect" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "token=${ACCESS_TOKEN}&scope=profile" | jq '{active, sub, client_id, exp, scope}'
```

## Limites e trade-offs
Sempre defina um TTL curto para `ttl.access_token` (ex.: `15m` a `1h`), especialmente quando utilizar a estratégia `jwt`, renovando sessões ativas via `refresh_token` com rotação automática.

## Como verificar
Verifique na resposta do `/admin/oauth2/introspect` que `"active": true` torna-se `"active": false` imediatamente após chamar `/oauth2/revoke`.

## Conexões
- [[oryhydra-gerenciamento-oauth2-clients-pkce-auth-methods-scopes]] — Veja também: Ory Hydra Gerenciamento de OAuth 2.0 Clients: `token_endpoint_auth_method`, obrigatoriedade de `PKCE` e escopos granulares.
- [[oryhydra-client-credentials-rfc6749-rfc7523-jwt-bearer-m2m]] — Veja também: Ory Hydra Autenticação Machine-to-Machine (`M2M`): `client_credentials` (`RFC 6749`) e `jwt-bearer` (`RFC 7523`).

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
