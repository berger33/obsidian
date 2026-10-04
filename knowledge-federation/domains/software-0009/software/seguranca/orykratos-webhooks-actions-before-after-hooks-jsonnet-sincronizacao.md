---
id: software.seguranca.tranche02.000138
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

# Ory Kratos Actions & Webhooks (`before` / `after` hooks): interceptação e enriquecimento de fluxos com templates `Jsonnet`

## Em uma frase
O sistema de **Hooks (`before` e `after`)** do Ory Kratos permite disparar **Webhooks HTTP** (síncronos bloqueantes ou assíncronos não-bloqueantes) antes ou depois de `login`, `registration`, `recovery`, `verification` e `settings`, utilizando templates **Jsonnet** para formatar o payload enviado e até modificar os atributos da identidade a partir da resposta do webhook (`can_interrupt: true` / `parse: true`).

## Por que importa
Frequentemente a aplicação precisa consultar um sistema antifraude/allowlist antes de permitir um novo cadastro (hook síncrono bloqueante) ou criar um registro correspondente no Stripe/CRM assim que o cadastro conclui (hook pós-registro).

## Como funciona
Quando `response.parse: true` está habilitado em um webhook `after` de `registration`, o serviço externo pode retornar um JSON atualizado com `metadata_public` (por exemplo o `stripe_customer_id` ou `tenant_id` recém-criado), e o próprio Kratos persiste esses metadados na identidade dentro da mesma transação de fluxo!

## Exemplo
```yaml
selfservice:
  flows:
    registration:
      after:
        hooks:
          - hook: web_hook
            config:
              url: http://billing-service.internal/webhooks/kratos-user-created
              method: POST
              body: file:///etc/config/kratos/user-created.jsonnet
              can_interrupt: false
              response:
                ignore: false
                parse: true
```

## Limites e trade-offs
Para notificações de analytics ou marketing onde uma falha no serviço externo não deve impedir o usuário de fazer login, configure `response.ignore: true` e `can_interrupt: false` para execução assíncrona.

## Como verificar
Verifique nos logs do Kratos e na tabela `courier_messages`/métricas o código de resposta dos webhooks disparados.

## Conexões
- [[orykratos-recovery-verification-one-time-codes-link-anti-enumeration]] — Veja também: Ory Kratos Fluxos de `Recovery` e `Verification`: códigos OTP (`code`) vs `link`, `courier` SMTP/HTTP e prevenção de enumeração de contas.
- [[orykratos-social-sign-in-oidc-federation-jsonnet-data-mapping]] — Veja também: Ory Kratos Social Sign-In e Federação OIDC: mapeamento de claims de provedores externos (`Google`, `GitHub`, `Microsoft`, `GitLab`) via `Jsonnet`.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
