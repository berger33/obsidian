---
id: software.devops.tranche11.001012
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
fontes: ["https://raw.githubusercontent.com/dexidp/dex/master/README.md", "https://dexidp.io/docs/getting-started/", "https://github.com/dexidp/dex"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ID Tokens no Dex: estrutura do JWT assinado, claims padrão (iss, sub, aud, email, groups) e consumo por Kubernetes e AWS STS

## Em uma frase
O principal artefato emitido pelo Dex é o **ID Token**, um JSON Web Token (JWT) assinado criptograficamente pelo Dex na resposta OAuth2 que atesta a identidade do usuário final por meio de claims padronizadas (`iss`, `sub`, `aud`, `exp`, `iat`, `email`, `email_verified`, `groups`, `name`) consumíveis diretamente pelo Kubernetes e pelo AWS STS.

## Por que importa
Em vez de usar tokens opacos que obrigam cada microsserviço a consultar um banco de dados de sessão a cada requisição, os ID Tokens assinados pelo Dex são autocontidos e verificáveis via chave pública (JWKS), permitindo que sistemas de infraestrutura os consumam como credenciais *service-to-service* ou *user-to-cluster*.

## Como funciona
Conforme mostra o README oficial do Dex, o payload JSON de um ID Token emitido contém: (1) **`iss`** (issuer URL do Dex, ex.: `http://127.0.0.1:5556/dex`); (2) **`sub`** (identificador único codificado pelo Dex combinando o ID do usuário upstream e o conector); (3) **`aud`** (o `client_id` da aplicação que autenticou o usuário, ex.: `example-app`); (4) **`exp`** e **`iat`** (timestamps Unix de expiração e emissão); (5) **`at_hash`** (hash do access token); e (6) claims de identidade como **`email`**, **`email_verified`**, **`name`** e a lista **`groups`** (ex.: `["admins", "developers"]`). Por seguir as especificações OpenID Connect Core 1.0, esses tokens são aceitos nativamente pelo plugin OIDC do **Kubernetes API Server** e pelo **AWS Security Token Service (AWS STS)** (`AssumeRoleWithWebIdentity`).

## Exemplo
```json
{
  "iss": "http://127.0.0.1:5556/dex",
  "sub": "CgcyMzQyNzQ5EgZnaXRodWI",
  "aud": "example-app",
  "exp": 1492882042,
  "iat": 1492795642,
  "email": "jane.doe@coreos.com",
  "email_verified": true,
  "groups": ["admins", "developers"],
  "name": "Jane Doe"
}
```

## Limites e trade-offs
Como os ID Tokens são JWTs assinados e validados localmente pelos consumidores até o timestamp `exp`, revogar o acesso de um usuário no diretório upstream não invalida instantaneamente um ID Token já emitido; por isso, mantenha o tempo de expiração dos ID Tokens curto e utilize *refresh tokens* para renová-los periodicamente contra o Dex.

## Como verificar
Decodifique o payload de um ID Token retornado pela aplicação de exemplo (`./bin/example-app`) usando `jq -R 'split(".") | .[1] | @base64d | fromjson'` para verificar as claims `iss`, `aud`, `email` e `groups`.

## Conexões
- [[dex-provedor-identidade-federado-openid-connect-cncf]] — Veja também: Dex: provedor de identidade federado OpenID Connect (CNCF) baseado em conectores upstream.
- [[dex-autenticacao-kubernetes-apiserver-kubelogin-crds]] — Veja também: Dex e Kubernetes: autenticação do API Server via plugin OIDC, armazenamento em CRDs e integração com kubelogin / kubectl.
- [[dex-conectores-upstream-ldap-github-oidc-matriz-suporte]] — Referência cruzada direta com dex-conectores-upstream-ldap-github-oidc-matriz-suporte.

## Fontes
- [Dex GitHub — README.md (ID Tokens, Kubernetes Authentication & Connectors Matrix)](https://raw.githubusercontent.com/dexidp/dex/master/README.md) — README oficial do dexidp/dex detalhando ID Tokens JWT, integração OIDC com Kubernetes e AWS STS, matriz de suporte de conectores (stable/beta/alpha) e alerta de segurança do conector SAML 2.0; consultado em 2026-10-03.
- [Dex Official Documentation — Getting Started (Container Images, Gomplate, DEX_EXPAND_ENV & Example App)](https://dexidp.io/docs/getting-started/) — Guia oficial Getting Started do Dex documentando imagens alpine e distroless, chart Helm, pré-processamento gomplate, expansão de variáveis de ambiente e validação com example-app; consultado em 2026-10-03.
- [Dex — Official GitHub Repository](https://github.com/dexidp/dex) — Repositório oficial do Dex; consultado em 2026-10-03.
