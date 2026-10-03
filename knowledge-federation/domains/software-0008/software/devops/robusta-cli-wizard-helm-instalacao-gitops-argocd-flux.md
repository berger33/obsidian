---
id: software.devops.tranche12.001170
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

# Robusta: Geração de Valores com Robusta CLI e Implantação GitOps (Argo CD e Flux)

## Em uma frase
Para implantar o Robusta com GitOps (Argo CD ou Flux), utiliza-se o wizard da CLI `robusta gen-config` apenas uma vez para gerar o `generated_values.yaml`, extraindo as chaves de API e tokens de sinks para `Secrets` Kubernetes externos antes de versionar o manifesto no Git.

## Por que importa
O arquivo `generated_values.yaml` produzido inicialmente pelo wizard contém chaves de assinatura, tokens de Slack/Teams e chaves de conta em texto puro que nunca devem ser commitados diretamente em um repositório Git.

## Como funciona
Na abordagem GitOps, os tokens sensíveis de `sinksConfig` e `globalConfig` são movidos para um `Secret` Kubernetes (gerenciado por External Secrets Operator ou Sealed Secrets) e referenciados no `generated_values.yaml` por variáveis de ambiente `{{ env.NOME_DA_VARIAVEL }}` injetadas via `runner.additional_env_vars` ou `runner.additional_env_froms`.

## Exemplo
```yaml
runner:
  additional_env_froms:
    - secretRef:
        name: robusta-sinks-secrets
sinksConfig:
  - slack_sink:
      name: main_slack_sink
      slack_channel: k8s-prod-alerts
      api_key: "{{ env.SLACK_API_KEY }}"
```

## Limites e trade-offs
Commitar o `generated_values.yaml` bruto gerado por `robusta gen-config` no repositório Git do Argo CD ou Flux vaza tokens de bot do Slack, chaves do PagerDuty e `signing_key` do runner.

## Como verificar
Substitua todos os segredos no `generated_values.yaml` por referências `{{ env.* }}` carregadas de um `Secret` Kubernetes e valide o pod `robusta-runner` após a sincronização do Argo CD/Flux.

## Conexões
- [[robusta-integracao-prometheus-gerenciado-amp-gmp-azure-victoriametrics]] — Veja também: Robusta: Integração com kube-prometheus-stack, VictoriaMetrics, Thanos e Managed Prometheus (AWS, GCP, Azure).

## Fontes
- [Robusta GitHub — README.md (Prometheus Alert Enrichment, Smart Grouping, Playbooks, Change-Tracking, KRR & Sinks Matrix)](https://raw.githubusercontent.com/robusta-dev/robusta/master/README.md) — README oficial do robusta-dev/robusta detalhando enriquecimento de alertas Prometheus, Smart Grouping em threads, detecção sem PromQL, Change-Tracking, auto-remediação, KRR e matriz de integrações/sinks; consultado em 2026-10-03.
- [Robusta Official Documentation — Overview & HolmesGPT AI Root Cause Analysis](https://docs.robusta.dev/master/index.html) — Documentação oficial do Robusta e integração com HolmesGPT para investigação automática de causa raiz em alertas Kubernetes; consultado em 2026-10-03.
- [Robusta — Official GitHub Repository](https://github.com/robusta-dev/robusta) — Repositório oficial do Robusta; consultado em 2026-10-03.
