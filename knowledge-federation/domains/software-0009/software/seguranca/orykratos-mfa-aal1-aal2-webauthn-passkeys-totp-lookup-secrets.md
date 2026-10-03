---
id: software.seguranca.tranche02.000135
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

# Ory Kratos Multi-Factor Authentication (`AAL1` vs `AAL2`): `Passkeys`, `WebAuthn` (FIDO2), `TOTP` e `lookup_secret` (códigos de backup)

## Em uma frase
O Ory Kratos modela a força da autenticação usando **Authenticator Assurance Levels (`aal1` para fator único e `aal2` para múltiplos fatores)**, suportando nativamente **Passkeys / WebAuthn (FIDO2)** (chaves de segurança YubiKey, TouchID, FaceID, Windows Hello), **TOTP (`RFC 6238`)** (Google Authenticator, Authy, 1Password) e **Lookup Secrets** (códigos de recuperação de uso único).

## Por que importa
Exigir 2FA apenas no momento do login inicial sem verificar o nível `authenticator_assurance_level` da sessão em rotas críticas permite que uma sessão `aal1` acesse operações sensíveis se o segundo fator foi configurado como opcional.

## Como funciona
No `kratos.yml`, você pode definir `selfservice.flows.settings.required_aal: highest_available` (exigindo que um usuário que cadastrou 2FA apresente `aal2` antes de alterar sua senha ou e-mail) e verificar `session.authenticator_assurance_level == "aal2"` no seu middleware de backend antes de autorizar transferências ou exclusões.

## Exemplo
```yaml
selfservice:
  methods:
    passkey:
      enabled: true
      config:
        rp:
          display_name: "Portal Corporativo"
          id: "example.com"
          origins:
            - "https://app.example.com"
    totp:
      enabled: true
      config:
        issuer: "ExampleCorp"
    lookup_secret:
      enabled: true
```

## Limites e trade-offs
Habilite sempre o método **`lookup_secret`** junto com `totp` ou `webauthn` para que o usuário possa gerar códigos de backup de emergência caso perca seu dispositivo autenticador.

## Como verificar
Verifique no JSON de `/sessions/whoami` a transição de `"authenticator_assurance_level": "aal1"` para `"aal2"` após completar o desafio de segundo fator.

## Conexões
- [[orykratos-sessoes-whoami-cookies-session-token-caching-tokenizer]] — Veja também: Ory Kratos Gerenciamento de Sessões (`/sessions/whoami`): validação por Cookie (`ory_kratos_session`), `X-Session-Token` e conversão para JWT.
- [[orykratos-seguranca-senhas-argon2id-haveibeenpwned-k-anonymity]] — Veja também: Ory Kratos Segurança de Credenciais `password`: hashing `Argon2id` (ou `bcrypt`), política de similaridade e checagem *Have I Been Pwned* (`k-Anonymity`).

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
