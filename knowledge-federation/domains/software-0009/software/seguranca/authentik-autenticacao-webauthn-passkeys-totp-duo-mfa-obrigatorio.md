---
id: software.seguranca.tranche14.001307
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

# Autenticação Resistente a Phishing no authentik: **WebAuthn / Passkeys (FIDO2)**, Restrição de **MDS Attestation (`AAUID`)**, TOTP e Códigos de Recuperação

## Em uma frase
Como configurar o authentik para que os usuários possam fazer login **100% Passwordless usando Passkeys / Chaves FIDO2 (`YubiKey`)** ou para exigir que **apenas chaves de hardware certificadas corporativamente (via FIDO Metadata Service — MDS)** possam ser cadastradas pelos administradores?

## Por que importa
No authentik, o suporte a **WebAuthn / FIDO2** atua em dois estágios: **(1) `Authenticator WebAuthn Setup Stage`** (que controla o cadastro de novas chaves FIDO2/Passkeys pelo usuário) e **(2) `Authenticator Validation Stage`** (ou diretamente no `Identification Stage` para *Passkey-first login*!).

## Como funciona
No **`Authenticator WebAuthn Setup Stage`**, você pode configurar controles avançados de segurança de hardware: **`User verification = Required`** (exige PIN ou biometria no próprio autenticador FIDO2!), **`Resident key requirement = Required`** (cria uma *Discoverable Credential / Passkey* residente no chip para login sem digitar username!) e **`Authenticator Attachment = Cross-platform`** com filtro de **`Device Type Restrictions` (baseado no catálogo oficial *FIDO Alliance Metadata Service — MDS3*)**, permitindo restringir o cadastro exclusivamente a modelos homologados (como YubiKey 5 Series FIPS)!

## Exemplo
```bash
# Verificar no log de eventos ou via API REST do authentik os dispositivos WebAuthn/FIDO2 confirmados no tenant
curl -sk -H "Authorization: Bearer ${AUTHENTIK_TOKEN}" \
  "https://sso.exemplo.br/api/v3/authenticators/admin/webauthn/" | jq '.results[] | {name: .name, aaguid: .aaguid, last_used: .last_used}'
```

## Limites e trade-offs
Ao exigir MFA obrigatório em um `Authenticator Validation Stage` para todos os usuários, configure na seção **`Configuration stages`** o estágio de cadastro (`Setup Stage`): assim, se um funcionário novo fizer seu primeiro login e ainda não tiver uma chave WebAuthn/TOTP cadastrada, o authentik o força automaticamente a cadastrar o 2FA **dentro do próprio fluxo de primeiro login** antes de liberar o acesso a qualquer sistema (**Zero-Gap MFA Enrollment**)!

## Como verificar
Combine sempre o estágio WebAuthn com um `Authenticator Static Stage` para gerar códigos de backup de uso único impressos e guardados com segurança caso o usuário perca o token físico.

## Conexões
- [[authentik-blueprints-infraestrutura-como-codigo-gitops-automacao]] — Veja também: Identidade como Código (**Identity-as-Code**) no authentik com **Blueprints YAML**: Versionando Fluxos, Políticas, Provedores e RBAC via GitOps.
- [[authentik-diretorio-ldap-active-directory-sync-federacao-fontes]] — Veja também: Sincronização de Diretório (**LDAP Source / Active Directory**) e Federação OAuth/SAML no authentik: Coexistência e Migração Gradual de Legados.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[authentik-motor-flows-stages-bindings-autenticacao-contextual]] — Referência cruzada direta com authentik-motor-flows-stages-bindings-autenticacao-contextual.
- [[kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas]] — Referência cruzada direta com kanidm-autenticacao-passkeys-webauthn-attested-passkeys-politicas.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
