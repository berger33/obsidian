---
id: software.devops.tranche02.000164
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

# Diferença entre o modelo push do Loki e o pull do Prometheus, em binário único ou microsserviços

## Em uma frase
O README oficial contrasta diretamente os dois projetos: o Loki é como o Prometheus para logs por preferir uma abordagem multidimensional baseada em labels e buscar um sistema de **binário único** (`single-binary`), fácil de operar e sem dependências obrigatórias, mas difere do Prometheus por focar em logs em vez de métricas e por entregar logs via **push** em vez de **pull**, além de destacar na seção `Further Reading` o artigo arquitetural `"How We Designed Loki to Work Easily Both as Microservices and as Monoliths"`.

## Por que importa
Ao contrário de métricas agregadas que podem ser raspadas periodicamente por HTTP pull, eventos de log são gerados continuamente e precisam ser empurrados (push) pelos agentes conforme ocorrem; além disso, compilar o mesmo código para rodar como monólito de binário único ou como microsserviços distribuídos permite escalar gradualmente.

## Como funciona
Opere o Loki em modo de binário único para ambientes pequenos, laboratórios ou borda e distribua os alvos em modo de microsserviços quando o volume diário de ingestão e consulta exigir escalonamento independente de leitura e escrita.

## Exemplo
Uma startup inicia com o binário único do Loki conectado a um bucket de objetos e, conforme o tráfego cresce para múltiplos terabytes diários, passa a escalar os componentes em modo de microsserviços usando a mesma imagem.

## Limites e trade-offs
No modelo push, picos repentinos de logs em loop (log storms) empurrados pelos agentes podem saturar a ingestão; configure limites de taxa (rate limits) por tenant e por stream no Loki.

## Como verificar
Conferi a abertura e a seção Further Reading no README oficial de `grafana/loki`.

## Conexões
- [[loki-three-component-stack-alloy-loki-grafana]] — Veja também: Pilha de três componentes (Alloy, Loki e Grafana) e transição do Promtail para o Grafana Alloy.
- [[loki-helm-chart-migration-march-2026]] — Veja também: Migração do Helm chart do Grafana Loki em março de 2026 para grafana-community/helm-charts.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki Documentation — Get Started & Operations](https://grafana.com/docs/loki/latest/get-started/) — Documentação oficial do Grafana Loki cobrindo instalação, Grafana Alloy, labels, LogCLI e Loki Canary.; consultado em 2026-10-03.
