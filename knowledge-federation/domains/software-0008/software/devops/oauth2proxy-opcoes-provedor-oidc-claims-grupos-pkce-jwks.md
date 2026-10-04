---
id: software.devops.tranche11.001024
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

# Configuração OIDC no OAuth2 Proxy: claims customizadas (aud, email, groups), --allowed-group, PKCE (S256) e validação JWKS

## Em uma frase
Ao operar com provedores OpenID Connect, o OAuth2 Proxy permite restringir o login a grupos específicos (`--allowed-group`), usar desafios **PKCE (`--code-challenge-method=S256`)**, mapear claims customizadas (`--oidc-email-claim`, `--oidc-groups-claim`, `--oidc-audience-claim`), adicionar audiências extras (`--oidc-extra-audience`) e restringir algoritmos de assinatura JWT (`--oidc-enabled-signing-alg`).

## Por que importa
Nem todo provedor OIDC utiliza os mesmos nomes de claims ou emite tokens apenas para um único `client_id`. Além disso, autenticar um usuário no IdP não significa que ele deva ter acesso a um painel crítico de produção: combinar `--allowed-group` com `--code-challenge-method=S256` garante autorização por grupo na borda e proteção contra interceptação de código de autorização.

## Como funciona
Conforme a tabela *General Provider Options* da documentação oficial (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) **`--allowed-group`** (`allowed_groups` no TOML) restringe o login aos membros dos grupos listados e, caso `scope` não tenha sido definido explicitamente no provedor OIDC genérico, adiciona implicitamente o escopo `groups`; (2) **`--code-challenge-method=S256`** ativa PKCE no fluxo OAuth2; (3) **`--oidc-issuer-url`** define o issuer para descoberta automática (ou pode-se usar `--oidc-jwks-url` / `--oidc-public-key-file` quando a descoberta OIDC está desativada); (4) **`--oidc-groups-claim`** (padrão `"groups"`), **`--oidc-email-claim`** (padrão `"email"`) e **`--oidc-audience-claim`** (padrão `"aud"`) selecionam quais claims do token contêm cada dado; e (5) **`--client-secret-file`** permite ler o segredo do cliente de um arquivo montado (que deve conter apenas o segredo, sem quebra de linha final).

## Exemplo
```toml
# Trecho de arquivo oauth2-proxy.cfg configurando provedor OIDC com PKCE S256 e restrição de grupos
provider = "oidc"
oidc_issuer_url = "https://auth.exemplo.com/realms/plataforma"
client_id = "painel-sre"
client_secret_file = "/var/run/secrets/oauth2-proxy/client-secret"
code_challenge_method = "S256"
oidc_groups_claim = "groups"
allowed_groups = ["sre-prod", "platform-admins"]
```

## Limites e trade-offs
Preste atenção especial ao requisito documentado para `--client-secret-file`: o arquivo deve conter apenas o segredo **sem quebra de linha no final** (*with no trailing newline*); se você criar o arquivo com `echo "segredo" > file` em vez de `echo -n "segredo" > file`, o `\n` será lido como parte da senha e causará erro `invalid_client` no provedor OIDC.

## Como verificar
Verifique que o arquivo de segredo não possui newline (`xxd /var/run/secrets/oauth2-proxy/client-secret`) e teste o login com um usuário fora de `allowed_groups` para confirmar o bloqueio HTTP `403 Forbidden`.

## Conexões
- [[oauth2proxy-geracao-cookie-secret-aes-sessoes]] — Veja também: Geração segura do Cookie Secret no OAuth2 Proxy para criptografia AES de sessões.
- [[oauth2proxy-flags-seguranca-oidc-nonce-issuer-ca-files]] — Veja também: Segurança de validação OIDC no OAuth2 Proxy: verificação de nonce, email verificado, issuer multi-tenant e CAs privadas.
- [[oauth2proxy-precedencia-configuracao-cli-env-toml-config-test]] — Referência cruzada direta com oauth2proxy-precedencia-configuracao-cli-env-toml-config-test.
- [[keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf]] — Referência cruzada direta com keycloak-gerenciamento-identidade-acesso-oidc-saml-cncf.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
