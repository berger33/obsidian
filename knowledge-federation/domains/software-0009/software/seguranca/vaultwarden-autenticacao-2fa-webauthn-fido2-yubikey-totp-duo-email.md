---
id: software.seguranca.tranche14.001324
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md", "https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Autenticação Multifator (**2FA**) e Derivação de Chave (**Argon2id Client-Side**) no Vaultwarden: **FIDO2 WebAuthn**, **YubiKey OTP**, **TOTP** e **Duo**

## Em uma frase
Qual é a diferença fundamental entre: **(A) A Derivação da Chave Mestra no Cliente (`KDF: Argon2id` vs. `PBKDF2`)** e **(B) O Segundo Fator de Autenticação no Servidor (`2FA: FIDO2 WebAuthn`)** no Vaultwarden/Bitwarden, e por que ambos são indispensáveis?

## Por que importa
A distinção é essencial: **(B) O 2FA (FIDO2 WebAuthn, TOTP, YubiKey OTP, Duo)** é validado pelo **servidor Vaultwarden** antes de permitir que um cliente faça o download do cofre criptografado (`ciphertext`) pela API! Já **(A) O KDF (`Argon2id` com ex.: 64 MiB RAM, 3 iterações e 4 threads de paralelismo)** protege a **descriptografia local do cofre** caso alguém roube um backup do banco `db.sqlite3` ou o cache local de um dispositivo!

## Como funciona
Portanto, todo usuário do Vaultwarden deve: **(1) Ativar o 2FA baseado em `FIDO2 WebAuthn` (YubiKey / Passkey)** para proteger o login na API contra Phishing e Credential Stuffing; e **(2) Mudar nas configurações de Segurança da conta o algoritmo KDF padrão de `PBKDF2-SHA256` para `Argon2id`**!

## Exemplo
```bash
# Verificar no arquivo .env do Vaultwarden a configuracao de limite de tentativas de login/2FA (LOGIN_RATELIMIT_*) e expiracao de 2FA incompleto
grep -E "^(LOGIN_RATELIMIT|ADMIN_RATELIMIT|INCOMPLETE_2FA)" .env || true
```

## Limites e trade-offs
No arquivo `.env` do Vaultwarden, o recurso **`INCOMPLETE_2FA_TIME_LIMIT=3`** (em minutos, verificado pelo job `INCOMPLETE_2FA_SCHEDULE`) envia uma notificação de alerta imediata por e-mail ao dono da conta se alguém acertar a Senha Mestra da conta mas parar na tela de desafio do 2FA — **alertando o usuário em tempo real de que sua Senha Mestra vazou e precisa ser trocada imediatamente**!

## Como verificar
Configure também **`LOGIN_RATELIMIT_MAX_BURST=5`** e **`LOGIN_RATELIMIT_SECONDS=60`** no `.env` para limitar tentativas de força bruta na API de autenticação.

## Conexões
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Veja também: Compartilhamento Corporativo no Vaultwarden: **Organizations**, **Collections**, Papéis RBAC (`Owner`, `Admin`, `Manager`, `User`), **Groups** e **Organization Policies**.
- [[vaultwarden-compartilhamento-efemero-send-acesso-emergencia-anexos]] — Veja também: Compartilhamento Efêmero (**Bitwarden Send**) e **Emergency Access** no Vaultwarden: Eliminando Senhas no Slack/E-mail com Expiração e Contagem de Visualizações.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting]] — Referência cruzada direta com vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting.
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Referência cruzada direta com keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
