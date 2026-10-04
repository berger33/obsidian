---
id: software.seguranca.tranche13.001248
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

# Automação em Tempo Real com **Webhooks Autenticados (`HMAC-SHA256`)** e **API REST** no Gophish: Integrando Simulações ao SOAR e Treinamento

## Em uma frase
Como acionar automaticamente um fluxo no seu **SOAR (Shuffle, Cortex XSOAR, n8n)**, enviar uma notificação ao canal do Red Team ou matricular automaticamente um colaborador em um micro-módulo educativo na plataforma de LMS no exato instante em que um evento **`Clicked Link`** ou **`Submitted Data`** ocorre no Gophish?

## Por que importa
Na aba **Webhooks** do Gophish, você cadastra um endpoint HTTPS receptor e define um **`Secret` compartilhado**. Toda vez que qualquer evento de campanha acontece (`Email Sent`, `Email Opened`, `Clicked Link`, `Submitted Data`, `Email Reported`), o Gophish dispara imediatamente um `POST` JSON contendo `campaign_id`, `email`, `time`, `message` e `details` — assinado criptograficamente no cabeçalho HTTP **`X-Gophish-Signature: sha256=<hmac_hex>`**!

## Como funciona
O seu receptor SOAR valida o `HMAC-SHA256` do corpo da requisição usando o `Secret` compartilhado (garantindo que o evento veio legitimamente do servidor Gophish!) e executa a automação em tempo real!

## Exemplo
```bash
# Listar todas as campanhas ou criar recursos programaticamente usando a API REST nativa do Gophish com autenticacao Bearer API Key
curl -sk -H "Authorization: Bearer ${GOPHISH_API_KEY}" \
  "https://127.0.0.1:3333/api/campaigns/" | jq '.[].name'
```

## Limites e trade-offs
Além dos Webhooks de saída, **100% das funcionalidades da interface web do Gophish são construídas sobre sua própria API REST (`/api/campaigns/`, `/api/groups/`, `/api/templates/`, `/api/pages/`, `/api/smtp/`, `/api/webhooks/`)**, além de contar com o cliente oficial em Python **`gophish` (`pip install gophish`)**!

## Como verificar
Nunca processe payloads de Webhook sem antes verificar criptograficamente o cabeçalho **`X-Gophish-Signature`** usando comparação em tempo constante (`hmac.compare_digest` em Python).

## Conexões
- [[gophish-relatorios-eventos-email-reportado-rid-metricas-soc]] — Veja também: Métricas de Sucesso e **Email Reporting (`/report?rid=...`)** no Gophish: Medindo Não Apenas Cliques, Mas a **Taxa de Reporte ao SOC (`Email Reported`)**.
- [[gophish-imap-monitoramento-caixa-entrada-respostas-automaticas]] — Veja também: Monitoramento **IMAP** de Caixa de Entrada no Gophish: Detectando Respostas Diretas dos Usuários e Auto-Replies (*Out-of-Office*).
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado]] — Referência cruzada direta com gophish-hardening-opsec-infraestrutura-gophish-headers-rid-customizado.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
