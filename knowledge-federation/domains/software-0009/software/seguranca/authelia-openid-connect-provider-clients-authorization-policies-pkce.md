---
id: software.seguranca.tranche02.000149
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
fontes: ["https://www.authelia.com/configuration/security/access-control/", "https://raw.githubusercontent.com/authelia/authelia/master/README.md", "https://github.com/authelia/authelia"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Authelia como Provedor OpenID Connect 1.0 (`identity_providers.oidc`): proteção de aplicações nativas OIDC (Grafana, Argo CD, GitLab)

## Em uma frase
Além do modo ForwardAuth no proxy reverso, o Authelia inclui um **Provedor OpenID Connect 1.0 Certificado (`identity_providers.oidc`)** com suporte a *Authorization Code Flow*, **PKCE (`require_pkce` / `S256`)**, *Pushed Authorization Requests (PAR)*, *Device Authorization Grant* e **`authorization_policies`** específicas para OIDC.

## Por que importa
Conforme o alerta importante no topo da documentação oficial de *Access Control* do Authelia, a seção `access_control:` **não se aplica a fluxos OpenID Connect 1.0**! Para restringir quais grupos podem fazer login via OIDC em um `client_id` específico (ou exigir `one_factor` vs `two_factor`), você configura `authorization_policy` diretamente no cliente OIDC e em `identity_providers.oidc.authorization_policies`.

## Como funciona
Além disso, o `client_secret` cadastrado no `configuration.yml` para cada cliente OIDC deve ser sempre um **hash criptográfico** (gerado com `authelia crypto hash generate pbkdf2`), nunca o segredo em texto claro.

## Exemplo
```yaml
identity_providers:
  oidc:
    hmac_secret: '${AUTHELIA_OIDC_HMAC_SECRET}'
    jwks:
      - key_id: 'main-rs256'
        algorithm: 'RS256'
        use: 'sig'
        key: ${AUTHELIA_OIDC_JWKS_KEY}
    clients:
      - client_id: 'argocd'
        client_name: 'Argo CD Production'
        client_secret: '$pbkdf2-sha512$310000$...'
        public: false
        authorization_policy: 'two_factor'
        require_pkce: true
        pkce_challenge_method: 'S256'
        redirect_uris:
          - 'https://argocd.example.com/auth/callback'
        scopes:
          - 'openid'
          - 'profile'
          - 'groups'
          - 'email'
```

## Limites e trade-offs
Use `authelia crypto pair rsa generate` para gerar os pares de chaves JWKS e `authelia crypto hash generate pbkdf2 --variant sha512` para gerar o hash do `client_secret`.

## Como verificar
Consulte `https://auth.example.com/.well-known/openid-configuration` para verificar a descoberta OIDC do Authelia.

## Conexões
- [[authelia-regulation-protecao-forca-bruta-max-retries-find-time-ban-time]] — Veja também: Authelia `regulation`: proteção integrada contra ataques de força bruta com `max_retries`, `find_time` e `ban_time`.
- [[authelia-gestao-segredos-variaveis-ambiente-file-filters-templates-k8s]] — Veja também: Authelia Gestão Segura de Segredos (`_FILE` e Templates): injeção de credenciais via arquivos Kubernetes Secrets sem expor texto claro.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://www.authelia.com/configuration/security/access-control/) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
