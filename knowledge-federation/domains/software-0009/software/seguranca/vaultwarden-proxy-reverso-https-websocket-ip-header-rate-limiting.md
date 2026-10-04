---
id: software.seguranca.tranche14.001326
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

# Arquitetura de Proxy Reverso, **WebSockets** e **`IP_HEADER`** no Vaultwarden: Sincronização Instantânea, Prevenção de IP Spoofing e **Fail2ban / CrowdSec**

## Em uma frase
Por que a configuração correta da variável **`IP_HEADER`** no `.env` do Vaultwarden em conjunto com o seu Proxy Reverso (Nginx, Caddy, Traefik, HAProxy) é um requisito crítico de segurança?

## Por que importa
Porque quando o Vaultwarden roda atrás de um Proxy Reverso, todas as conexões TCP chegam do IP interno do proxy (ex.: `172.18.0.2`). Se você não configurar **`IP_HEADER=X-Real-IP`** (ou `X-Forwarded-For` / `CF-Connecting-IP` garantido pelo proxy!), o Vaultwarden achará que **todos os usuários da internet têm o mesmo IP `172.18.0.2`**: com isso, um único atacante errando a senha 5 vezes bloquearia no *Rate Limiter* interno todos os funcionários legítimos da empresa, e os logs de auditoria e do **Fail2ban** não saberiam qual IP real atacar!

## Como funciona
Ao mesmo tempo, garanta no Proxy Reverso que o cabeçalho configurado em `IP_HEADER` seja **sobrescrito** com o `$remote_addr` real da conexão TCP (`proxy_set_header X-Real-IP $remote_addr;`) e habilite o upgrade de **WebSocket (`/notifications/hub`)** (`ENABLE_WEBSOCKET=true`) para que alterações de senhas sincronizem em tempo real com todos os clientes conectados!

## Exemplo
```nginx
# Configuracao segura de Nginx para o Vaultwarden: cabecalho X-Real-IP confiavel, WebSocket (/notifications/hub) e bloqueio externo de /admin
server {
    listen 443 ssl http2;
    server_name cofre.exemplo.br;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    location /admin {
        allow 10.10.10.0/24;
        deny all;
        proxy_pass http://127.0.0.1:8000;
    }

    location /notifications/hub {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass http://127.0.0.1:8000;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## Limites e trade-offs
Combine o `LOG_FILE=/data/vaultwarden.log` do Vaultwarden com uma jail do **Fail2ban** (ou parser do **CrowdSec** / **Wazuh**): o Vaultwarden registra cada tentativa falha de login, 2FA ou Admin Token com o IP real extraído de `IP_HEADER`, permitindo banir o IP infrator diretamente no firewall `nftables`!

## Como verificar
Para privacidade adicional ao buscar ícones de sites (`Website Icons`), configure **`ICON_BLACKLIST_NON_GLOBAL_IPS=true`** (ativo por padrão para mitigar SSRF na rede interna!) ou **`DISABLE_ICON_DOWNLOAD=true`** se quiser proibir que o servidor Vaultwarden faça requisições HTTP para domínios externos salvos nos cofres.

## Conexões
- [[vaultwarden-compartilhamento-efemero-send-acesso-emergencia-anexos]] — Veja também: Compartilhamento Efêmero (**Bitwarden Send**) e **Emergency Access** no Vaultwarden: Eliminando Senhas no Slack/E-mail com Expiração e Contagem de Visualizações.
- [[vaultwarden-auditoria-event-logs-retencao-monitoramento-siem-soc]] — Veja também: Logs de Auditoria Organizacional (**Event Logs**) e Retenção (`EVENTS_DAYS_RETAIN`) no Vaultwarden: Rastreando Acessos, Exportações de Cofre e Mudanças de Permissão.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[vaultwarden-blindagem-painel-admin-token-argon2-phc-signups-allowed]] — Referência cruzada direta com vaultwarden-blindagem-painel-admin-token-argon2-phc-signups-allowed.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
