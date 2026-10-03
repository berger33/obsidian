---
id: software.seguranca.tranche02.000121
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

# Ory Hydra: arquitetura do servidor OAuth 2.0 e OpenID Connect Certificado (*OpenID Certified*) desacoplado de banco de usuários

## Em uma frase
O **Ory Hydra** (`ory/hydra`, escrito em Go e licenciado sob Apache 2.0) é um servidor **OAuth 2.0** e **OpenID Connect (OIDC) 1.0 Certificado pela OpenID Foundation**, projetado para baixa latência e alto throughput, que **não possui banco de dados de usuários nem telas fixas de login**: em vez disso, delega a autenticação e a interface de usuário para um **Login & Consent App** externo via redirecionamento e API REST.

## Por que importa
Servidores OIDC monolíticos forçam você a migrar sua tabela de usuários existente, seus hashes de senha e suas regras de MFA para dentro do banco deles; o Ory Hydra conecta-se a **qualquer** sistema de identidade existente (Ory Kratos, banco legado, LDAP ou SAML).

## Como funciona
O servidor Hydra expõe duas portas separadas por design de segurança: a **Porta Pública (`:4444`)**, que serve os endpoints OAuth2/OIDC padrão (`/oauth2/auth`, `/oauth2/token`, `/oauth2/revoke`, `/userinfo`, `/.well-known/jwks.json`, `/.well-known/openid-configuration`), e a **Porta Administrativa (`:4445`)**, que nunca deve ser exposta à internet pública!

## Exemplo
```bash
# Iniciando o Ory Hydra e consultando o documento público de descoberta OpenID Connect:
curl -sS http://localhost:4444/.well-known/openid-configuration | jq '{issuer, authorization_endpoint, token_endpoint, jwks_uri}'
```

## Limites e trade-offs
Mantenha a porta administrativa (`:4445`, endpoints `/admin/*`) estritamente isolada na rede interna/mTLS do cluster, acessível apenas pelo seu Login/Consent App e pelos jobs de provisionamento.

## Como verificar
Execute `hydra version` e consulte `http://localhost:4445/health/ready` para verificar a prontidão do banco de dados.

## Conexões
- [[oryhydra-fluxo-login-consent-challenge-verifier-delegacao-ui]] — Veja também: Ory Hydra Login & Consent Flow: orquestração via `login_challenge`, `consent_challenge` e `skip` com sua própria UI.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
