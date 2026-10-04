---
id: software.seguranca.tranche02.000136
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

# Ory Kratos Segurança de Credenciais `password`: hashing `Argon2id` (ou `bcrypt`), política de similaridade e checagem *Have I Been Pwned* (`k-Anonymity`)

## Em uma frase
No método `password` do Ory Kratos, as senhas são armazenadas com hashing **Argon2id** (ou `bcrypt`) calibrado para o hardware do servidor e validadas no momento do cadastro/alteração contra: 1) comprimento mínimo e entropia; 2) distância de edição em relação aos identificadores do usuário (impedindo usar o próprio e-mail/nome como senha); e 3) a API de senhas vazadas do **Have I Been Pwned (HIBP)** via modelo de **k-Anonymity**.

## Por que importa
Regras antigas de complexidade ("1 letra maiúscula, 1 número e 1 símbolo") aceitam senhas como `Senha@123`, que já aparecem milhões de vezes em listas públicas de vazamentos (*credential stuffing*).

## Como funciona
Com a proteção HIBP por *k-Anonymity* ativa no Kratos (`max_breaches: 0`), a senha em texto claro ou seu hash completo **nunca sai do seu servidor**: o Kratos calcula o hash SHA-1 da senha, envia apenas os **5 primeiros caracteres hexadecimais** para a API Pwned Passwords e verifica localmente em memória se o sufixo consta na lista retornada!

## Exemplo
```yaml
selfservice:
  methods:
    password:
      enabled: true
      config:
        haveibeenpwned_enabled: true
        max_breaches: 0
        min_password_length: 12
        identifier_similarity_check_enabled: true
hashers:
  algorithm: argon2
  argon2:
    memory: 128MB
    iterations: 2
    parallelism: 4
```

## Limites e trade-offs
Em ambientes totalmente desconectados da internet (*air-gapped*), você pode apontar `haveibeenpwned_host` para um espelho interno ou desativar a checagem externa mantendo `min_password_length: 12` e `identifier_similarity_check_enabled: true`.

## Como verificar
Tente cadastrar um usuário de teste com a senha `Password123!` e confirme que o Kratos rejeita a senha por constar em vazamentos conhecidos.

## Conexões
- [[orykratos-mfa-aal1-aal2-webauthn-passkeys-totp-lookup-secrets]] — Veja também: Ory Kratos Multi-Factor Authentication (`AAL1` vs `AAL2`): `Passkeys`, `WebAuthn` (FIDO2), `TOTP` e `lookup_secret` (códigos de backup).
- [[orykratos-recovery-verification-one-time-codes-link-anti-enumeration]] — Veja também: Ory Kratos Fluxos de `Recovery` e `Verification`: códigos OTP (`code`) vs `link`, `courier` SMTP/HTTP e prevenção de enumeração de contas.

## Fontes
- [Ory Kratos GitHub — README.md (Headless Cloud-Native Identity & User Management, Self-Service Flows, Credentials & JSON Schema Traits)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/kratos apresentando o sistema headless de gerenciamento de identidades, fluxos de autoatendimento e suporte a Passkeys/WebAuthn, OIDC e TOTP; consultado em 2026-10-03.
- [Ory Kratos Official Documentation — Manage Identities Overview (Identity Data Model, Traits, JSON Schema Validation, Credentials & Lifecycle States)](https://www.ory.com/docs/kratos/manage-identities/overview) — Documentação oficial de gerenciamento de identidades do Ory Kratos detalhando a estrutura de uma Identity, validação por JSON Schema, metadados público/admin e credenciais; consultado em 2026-10-03.
- [Ory Kratos — Official GitHub Repository](https://github.com/ory/kratos) — Repositório oficial Apache-2.0 do Ory Kratos; consultado em 2026-10-03.
