---
id: software.devops.tranche02.000161
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

# Definição do Loki: agregação de logs inspirada no Prometheus que indexa apenas labels

## Em uma frase
O README oficial no repositório `grafana/loki` apresenta o projeto com o lema `"Loki: like Prometheus, but for logs"`, definindo-o como um sistema de agregação de logs escalável horizontalmente, altamente disponível e multi-tenant inspirado no Prometheus, projetado para ser muito econômico e fácil de operar por **não** indexar o conteúdo dos logs, mas sim um conjunto de labels para cada stream de log (`does not index the contents of the logs, but rather a set of labels for each log stream`).

## Por que importa
Sistemas tradicionais de busca que criam índices invertidos completos (full-text index) de cada palavra do log consomem grandes volumes de RAM, CPU e armazenamento; ao comprimir logs não estruturados e indexar apenas metadados (labels), o Loki reduz drasticamente o custo de operação.

## Como funciona
Implante o Loki para armazenar logs comprimidos em Object Storage ou disco, mantendo os conjuntos de labels enxutos e deixando a filtragem de texto para o momento da consulta.

## Exemplo
Uma plataforma que antes descartava logs de debug por alto custo de indexação passa a retê-los no Loki comprimidos e indexados apenas por cluster, namespace e aplicação.

## Limites e trade-offs
Evite colocar identificadores de cardinalidade ilimitada (como `user_id`, `request_id` ou endereços IP dinâmicos) dentro dos labels indexados do Loki; mantenha esses valores no corpo da linha de log.

## Como verificar
Conferi a abertura do README oficial de `grafana/loki`.

## Conexões
- [[loki-shared-prometheus-and-kubernetes-pod-labels]] — Veja também: Correlação direta entre métricas e logs usando os mesmos labels do Prometheus e de Pods Kubernetes.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki Documentation — Get Started & Operations](https://grafana.com/docs/loki/latest/get-started/) — Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.; consultado em 2026-10-03.
