---
id: software.devops.tranche11.001025
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
fontes: ["https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/", "https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md", "https://github.com/oauth2-proxy/oauth2-proxy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Segurança de validação OIDC no OAuth2 Proxy: verificação de nonce, email verificado, issuer multi-tenant e CAs privadas

## Em uma frase
O OAuth2 Proxy expõe controles granulares para a validação criptográfica e semântica de ID Tokens OIDC, incluindo `--insecure-oidc-skip-nonce`, `--insecure-oidc-allow-unverified-email`, `--insecure-oidc-skip-issuer-verification`, `--provider-ca-file` e `--backend-logout-url`.

## Por que importa
Em ambientes corporativos com autoridades certificadoras (CAs) privadas internas ou provedores multi-tenant (como Azure AD / Entra ID multi-tenant), a validação TLS ou a comparação estrita do campo `iss` pode falhar. Por outro lado, habilitar flags `--insecure-oidc-*` sem entender suas implicações reduz garantias importantes do protocolo OpenID Connect.

## Como funciona
Segundo a tabela *General Provider Options* (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) **`--provider-ca-file`** (`provider_ca_files` no TOML) especifica caminhos para certificados CA em formato PEM confiáveis ao conectar-se ao provedor OIDC interno (substituindo o bundle padrão do Go); (2) **`--insecure-oidc-allow-unverified-email`** (padrão `false`) impede que o login falhe quando a claim `email_verified` do ID Token é `false`; (3) **`--insecure-oidc-skip-issuer-verification`** (padrão `false`) permite que a URL `iss` do token difira da esperada (necessário apenas em cenários específicos de compatibilidade multi-tenant); (4) **`--insecure-oidc-skip-nonce`** (cujo padrão histórico é `true`, podendo ser definido como `false` para exigir verificação estrita da claim `nonce`); e (5) **`--backend-logout-url`** permite configurar a URL de logout no provedor, substituindo o placeholder `{id_token}` pelo `id_token` real da sessão do usuário.

## Exemplo
```toml
# Configurar CA privada para o provedor OIDC, exigir verificação estrita de nonce e habilitar logout federado com {id_token}
provider = "oidc"
oidc_issuer_url = "https://dex.interno.exemplo.com/dex"
provider_ca_files = ["/etc/ssl/certs/ca-corporativa.pem"]
insecure_oidc_skip_nonce = false
insecure_oidc_allow_unverified_email = false
backend_logout_url = "https://auth.interno.exemplo.com/realms/corp/protocol/openid-connect/logout?id_token_hint={id_token}"
```

## Limites e trade-offs
Nunca utilize `--insecure-oidc-allow-unverified-email=true` em provedores públicos ou quando a autorização na aplicação upstream é baseada no endereço de e-mail ou domínio de e-mail, pois um usuário poderia cadastrar uma conta com um e-mail ainda não verificado de outro domínio e obter acesso indevido.

## Como verificar
Execute `oauth2-proxy --config=/etc/oauth2-proxy.cfg --config-test` e verifique nos logs do proxy a negociação TLS bem-sucedida usando o certificado listado em `provider_ca_files`.

## Conexões
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Veja também: Configuração OIDC no OAuth2 Proxy: claims customizadas (aud, email, groups), --allowed-group, PKCE (S256) e validação JWKS.
- [[oauth2proxy-imagens-distroless-alpine-arquiteturas-seguranca]] — Veja também: Imagens de container e segurança do OAuth2 Proxy: migração para Distroless (v7.6.0+), tags -alpine e histórico de segurança.
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Referência cruzada direta com dex-id-tokens-jwt-claims-padrao-consumidores-sts.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
