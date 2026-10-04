---
id: software.devops.tranche02.000163
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

# Pilha de três componentes (Alloy, Loki e Grafana) e transição do Promtail para o Grafana Alloy

## Em uma frase
O README oficial explica que uma pilha de logging baseada no Loki consiste em três componentes: **Alloy** (`github.com/grafana/alloy`, o agente responsável por coletar logs e enviá-los ao Loki), **Loki** (`github.com/grafana/loki`, o serviço principal responsável por armazenar logs e processar consultas) e **Grafana** (`github.com/grafana/grafana`, para consultar e exibir os logs), trazendo uma nota explícita em negrito: o **Alloy substituiu o Promtail** na pilha porque o Promtail é considerado feature complete e o desenvolvimento futuro para coleta de logs ocorrerá no Grafana Alloy.

## Por que importa
Equipes que ainda iniciam novos projetos instalando o Promtail por hábito de tutoriais antigos ficam presas a um coletor considerado encerrado em novas funcionalidades, perdendo a convergência de telemetria do Grafana Alloy.

## Como funciona
Em novas implantações e migrações da pilha Loki, adote o **Grafana Alloy** (`grafana.com/docs/loki/latest/send-data/alloy/`) como agente coletor oficial nos nós ou ambientes de aplicação.

## Exemplo
Uma equipe de plataforma atualiza seus DaemonSets de coleta nos clusters Kubernetes, substituindo o Promtail pelo Grafana Alloy para enviar logs ao Loki.

## Limites e trade-offs
Agentes alternativos do ecossistema (como Fluent Bit, Vector ou OpenTelemetry Collector) também podem enviar logs para a API de push do Loki conforme a arquitetura da organização.

## Como verificar
Conferi a abertura e a seção Getting started no README oficial de `grafana/loki`.

## Conexões
- [[loki-shared-prometheus-and-kubernetes-pod-labels]] — Veja também: Correlação direta entre métricas e logs usando os mesmos labels do Prometheus e de Pods Kubernetes.
- [[loki-push-model-and-single-binary-or-microservices]] — Veja também: Diferença entre o modelo push do Loki e o pull do Prometheus, em binário único ou microsserviços.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki Documentation — Get Started & Operations](https://grafana.com/docs/loki/latest/get-started/) — Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.; consultado em 2026-10-03.
