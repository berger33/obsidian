---
id: software.devops.tranche12.001162
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

# Robusta: Modelo de Playbooks com Triggers, Actions e Sinks (generated_values.yaml)

## Em uma frase
A automação no Robusta Classic é estruturada em `customPlaybooks` declarados nos valores do Helm (`generated_values.yaml`), onde cada playbook conecta três blocos: `triggers` (o que dispara a regra), `actions` (quais dados coletar ou qual remediação executar) e `sinks` (para onde enviar o resultado).

## Por que importa
Codificar scripts ad-hoc para monitorar eventos do Kubernetes ou reagir a alertas Prometheus cria ferramentas frágeis sem padronização de filtros de namespace, rate limiting ou roteamento multi-canal.

## Como funciona
Um `trigger` pode ser um alerta específico do Prometheus (`on_prometheus_alert`) ou um evento nativo do Kubernetes sem necessidade de PromQL (`on_pod_crash_loop`, `on_pod_oom_killed`, `on_job_failure`, `on_deployment_update`). Quando o gatilho dispara, o runner executa a lista de `actions` em sequência (como `logs_enricher`, `pod_events_enricher`, `node_cpu_enricher`) e despacha o objeto enriquecido.

## Exemplo
```yaml
customPlaybooks:
  - triggers:
      - on_pod_crash_loop:
          restart_count: 2
    actions:
      - report_crash_loop: {}
      - logs_enricher:
          warn_on_missing_label: false
    sinks:
      - slack_sre_sink
```

## Limites e trade-offs
Criar um playbook com `on_pod_update` genérico sem filtrar por condição de erro ou namespace dispara centenas de execuções por minuto em clusters com alto churn de Pods.

## Como verificar
Use gatilhos específicos de falha (`on_pod_crash_loop`, `on_pod_oom_killed`, `on_prometheus_alert`) e restrinja escopos de namespace e labels diretamente na configuração do trigger.

## Conexões
- [[robusta-arquitetura-enriquecimento-alertas-prometheus-kubernetes]] — Veja também: Robusta: Arquitetura de Enriquecimento de Alertas Prometheus e Observabilidade no Kubernetes.
- [[robusta-deteccao-nativa-oomkill-crashloop-jobs-sem-promql]] — Veja também: Robusta: Detecção Nativa de OOMKills, CrashLoops e Falhas de Jobs sem PromQL.

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
