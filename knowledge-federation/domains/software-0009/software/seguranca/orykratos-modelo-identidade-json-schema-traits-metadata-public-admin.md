---
id: software.seguranca.tranche02.000132
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

# Ory Kratos Modelo de Identidade e `JSON Schema`: validação de `traits`, `credentials`, `metadata_public` e `metadata_admin`

## Em uma frase
Conforme documentado na visão geral oficial *What is an identity in Ory?* (`ory.com/docs/kratos/manage-identities/overview`), toda **Identity** no Kratos é validada contra um **JSON Schema (`schema_id`)** customizável e estruturada em: **`id`** (UUID imutável), **`state`** (`active` ou `inactive`), **`traits`** (atributos mutáveis pelo usuário, como `email` e `name`), **`credentials`** (`password`, `oidc`, `totp`, `webauthn`, `passkey`), **`metadata_public`** e **`metadata_admin`**.

## Por que importa
Bancos de usuários rígidos com colunas fixas (`first_name`, `phone`) obrigam migrações SQL a cada campo novo ou misturam dados editáveis pelo próprio usuário com atributos internos de permissão/plano.

## Como funciona
No Kratos, você nunca armazena dados sensíveis de controle de acesso dentro de `traits` (pois o próprio usuário pode editar seus `traits` no fluxo de *Settings*)! Atributos visíveis no `/sessions/whoami` mas somente-leitura para o usuário ficam em **`metadata_public`**, e dados internos restritos ao backend ficam em **`metadata_admin`** (visíveis apenas na Admin API `:4434`).

## Exemplo
```json
{
  "$id": "https://schemas.example.com/customer.v1.schema.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Customer Identity",
  "type": "object",
  "properties": {
    "traits": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string",
          "format": "email",
          "title": "E-Mail",
          "ory.sh/kratos": {
            "credentials": { "password": { "identifier": true }, "webauthn": { "identifier": true } },
            "verification": { "via": "email" },
            "recovery": { "via": "email" }
          }
        }
      },
      "required": ["email"],
      "additionalProperties": false
    }
  }
}
```

## Limites e trade-offs
Use sempre `"additionalProperties": false` dentro do bloco `traits` do seu JSON Schema de identidade para impedir que usuários injetem campos arbitrários não previstos durante o cadastro ou edição de perfil.

## Como verificar
Valide seu arquivo de schema executando `kratos validate identity-schema ./customer.schema.json` ou via endpoint `/schemas`.

## Conexões
- [[orykratos-arquitetura-api-first-identity-user-management-cloud-native]] — Veja também: Ory Kratos: arquitetura API-first de gerenciamento de identidades, credenciais e fluxos de autoatendimento (*Self-Service*).
- [[orykratos-fluxos-self-service-browser-vs-api-ui-nodes-csrf]] — Veja também: Ory Kratos Self-Service Flows (`login`, `registration`, `recovery`, `verification`, `settings`): arquitetura *Headless UI Nodes* para Browser e API.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://www.ory.com/docs/kratos/manage-identities/overview) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
