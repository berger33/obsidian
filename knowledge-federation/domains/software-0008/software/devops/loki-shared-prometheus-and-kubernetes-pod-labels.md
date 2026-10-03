---
id: software.devops.tranche02.000162
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/grafana/loki/main/README.md", "https://grafana.com/docs/loki/latest/get-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Correlação direta entre métricas e logs usando os mesmos labels do Prometheus e de Pods Kubernetes

## Em uma frase
Na lista comparativa da abertura do README, o projeto destaca três diferenciais operacionais: o Loki indexa e agrupa streams de logs usando os **mesmos labels** que você já utiliza com o Prometheus (permitindo alternar perfeitamente entre métricas e logs com os mesmos seletores), é especialmente adequado para armazenar logs de Pods do Kubernetes (cujos metadados como Pod labels são automaticamente coletados e indexados) e possui suporte nativo no Grafana (a partir do Grafana `v6.0`).

## Por que importa
Durante a investigação de um incidente, perder minutos traduzindo o nome de um alerta do Prometheus para outro esquema de tags no sistema de logs atrasa o MTTR; compartilhar exatamente os mesmos labels (`namespace`, `pod`, `job`, `app`) permite saltar do gráfico de erro diretamente para os logs daquele pod no Grafana.

## Como funciona
Padronize o pipeline de coleta de logs para preservar os mesmos labels de descoberta de serviços do Kubernetes usados pelo Prometheus e configure o datasource nativo do Loki no Grafana.

## Exemplo
Ao observar um pico de erros HTTP 500 em um gráfico do Prometheus/Thanos no Grafana, o engenheiro abre o painel dividido com o Loki mantendo o mesmo seletor `{namespace="checkout", app="payments"}`.

## Limites e trade-offs
O suporte nativo no Grafana requer Grafana `v6.0` ou superior; mantenha o Grafana atualizado para aproveitar as integrações mais recentes de correlação entre métricas, logs e traces.

## Como verificar
Conferi a seção inicial do README oficial de `grafana/loki`.

## Conexões
- [[loki-prometheus-inspired-label-indexed-log-aggregation]] — Veja também: Definição do Loki: agregação de logs inspirada no Prometheus que indexa apenas labels.
- [[loki-three-component-stack-alloy-loki-grafana]] — Veja também: Pilha de três componentes (Alloy, Loki e Grafana) e transição do Promtail para o Grafana Alloy.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki Documentation — Get Started & Operations](https://grafana.com/docs/loki/latest/get-started/) — Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.; consultado em 2026-10-03.
