---
id: software.seguranca.tranche02.000129
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

# Ory Hydra em Produção: `hydra migrate sql`, limpeza de tokens expirados com `hydra janitor` e escalabilidade stateless

## Em uma frase
Para operar o Ory Hydra em produção sobre **PostgreSQL**, **CockroachDB** ou **MySQL**, o ciclo operacional exige rodar migrações explícitas de schema (**`hydra migrate sql`**) antes do deploy e agendar a execução periódica do comando **`hydra janitor`** para expurgar tokens expirados, códigos de autorização consumidos e fluxos de login/consent antigos.

## Por que importa
Como cada fluxo OAuth2 grava registros de `login_challenge`, `consent_challenge`, `authorization_code` e tokens no banco relacional, operar meses sem rodar o `hydra janitor` faz as tabelas crescerem indefinidamente e degradarem a latência.

## Como funciona
O comando `hydra janitor` suporta flags de controle fino (`--tokens`, `--requests`, `--grants`, `--batch-size`, `--limit`) para remover registros expirados em pequenos lotes sem causar contention de locks nas transações em tempo real.

## Exemplo
```bash
# 1. Aplicando migrações de schema do banco de dados de forma segura:
hydra migrate sql -e --yes

# 2. Executando o job de limpeza (Janitor) em lotes controlados via CronJob do Kubernetes:
hydra janitor --tokens --requests --grants --batch-size 100 --limit 10000 --read-from-env
```

## Limites e trade-offs
Nunca execute o servidor Hydra em produção com `--dangerous-force-http`; exija TLS ponta-a-ponta ou terminação TLS segura no Ingress com cabeçalhos `X-Forwarded-Proto: https` validados.

## Como verificar
Monitore as métricas Prometheus do Hydra e o tamanho das tabelas `hydra_oauth2_*` após a execução do `hydra janitor`.

## Conexões
- [[oryhydra-deteccao-reuso-refresh-token-rotacao-mitigacao-roubo]] — Veja também: Ory Hydra Segurança de `Refresh Tokens`: rotação automática a cada uso e invalidação de toda a família em caso de *Replay*.
- [[oryhydra-integracao-ory-kratos-arquitetura-idp-completo-drop-in]] — Veja também: Ory Hydra + Ory Kratos: arquitetura combinada de Identidade (`Kratos`) e Provedor OAuth2/OIDC (`Hydra`) como substituto de Auth0/Okta.

## Fontes
- [Ory Hydra GitHub — README.md (Cloud Native OAuth 2.0 & OpenID Connect Certified Server, RFC Implementations & Headless Design)](https://raw.githubusercontent.com/ory/hydra/master/README.md) — README oficial do ory/hydra documentando a arquitetura headless OAuth 2.0 e OpenID Connect Certified, especificações IETF/OIDC suportadas e separação de responsabilidades; consultado em 2026-10-03.
- [Ory Official Documentation — Custom Login & Consent Flow (login_challenge, consent_challenge, Accept/Reject Admin APIs, remember & prompt=none)](https://www.ory.com/docs/oauth2-oidc/custom-login-consent/flow) — Documentação oficial do fluxo de Login e Consentimento do Ory Hydra detalhando os desafios criptográficos, chamadas Admin API e sessões SSO; consultado em 2026-10-03.
- [Ory Hydra — Official GitHub Repository](https://github.com/ory/hydra) — Repositório oficial Apache-2.0 do Ory Hydra; consultado em 2026-10-03.
