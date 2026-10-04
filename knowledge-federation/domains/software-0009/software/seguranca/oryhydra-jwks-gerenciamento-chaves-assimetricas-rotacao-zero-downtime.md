---
id: software.seguranca.tranche02.000126
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

# Ory Hydra Gerenciamento e Rotação de Chaves Criptográficas (`JWKS`): conjuntos `hydra.openid.id-token` e `hydra.jwt.access-token`

## Em uma frase
O Ory Hydra inclui um gerenciador completo de **JSON Web Key Sets (JWKS)** na API Administrativa (`/admin/keys/{set}`) e na CLI (`hydra create jwk`), armazenando as chaves privadas criptografadas no banco de dados (usando `secrets.system` AES-GCM) e publicando as chaves públicas em `/.well-known/jwks.json`.

## Por que importa
Rotacionar a chave privada de assinatura de tokens OIDC substituindo a chave antiga de uma só vez invalida instantaneamente todos os `id_token` e `access_token` JWT emitidos nos últimos minutos que ainda estão em posse dos clientes.

## Como funciona
Ao executar `hydra create jwk hydra.openid.id-token --alg RS256` (ou `ES256`), o Hydra adiciona a nova chave como primária no início do conjunto (usada para assinar novos tokens) enquanto **mantém a chave pública anterior no `/.well-known/jwks.json`** pelo período de transição até que os tokens antigos expirem, permitindo rotação com zero downtime!

## Exemplo
```bash
# Rotacionando o par de chaves assimétricas ES256 usado para assinar ID Tokens no Ory Hydra:
hydra create jwk hydra.openid.id-token \
  --endpoint http://localhost:4445 \
  --alg ES256 \
  --use sig
```

## Limites e trade-offs
A variável `secrets.system` (mínimo de 16 caracteres, recomendado 32 bytes aleatórios) cifra as chaves JWKS no banco; o Hydra suporta múltiplos segredos em `secrets.system` para permitir a rotação da própria chave de criptografia em repouso!

## Como verificar
Consulte `curl -sS http://localhost:4444/.well-known/jwks.json | jq '.keys[].kid'` para verificar as chaves públicas expostas.

## Conexões
- [[oryhydra-client-credentials-rfc6749-rfc7523-jwt-bearer-m2m]] — Veja também: Ory Hydra Autenticação Machine-to-Machine (`M2M`): `client_credentials` (`RFC 6749`) e `jwt-bearer` (`RFC 7523`).
- [[oryhydra-oidc-frontchannel-backchannel-logout-revogacao-sessao]] — Veja também: Ory Hydra Logout Federado OpenID Connect: `RP-Initiated`, `Front-Channel Logout 1.0` e `Back-Channel Logout 1.0`.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
