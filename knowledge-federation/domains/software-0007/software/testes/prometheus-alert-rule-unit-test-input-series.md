---
id: software.testes.tranche08.000230
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
fontes: ["https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/", "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: testar alert rules com séries controladas

## Em uma frase
Use promtool test rules para fornecer séries de entrada e validar quando alertas disparam ou deixam de disparar.

## Por que importa
Testes com tempo e amostras conhecidos tornam mudanças em expressão, labels e janelas mais fáceis de revisar.

## Como funciona
Declare arquivo de regras, séries de input, instante de avaliação e expectativa do alerta. Inclua caso positivo e negativo em momentos relevantes.

## Exemplo
Uma série ultrapassa limite durante período suficiente e o teste espera alerta; série abaixo do limite não deve produzir firing.

## Limites e trade-offs
Teste unitário valida semântica da regra sobre dados artificiais, não ingestão real, roteamento Alertmanager ou resposta operacional.

## Como verificar
Execute promtool no mesmo arquivo versionado, confirme instante, labels e annotations esperados e reveja falha em séries de fronteira.

## Conexões
- [[prometheus-alert-for-pending-firing]] — Veja também: Prometheus: cobrir estados pending e firing de alertas.
- [[prometheus-alert-labels-annotations-invariantes]] — Veja também: Prometheus: validar labels e annotations de alertas.

## Fontes
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
- [Prometheus — Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) — expressões, for duration, labels e annotations de alertas; consultado em 2026-10-02.
