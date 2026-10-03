---
id: software.seguranca.tranche02.000128
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

# Ory Hydra Segurança de `Refresh Tokens`: rotação automática a cada uso e invalidação de toda a família em caso de *Replay*

## Em uma frase
No Ory Hydra, todo uso de um `refresh_token` no endpoint `/oauth2/token` (`grant_type=refresh_token`) realiza **rotação automática (*Refresh Token Rotation*)**: o token de atualização usado é invalidado e um novo par `(access_token, refresh_token)` é emitido dentro da mesma família de concessão.

## Por que importa
Se um invasor conseguir roubar um `refresh_token` do armazenamento local de um cliente e tentar utilizá-lo após o cliente legítimo já tê-lo rotacionado (ou vice-versa), um servidor sem detecção de reuso não perceberia que há duas partes usando a mesma cadeia.

## Como funciona
Quando o Ory Hydra detecta que um `refresh_token` **já consumido** está sendo apresentado novamente (*Refresh Token Replay Detection*, conforme recomenda a RFC 6819 / OAuth 2.0 Security Best Current Practice), ele assume que houve comprometimento da credencial e **revoga imediatamente toda a família de tokens ativa** daquela concessão, forçando nova autenticação interativa!

## Exemplo
```bash
# Renovando um Access Token via Refresh Token (o refresh_token antigo torna-se inválido imediatamente):
curl -fsS -X POST "https://auth.internal.corp/oauth2/token" \
  -u "${CLIENT_ID}:${CLIENT_SECRET}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token&refresh_token=${REFRESH_TOKEN}"
```

## Limites e trade-offs
Garanta no código do seu cliente que chamadas concorrentes de renovação de token usem um mutex/singleflight para não enviar o mesmo `refresh_token` duas vezes em paralelo e acionar a proteção anti-replay.

## Como verificar
Teste enviar o mesmo `refresh_token` duas vezes seguidas e confirme que a segunda chamada falha E invalida o novo token gerado na primeira.

## Conexões
- [[oryhydra-oidc-frontchannel-backchannel-logout-revogacao-sessao]] — Veja também: Ory Hydra Logout Federado OpenID Connect: `RP-Initiated`, `Front-Channel Logout 1.0` e `Back-Channel Logout 1.0`.
- [[oryhydra-operacao-producao-postgres-cockroachdb-migrate-janitor]] — Veja também: Ory Hydra em Produção: `hydra migrate sql`, limpeza de tokens expirados com `hydra janitor` e escalabilidade stateless.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
