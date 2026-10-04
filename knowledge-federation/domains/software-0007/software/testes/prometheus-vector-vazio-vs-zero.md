---
id: software.testes.tranche08.000235
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://prometheus.io/docs/prometheus/latest/querying/functions/", "https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: diferenciar vetor vazio de valor zero

## Em uma frase
Teste explicitamente se ausência de série deve significar zero, estado desconhecido ou ausência de alerta.

## Por que importa
Query com vetor vazio pode produzir comportamento diferente de uma amostra cujo valor é zero e alterar dashboards ou alertas.

## Como funciona
Forneça cenário sem amostra e com zero, examine operadores e funções e defina fallback somente quando semântica do domínio permitir.

## Exemplo
Sem tráfego, taxa pode não existir; com tráfego sem erro, taxa é zero. Alerta de disponibilidade cobre ambos conforme requisito explícito.

## Limites e trade-offs
Aplicar `or vector(0)` indiscriminadamente pode ocultar falha de scrape ou série ausente que deveria gerar alerta próprio.

## Como verificar
Execute casos de série ausente, zero e stale; confira output da query e alertas associados a falha de telemetria.

## Conexões
- [[prometheus-alert-no-data-scrape-failure]] — Veja também: Prometheus: separar condição saudável de ausência de telemetria.
- [[prometheus-rate-counter-reset]] — Veja também: Prometheus: testar rate diante de reset de counter.

## Fontes
- [Prometheus — Query functions](https://prometheus.io/docs/prometheus/latest/querying/functions/) — semântica de funções e tipos de dados PromQL; consultado em 2026-10-02.
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
