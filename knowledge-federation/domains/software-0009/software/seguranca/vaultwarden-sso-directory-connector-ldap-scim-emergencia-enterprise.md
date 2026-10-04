---
id: software.seguranca.tranche14.001330
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

# Provisionamento Corporativo no Vaultwarden: **Bitwarden Directory Connector (LDAP / Active Directory / Entra ID / Okta)**, Notificações Push e Hardening de Container

## Em uma frase
Como automatizar a criação de grupos e o convite/remoção de usuários no **Vaultwarden** a partir do seu diretório central (**Active Directory, FreeIPA, Kanidm, Authentik, Entra ID ou Google Workspace**) sem precisar cadastrar cada colaborador manualmente?

## Por que importa
A API de Organizações do Vaultwarden é 100% compatível com o utilitário oficial open-source **Bitwarden Directory Connector (`bwdc` CLI / Desktop)**!

## Como funciona
Você autentica o `bwdc` na sua Organização do Vaultwarden usando a **Organization API Key (`organization.<uuid>`, habilitada no painel da Organização do Vaultwarden)** e o conecta ao seu servidor **LDAPS** (como Active Directory, FreeIPA ou Kanidm): o `bwdc` consulta os filtros LDAP de usuários e grupos, sincroniza automaticamente toda a árvore de **Groups** na Organização do Vaultwarden, envia convites para os novos contratados e **revoga automaticamente da Organização qualquer usuário desativado ou removido no LDAP**!

## Exemplo
```bash
# Testar e executar uma sincronizacao de grupos e usuarios entre o LDAP/AD e a Organizacao do Vaultwarden usando o Bitwarden Directory Connector (bwdc)
bwdc config server https://cofre.exemplo.br
bwdc test
bwdc sync
```

## Limites e trade-offs
Use sempre **`bwdc test`** antes da primeira execução de **`bwdc sync`** (especialmente ao habilitar a opção *Remove and re-add organization users* / *Overwrite existing*), pois o `bwdc test` simula a consulta no LDAP e imprime exatamente quais usuários e grupos seriam adicionados ou removidos sem alterar nada no Vaultwarden!

## Como verificar
No container de produção do Vaultwarden, rode sempre como **usuário não-root (`user: 1000:1000` no Docker Compose / `runAsNonRoot: true` no Kubernetes)** com `read_only: true` no rootfs (montando apenas `/data` gravável) e `cap_drop: [ALL]`.

## Conexões
- [[vaultwarden-backups-consistentes-sqlite3-online-backup-rsa-keys-anexos]] — Veja também: Estratégia de **Backup e Disaster Recovery** do Vaultwarden: Backup Online Atômico do **SQLite (`sqlite3 .backup`)**, Chaves **`rsa_key*`**, `attachments` e Criptografia **`age` / `GPG`**.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Referência cruzada direta com vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas.
- [[kanidm-gateway-ldaps-read-only-service-accounts-api-tokens]] — Referência cruzada direta com kanidm-gateway-ldaps-read-only-service-accounts-api-tokens.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
