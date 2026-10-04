---
id: software.seguranca.tranche14.001303
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

# Motor de Políticas (**Policy Engine**) do authentik: **Expression Policies** em Python, **Reputation Policy** Anti-Brute-Force, GeoIP e HIBP

## Em uma frase
Como bloquear no authentik um acesso originado de um país inesperado (GeoIP), exigir reautenticação se o usuário tiver histórico de falhas recentes (**Reputation Policy**), proibir senhas vazadas no **HaveIBeenPwned** ou implementar uma regra de autorização **ABAC (*Attribute-Based Access Control*)** arbitrária?

## Por que importa
O **Policy Engine** do authentik avalia políticas vinculadas a **Aplicações** (controlando quem pode acessar qual sistema), a **Stage Bindings** (controlando quais etapas do fluxo rodam) e a **Grupos/Eventos**!

## Como funciona
Além das políticas prontas — como **`Reputation Policy`** (que rastreia scores negativos por endereço IP e por username a cada falha de login para bloquear ataques de força bruta e *Credential Stuffing*!), **`Password Policy`** e **`HaveIBeenPwned Policy`** (via k-Anonymity) — o diferencial supremo do authentik é a **`Expression Policy`**: um ambiente sandboxed em **Python** onde você tem acesso aos objetos `request` (`request.user`, `request.http_request`, `request.context`), `ak_is_group_member(request.user, name="...")` e `ak_logger`, podendo escrever qualquer lógica condicional booleana (`return True` / `return False`)!

## Exemplo
```python
# Exemplo de Expression Policy em Python no authentik: exige que o usuario pertenca ao grupo 'sre-prod' E tenha um dispositivo MFA WebAuthn registrado
from authentik.stages.authenticator_webauthn.models import WebAuthnDevice

if not ak_is_group_member(request.user, name="sre-prod"):
    ak_message("Acesso restrito aos engenheiros do grupo sre-prod.")
    return False

has_fido2 = WebAuthnDevice.objects.filter(user=request.user, confirmed=True).exists()
if not has_fido2:
    ak_message("Este sistema critico exige uma chave de seguranca FIDO2/WebAuthn cadastrada.")
    return False

return True
```

## Limites e trade-offs
Veja na *Expression Policy* acima como é simples impor **Phishing-Resistant MFA (FIDO2/WebAuthn)** apenas para aplicações críticas de produção consultando diretamente `WebAuthnDevice.objects.filter(user=request.user, confirmed=True).exists()`!

## Como verificar
Você pode testar qualquer política antes de colocá-la em produção clicando no botão **"Test"** ao lado da política na interface administrativa do authentik e selecionando um usuário e contexto simulados.

## Conexões
- [[authentik-motor-flows-stages-bindings-autenticacao-contextual]] — Veja também: O Motor de **Flows, Stages e Stage Bindings** no authentik: Construindo Jornadas de Autenticação, MFA Adaptativo, Enrollment e Recovery sem Código Fixo.
- [[authentik-providers-oauth2-oidc-saml-scim-federacao-sso]] — Veja também: Provedores **OAuth2 / OIDC**, **SAML 2.0** e **SCIM 2.0** no authentik: Assinatura de JWTs, Property Mappings (Scopes) e Provisionamento Automático de Ciclo de Vida.
- [[authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql]] — Referência cruzada direta com authentik-arquitetura-idp-core-embedded-outpost-worker-postgresql.
- [[keepassxc-auditoria-saude-senhas-hibp-k-anonymity-relatorios]] — Referência cruzada direta com keepassxc-auditoria-saude-senhas-hibp-k-anonymity-relatorios.

## Fontes
- [authentik Official GitHub Repository (`goauthentik/authentik`)](https://raw.githubusercontent.com/goauthentik/authentik/main/README.md) — repositório oficial do provedor de identidade open-source authentik cobrindo OAuth2/OIDC, SAML, LDAP, RADIUS, SCIM e Flows; consultado em 2026-10-03.
- [authentik Official Architecture Documentation (`docs.goauthentik.io/docs/core/architecture`)](https://docs.goauthentik.io/docs/core/architecture) — documentação arquitetural oficial do authentik detalhando Server (Go Router + Python/Django API), Workers, PostgreSQL, Outposts e Blueprints declarativos; consultado em 2026-10-03.
