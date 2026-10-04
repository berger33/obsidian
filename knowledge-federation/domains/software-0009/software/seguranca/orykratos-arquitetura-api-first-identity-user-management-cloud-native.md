---
id: software.seguranca.tranche02.000131
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

# Ory Kratos: arquitetura API-first de gerenciamento de identidades, credenciais e fluxos de autoatendimento (*Self-Service*)

## Em uma frase
O **Ory Kratos** (`ory/kratos`, escrito em Go e licenciado sob Apache 2.0) é um sistema **API-first** e cloud-native de gerenciamento de identidades e usuários que centraliza os fluxos mais críticos de segurança de contas — **Login**, **Registration**, **Account Recovery**, **Email/Phone Verification**, **Settings/Profile Management** e **Multi-Factor Authentication (MFA)** — expondo-os por APIs HTTP para qualquer frontend.

## Por que importa
Reimplementar do zero em cada projeto fluxos de redefinição de senha, proteção contra enumeração de contas, rotação de sessão, TOTP e WebAuthn/Passkeys é uma das maiores fontes de vulnerabilidades de autenticação.

## Como funciona
Assim como o Hydra, o Ory Kratos separa estritamente a **API Pública (`:4433`)** — consumida diretamente pelo navegador ou aplicativo mobile em fluxos *Self-Service* — da **API Administrativa (`:4434`)** — usada exclusivamente pelo backend para provisionar identidades (`/admin/identities`), gerenciar schemas e auditar estados.

## Exemplo
```bash
# Verificando a prontidão do Ory Kratos e listando os JSON Schemas de identidade configurados:
curl -sS http://localhost:4433/health/ready
curl -sS http://localhost:4433/schemas | jq .
```

## Limites e trade-offs
Nunca exponha a porta administrativa (`:4434`) do Ory Kratos para fora da rede privada do cluster, pois os endpoints `/admin/*` permitem criar, bloquear e alterar identidades sem autenticação de usuário final.

## Como verificar
Execute `kratos version` e consulte `http://localhost:4433/health/alive`.

## Conexões
- [[orykratos-modelo-identidade-json-schema-traits-metadata-public-admin]] — Veja também: Ory Kratos Modelo de Identidade e `JSON Schema`: validação de `traits`, `credentials`, `metadata_public` e `metadata_admin`.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
