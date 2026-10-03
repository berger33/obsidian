---
id: software.seguranca.tranche02.000125
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
fontes: ["https://raw.githubusercontent.com/ory/hydra/master/README.md", "https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow", "https://github.com/ory/hydra"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ory Hydra Autenticação Machine-to-Machine (`M2M`): `client_credentials` (`RFC 6749`) e `jwt-bearer` (`RFC 7523`)

## Em uma frase
Conforme listado nos padrões IETF implementados no README oficial do Hydra, para autenticação máquina-a-máquina (microsserviços, pipelines de CI/CD e integrações B2B sem usuário humano), o Hydra implementa o **Client Credentials Grant (`RFC 6749`)** e o **JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants (`RFC 7523`)**.

## Por que importa
Compartilhar chaves de API estáticas que nunca expiram entre dezenas de microsserviços ou parceiros B2B impede a rotação automatizada e dificulta revogar credenciais comprometidas.

## Como funciona
Com `grant_type=client_credentials` e autenticação de cliente via **`private_key_jwt`** (`RFC 7523`), o serviço cliente nunca envia um segredo simétrico pela rede: ele assina localmente um JWT de curta duração com sua chave privada e o Hydra verifica a assinatura contra a `jwks_uri` pública cadastrada no cliente antes de emitir o `access_token`.

## Exemplo
```bash
# Solicitando um token M2M via fluxo Client Credentials na porta pública (:4444) do Ory Hydra:
curl -sS -X POST "http://localhost:4444/oauth2/token" \
  -u "${CLIENT_ID}:${CLIENT_SECRET}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&scope=payments:read+payments:write"
```

## Limites e trade-offs
Use o hook de Webhooks de Token do Hydra (*Token Hook*) caso precise enriquecer tokens emitidos via `client_credentials` com claims dinâmicas de um serviço de permissões.

## Como verificar
Valide o token M2M emitido chamando o endpoint `/admin/oauth2/introspect`.

## Conexões
- [[oryhydra-estrategias-access-token-opaque-vs-jwt-token-introspection-rfc7662]] — Veja também: Ory Hydra Estratégias de Access Token (`opaque` vs `jwt`) e Token Introspection (`RFC 7662`).
- [[oryhydra-jwks-gerenciamento-chaves-assimetricas-rotacao-zero-downtime]] — Veja também: Ory Hydra Gerenciamento e Rotação de Chaves Criptográficas (`JWKS`): conjuntos `hydra.openid.id-token` e `hydra.jwt.access-token`.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
