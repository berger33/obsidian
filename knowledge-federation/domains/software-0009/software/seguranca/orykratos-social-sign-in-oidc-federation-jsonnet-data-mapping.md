---
id: software.seguranca.tranche02.000139
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

# Ory Kratos Social Sign-In e Federação OIDC: mapeamento de claims de provedores externos (`Google`, `GitHub`, `Microsoft`, `GitLab`) via `Jsonnet`

## Em uma frase
No método **`oidc`** do Ory Kratos, você integra provedores externos de OpenID Connect e OAuth2 (Google, GitHub, Apple, Microsoft Entra ID, GitLab, Discord ou qualquer IdP corporativo OIDC) usando um script **`mapper_url` em Jsonnet** para transformar as claims retornadas pelo provedor externo nos `traits` e `metadata_public` do seu JSON Schema de identidade.

## Por que importa
Cada provedor social devolve dados em formatos ligeiramente diferentes; usar um mapeador Jsonnet declarativo evita escrever código backend customizado para cada botão "Entrar com GitHub/Google".

## Como funciona
Dentro do arquivo `.jsonnet`, a variável `std.extVar('claims')` expõe as claims validadas do `id_token` / `userinfo` do provedor (incluindo `email`, `email_verified`, `given_name`, `hd`), permitindo preencher `traits` de forma segura.

## Exemplo
```jsonnet
local claims = std.extVar('claims');
{
  identity: {
    traits: {
      [if 'email' in claims && claims.email_verified then 'email' else null]: claims.email,
      name: {
        first: if 'given_name' in claims then claims.given_name else '',
        last: if 'family_name' in claims then claims.family_name else '',
      },
    },
  },
}
```

## Limites e trade-offs
Observe a verificação crítica `claims.email_verified` no exemplo Jsonnet acima: **nunca** mapeie automaticamente um e-mail de um provedor OIDC externo como verificado se `claims.email_verified` for `false`, para evitar ataques de *Account Takeover* por pré-vinculação de e-mail não verificado!

## Como verificar
Teste o fluxo de login OIDC e inspecione os `traits` e a entrada `credentials.oidc` da identidade criada em `GET /admin/identities/{id}`.

## Conexões
- [[orykratos-webhooks-actions-before-after-hooks-jsonnet-sincronizacao]] — Veja também: Ory Kratos Actions & Webhooks (`before` / `after` hooks): interceptação e enriquecimento de fluxos com templates `Jsonnet`.
- [[orykratos-importacao-migracao-identidades-hashes-bcrypt-argon2-pbkdf2]] — Veja também: Ory Kratos Migração de Identidades sem Reset de Senha (`POST /admin/identities`): importação de hashes `bcrypt`, `argon2`, `pbkdf2` e `scrypt`.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://www.ory.com/docs/kratos/manage-identities/overview) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
