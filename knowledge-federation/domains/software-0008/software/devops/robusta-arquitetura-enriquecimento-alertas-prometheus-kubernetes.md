---
id: software.devops.tranche12.001161
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

# Robusta: Arquitetura de Enriquecimento de Alertas Prometheus e Observabilidade no Kubernetes

## Em uma frase
Robusta é um motor open-source de observabilidade, enriquecimento de alertas e automação de resposta a incidentes para Kubernetes que recebe alertas do Prometheus Alertmanager via webhook e anexa automaticamente logs de Pods, eventos do cluster, gráficos e diagnósticos de causa raiz antes de entregá-los aos canais de notificação.

## Por que importa
Receber um alerta cru do Alertmanager no Slack ou PagerDuty dizendo apenas `KubePodCrashLooping` obriga o engenheiro de plantão a abrir o terminal, autenticar no cluster e rodar `kubectl logs` e `kubectl describe` manualmente para entender o que aconteceu.

## Como funciona
Instalado no cluster via Helm (`robusta-runner` e `robusta-forwarder`), o Robusta escuta tanto eventos nativos da API do Kubernetes quanto webhooks disparados pelo Alertmanager (local ou gerenciado como AWS/GCP/Azure Managed Prometheus, VictoriaMetrics e Thanos), executa playbooks de coleta de evidências e envia a notificação enriquecida para os `sinks` configurados.

## Exemplo
```bash
helm repo add robusta https://robusta-charts.storage.googleapis.com
helm repo update
kubectl get pods -A -l app.kubernetes.io/name=robusta
```

## Limites e trade-offs
Configurar o Alertmanager para enviar alertas tanto diretamente para o Slack quanto para o Robusta mirando o mesmo canal gera notificações duplicadas (uma crua do Alertmanager e outra enriquecida pelo Robusta).

## Como verificar
Roteie os alertas do Alertmanager para o webhook interno do `robusta-runner` e deixe o Robusta gerenciar a entrega agrupada e enriquecida para os sinks finais.

## Conexões
- [[robusta-playbooks-triggers-actions-sinks-modelo-regras]] — Veja também: Robusta: Modelo de Playbooks com Triggers, Actions e Sinks (generated_values.yaml).

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
