---
id: software.devops.tranche11.001030
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

# Verificação de assinatura JWT no OAuth2 Proxy: --oidc-enabled-signing-alg, --oidc-jwks-url e --oidc-public-key-file

## Em uma frase
O OAuth2 Proxy restringe os algoritmos criptográficos aceitos na verificação de tokens JWT via **`--oidc-enabled-signing-alg`** (calculando a interseção com os algoritmos descobertos no provedor) e suporta verificação offline sem OIDC discovery por meio de **`--oidc-jwks-url`** ou arquivos PEM locais em **`--oidc-public-key-file`**.

## Por que importa
Restringir explicitamente os algoritmos de assinatura permitidos (por exemplo, exigindo apenas `RS256` ou `ES256`) previne ataques de downgrade de algoritmo, enquanto o suporte a chaves públicas PEM locais ou JWKS explícito viabiliza a operação do OAuth2 Proxy mesmo diante de emissores OIDC que não expõem um endpoint público `.well-known/openid-configuration`.

## Como funciona
Conforme especifica a tabela *General Provider Options* (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) **`--oidc-enabled-signing-alg`** (`oidc_enabled_signing_algs` no TOML) define a lista de algoritmos de assinatura JWT permitidos; quando a descoberta OIDC está habilitada, o conjunto efetivo de algoritmos aceitos é a **interseção** entre essa lista configurada e os algoritmos suportados anunciados pelo provedor; (2) **`--oidc-jwks-url`** (`oidc_jwks_url`) fornece a URI JWKS para verificação de tokens, sendo obrigatória se a descoberta OIDC estiver desabilitada e arquivos de chave pública não forem fornecidos; e (3) **`--oidc-public-key-file`** (`oidc_public_key_files`, que pode ser repetido múltiplas vezes) aponta para arquivos de chave pública em formato PEM no disco para validar a assinatura dos JWTs quando nem OIDC discovery nem JWKS URL são utilizados.

## Exemplo
```toml
# Restringir algoritmos de assinatura JWT aceitos no OAuth2 Proxy a RS256 e ES256
provider = "oidc"
oidc_issuer_url = "https://auth.exemplo.com/realms/corp"
oidc_enabled_signing_algs = ["RS256", "ES256"]
```

## Limites e trade-offs
Se a interseção entre `oidc_enabled_signing_algs` e o campo `id_token_signing_alg_values_supported` retornado pelo discovery endpoint do provedor for vazia, ou se você usar `oidc_public_key_files` estáticos e o IdP rotacionar suas chaves de assinatura sem atualizar o volume montado no pod, todas as validações de login falharão.

## Como verificar
Execute `oauth2-proxy --config=/etc/oauth2-proxy.cfg --config-test` e confira no documento `.well-known/openid-configuration` do seu IdP que o algoritmo configurado consta em `id_token_signing_alg_values_supported`.

## Conexões
- [[oauth2proxy-controle-fluxo-login-prompt-acr-values-approval]] — Veja também: Controle do fluxo de autenticação no OAuth2 Proxy: --prompt, --approval-prompt, --acr-values e --auth-request-response-mode.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Referência cruzada direta com oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks.
- [[oauth2proxy-flags-seguranca-oidc-nonce-issuer-ca-files]] — Referência cruzada direta com oauth2proxy-flags-seguranca-oidc-nonce-issuer-ca-files.
- [[dex-id-tokens-jwt-claims-padrao-consumidores-sts]] — Referência cruzada direta com dex-id-tokens-jwt-claims-padrao-consumidores-sts.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
