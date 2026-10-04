---
id: software.seguranca.tranche14.001328
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

# Automação com **Bitwarden CLI (`bw`)**, **Personal API Keys (`client_id` / `client_secret`)** e **SSH Agent** Conectados ao Vaultwarden

## Em uma frase
Como desenvolvedores e pipelines de automação autenticam programaticamente em uma instância do **Vaultwarden** sem precisar resolver desafios de CAPTCHA ou TOTP interativo, e como usar os clientes Desktop modernos com o Vaultwarden para servir chaves SSH via **`ssh-agent`**?

## Por que importa
Para automação em terminal e scripts (`bw` CLI), cada usuário ou conta de serviço gera no Web Vault do Vaultwarden (`Settings -> Security -> Keys`) a sua **Personal API Key (`client_id: user.<uuid>` e `client_secret`)**! Com `BW_CLIENTID` e `BW_CLIENTSECRET`, o comando `bw login --apikey` autentica a sessão na API, e `bw unlock --passwordenv BW_PASSWORD --raw` retorna o `BW_SESSION` efêmero em memória para ler segredos de Collections compartilhadas!

## Como funciona
Além disso, o Vaultwarden suporta os novos tipos de itens de **SSH Key** dos clientes Bitwarden Desktop modernos: você armazena suas chaves privadas `Ed25519` dentro do cofre sincronizado pelo Vaultwarden e habilita o **Bitwarden SSH Agent** local na estação!

## Exemplo
```bash
# Autenticar a Bitwarden CLI (bw) em uma instancia auto-hospedada do Vaultwarden usando API Key e extrair uma senha em memoria
bw config server https://cofre.exemplo.br
export BW_SESSION="$(bw unlock --passwordenv BW_PASSWORD --raw)"
bw get password "Postgres-Producao-Master" --session "$BW_SESSION"
bw lock
```

## Limites e trade-offs
Regra de segurança obrigatória em scripts que usam a CLI `bw`: **sempre execute `bw lock` (e `bw logout` em runners compartilhados) usando um `trap 'bw lock' EXIT` no shell script** para garantir que o cofre local seja trancado imediatamente mesmo que o script falhe no meio da execução!

## Como verificar
Quando um usuário rotaciona sua Senha Mestra ou clica em *"Deauthorize Sessions"* no Web Vault do Vaultwarden, o `security_stamp` da conta é alterado e todos os tokens JWT e sessões de CLI anteriores são invalidados instantaneamente.

## Conexões
- [[vaultwarden-auditoria-event-logs-retencao-monitoramento-siem-soc]] — Veja também: Logs de Auditoria Organizacional (**Event Logs**) e Retenção (`EVENTS_DAYS_RETAIN`) no Vaultwarden: Rastreando Acessos, Exportações de Cofre e Mudanças de Permissão.
- [[vaultwarden-backups-consistentes-sqlite3-online-backup-rsa-keys-anexos]] — Veja também: Estratégia de **Backup e Disaster Recovery** do Vaultwarden: Backup Online Atômico do **SQLite (`sqlite3 .backup`)**, Chaves **`rsa_key*`**, `attachments` e Criptografia **`age` / `GPG`**.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Referência cruzada direta com keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura.
- [[keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock]] — Referência cruzada direta com keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
