---
id: software.seguranca.tranche14.001327
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

# Logs de Auditoria Organizacional (**Event Logs**) e Retenção (`EVENTS_DAYS_RETAIN`) no Vaultwarden: Rastreando Acessos, Exportações de Cofre e Mudanças de Permissão

## Em uma frase
Em ambientes corporativos sujeitos a auditorias **SOC 2, ISO 27001, PCI-DSS e LGPD**, os auditores e o SOC precisam responder com precisão: *"Quem visualizou ou copiou a senha do banco de produção na terça-feira às 15h? Algum usuário exportou o cofre da Organização (`Exported organization vault`) antes de pedir demissão? Quem alterou as permissões da Collection `Infra/Prod`?"*

## Por que importa
O Vaultwarden implementa nativamente o subsistema completo de **Organization Event Logs** do Bitwarden (`ORG_EVENTS_ENABLED=true`)!

## Como funciona
Quando habilitado no `.env`, o Vaultwarden grava na tabela `event` cada evento organizacional relevante com **Timestamp UTC, Usuário autor, Tipo de evento (mais de 50 códigos padronizados: `Item_Viewed`, `Item_Created`, `Item_Updated`, `Collection_Updated`, `OrganizationUser_Invited`, `Organization_PurgedVault`, `User_LoggedIn`, `User_FailedLogIn2fa`), Endereço IP e Tipo de Dispositivo (`Chrome Extension`, `CLI`, `Linux Desktop`)**!

## Exemplo
```bash
# Configurar no .env a ativacao dos Event Logs da Organizacao com retencao automatica de 365 dias e limpeza diaria via cron interno
cat << 'EOF' >> .env
ORG_EVENTS_ENABLED=true
EVENTS_DAYS_RETAIN=365
EVENT_CLEANUP_SCHEDULE="0 10 0 * * *"
EXTENDED_LOGGING=true
EOF
```

## Limites e trade-offs
Atenção ao detalhe documentado no `.env.template`: se **`EVENTS_DAYS_RETAIN`** for deixado em branco, os eventos da tabela `event` são mantidos indefinidamente e o job de limpeza `EVENT_CLEANUP_SCHEDULE` permanece desativado; defina `EVENTS_DAYS_RETAIN=365` (ou o prazo regulatório da sua empresa) para manter o banco enxuto!

## Como verificar
Crie no seu SIEM (Wazuh / OpenSearch) alertas de alta severidade para eventos de exportação em massa ou alteração de políticas organizacionais.

## Conexões
- [[vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting]] — Veja também: Arquitetura de Proxy Reverso, **WebSockets** e **`IP_HEADER`** no Vaultwarden: Sincronização Instantânea, Prevenção de IP Spoofing e **Fail2ban / CrowdSec**.
- [[vaultwarden-automacao-cli-bw-api-keys-ssh-agent-pipelines-devops]] — Veja também: Automação com **Bitwarden CLI (`bw`)**, **Personal API Keys (`client_id` / `client_secret`)** e **SSH Agent** Conectados ao Vaultwarden.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Referência cruzada direta com vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas.
- [[authentik-auditoria-eventos-notificacoes-webhooks-siem-rbac]] — Referência cruzada direta com authentik-auditoria-eventos-notificacoes-webhooks-siem-rbac.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
