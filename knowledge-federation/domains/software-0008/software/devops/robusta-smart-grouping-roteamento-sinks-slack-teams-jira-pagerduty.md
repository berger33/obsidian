---
id: software.devops.tranche12.001164
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md", "https://docs.robusta.dev/master/index.html", "https://github.com/robusta-dev/robusta"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Robusta: Smart Grouping e Roteamento Avançado para Sinks (Slack, MS Teams, PagerDuty e Jira)

## Em uma frase
O Robusta suporta dezenas de destinos de notificação (`sinksConfig`, incluindo Slack, Microsoft Teams, Discord, Google Chat, Mattermost, PagerDuty, Opsgenie, Jira, ServiceNow, DataDog e Kafka), oferecendo agrupamento inteligente (`Smart Grouping` com threads no Slack), roteamento por namespace/severidade e auto-resolução.

## Por que importa
Durante uma falha de nó ou indisponibilidade de banco de dados, dezenas de alertas correlacionados inundam o canal do Slack, enterrando as mensagens importantes e gerando fadiga de alertas severa no plantão.

## Como funciona
Na configuração de cada sink em `sinksConfig`, é possível definir `match` (filtrando por `namespace`, `severity`, `labels` ou `title`), configurar agrupamento de notificações em threads e habilitar atualização automática quando o alerta é resolvido no Alertmanager (por exemplo, fechando ou atualizando o ticket no Jira ou mudando o status no Slack).

## Exemplo
```yaml
sinksConfig:
  - slack_sink:
      name: slack_payments_sink
      slack_channel: alerts-payments
      api_key: "{{ env.SLACK_BOT_TOKEN }}"
      match:
        namespace: ^payments-.*
        severity: [high, critical]
```

## Limites e trade-offs
Configurar múltiplos sinks sem filtros `match` ou sem `stop: true` em playbooks específicos faz com que alertas de desenvolvimento ou baixa severidade sejam enviados para canais de PagerDuty de produção.

## Como verificar
Separe sinks por criticidade e domínio (`match.namespace` e `match.severity`) e valide o roteamento disparando um alerta de teste.

## Conexões
- [[robusta-deteccao-nativa-oomkill-crashloop-jobs-sem-promql]] — Veja também: Robusta: Detecção Nativa de OOMKills, CrashLoops e Falhas de Jobs sem PromQL.
- [[robusta-auto-remediacao-self-healing-playbooks-seguranca]] — Veja também: Robusta: Auto-Remediação (Self-Healing) e Ações Interativas sobre Alertas Kubernetes.

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
