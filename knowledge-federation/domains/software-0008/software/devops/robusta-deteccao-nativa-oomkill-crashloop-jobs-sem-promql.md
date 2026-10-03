---
id: software.devops.tranche12.001163
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

# Robusta: Detecção Nativa de OOMKills, CrashLoops e Falhas de Jobs sem PromQL

## Em uma frase
O Robusta monitora diretamente o stream de eventos e mudanças de estado da API do Kubernetes por meio do `robusta-forwarder`, detectando instantaneamente `OOMKilled`, `CrashLoopBackOff`, falhas de `Job` e erros de `ImagePullBackOff` mesmo sem depender de regras PromQL ou intervalos de scrape do Prometheus.

## Por que importa
Quando um Pod sofre `OOMKilled` ou falha rapidamente e é substituído ou reiniciado entre dois ciclos de coleta do Prometheus, os logs do container anterior podem já ter sido perdidos quando o alerta de métrica finalmente dispara.

## Como funciona
Ao capturar o evento de transição do Pod em tempo real na API do Kubernetes, os playbooks nativos do Robusta buscam imediatamente os logs do container anterior (`--previous`), o código de saída (`exitCode: 137` para OOMKill) e o consumo de memória no instante da falha, enviando o relatório completo para a equipe.

## Exemplo
```bash
# Verificar os pods do Robusta (runner e forwarder) em execucao:
kubectl get pods -l "robustaComponent in (runner,forwarder)" -A
kubectl logs deployment/robusta-runner -c runner --tail=50
```

## Limites e trade-offs
Desativar a retenção de logs anteriores no runtime do nó ou definir limites de memória muito baixos no próprio `robusta-runner` ao coletar dumps grandes de logs pode causar OOMKill no próprio pod do Robusta.

## Como verificar
Dimensione adequadamente a memória do `robusta-runner` de acordo com o tamanho do cluster e verifique nos logs do runner que o `robusta-forwarder` está conectado e enviando eventos.

## Conexões
- [[robusta-playbooks-triggers-actions-sinks-modelo-regras]] — Veja também: Robusta: Modelo de Playbooks com Triggers, Actions e Sinks (generated_values.yaml).
- [[robusta-smart-grouping-roteamento-sinks-slack-teams-jira-pagerduty]] — Veja também: Robusta: Smart Grouping e Roteamento Avançado para Sinks (Slack, MS Teams, PagerDuty e Jira).

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
