---
id: software.testes.tranche08.000236
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

# Prometheus: testar agregação e preservação de labels

## Em uma frase
Declare quais labels a agregação deve preservar e quais devem desaparecer para manter significado e cardinalidade previsíveis.

## Por que importa
Agrupar por label errado mistura serviços ou cria séries demais, prejudicando interpretação e custo de monitoramento.

## Como funciona
Construa input com valores de múltiplas dimensões e compare conjunto de labels e amostras da expressão agregada.

## Exemplo
Consulta soma erros por serviço e remove instance; teste garante que dois serviços continuam separados e réplicas são agregadas.

## Limites e trade-offs
Número baixo em fixture não revela crescimento cardinalidade sob produção; política de label exige análise de origem e escala.

## Como verificar
Inclua label inesperada, conte séries após regra e examine se output permite responder pergunta operacional pretendida.

## Conexões
- [[prometheus-recording-rule-expression-output]] — Veja também: Prometheus: testar recording rules e série resultante.
- [[prometheus-rate-counter-reset]] — Veja também: Prometheus: testar rate diante de reset de counter.

## Fontes
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
- [Prometheus — Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) — avaliação e regras de gravação; consultado em 2026-10-02.
