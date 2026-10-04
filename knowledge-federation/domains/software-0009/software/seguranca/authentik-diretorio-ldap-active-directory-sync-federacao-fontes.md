---
id: software.seguranca.tranche14.001308
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

# Sincronização de Diretório (**LDAP Source / Active Directory**) e Federação OAuth/SAML no authentik: Coexistência e Migração Gradual de Legados

## Em uma frase
Como introduzir o authentik em uma empresa que já possui milhares de usuários e grupos no **Active Directory (AD)** ou **FreeIPA / OpenLDAP** sem obrigar os usuários a criarem novas contas do zero?

## Por que importa
Através das **Sources (*Fontes de Identidade*)** do authentik! Uma **`LDAP Source`** conecta o Worker do authentik via **LDAPS (`ldaps://ad.empresa.interna:636`)** ao seu Active Directory ou servidor LDAP e executa tarefas periódicas de sincronização (divididas em micro-tarefas paralelas por página para alta performance!) que importam **Usuários**, **Grupos** e atributos customizados via **LDAP Property Mappings**!

## Como funciona
E como funciona a autenticação da senha quando o usuário vem do Active Directory? Você pode escolher dois modos: **(1) Sincronização com Bind Direto no AD** (quando o usuário digita a senha no `Password Stage` do authentik, o authentik valida a senha fazendo um `LDAP Bind` em tempo real contra o Domain Controller do AD e logo em seguida aplica o MFA WebAuthn/TOTP do próprio authentik!); ou **(2) Migração Gradual de Senhas (*Password Writeback / Capture*)**, onde o authentik passa a assumir o hash da senha localmente para desligar o AD legado no futuro!

## Exemplo
```bash
# Consultar via API REST do authentik o status da sincronizacao de uma LDAP Source (Active Directory / FreeIPA)
curl -sk -H "Authorization: Bearer ${AUTHENTIK_TOKEN}" \
  "https://sso.exemplo.br/api/v3/sources/ldap/" | jq '.results[] | {name: .name, slug: .slug, enabled: .enabled, sync_users: .sync_users}'
```

## Limites e trade-offs
Ao conectar uma **`LDAP Source`** ao Active Directory, utilize sempre uma conta de serviço dedicada de **Somente Leitura (*Read-Only*)** (a menos que você habilite explicitamente `sync_users_password` para troca de senhas), conecte obrigatoriamente sobre **LDAPS (`:636`) ou StartTLS (`:389`) com verificação estrita do certificado da CA interna**!

## Como verificar
Para federar com provedores externos (Google Workspace, GitHub, Entra ID, Okta), configure uma **`OAuth Source`** ou **`SAML Source`** e defina a política de **`User Matching Mode`** como `Link to user with identical email` apenas se o provedor externo garantir que o endereço de e-mail já foi verificado (`email_verified == true`)!

## Conexões
- [[authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio]] — Veja também: Autenticação Resistente a Phishing no authentik: **WebAuthn / Passkeys (FIDO2)**, Restrição de **MDS Attestation (`AAUID`)**, TOTP e Códigos de Recuperação.
- [[authentik-auditoria-eventos-notificacoes-webhooks-siem-rbac]] — Veja também: Auditoria de Eventos de Segurança, **Notification Rules / Webhooks** e **RBAC Granular por Objeto** no authentik: Monitorando o IdP no SIEM.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Referência cruzada direta com authentik-providers-oauth2-oidc-saml-scim-federacao-sso.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
