---
id: software.testes.tranche08.000234
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

# Prometheus: testar rate diante de reset de counter

## Em uma frase
Inclua amostras com reset de counter ao verificar expressões rate, sem assumir que contador é monotônico em toda janela.

## Por que importa
Reinício de processo zera counter e pode distorcer interpretação se query, range ou tipo da métrica estiverem incorretos.

## Como funciona
Crie séries de incremento e reset em timestamps conhecidos, avalie intervalo correspondente e compare resultado com semântica PromQL da função usada.

## Exemplo
Counter sobe, processo reinicia e valor volta a zero; teste verifica query rate sem transformar reset esperado em taxa negativa.

## Limites e trade-offs
Amostragem irregular e staleness em produção diferem do fixture; teste unitário não escolhe automaticamente janela adequada para tráfego real.

## Como verificar
Rode promtool com reset, lacuna e baixa frequência, inspecione resultado e compare query com métrica counter adequada.

## Conexões
- [[prometheus-vector-vazio-vs-zero]] — Veja também: Prometheus: diferenciar vetor vazio de valor zero.
- [[prometheus-recording-rule-expression-output]] — Veja também: Prometheus: testar recording rules e série resultante.

## Fontes
- [Prometheus — Query functions](https://prometheus.io/docs/prometheus/latest/querying/functions/) — semântica de funções e tipos de dados PromQL; consultado em 2026-10-02.
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
