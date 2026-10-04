---
id: software.seguranca.tranche02.000122
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
fontes: ["https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow", "https://raw.githubusercontent.com/ory/hydra/master/README.md", "https://github.com/ory/hydra"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Hydra Login & Consent Flow: orquestração via `login_challenge`, `consent_challenge` e `skip` com sua própria UI

## Em uma frase
Conforme documentado no guia oficial *User login and consent flow* (`ory.com/docs/oauth2-oidc/custom-login-consent/flow`), sempre que um cliente inicia o fluxo em `/oauth2/auth`, o Ory Hydra redireciona o navegador para a sua aplicação de Login (`/urls/login?login_challenge=<ID>`) e, em seguida, para a sua aplicação de Consentimento (`/urls/consent?consent_challenge=<ID>`).

## Por que importa
Delegar a autenticação via `login_challenge` e `consent_challenge` permite que você construa a tela de login no seu próprio framework web (Next.js, Go, Node.js, Rails) com controle total sobre branding, WebAuthn, antifraude e seleção de organização/tenant.

## Como funciona
O fluxo de Login ocorre em 4 passos: 1) seu backend lê `login_challenge` da query string e chama `GET /admin/oauth2/auth/requests/login?login_challenge=...`; 2) se a resposta indicar **`skip: true`** (o usuário já possui sessão SSO ativa no Hydra), seu backend aceita imediatamente sem exibir tela; 3) se `skip: false`, você exibe o formulário, valida as credenciais no seu IdP (ex.: Ory Kratos) e chama `PUT /admin/oauth2/auth/requests/login/accept` informando `subject`, `remember` e `remember_for`; e 4) redireciona o usuário para a URL `redirect_to` retornada pelo Hydra!

## Exemplo
```bash
# Consultando os detalhes de um login_challenge na API Administrativa do Ory Hydra:
curl -sS "http://localhost:4445/admin/oauth2/auth/requests/login?login_challenge=${CHALLENGE}" \
  | jq '{skip: .skip, subject: .subject, client_id: .client.client_id, requested_scope: .requested_scope}'
```

## Limites e trade-offs
No passo de aceitação do `consent_challenge` (`acceptOAuth2ConsentRequest`), você injeta as claims customizadas que devem constar no `access_token` e no `id_token` dentro do objeto `session: { access_token: {...}, id_token: {...} }`.

## Como verificar
Teste o fluxo completo usando o app de referência `ory/hydra-login-consent-node` em ambiente de desenvolvimento.

## Conexões
- [[oryhydra-arquitetura-oauth2-openid-connect-certified-headless-server]] — Veja também: Ory Hydra: arquitetura do servidor OAuth 2.0 e OpenID Connect Certificado (*OpenID Certified*) desacoplado de banco de usuários.
- [[oryhydra-gerenciamento-oauth2-clients-pkce-auth-methods-scopes]] — Veja também: Ory Hydra Gerenciamento de OAuth 2.0 Clients: `token_endpoint_auth_method`, obrigatoriedade de `PKCE` e escopos granulares.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
