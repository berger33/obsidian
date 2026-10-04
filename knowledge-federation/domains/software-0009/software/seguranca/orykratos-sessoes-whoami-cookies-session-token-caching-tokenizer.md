---
id: software.seguranca.tranche02.000134
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
fontes: ["https://raw.githubusercontent.com/ory/kratos/master/README.md", "https://www.ory.com/docs/kratos/manage-identities/overview", "https://github.com/ory/kratos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Kratos Gerenciamento de Sessões (`/sessions/whoami`): validação por Cookie (`ory_kratos_session`), `X-Session-Token` e conversão para JWT

## Em uma frase
Para autenticar requisições nas suas aplicações e APIs, o endpoint **`GET /sessions/whoami`** do Ory Kratos valida o cookie de sessão HTTP (`ory_kratos_session` para aplicações web no mesmo domínio raiz) ou o cabeçalho `X-Session-Token` / `Authorization: Bearer <session_token>` (para clientes mobile/nativos), retornando o objeto `Session` completo com `identity`, `authenticator_assurance_level` (`aal1` ou `aal2`) e `authentication_methods`.

## Por que importa
Se os seus microsserviços internos preferirem receber um token JWT assinado com claims específicas em vez de consultar o objeto JSON completo do Kratos, o recurso **`tokenize_as`** do `/sessions/whoami` resolve isso nativamente.

## Como funciona
Ao chamar `GET /sessions/whoami?tokenize_as=internal_jwt_template`, o próprio Kratos aplica um template Jsonnet aos dados da sessão, assina um JWT com o conjunto de chaves configurado em `session.whoami.tokenizer.templates` e o devolve no campo `tokenized` da resposta!

## Exemplo
```bash
# Verificando a sessão ativa a partir do cookie ou token e inspecionando o nível de garantia (AAL):
curl -sS -H "X-Session-Token: ${KRATOS_SESSION_TOKEN}" \
  "http://localhost:4433/sessions/whoami" | jq '{active, aal: .authenticator_assurance_level, identity_id: .identity.id, email: .identity.traits.email}'
```

## Limites e trade-offs
Configure `session.lifespan` e `session.earliest_possible_extend` para renovar sessões ativas de forma controlada, e use `DELETE /admin/identities/{id}/sessions` para encerrar remotamente todas as sessões de um usuário.

## Como verificar
Invoque `/sessions/whoami` com um token válido e confirme `"active": true`.

## Conexões
- [[orykratos-fluxos-self-service-browser-vs-api-ui-nodes-csrf]] — Veja também: Ory Kratos Self-Service Flows (`login`, `registration`, `recovery`, `verification`, `settings`): arquitetura *Headless UI Nodes* para Browser e API.
- [[orykratos-mfa-aal1-aal2-webauthn-passkeys-totp-lookup-secrets]] — Veja também: Ory Kratos Multi-Factor Authentication (`AAL1` vs `AAL2`): `Passkeys`, `WebAuthn` (FIDO2), `TOTP` e `lookup_secret` (códigos de backup).

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
