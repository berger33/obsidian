---
id: software.seguranca.tranche14.001322
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

# Hardening Crítico do **Vaultwarden**: Desabilitando Cadastros Abertos (**`SIGNUPS_ALLOWED=false`**), Convites e Protegendo o **`ADMIN_TOKEN` com Argon2id PHC**

## Em uma frase
Quais são os dois maiores erros de configuração que um administrador pode cometer ao colocar uma instância do **Vaultwarden** no ar? **(1) Deixar o cadastro público aberto (`SIGNUPS_ALLOWED=true`)** permitindo que desconhecidos na internet criem contas no seu servidor; e **(2) Definir um `ADMIN_TOKEN` em texto claro fraco ou deixar a rota `/admin` exposta para a Internet pública**!

## Por que importa
No arquivo `.env` (ou variáveis de ambiente do container) do Vaultwarden, aplique imediatamente três travas de segurança: **(1) `SIGNUPS_ALLOWED=false`** (e opcionalmente `SIGNUPS_DOMAINS_WHITELIST=empresa.exemplo.br` + `SIGNUPS_VERIFY=true` se quiser permitir auto-cadastro restrito exclusivamente a e-mails verificados do domínio da empresa!); **(2) `INVITATIONS_ALLOWED=true`** (para que apenas administradores da Organização possam convidar novos funcionários!); e **(3) Hash `Argon2id` no formato PHC para o `ADMIN_TOKEN`**!

## Como funciona
Em vez de colocar a senha do painel `/admin` em texto claro na variável `ADMIN_TOKEN`, execute o subcomando nativo **`vaultwarden hash`** (que gera uma string PHC **`$argon2id$v=19$m=65540,t=3,p=4$...`**) — ou, melhor ainda, quando não estiver usando o painel `/admin`, remova a variável `ADMIN_TOKEN` (ou defina `DISABLE_ADMIN_TOKEN=false` e bloqueie `/admin` no Proxy Reverso para aceitar apenas IPs da VPN interna)!

## Exemplo
```bash
# Gerar um hash Argon2id seguro no formato PHC (OWASP recommended) usando o proprio binario do Vaultwarden para proteger o ADMIN_TOKEN
docker run --rm -it vaultwarden/server:latest /vaultwarden hash --preset owasp
```

## Limites e trade-offs
Atenção ao colocar o hash PHC `$argon2id$...` dentro de um arquivo **`docker-compose.yml`**: como o Docker Compose interpreta o caractere `$` como interpolação de variável, você deve **escapar cada `$` duplicando-o como `$$`** (`$$argon2id$$v=19$$...`) ou carregar o valor a partir de um arquivo `.env` entre aspas simples!

## Como verificar
Lembre-se também do comportamento documentado no `.env.template`: se você salvar configurações pela interface `/admin`, o Vaultwarden grava o arquivo **`data/config.json`**, cujos valores **têm precedência sobre as variáveis de ambiente do `.env`**!

## Conexões
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Veja também: Arquitetura do **Vaultwarden (`dani-garcia/vaultwarden`)**: Servidor Alternativo **Bitwarden** em **Rust**, Criptografia **Zero-Knowledge Client-Side** e Bancos SQLite/PostgreSQL.
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Veja também: Compartilhamento Corporativo no Vaultwarden: **Organizations**, **Collections**, Papéis RBAC (`Owner`, `Admin`, `Manager`, `User`), **Groups** e **Organization Policies**.
- [[vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting]] — Referência cruzada direta com vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
