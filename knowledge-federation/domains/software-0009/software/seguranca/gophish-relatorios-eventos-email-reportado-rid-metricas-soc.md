---
id: software.seguranca.tranche13.001247
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

# Métricas de Sucesso e **Email Reporting (`/report?rid=...`)** no Gophish: Medindo Não Apenas Cliques, Mas a **Taxa de Reporte ao SOC (`Email Reported`)**

## Em uma frase
Durante muitos anos, empresas avaliavam campanhas de conscientização olhando apenas para uma métrica negativa: a **Taxa de Cliques (*Click Rate*)**. Porém, a engenharia de segurança moderna sabe que uma métrica ainda mais importante para a defesa real de uma organização é a **Taxa e o Tempo de Reporte ao SOC (`Email Reported` / *Time-to-Report*)**: quantos colaboradores reconheceram o e-mail suspeito e clicaram no botão **"Reportar Phishing"** do cliente de e-mail nos primeiros 5 minutos?

## Por que importa
O Gophish suporta nativamente o evento **`Email Reported`**! Como cada link e pixel enviado pelo Gophish carrega o parâmetro único **`?rid=<Result_ID>`** daquele destinatário, quando o colaborador clica no botão de reportar phishing no Outlook/Gmail (usando add-ins que extraem o `rid` ou encaminham para uma caixa de triagem automatizada do SOC/SOAR), basta uma requisição **`GET {{.BaseURL}}/report?rid={{.RId}}`** no `phish_server` para que o Gophish registre na timeline daquele colaborador o selo verde **`Email Reported`**!

## Como funciona
No dashboard da campanha, você passa a medir os **5 estágios completos do funil**: `Email Sent` -> `Email Opened` -> `Clicked Link` -> `Submitted Data` -> e o indicador positivo de maturidade **`Email Reported`**!

## Exemplo
```bash
# Simular ou integrar via SOAR o registro de que um colaborador reportou corretamente o e-mail suspeito (usando o rid extraido do link)
curl -sk "https://simulacao.exemplo.br/report?rid=AbCdEf12345"
```

## Limites e trade-offs
Por que medir a **Taxa de Reporte (`Email Reported`)** transforma a cultura de segurança da empresa? Porque permite **reconhecer e parabenizar positivamente** as equipes e colaboradores que atuaram como sensores humanos de detecção precoce para o SOC!

## Como verificar
Você pode exportar todos os eventos brutos da campanha clicando em **`Export CSV` -> `Raw Events`** no painel da campanha ou consultando o endpoint `/api/campaigns/:id/results` para alimentar dashboards executivos de evolução trimestral.

## Conexões
- [[gophish-execucao-campanhas-agendamento-send-by-date-throttling]] — Veja também: Orquestração de **Campaigns** no Gophish: Cadência de Disparo (**`Send Emails By`**), Prevenção de *Rate-Limiting* SMTP e Escalonamento Temporal.
- [[gophish-webhooks-integracao-soar-slack-automacao-api-rest]] — Veja também: Automação em Tempo Real com **Webhooks Autenticados (`HMAC-SHA256`)** e **API REST** no Gophish: Integrando Simulações ao SOAR e Treinamento.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.
- [[gophish-templates-email-variaveis-dinamicas-tracking-pixel-links]] — Referência cruzada direta com gophish-templates-email-variaveis-dinamicas-tracking-pixel-links.

## Fontes
- [Gophish Official GitHub — Open-Source Phishing Toolkit](https://raw.githubusercontent.com/gophish/gophish/master/README.md) — repositório oficial do Gophish detalhando arquitetura em Go (`admin_server` e `phish_server`), instalação e inicialização segura; consultado em 2026-10-03.
- [Gophish Official User Guide Documentation (`docs.getgophish.com`)](https://docs.getgophish.com/user-guide/documentation) — documentação oficial do Gophish cobrindo Sending Profiles, Email Templates (`{{.URL}}`, `{{.Tracker}}`), Landing Pages, Users & Groups, Campaigns, Email Reporting (`rid`) e Webhooks; consultado em 2026-10-03.
