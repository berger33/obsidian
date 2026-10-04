---
id: software.seguranca.tranche02.000147
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
fontes: ["https://raw.githubusercontent.com/authelia/authelia/master/README.md", "https://www.authelia.com/configuration/security/access-control/", "https://github.com/authelia/authelia"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Authelia Sessões e Persistência de Produção: `session.redis` (HA Sentinel/Cluster) e `storage.postgres` com `encryption_key`

## Em uma frase
Para operar o Authelia com múltiplas réplicas em alta disponibilidade, a arquitetura separa o **armazenamento de sessões voláteis (`session`)** — suportado em **Redis** (standalone, Redis Sentinel ou Redis Cluster) — do **armazenamento persistente de estado (`storage`)** — suportado em **PostgreSQL**, **MySQL/MariaDB** ou `local` (SQLite para instância única), protegido por uma **`encryption_key`** obrigatória.

## Por que importa
Como o `storage` guarda os segredos de dispositivos TOTP, chaves públicas/metadados WebAuthn, preferências de 2FA e logs de tentativas de login, armazenar esses segredos em texto claro no banco de dados permitiria que um vazamento de backup comprometesse o 2FA de todos os usuários.

## Como funciona
Por isso, o Authelia exige a configuração de **`storage.encryption_key`** (mínimo de 20 caracteres), usando-a para cifrar criptograficamente no banco todas as colunas sensíveis de segundo fator e tokens OAuth2/OIDC!

## Exemplo
```yaml
session:
  secret: '${AUTHELIA_SESSION_SECRET}'
  cookies:
    - domain: 'example.com'
      authelia_url: 'https://auth.example.com'
      expiration: '1h'
      inactivity: '15m'
  redis:
    host: 'redis-primary.internal'
    port: 6379

storage:
  encryption_key: '${AUTHELIA_STORAGE_ENCRYPTION_KEY}'
  postgres:
    address: 'tcp://pg-primary.internal:5432'
    database: 'authelia'
    username: 'authelia'
```

## Limites e trade-offs
Se precisar rotacionar a `storage.encryption_key` em um banco existente, utilize o subcomando dedicado **`authelia storage encryption change-key`** para recifrar todas as colunas com segurança.

## Como verificar
Execute `authelia storage schema-info --config configuration.yml` para verificar a versão do schema e o status de criptografia do banco.

## Conexões
- [[authelia-mfa-webauthn-passkeys-totp-duo-push-configuracao]] — Veja também: Authelia Segundo Fator (`2FA`): configuração de `WebAuthn` (FIDO2 / YubiKey / Passkeys), `TOTP` e notificações `Duo Push`.
- [[authelia-regulation-protecao-forca-bruta-max-retries-find-time-ban-time]] — Veja também: Authelia `regulation`: proteção integrada contra ataques de força bruta com `max_retries`, `find_time` e `ban_time`.

## Fontes
- [Authelia Official Documentation — Access Control Configuration (Rules Evaluation Order, 7 Specificity Dimensions, Policy Levels & Subject/Network/Method Matching)](https://raw.githubusercontent.com/authelia/authelia/master/README.md) — Documentação oficial do motor de Controle de Acesso do Authelia detalhando default_policy, políticas bypass/one_factor/two_factor/deny, avaliação sequencial e as 7 dimensões de especificidade; consultado em 2026-10-03.
- [Authelia GitHub — README.md (Open-Source Authentication & Authorization Server, ForwardAuth Reverse Proxy Integrations & OIDC Provider)](https://www.authelia.com/configuration/security/access-control/) — README oficial do authelia/authelia descrevendo a arquitetura SSO/2FA acoplada a proxies reversos e provedor OpenID Connect; consultado em 2026-10-03.
- [Authelia — Official GitHub Repository](https://github.com/authelia/authelia) — Repositório oficial Apache-2.0 do Authelia; consultado em 2026-10-03.
