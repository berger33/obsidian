---
id: software.seguranca.tranche03.000235
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/connectors/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex Conector `OIDC` Upstream vs Alerta de Segurança sobre o Conector `SAML 2.0`

## Em uma frase
Na tabela oficial de conectores do README do Dex (`dexidp/dex`), o conector **`oidc`** permite encadear o Dex a provedores OpenID Connect corporativos (como Okta, Microsoft Entra ID / Azure AD, Google Cloud Identity, Keycloak ou Salesforce), enquanto a linha do conector **`SAML 2.0`** traz um alerta explícito de segurança no README oficial: **`WARNING: Unmaintained and likely vulnerable to auth bypasses (#1884)`**!

## Por que importa
Em ambientes corporativos onde o provedor central (Okta, Entra ID, Keycloak, PingFederate) suporta tanto SAML 2.0 quanto OpenID Connect, escolher o conector `saml` no Dex por hábito legado expõe a autenticação a riscos documentados na biblioteca XML/SAML subjacente, além de perder suporte a `refresh_tokens` e `preferred_username`!

## Como funciona
Sempre prefira o conector **`oidc`** (ou **`microsoft`** para Entra ID) ao integrar o Dex com provedores de identidade corporativos modernos: além de evitar o parser SAML XML, o conector `oidc` suporta `refresh_tokens`, busca de `userInfo` e propagação de `groups`.

## Exemplo
```yaml
connectors:
  - type: oidc
    id: okta-oidc
    name: Okta SSO
    config:
      issuer: https://corp.okta.com
      clientID: $OKTA_OIDC_CLIENT_ID
      clientSecret: $OKTA_OIDC_CLIENT_SECRET
      redirectURI: https://dex.internal.corp/dex/callback
      scopes:
        - openid
        - profile
        - email
        - groups
      insecureEnableGroups: true
```

## Limites e trade-offs
No conector `oidc` do Dex, a flag `insecureEnableGroups: true` é necessária para instruir o Dex a repassar a claim `groups` recebida do IdP upstream; certifique-se de que você confia 100% nos nomes de grupos emitidos por aquele IdP upstream.

## Como verificar
Verifique na configuração do seu Dex que nenhum conector `type: saml` está em uso quando o provedor suporta `type: oidc`.

## Conexões
- [[dexidp-conectores-github-gitlab-orgs-teams-groups-filtragem]] — Veja também: Dex Conectores `GitHub` e `GitLab`: controle de acesso baseado em Organizações, Teams (`org:team`) e Grupos de engenharia.
- [[dexidp-staticclients-trustedpeers-cross-client-trust-aud-azp]] — Veja também: Dex `staticClients` e `trustedPeers`: delegação de tokens entre serviços (*Cross-Client Trust*) com claims `aud` e `azp`.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://dexidp.io/docs/connectors/) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
