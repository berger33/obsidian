---
id: software.seguranca.tranche02.000127
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

# Ory Hydra Logout Federado OpenID Connect: `RP-Initiated`, `Front-Channel Logout 1.0` e `Back-Channel Logout 1.0`

## Em uma frase
Conforme listado no README oficial, o Ory Hydra é certificado nas especificações **OpenID Connect Front-Channel Logout 1.0** e **OpenID Connect Back-Channel Logout 1.0**, além de suportar o fluxo de `logout_challenge` para coordenar o encerramento de sessão entre o provedor de identidade e todas as aplicações clientes (*Relying Parties — RPs*).

## Por que importa
Em um ambiente Single Sign-On (SSO) com 10 aplicações web integradas via OIDC, se o usuário clicar em "Sair" na Aplicação A e apenas o cookie local da Aplicação A for apagado, a sessão global no Hydra e nas Aplicações B..J continuará aberta.

## Como funciona
Quando o logout é iniciado em `/oauth2/sessions/logout`, o Hydra redireciona para `/urls/logout?logout_challenge=...` e, após a aceitação (`acceptOAuth2LogoutRequest`), dispara **Logout Tokens JWT** via POST servidor-a-servidor para a `backchannel_logout_uri` de cada cliente participante daquela sessão (`sid`) ou renderiza iframes de `frontchannel_logout_uri`!

## Exemplo
```bash
# Revogando programaticamente todas as sessões de consentimento e login de um usuário específico via Admin API:
curl -sS -X DELETE "http://localhost:4445/admin/oauth2/auth/sessions/login?subject=${USER_ID}"
curl -sS -X DELETE "http://localhost:4445/admin/oauth2/auth/sessions/consent?subject=${USER_ID}&all=true"
```

## Limites e trade-offs
Em caso de comprometimento de conta ou desligamento de colaborador, chame os endpoints `DELETE /admin/oauth2/auth/sessions/login` e `consent` para revogar imediatamente todos os refresh tokens e sessões do `subject`.

## Como verificar
Verifique que qualquer tentativa subsequente de usar um `refresh_token` revogado retorna erro `invalid_grant`.

## Conexões
- [[oryhydra-jwks-gerenciamento-chaves-assimetricas-rotacao-zero-downtime]] — Veja também: Ory Hydra Gerenciamento e Rotação de Chaves Criptográficas (`JWKS`): conjuntos `hydra.openid.id-token` e `hydra.jwt.access-token`.
- [[oryhydra-deteccao-reuso-refresh-token-rotacao-mitigacao-roubo]] — Veja também: Ory Hydra Segurança de `Refresh Tokens`: rotação automática a cada uso e invalidação de toda a família em caso de *Replay*.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
