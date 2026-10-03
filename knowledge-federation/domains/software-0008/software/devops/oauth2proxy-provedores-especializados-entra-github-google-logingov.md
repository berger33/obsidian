---
id: software.devops.tranche11.001028
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md", "https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/", "https://github.com/oauth2-proxy/oauth2-proxy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Provedores especializados no OAuth2 Proxy: Google, Microsoft Entra ID, GitHub, login.gov e JWT Signing Keys

## Em uma frase
Além do cliente OIDC genérico, o OAuth2 Proxy inclui implementações especializadas de provedores para **Google**, **Microsoft Entra ID**, **GitHub**, **GitLab** e **login.gov**, capazes de consultar APIs específicas de cada plataforma para extrair nomes de usuário preferenciais, organizações, equipes e grupos, além de suportar assinatura de requisições com chave privada JWT (`--jwt-key` / `--jwt-key-file`).

## Por que importa
Alguns provedores OAuth2 (como o GitHub, que usa OAuth2 puro em vez de OIDC completo para login de aplicativos, ou o `login.gov`, que exige asserções JWT assinadas por chave privada PEM) não fornecem grupos ou identidade completa apenas pelo endpoint OIDC padrão. Os provedores especializados do OAuth2 Proxy encapsulam essas chamadas extras de API automaticamente.

## Como funciona
Conforme explicam o README oficial e a referência *General Provider Options* (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) o flag `--provider` seleciona o provedor (`google` por padrão, `oidc`, `entra-id`/`azure`, `github`, `gitlab`, `login.gov` etc.); (2) implementações especializadas consultam endpoints de perfil (`--profile-url`), resgate de token (`--redeem-url`) e APIs de membros/equipes para enriquecer os cabeçalhos HTTP de grupos e username; e (3) para provedores governamentais de alta segurança como o **`login.gov`**, o OAuth2 Proxy suporta `--jwt-key` (ou `--jwt-key-file=/etc/ssl/private/jwt_signing_key.pem`) e `--pubjwk-url` para assinar requisições de autenticação com uma chave privada PEM.

## Exemplo
```toml
# Configuração do OAuth2 Proxy usando provedor especializado e customizando o nome exibido na página de login
provider = "github"
provider_display_name = "GitHub Engenharia Corporativa"
client_id = "Iv1.1234567890abcdef"
client_secret_file = "/etc/oauth2-proxy/github-client-secret"
email_domains = ["*"]
```

## Limites e trade-offs
Ao utilizar o provedor padrão `--provider=google` sem sobrescrevê-lo explicitamente quando você na verdade deseja conectar ao Keycloak ou Dex, o OAuth2 Proxy tentará autenticar contra os endpoints do Google; sempre declare `provider = "oidc"` ao integrar com provedores OpenID Connect autogerenciados.

## Como verificar
Verifique o valor de `provider` e `provider_display_name` executando `oauth2-proxy --config=/etc/oauth2-proxy.cfg --config-test` e inspecionando a página HTML de login renderizada em `/oauth2/sign_in`.

## Conexões
- [[oauth2proxy-integracao-ingress-nginx-ext-authz-headers]] — Veja também: OAuth2 Proxy como Middleware de Ingress (NGINX auth-url / Envoy ext_authz) e repasse de cabeçalhos de identidade.
- [[oauth2proxy-controle-fluxo-login-prompt-acr-values-approval]] — Veja também: Controle do fluxo de autenticação no OAuth2 Proxy: --prompt, --approval-prompt, --acr-values e --auth-request-response-mode.
- [[oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2]] — Referência cruzada direta com oauth2proxy-proxy-reverso-middleware-autenticacao-oidc-oauth2.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Referência cruzada direta com oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks.
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Referência cruzada direta com dex-conectores-upstream-ldap-github-oidc-matriz-suporte.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
