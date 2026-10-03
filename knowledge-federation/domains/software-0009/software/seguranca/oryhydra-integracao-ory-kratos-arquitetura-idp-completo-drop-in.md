---
id: software.seguranca.tranche02.000130
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
fontes: ["https://raw.githubusercontent.com/ory/kratos/master/README.md", "https://raw.githubusercontent.com/ory/hydra/master/README.md", "https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Hydra + Ory Kratos: arquitetura combinada de Identidade (`Kratos`) e Provedor OAuth2/OIDC (`Hydra`) como substituto de Auth0/Okta

## Em uma frase
Conforme destacado na seção *Migrating from Auth0, Okta, and similar providers* dos READMEs oficiais do Ory, a combinação de **Ory Kratos** (gerenciamento de identidades, credenciais, MFA, passkeys e fluxos de autoatendimento) com **Ory Hydra** (servidor de autorização OAuth 2.0 e OpenID Connect) forma um provedor de identidade completo e nativo em nuvem.

## Por que importa
O Ory Kratos gerencia quem o usuário é (cadastro, login, recuperação de senha, verificação de e-mail, WebAuthn), mas não emite tokens OAuth2 para terceiros; já o Ory Hydra emite tokens OAuth2/OIDC certificados, mas delega o login de usuários.

## Como funciona
Integrando ambos nativamente (configurando `oauth2_provider.url` no Kratos apontando para a porta administrativa do Hydra), o Kratos atua diretamente como o *Login Provider* do Hydra, lidando com `login_challenge` automaticamente sem precisar escrever código de colagem customizado para autenticação!

## Exemplo
```yaml
# Trecho do kratos.yml integrando nativamente o Ory Kratos como provedor de login do Ory Hydra:
oauth2_provider:
  url: http://hydra-admin.identity.svc.cluster.local:4445
```

## Limites e trade-offs
Essa separação de responsabilidades permite usar sessões leves do Kratos (`/sessions/whoami`) para suas próprias aplicações first-party enquanto expõe OAuth2/OIDC padrão via Hydra para integrações externas e SSO.

## Como verificar
Teste iniciar um fluxo `/oauth2/auth` no Hydra e confirme o redirecionamento automático para o fluxo de login do Kratos com `?login_challenge=...`.

## Conexões
- [[oryhydra-operacao-producao-postgres-cockroachdb-migrate-janitor]] — Veja também: Ory Hydra em Produção: `hydra migrate sql`, limpeza de tokens expirados com `hydra janitor` e escalabilidade stateless.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/kratos/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
