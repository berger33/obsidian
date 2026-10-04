---
id: software.seguranca.tranche14.001304
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/goauthentik/authentik/main/README.md", "https://docs.goauthentik.io/docs/core/architecture"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Provedores **OAuth2 / OIDC**, **SAML 2.0** e **SCIM 2.0** no authentik: Assinatura de JWTs, Property Mappings (Scopes) e Provisionamento Automático de Ciclo de Vida

## Em uma frase
No modelo de domínio do authentik, toda integração de sistema é dividida em um par **`Application` + `Provider`**: a **Application** representa o item visual no portal do usuário e concentra as políticas de controle de acesso (quem pode entrar), enquanto o **Provider** implementa o protocolo técnico de autenticação/provisionamento!

## Por que importa
Para aplicações modernas, o **OAuth2 / OpenID Connect Provider** suporta Authorization Code Flow com **PKCE (`S256`)**, Device Code Flow, Client Credentials, **JWKS** assinados com chaves RSA/ECDSA gerenciadas pelo authentik, criptografia de token **JWE** e **federated Machine-to-Machine (M2M) Authentication** (onde um JWT emitido por outro IdP ou pelo Kubernetes/GitHub Actions pode ser trocado por um Access Token do authentik sem segredos estáticos!).

## Como funciona
Já o **SCIM 2.0 Provider (*Outbound SCIM*)** resolve um dos maiores desafios de governança corporativa (**Joiner-Mover-Leaver**): sempre que um usuário é criado, muda de grupo ou é **desativado** no authentik, o Worker dispara imediatamente chamadas SCIM para criar, atualizar ou revogar a conta correspondente em aplicações externas (Slack, GitHub Enterprise, AWS IAM Identity Center, Grafana)!

## Exemplo
```bash
# Inspecionar o documento de descoberta OpenID Connect (.well-known/openid-configuration) e as chaves publicas JWKS de um Provider do authentik
curl -sk https://sso.exemplo.br/application/o/minha-app/.well-known/openid-configuration | jq .
```

## Limites e trade-offs
Como customizar quais *claims* (ex.: `groups`, `department`, `ssh_username` ou papéis específicos do Kubernetes RBAC) vão dentro do `id_token` / `access_token` OIDC ou da asserção SAML? Através dos **Scope Mappings / Property Mappings** em Python do authentik, onde você retorna um dicionário JSON com exatamente os atributos exigidos pela aplicação cliente!

## Como verificar
Defina tempos de expiração curtos para o `Access Token` (ex.: `minutes=5` a `minutes=15`) e habilite a validação estrita de `Redirect URIs` com expressões regulares exatas.

## Conexões
- [[authentik-politicas-reputacao-ip-expressoes-python-rbac-abac]] — Veja também: Motor de Políticas (**Policy Engine**) do authentik: **Expression Policies** em Python, **Reputation Policy** Anti-Brute-Force, GeoIP e HIBP.
- [[authentik-outposts-proxy-forwardauth-ldap-radius-arquitetura-distribuida]] — Veja também: Arquitetura de **Outposts** no authentik: Protegendo Aplicações Sem SSO via **Proxy / ForwardAuth (Traefik, Nginx, Envoy)** e Gateways **LDAP / RADIUS**.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
