---
id: software.devops.tranche02.000165
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
fontes: ["https://raw.githubusercontent.com/grafana/loki/main/README.md", "https://github.com/grafana/loki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Migração do Helm chart do Grafana Loki em março de 2026 para grafana-community/helm-charts

## Em uma frase
A subseção `⚠️ Helm Chart Migration` na seção `Getting started` do README emite um aviso operacional importante: a partir de **16 de março de 2026**, o Helm chart do Grafana Loki é bifurcado (forked) para o novo repositório `grafana-community/helm-charts` (`github.com/grafana-community/helm-charts`), enquanto o chart mantido dentro do repositório `grafana/loki` continuará sendo mantido apenas para usuários do Grafana Enterprise Logs (GEL), remetendo à issue `#20705` para detalhes.

## Por que importa
Pipelines de GitOps (Argo CD, Flux ou Helm) que continuarem apontando para a origem antiga esperando atualizações comunitárias do Loki open source após março de 2026 deixarão de receber as evoluções comunitárias do chart.

## Como funciona
Atualize as referências de repositório Helm em seus manifestos do Argo CD, Flux ou Helmfile para consumir o chart comunitário do Loki a partir de `grafana-community/helm-charts` caso utilize o Loki open source.

## Exemplo
Durante a revisão de dependências em 2026, a equipe de plataforma migra a fonte do HelmRelease do Loki para `grafana-community/helm-charts` conforme o aviso oficial da issue `#20705`.

## Limites e trade-offs
Antes de trocar a origem do chart em produção, execute `helm diff` ou revise os manifestos renderizados para verificar eventuais mudanças de defaults no chart comunitário.

## Como verificar
Conferi a subseção Helm Chart Migration no README oficial de `grafana/loki`.

## Conexões
- [[loki-push-model-and-single-binary-or-microservices]] — Veja também: Diferença entre o modelo push do Loki e o pull do Prometheus, em binário único ou microsserviços.
- [[loki-api-labels-docker-driver-and-grafana-datasource]] — Veja também: Seções essenciais da documentação: API de ingestão, Labels, Docker Driver Client e Grafana.

## Fontes
- [Grafana Loki — GitHub README](https://raw.githubusercontent.com/grafana/loki/main/README.md) — Visão geral do Loki (agregação de logs indexada por labels no estilo Prometheus), pilha Alloy + Loki + Grafana, migração do Helm chart em março de 2026, LogCLI, Loki Canary e build a partir do fonte.; consultado em 2026-10-03.
- [Grafana Loki — Repositório Oficial no GitHub](https://github.com/grafana/loki) — Repositório oficial do Grafana Loki com código-fonte em Go, cmd/loki/loki-local-config.yaml e Makefile.; consultado em 2026-10-03.
