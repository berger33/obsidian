---
id: software.seguranca.tranche03.000234
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
fontes: ["https://dexidp.io/docs/connectors/", "https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dex Conectores `GitHub` e `GitLab`: controle de acesso baseado em Organizações, Teams (`org:team`) e Grupos de engenharia

## Em uma frase
Os conectores **`github`** (`stable`) e **`gitlab`** (`beta`) do Dex permitem autenticar desenvolvedores usando suas identidades do GitHub (ou GitHub Enterprise) e GitLab, restringindo o login apenas a membros de **Organizações (`orgs`)** e **Equipes (`teams`)** específicas e populando automaticamente a claim `groups` do `id_token` no formato `<org>:<team>`!

## Por que importa
Se você configurar um OAuth App do GitHub sem restringir a propriedade **`orgs`** no conector do Dex, **qualquer conta pública do GitHub no mundo** conseguirá autenticar-se no Dex e obter um `id_token` válido!

## Como funciona
Declarando `orgs: [{name: "minha-empresa", teams: ["platform", "security"]}]` no conector `github`, o Dex consulta a API do GitHub durante o login, rejeita qualquer usuário que não pertença às equipes listadas e inclui `"groups": ["minha-empresa:platform", "minha-empresa:security"]` no JWT assinado.

## Exemplo
```yaml
connectors:
  - type: github
    id: github
    name: GitHub Corporativo
    config:
      clientID: $GITHUB_CLIENT_ID
      clientSecret: $GITHUB_CLIENT_SECRET
      redirectURI: https://dex.internal.corp/dex/callback
      orgs:
        - name: minha-org-engenharia
          teams:
            - platform-sre
            - appsec-team
      loadAllGroups: false
```

## Limites e trade-offs
Para que o Dex inclua as claims `groups` no token quando o cliente solicitar `scope: openid profile email groups`, garanta que a organização GitHub autorizou o OAuth App com permissão `read:org`.

## Como verificar
Teste o login com um usuário membro da equipe listada e um usuário externo à equipe, confirmando que o segundo é bloqueado no callback do Dex.

## Conexões
- [[dexidp-conector-ldap-active-directory-usersearch-groupsearch-starttls]] — Veja também: Dex Conector `LDAP` (`ldap`): integração segura com Active Directory / OpenLDAP via `userSearch`, `groupSearch` e `startTLS` / `rootCA`.
- [[dexidp-conector-oidc-upstream-okta-entra-google-alerta-saml]] — Veja também: Dex Conector `OIDC` Upstream vs Alerta de Segurança sobre o Conector `SAML 2.0`.

## Fontes
- [CNCF Dex GitHub — README.md (Federated OpenID Connect Provider, ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://dexidp.io/docs/connectors/) — README oficial do dexidp/dex detalhando a emissão de ID Tokens JWT, integração com Kubernetes/AWS STS e matriz de estabilidade e recursos dos conectores; consultado em 2026-10-03.
- [CNCF Dex Official Documentation — Connectors Reference (Upstream IdP Protocol Translation, Refresh Token & Groups Support)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — Documentação oficial de conectores do Dex cobrindo configuração de LDAP, GitHub, GitLab, OIDC e limitações de protocolo; consultado em 2026-10-03.
- [CNCF Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial Apache-2.0 do CNCF Dex; consultado em 2026-10-03.
