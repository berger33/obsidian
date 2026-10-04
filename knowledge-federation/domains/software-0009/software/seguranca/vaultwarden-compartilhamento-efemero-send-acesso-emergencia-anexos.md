---
id: software.seguranca.tranche14.001325
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

# Compartilhamento Efêmero (**Bitwarden Send**) e **Emergency Access** no Vaultwarden: Eliminando Senhas no Slack/E-mail com Expiração e Contagem de Visualizações

## Em uma frase
Quando um engenheiro precisa enviar um segredo temporário, certificado `.pfx` ou chave de API para um cliente externo ou colega que não faz parte da mesma Collection, enviar por e-mail, Slack, Teams ou WhatsApp deixa o segredo eternamente gravado no histórico de mensagens em texto claro!

## Por que importa
O recurso **Bitwarden Send** implementado nativamente no Vaultwarden resolve esse problema com **Criptografia de Ponta a Ponta no Navegador**: quando você cria um *Send* (de Texto ou Arquivo), o cliente gera uma chave aleatória efêmera, cifra o conteúdo localmente e coloca a chave de descriptografia **apenas após o fragmento `#` da URL (`https://cofre.exemplo.br/#/send/<id>/<chave>`)** — como os navegadores jamais enviam a parte após o `#` (*URI Fragment*) nas requisições HTTP para o servidor, **nem mesmo o servidor Vaultwarden consegue ler o conteúdo do Send**!

## Como funciona
Além disso, cada *Send* permite definir **Data de Deleção Automática** (purgada pelo job `SEND_PURGE_SCHEDULE`), **Data de Expiração**, **Número Máximo de Acessos (`Max Access Count = 1`, autodestruindo após a primeira leitura!)** e **Senha adicional**!

## Exemplo
```bash
# Criar pelo terminal usando a Bitwarden CLI (bw send) um link criptografado de leitura unica (--maxAccessCount 1) que se autodestroi em 1 dia
bw send create --text --name "Credencial Temporaria Homolog" \
  --deleteInDays 1 --maxAccessCount 1 \
  "SenhaTemporariaSecreta#2026"
```

## Limites e trade-offs
Se a política de DLP (*Data Loss Prevention*) da sua empresa proibir que usuários compartilhem links externos a partir do cofre corporativo, você pode desativar o Bitwarden Send globalmente com **`SENDS_ALLOWED=false`** no `.env` ou através da Organization Policy **`Disable Send`**!

## Como verificar
Já o recurso **Emergency Access** (controlado pelos jobs `EMERGENCY_NOTIFICATION_REMINDER_SCHEDULE` e `EMERGENCY_REQUEST_TIMEOUT_SCHEDULE`) permite designar contatos de emergência confiáveis que podem solicitar acesso de leitura (`View`) ou tomada de controle (`Takeover`) caso o titular fique inacessível após um período de espera configurável (ex.: 7 dias).

## Conexões
- [[vaultwarden-autenticacao-2fa-webauthn-fido2-yubikey-totp-duo-email]] — Veja também: Autenticação Multifator (**2FA**) e Derivação de Chave (**Argon2id Client-Side**) no Vaultwarden: **FIDO2 WebAuthn**, **YubiKey OTP**, **TOTP** e **Duo**.
- [[vaultwarden-proxy-reverso-https-websocket-ip-header-rate-limiting]] — Veja também: Arquitetura de Proxy Reverso, **WebSockets** e **`IP_HEADER`** no Vaultwarden: Sincronização Instantânea, Prevenção de IP Spoofing e **Fail2ban / CrowdSec**.
- [[vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres]] — Referência cruzada direta com vaultwarden-arquitetura-bitwarden-rust-zero-knowledge-sqlite-postgres.
- [[vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas]] — Referência cruzada direta com vaultwarden-organizacoes-colecoes-rbac-grupos-politicas-corporativas.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Referência cruzada direta com keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura.

## Fontes
- [Vaultwarden Official GitHub Repository (`dani-garcia/vaultwarden`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/README.md) — repositório oficial do servidor Vaultwarden em Rust cobrindo compatibilidade com clientes Bitwarden, Organizations, Send, 2FA WebAuthn, Emergency Access e requisito HTTPS/Web Crypto API; consultado em 2026-10-03.
- [Vaultwarden Official Configuration Template (`.env.template`)](https://raw.githubusercontent.com/dani-garcia/vaultwarden/main/.env.template) — referência oficial de configuração `.env.template` do Vaultwarden cobrindo `ADMIN_TOKEN` Argon2 PHC, `SIGNUPS_ALLOWED`, `ENABLE_DB_WAL`, `IP_HEADER`, Rate Limiting e `ORG_EVENTS_ENABLED`; consultado em 2026-10-03.
