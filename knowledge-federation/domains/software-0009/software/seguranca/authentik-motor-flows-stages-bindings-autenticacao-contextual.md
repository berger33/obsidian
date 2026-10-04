---
id: software.seguranca.tranche14.001302
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

# O Motor de **Flows, Stages e Stage Bindings** no authentik: Construindo Jornadas de Autenticação, MFA Adaptativo, Enrollment e Recovery sem Código Fixo

## Em uma frase
Em muitos provedores de identidade tradicionais, a sequência de telas de login (usuário -> senha -> 2FA) é rígida e difícil de adaptar para cenários como **Login Passwordless com Passkeys**, **Onboarding com aprovação de gestor** ou **Desafio de MFA apenas quando o IP de origem não é corporativo**.

## Por que importa
No authentik, toda interação com o usuário (login, logout, recuperação de senha, cadastro, consentimento OAuth2, configuração de autenticador) é modelada como um **Flow (*Fluxo*)** composto por uma sequência ordenada de **Stages (*Estágios*)** conectados por **Stage Bindings**!

## Como funciona
Existem mais de 20 tipos de **Stages** nativos que você encadeia como blocos de montar: **`Identification Stage`** (identifica o usuário por e-mail/username ou já dispara WebAuthn Passkey!), **`Password Stage`**, **`Authenticator Validation Stage`** (valida TOTP, WebAuthn FIDO2, Duo, SMS ou Static Tokens), **`User Login Stage`**, **`Consent Stage`**, **`Prompt Stage`** (cria formulários customizados) e **`Deny Stage`**! E o melhor: cada **Stage Binding** pode ter **Políticas (*Policies*)** anexadas que são avaliadas dinamicamente (`Evaluate when flow is planned` ou `Evaluate when stage is run`) para decidir em tempo real se aquele estágio deve ser executado ou pulado!

## Exemplo
```yaml
# Exemplo declarativo (Blueprint YAML) de um Stage Binding que anexa validacao obrigatoria de MFA WebAuthn/TOTP a um Flow de autenticacao
version: 1
entries:
  - model: authentik_flows.flowstagebinding
    attrs:
      target: !KeyOf flow-login-corporativo
      stage: !KeyOf stage-validacao-mfa-fido2
      order: 30
      evaluate_on_plan: true
      re_evaluate_policies: true
```

## Limites e trade-offs
Sempre marque a opção **`Re-evaluate policies` (`re_evaluate_policies: true`)** nos *Stage Bindings* que dependem da identidade do usuário recém-informada no `Identification Stage` anterior — pois no início do planejamento do fluxo (`evaluate_on_plan`), o authentik ainda não sabe qual usuário está tentando logar!

## Como verificar
Configure também no Flow a diretiva **`Compatibility mode`** ou proteção contra enumeração de contas para que usuários inexistentes vejam exatamente a mesma progressão visual de tela de um usuário real antes de receberem erro de credencial inválida.

## Conexões
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Veja também: Arquitetura do **authentik (`goauthentik/authentik`)**: Core Server, **Embedded Outpost** em Go, **Worker** Assíncrono e **PostgreSQL**.
- [[authentik-politicas-reputacao-ip-expressoes-python-rbac-abac]] — Veja também: Motor de Políticas (**Policy Engine**) do authentik: **Expression Policies** em Python, **Reputation Policy** Anti-Brute-Force, GeoIP e HIBP.
- [[authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio]] — Referência cruzada direta com authentik-autenticacao-webauthn-passkeys-totp-duo-mfa-obrigatorio.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
