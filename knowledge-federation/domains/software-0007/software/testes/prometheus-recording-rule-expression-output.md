---
id: software.testes.tranche08.000233
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
fontes: ["https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/", "https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: testar recording rules e série resultante

## Em uma frase
Valide nome, valor e labels da série gravada, incluindo ausência de resultado quando expressão não deve produzir amostra.

## Por que importa
Recording rule incorreta pode propagar métrica derivada errada para dashboards e alertas sem chamar atenção imediata.

## Como funciona
Forneça input series e evaluation time e compare expected samples da regra; teste agregações por label e comportamento em ausência de entrada.

## Exemplo
Uma regra agrega requisições por serviço; teste espera valor correto para cada label e não cria série para serviço sem amostra.

## Limites e trade-offs
Uma série gravada não garante scrape, retenção ou cardinalidade saudável em produção; regra real precisa ser observada após deploy.

## Como verificar
Execute promtool test rules, confronte valor e labels e valide query no Prometheus de teste para compatibilidade com uso downstream.

## Conexões
- [[prometheus-alert-rule-unit-test-input-series]] — Veja também: Prometheus: testar alert rules com séries controladas.
- [[prometheus-aggregation-labels-cardinality]] — Veja também: Prometheus: testar agregação e preservação de labels.

## Fontes
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
- [Prometheus — Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) — avaliação e regras de gravação; consultado em 2026-10-02.
