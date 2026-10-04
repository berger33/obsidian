---
id: software.seguranca.tranche13.001241
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/gophish/gophish/master/README.md", "https://docs.getgophish.com/user-guide/documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura do **Gophish (`gophish/gophish`)**: Plataforma Open-Source de Simulação de Phishing, Red Team e Treinamento de Conscientização em Segurança

## Em uma frase
Como equipes internas de **Segurança da Informação (Blue Team / GRC)** e **Red Teams** medem de forma objetiva e ética a resiliência dos colaboradores contra ataques de **Engenharia Social e Phishing**, além de testar se os filtros de e-mail corporativos (SPF, DKIM, DMARC, SEG) e o SOC detectam campanhas simuladas?

## Por que importa
Escrito em **Go (`Golang`)** por Jordan Wright e distribuído como um único binário autocontido (com banco SQLite3 embutido ou MySQL/MariaDB para escala corporativa), o **Gophish** é o framework open-source padrão mundial para **simulação controlada de campanhas de phishing e treinamento de conscientização (*Security Awareness*)**!

## Como funciona
Sua arquitetura separa estritamente dois servidores HTTP/HTTPS configurados no arquivo **`config.json`**: **(1) O `admin_server`** (por padrão em `127.0.0.1:3333` com TLS habilitado, onde os operadores autenticados criam campanhas, gerenciam modelos e acompanham dashboards e métricas em tempo real via UI ou API REST); e **(2) O `phish_server`** (por padrão em `0.0.0.0:80` ou `:443`, que serve exclusivamente as **Landing Pages** de simulação e registra os eventos associados ao identificador único `rid` de cada destinatário)!

## Exemplo
```json
{
  "admin_server": {
    "listen_url": "127.0.0.1:3333",
    "use_tls": true,
    "cert_path": "gophish_admin.crt",
    "key_path": "gophish_admin.key"
  },
  "phish_server": {
    "listen_url": "0.0.0.0:443",
    "use_tls": true,
    "cert_path": "simulacao_tls.crt",
    "key_path": "simulacao_tls.key"
  },
  "db_name": "sqlite3",
  "db_path": "gophish.db"
}
```

## Limites e trade-offs
Regra número 1 de segurança operacional (**OPSEC**) ao implantar o Gophish: **NUNCA exponha a porta do `admin_server` (`:3333`) diretamente para a Internet pública!** Mantenha `"listen_url": "127.0.0.1:3333"` e acesse o painel administrativo exclusivamente via túnel SSH (`ssh -L 3333:127.0.0.1:3333`) ou VPN WireGuard/Tailscale.

## Como verificar
Na primeira inicialização do binário `./gophish`, o servidor gera uma senha aleatória única para o usuário `admin` impressa no log do terminal e exige a troca imediata de senha no primeiro login.

## Conexões
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Veja também: Configuração de **Sending Profiles (Perfis SMTP)** e Cabeçalhos Customizados (`X-Phish-Test`) no Gophish: Entregabilidade, SPF/DKIM/DMARC e Autorização.
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Referência cruzada direta com gophish-templates-email-variaveis-dinamicas-tracking-pixel-links.
- [[keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing]] — Referência cruzada direta com keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
