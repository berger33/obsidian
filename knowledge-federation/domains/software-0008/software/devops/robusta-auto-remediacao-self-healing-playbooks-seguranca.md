---
id: software.devops.tranche12.001165
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

# Robusta: Auto-Remediação (Self-Healing) e Ações Interativas sobre Alertas Kubernetes

## Em uma frase
Além de enriquecer alertas de forma somente leitura, os playbooks do Robusta permitem configurar ações de auto-remediação automática ou acionadas por botão interativo no chat (como reiniciar um Deployment travado, escalar réplicas, executar comandos de diagnóstico ou drenar um nó problemático).

## Por que importa
Problemas recorrentes e bem conhecidos (como um serviço legado que exige restart após falha transitória de dependência ou necessidade de coletar um profile de CPU exatamente durante um pico) desperdiçam tempo humano quando exigem intervenção manual às 3h da manhã.

## Como funciona
Um playbook vincula um `on_prometheus_alert` (filtrando por `alert_name`) a uma action remediadora ou expõe um callback interativo na mensagem do Slack/Teams para que o engenheiro aprove a ação com um clique, mantendo auditoria no canal de quem acionou o comando.

## Exemplo
```yaml
customPlaybooks:
  - triggers:
      - on_prometheus_alert:
          alert_name: KubeHpaMaxedOut
    actions:
      - create_finding:
          title: "HPA atingiu o limite maximo de replicas"
          aggregation_key: "hpa_maxed_out"
```

## Limites e trade-offs
Habilitar ações de auto-remediação que alteram réplicas ou especificações de `Deployment` diretamente no cluster quando o mesmo recurso é gerenciado por Argo CD com `selfHeal: true` gera disputa imediata entre o Robusta e o controlador GitOps.

## Como verificar
Em clusters GitOps, prefira usar o Robusta para diagnóstico profundo, coleta de perfis/logs efêmeros ou ações que não conflitem com os campos reconciliados pelo Argo CD/Flux.

## Conexões
- [[robusta-smart-grouping-roteamento-sinks-slack-teams-jira-pagerduty]] — Veja também: Robusta: Smart Grouping e Roteamento Avançado para Sinks (Slack, MS Teams, PagerDuty e Jira).
- [[robusta-change-tracking-correlacao-rollouts-config-alertas]] — Veja também: Robusta: Change-Tracking de Recursos Kubernetes para Correlação entre Deploys e Incidentes.

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
