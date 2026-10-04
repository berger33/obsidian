---
id: software.seguranca.tranche02.000133
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

# Ory Kratos Self-Service Flows (`login`, `registration`, `recovery`, `verification`, `settings`): arquitetura *Headless UI Nodes* para Browser e API

## Em uma frase
O Ory Kratos implementa seus cinco fluxos de autoatendimento (**`login`**, **`registration`**, **`recovery`**, **`verification`** e **`settings`**) de forma 100% *headless*: quando o frontend inicia um fluxo (`/self-service/login/browser` para web com proteção CSRF por cookie ou `/self-service/login/api` para clientes nativos mobile), o Kratos retorna uma máquina de estados JSON contendo **`ui.nodes`** (os campos de formulário, botões, tokens CSRF e mensagens de erro/validação).

## Por que importa
Mudar o método de autenticação (por exemplo, habilitar Passkeys, um novo provedor social OIDC ou exigir um campo novo no JSON Schema) atualiza automaticamente o array `ui.nodes` retornado pela API, permitindo que o frontend renderize os novos campos dinamicamente sem quebrar contratos.

## Como funciona
Nos fluxos `/browser`, o Kratos emite e valida rigorosamente cookies `csrf_token` (`SameSite`, `HttpOnly`, `Secure`) e previne ataques de *Session Fixation* e *Open Redirect* validando qualquer parâmetro `return_to` contra a allowlist `selfservice.allowed_return_urls`.

## Exemplo
```bash
# Iniciando um fluxo de login para cliente nativo/API e inspecionando os ui.nodes gerados pelo Kratos:
curl -sS -H "Accept: application/json" \
  "http://localhost:4433/self-service/login/api" | jq '{id: .id, action: .ui.action, nodes: [.ui.nodes[].attributes.name]}'
```

## Limites e trade-offs
Para acelerar o desenvolvimento sem construir as telas do zero, você pode usar o **Ory Elements** (componentes UI para React/Next.js/Prebuilt UI) ou o `kratos-selfservice-ui-node` oficial.

## Como verificar
Verifique que passar uma URL externa não listada em `allowed_return_urls` para `?return_to=...` é bloqueado pelo Kratos.

## Conexões
- [[orykratos-modelo-identidade-json-schema-traits-metadata-public-admin]] — Veja também: Ory Kratos Modelo de Identidade e `JSON Schema`: validação de `traits`, `credentials`, `metadata_public` e `metadata_admin`.
- [[orykratos-sessoes-whoami-cookies-session-token-caching-tokenizer]] — Veja também: Ory Kratos Gerenciamento de Sessões (`/sessions/whoami`): validação por Cookie (`ory_kratos_session`), `X-Session-Token` e conversão para JWT.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
