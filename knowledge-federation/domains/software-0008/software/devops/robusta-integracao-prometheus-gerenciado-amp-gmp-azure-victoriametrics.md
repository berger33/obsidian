---
id: software.devops.tranche12.001169
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

# Robusta: Integração com kube-prometheus-stack, VictoriaMetrics, Thanos e Managed Prometheus (AWS, GCP, Azure)

## Em uma frase
O Robusta pode ser instalado como um pacote all-in-one (incluindo um `kube-prometheus-stack` pré-configurado) ou conectado a uma instância existente do Prometheus Operator, VictoriaMetrics, Thanos, Grafana Alertmanager, Coralogix ou serviços gerenciados (AWS Managed Prometheus, Google Managed Prometheus e Azure Managed Prometheus).

## Por que importa
Em arquiteturas multi-cluster onde as métricas e o Alertmanager residem fora do cluster ou em serviços gerenciados da nuvem, o `robusta-runner` precisa saber exatamente qual URL de query consultar para gerar gráficos e enriquecer alertas.

## Como funciona
No arquivo `generated_values.yaml` do Helm chart do Robusta, configura-se `enablePrometheusStack: false` (quando já existe Prometheus) e define-se a URL do Prometheus/VictoriaMetrics/Thanos e as credenciais/IAM necessárias para que o runner consulte métricas históricas durante o enriquecimento dos alertas.

## Exemplo
```yaml
# Exemplo de configuracao no generated_values.yaml para Prometheus existente:
enablePrometheusStack: false
globalConfig:
  prometheus_url: "http://vmsingle-victoria-metrics.monitoring.svc:8428"
  alertmanager_url: "http://vmalertmanager.monitoring.svc:9093"
```

## Limites e trade-offs
Deixar `enablePrometheusStack: true` em um cluster que já possui `kube-prometheus-stack` instalado causa conflito de CRDs (`ServiceMonitor`, `PrometheusRule`) e duplica o consumo de memória com dois coletores Prometheus.

## Como verificar
Verifique se o cluster já possui Prometheus instalado antes de gerar o `generated_values.yaml` e aponte `prometheus_url` para o endpoint existente.

## Conexões
- [[robusta-krr-kubernetes-resource-recommender-otimizacao-custos]] — Veja também: Robusta: Integração com KRR (Kubernetes Resource Recommender) para Otimização de CPU e Memória.
- [[robusta-cli-wizard-helm-instalacao-gitops-argocd-flux]] — Veja também: Robusta: Geração de Valores com Robusta CLI e Implantação GitOps (Argo CD e Flux).

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
