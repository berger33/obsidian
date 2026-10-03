---
id: software.seguranca.tranche02.000140
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
fontes: ["https://www.ory.com/docs/kratos/manage-identities/overview", "https://raw.githubusercontent.com/ory/kratos/master/README.md", "https://github.com/ory/kratos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Kratos Migração de Identidades sem Reset de Senha (`POST /admin/identities`): importação de hashes `bcrypt`, `argon2`, `pbkdf2` e `scrypt`

## Em uma frase
A API Administrativa do Ory Kratos (`POST /admin/identities` e importação em lote `PATCH /admin/identities`) permite migrar usuários de sistemas legados ou de outros provedores (Auth0, Okta, Firebase, Django, Devise) **importando diretamente o hash de senha existente (`hashed_password`)** nos formatos PHPass/Modular Crypt Format (`$2a$`/`$2b$` bcrypt, `$argon2id$`, `$pbkdf2-...$`, `$scrypt$`, Firebase Scrypt).

## Por que importa
Forçar 1 milhão de usuários a redefinirem suas senhas no dia da migração de provedor de identidade derruba a conversão e sobrecarrega o suporte técnico.

## Como funciona
Ao importar a identidade com `credentials.password.config.hashed_password` no formato original suportado, o usuário faz login normalmente com sua senha atual; e, quando o Kratos valida um hash legado (ex.: `pbkdf2` ou `bcrypt` antigo) durante o login, ele pode re-hashear transparentemente a senha para **Argon2id** atualizado no banco!

## Exemplo
```bash
# Importando uma identidade na Admin API (:4434) do Ory Kratos preservando seu hash bcrypt existente:
curl -sS -X POST "http://localhost:4434/admin/identities" \
  -H "Content-Type: application/json" \
  -d '{
    "schema_id": "default",
    "state": "active",
    "traits": {
      "email": "maria.silva@example.com"
    },
    "credentials": {
      "password": {
        "config": {
          "hashed_password": "$2a$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUW"
        }
      }
    }
  }'
```

## Limites e trade-offs
Para importar milhares de identidades rapidamente durante uma janela de migração, utilize o endpoint em lote `PATCH /admin/identities` enviando até centenas de objetos por chamada.

## Como verificar
Verifique a identidade importada com `kratos get identity <id>` e teste autenticar com a senha correspondente ao hash importado.

## Conexões
- [[orykratos-social-sign-in-oidc-federation-jsonnet-data-mapping]] — Veja também: Ory Kratos Social Sign-In e Federação OIDC: mapeamento de claims de provedores externos (`Google`, `GitHub`, `Microsoft`, `GitLab`) via `Jsonnet`.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://www.ory.com/docs/kratos/manage-identities/overview) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
