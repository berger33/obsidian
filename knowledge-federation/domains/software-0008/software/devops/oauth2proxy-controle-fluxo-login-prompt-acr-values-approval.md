---
id: software.devops.tranche11.001029
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

# Controle do fluxo de autenticação no OAuth2 Proxy: --prompt, --approval-prompt, --acr-values e --auth-request-response-mode

## Em uma frase
O OAuth2 Proxy permite ajustar os parâmetros enviados na requisição OAuth2/OIDC de autorização por meio das opções **`--prompt`**, **`--approval-prompt`**, **`--acr-values`** (Authentication Context Class Reference) e **`--auth-request-response-mode`**.

## Por que importa
Em sistemas críticos, a plataforma pode exigir que o provedor de identidade aplique um nível específico de autenticação multifator (`acr_values`), force o usuário a reautenticar-se ou selecionar a conta (`prompt=login` ou `select_account`), ou evite que o parâmetro legado `approval_prompt=force` cause erros em provedores OIDC estritos.

## Como funciona
De acordo com a tabela *General Provider Options* da documentação oficial (`oauth2-proxy.github.io/oauth2-proxy/configuration/overview/`): (1) **`--approval-prompt`** (`approval_prompt` no TOML) tem valor padrão `"force"`, que instrui provedores OAuth2 tradicionais a solicitar consentimento/refresh token; (2) **`--prompt`** (`prompt` no TOML, padrão `""`) implementa o parâmetro padrão do OpenID Connect Core 1.0 (`none`, `login`, `consent`, `select_account`) e, **quando `--prompt` está presente, `--approval-prompt` é automaticamente ignorado**; (3) **`--acr-values`** (`acr_values`) solicita níveis específicos de garantia de autenticação ao IdP; e (4) **`--auth-request-response-mode`** define o modo de resposta solicitado durante a requisição de autenticação.

## Exemplo
```toml
# Configurar o parâmetro OIDC prompt (que substitui automaticamente approval_prompt) e solicitar nível ACR de MFA
provider = "oidc"
oidc_issuer_url = "https://auth.exemplo.com/realms/corp"
prompt = "select_account"
acr_values = "phr"
```

## Limites e trade-offs
Alguns provedores OIDC rejeitam requisições de autorização que contenham simultaneamente `prompt` e `approval_prompt` ou não reconhecem `approval_prompt=force`; definir `prompt = "login"` ou `prompt = "consent"` no OAuth2 Proxy resolve essa incompatibilidade porque suprime o envio de `approval_prompt`.

## Como verificar
Inspecione a URL de redirecionamento gerada por `/oauth2/start` (`curl -sI http://localhost:4180/oauth2/start | grep -i location`) para confirmar a presença de `prompt=` e `acr_values=` na query string enviada ao IdP.

## Conexões
- [[oauth2proxy-provedores-especializados-entra-github-google-logingov]] — Veja também: Provedores especializados no OAuth2 Proxy: Google, Microsoft Entra ID, GitHub, login.gov e JWT Signing Keys.
- [[oauth2proxy-verificacao-assinatura-jwks-chaves-publicas-algoritmos]] — Veja também: Verificação de assinatura JWT no OAuth2 Proxy: --oidc-enabled-signing-alg, --oidc-jwks-url e --oidc-public-key-file.
- [[oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks]] — Referência cruzada direta com oauth2proxy-opcoes-provedor-oidc-claims-grupos-pkce-jwks.
- [[oauth2proxy-precedencia-configuracao-cli-env-toml-config-test]] — Referência cruzada direta com oauth2proxy-precedencia-configuracao-cli-env-toml-config-test.
- [[keycloak-padroes-modernos-seguranca-dpop-token-exchange-mcp]] — Referência cruzada direta com keycloak-padroes-modernos-seguranca-dpop-token-exchange-mcp.

## Fontes
- [OAuth2 Proxy GitHub — README.md (Architecture, Distroless & Alpine Images, Security & CNCF Sandbox)](https://oauth2-proxy.github.io/oauth2-proxy/configuration/overview/) — README oficial do oauth2-proxy/oauth2-proxy detalhando modos reverse proxy e middleware, migração para imagens base distroless na v7.6.0+, variantes -alpine e histórico de segurança; consultado em 2026-10-03.
- [OAuth2 Proxy Official Documentation — Configuration Overview (Precedence, Cookie Secret, --config-test & General Provider Options)](https://raw.githubusercontent.com/oauth2-proxy/oauth2-proxy/master/README.md) — Documentação oficial de configuração do OAuth2 Proxy (v7.15.x) cobrindo precedência CLI/Env/Config, geração de Cookie Secret AES, --config-test, PKCE S256, claims OIDC e flags de verificação; consultado em 2026-10-03.
- [OAuth2 Proxy — Official GitHub Repository](https://github.com/oauth2-proxy/oauth2-proxy) — Repositório oficial MIT do OAuth2 Proxy; consultado em 2026-10-03.
