---
id: software.seguranca.tranche14.001321
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

# Arquitetura do **Vaultwarden (`dani-garcia/vaultwarden`)**: Servidor Alternativo **Bitwarden** em **Rust**, Criptografia **Zero-Knowledge Client-Side** e Bancos SQLite/PostgreSQL

## Em uma frase
Quando uma equipe de Engenharia, DevSecOps ou empresa inteira precisa de um **Gerenciador de Senhas e Segredos Self-Hosted** compatível com todos os aplicativos oficiais **Bitwarden** (Desktop, Mobile iOS/Android, Extensões de Navegador e CLI `bw`), mas sem o alto consumo de memória RAM e a dezena de containers .NET/MSSQL exigidos pelo servidor Bitwarden oficial, qual é a solução open-source padrão mundial?

## Por que importa
O **Vaultwarden** (anteriormente conhecido como `bitwarden_rs`)! Escrito em **Rust** sobre o framework web **Rocket** e o ORM **Diesel** (suportando **SQLite3 com WAL ativado por padrão**, **PostgreSQL** ou **MySQL/MariaDB**), um único container do Vaultwarden consome cerca de **15 a 30 MB de memória RAM** e implementa a quase totalidade da API de cliente do Bitwarden — incluindo Cofres Pessoais, **Organizations & Collections**, **Bitwarden Send**, **Anexos**, **Emergency Access**, **2FA (FIDO2 WebAuthn, YubiKey, TOTP, Duo)** e **SSH Agent**!

## Como funciona
Fundamentalmente, o modelo criptográfico é **100% Zero-Knowledge Client-Side**: toda derivação de chave (`Argon2id` ou `PBKDF2-SHA256`) e cifragem (`AES-256-CBC` + `HMAC-SHA256`) ocorre **exclusivamente nos dispositivos clientes antes do envio pela rede**, de modo que o servidor Vaultwarden armazena apenas *ciphertexts* opacos e jamais conhece a Senha Mestra nem os segredos em texto claro!

## Exemplo
```bash
# Inspecionar o endpoint de saude (/alive) e a configuracao de versao de uma instancia Vaultwarden rodando sobre HTTPS
curl -sk https://cofre.exemplo.br/alive
curl -sk https://cofre.exemplo.br/api/config | jq .
```

## Limites e trade-offs
Requisito técnico inegociável da arquitetura Bitwarden/Vaultwarden: **o Web Vault exige obrigatoriamente `HTTPS` (TLS)**! Por quê? Porque os navegadores modernos bloqueiam a API criptográfica nativa **`window.crypto.subtle` (Web Crypto API)** em contextos inseguros (`http://`), impedindo a descriptografia client-side sem TLS!

## Como verificar
Para implantações de até centenas de usuários, o banco **SQLite3 (`db.sqlite3`) com `ENABLE_DB_WAL=true`** (Write-Ahead Logging) oferece performance extraordinária e backups atômicos triviais.

## Conexões
- [[vaultwarden-blindagem-painel-admin-token-argon2-phc-signups-allowed]] — Veja também: Hardening Crítico do **Vaultwarden**: Desabilitando Cadastros Abertos (**`SIGNUPS_ALLOWED=false`**), Convites e Protegendo o **`ADMIN_TOKEN` com Argon2id PHC**.
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Referência cruzada direta com vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
