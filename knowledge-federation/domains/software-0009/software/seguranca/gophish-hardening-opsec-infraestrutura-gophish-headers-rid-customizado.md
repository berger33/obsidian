---
id: software.seguranca.tranche13.001250
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

# OPSEC e Hardening de Infraestrutura **Gophish** para Red Teams: Customizando o Parâmetro `rid`, Cabeçalhos `X-Gophish` e Proteção com Proxy Reverso

## Em uma frase
Quando uma equipe de **Red Team** utiliza o Gophish em uma operação autorizada de simulação de adversário (*Adversary Emulation*), scanners de Threat Intelligence na internet (como Shodan, Censys e URLScan) e gateways de e-mail modernos conseguem identificar uma instalação padrão do Gophish em segundos! Por quê?

## Por que importa
Porque a instalação padrão do Gophish deixa **três impressões digitais (*fingerprints*) estáticas óbvias**: **(1)** Nos e-mails enviados, ele adiciona por padrão o cabeçalho `X-Mailer: gophish`; **(2)** Nas respostas HTTP do servidor, ele inclui cabeçalhos e mensagens de erro padrão do Gophish; e **(3)** Todos os links de campanha usam na query string o parâmetro literal **`?rid=`**!

## Como funciona
Para aplicar **Hardening e OPSEC** em uma infraestrutura Gophish de Red Team: **(1) No `config.json`**, altere a chave **`"contact_address"`** e personalize o código/configuração para remover assinaturas `gophish`; **(2) Coloque um Proxy Reverso (Nginx / Caddy / Apache com ModSecurity)** na frente do `phish_server` (`127.0.0.1:8080`) que oculta cabeçalhos do backend, filtra *User-Agents* de scanners conhecidos e redireciona qualquer requisição sem um `rid` válido para um site institucional inócuo; e **(3) Mantenha o `admin_server` (`127.0.0.1:3333`) 100% isolado do mundo externo**!

## Exemplo
```nginx
# Exemplo de bloco Nginx atuando como proxy reverso de OPSEC na frente do phish_server local do Gophish
server {
    listen 443 ssl http2;
    server_name portal-revisao.exemplo.br;

    proxy_hide_header X-Server;
    proxy_hide_header Server;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Limites e trade-offs
Do ponto de vista do **Blue Team / SOC**, conhecer esses *fingerprints* padrão do Gophish (`X-Mailer: gophish`, URLs com `?rid=[a-zA-Z0-9]{7}` e certificados TLS recém-emitidos para domínios similares à marca da empresa) também permite criar regras de detecção no gateway de e-mail e no proxy web para detectar atores de ameaça reais que utilizam o Gophish de forma maliciosa sem customização!

## Como verificar
Ao final de qualquer campanha ou operação autorizada, desative imediatamente o `phish_server` e arquive os logs de evidência de forma criptografada.

## Conexões
- [[gophish-imap-monitoramento-caixa-entrada-respostas-automaticas]] — Veja também: Monitoramento **IMAP** de Caixa de Entrada no Gophish: Detectando Respostas Diretas dos Usuários e Auto-Replies (*Out-of-Office*).
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Referência cruzada direta com gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
