---
id: software.seguranca.tranche13.001246
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

# Orquestração de **Campaigns** no Gophish: Cadência de Disparo (**`Send Emails By`**), Prevenção de *Rate-Limiting* SMTP e Escalonamento Temporal

## Em uma frase
O que acontece se você iniciar uma campanha no Gophish para 2.000 colaboradores sem configurar uma data/hora limite de espaçamento (**`Send Emails By`**)?

## Por que importa
O Gophish tentará disparar todos os 2.000 e-mails o mais rápido possível logo no minuto inicial da campanha! Isso gera dois problemas operacionais imediatos: **(1) Bloqueio por *Rate Limiting* / Throttling no servidor SMTP**; e **(2) O "Efeito Corredor / Slack"** — quando todos os funcionários do mesmo andar ou canal do Slack recebem exatamente o mesmo e-mail no mesmo segundo (`10:00:01`), basta a primeira pessoa avisar no chat *"Pessoal, acabou de chegar o teste de phishing trimestral do time de Segurança!"* para invalidar a medição de toda a empresa!

## Como funciona
Para evitar ambos os problemas, configure sempre na criação da campanha do Gophish tanto o **`Launch Date`** (data/hora de início) quanto o **`Send Emails By`** (data/hora final de conclusão dos envios, por exemplo, distribuindo os envios ao longo de **3 a 5 dias úteis**)! Quando o `Send Emails By` é definido, o motor de agendamento do Gophish divide a janela total pelo número de destinatários e dispara os e-mails de forma espaçada e contínua ao longo dos dias!

## Exemplo
```bash
# Consultar via API REST do Gophish o resumo de status de uma campanha em andamento (enviados, abertos, clicados, reportados)
curl -sk -H "Authorization: Bearer ${GOPHISH_API_KEY}" \
  "https://127.0.0.1:3333/api/campaigns/1/summary" | jq .
```

## Limites e trade-offs
Distribua grandes campanhas corporativas em janelas de `Send Emails By` de pelo menos **48 a 72 horas**: além de respeitar os limites de reputação de envio por hora do seu servidor SMTP, cada colaborador recebe a simulação em um momento diferente da semana, simulando fielmente a dinâmica de ataques reais.

## Como verificar
Quando todos os destinatários precisam de pelo menos 48 horas após o último envio para interagir com o e-mail antes do encerramento da campanha, só clique em *"Complete Campaign"* 2 a 3 dias após o horário configurado em `Send Emails By`.

## Conexões
- [[gophish-grupos-usuarios-importacao-csv-segmentacao-departamentos]] — Veja também: Gerenciamento de **Users & Groups** no Gophish: Importação em Lote via CSV e Segmentação de Campanhas por Perfil de Risco (`Position`).
- [[gophish-relatorios-eventos-email-reportado-rid-metricas-soc]] — Veja também: Métricas de Sucesso e **Email Reporting (`/report?rid=...`)** no Gophish: Medindo Não Apenas Cliques, Mas a **Taxa de Reporte ao SOC (`Email Reported`)**.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade]] — Referência cruzada direta com gophish-configuracao-sending-profiles-smtp-tls-headers-autenticidade.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
