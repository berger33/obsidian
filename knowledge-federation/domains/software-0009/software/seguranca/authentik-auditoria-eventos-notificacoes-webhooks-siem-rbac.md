---
id: software.seguranca.tranche14.001309
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/goauthentik/authentik/main/README.md", "https://docs.goauthentik.io/docs/core/architecture"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Eventos de Segurança, **Notification Rules / Webhooks** e **RBAC Granular por Objeto** no authentik: Monitorando o IdP no SIEM

## Em uma frase
Como o **Identity Provider (IdP)** é a "joia da coroa" da infraestrutura de segurança, toda ação administrativa ou anomalia de autenticação (como falha de login `login_failed`, criação de usuário `model_created`, alteração de política `policy_execution`, emissão de token `authorize_application`, erro de configuração ou impersonação de usuário `user_impersonated`) precisa ser auditada e enviada em tempo real para o SIEM/SOC!

## Por que importa
O authentik possui um subsistema nativo de **Events & Notifications**: cada evento registrado no banco e emitido em JSON no `stdout` dos containers (pronto para coleta via Vector/FluentBit/Loki/OpenSearch!) passa por **Notification Rules** baseadas em **Event Matcher Policies**!

## Como funciona
Quando uma **Event Matcher Policy** detecta um evento crítico (por exemplo, `Action = Login Failed` repetido ou `Action = User Impersonated` ou modificação em uma `Expression Policy`), o Worker dispara imediatamente uma notificação via **Webhook JSON** (para Slack, Microsoft Teams, PagerDuty ou SOAR) ou e-mail para a equipe de Segurança!

## Exemplo
```bash
# Consultar via API REST do authentik os ultimos eventos de seguranca do tipo 'login_failed' ou 'user_impersonated'
curl -sk -H "Authorization: Bearer ${AUTHENTIK_TOKEN}" \
  "https://sso.exemplo.br/api/v3/events/events/?action=login_failed&ordering=-created" | jq '.results[:5]'
```

## Limites e trade-offs
Além da auditoria de eventos, utilize o sistema de **RBAC (*Role-Based Access Control*) com Permissões por Objeto** do authentik para eliminar o uso de contas `Superuser` globais no dia a dia: você pode criar um Role `Helpdesk-MFA-Reset` que tem permissão exclusivamente para visualizar usuários e remover dispositivos TOTP perdidos, sem permissão para editar Flows, Providers ou políticas!

## Como verificar
Desabilite a funcionalidade de **Impersonation (*Personificação de Usuário*)** nas configurações globais ou restrinja a permissão `Can impersonate other users` com um alerta imediato de severidade crítica no SIEM toda vez que o evento `user_impersonated` ocorrer.

## Conexões
- [[authentik-diretorio-ldap-active-directory-sync-federacao-fontes]] — Veja também: Sincronização de Diretório (**LDAP Source / Active Directory**) e Federação OAuth/SAML no authentik: Coexistência e Migração Gradual de Legados.
- [[authentik-hardening-producao-secret-key-reverse-proxy-tls-backups]] — Veja também: Hardening de Produção do **authentik**: Proteção da **`AUTHENTIK_SECRET_KEY`**, Configuração de `trusted_proxies`, Isolamento de Outposts e Backups.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[authentik-politicas-reputacao-ip-expressoes-python-rbac-abac]] — Referência cruzada direta com authentik-politicas-reputacao-ip-expressoes-python-rbac-abac.
- [[gophish-webhooks-integracao-soar-slack-automacao-api-rest]] — Referência cruzada direta com gophish-webhooks-integracao-soar-slack-automacao-api-rest.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
