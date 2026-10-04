---
id: software.testes.tranche09.000314
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://opentelemetry.io/docs/languages/java/sdk/", "https://opentelemetry.io/docs/specs/otel/metrics/sdk/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: testar agregação de métricas em memória

## Em uma frase
Reader de métricas em memória permite consultar medidas agregadas por instruments configurados no SDK sem consultar backend.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Verificar somente que instrumento foi criado não confirma valor, atributos ou agregação observados após a operação.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Execute fluxo controlado, force coleta e confira tipo de instrumento, pontos de dados e atributos esperados.

## Exemplo
Duas chamadas válidas incrementam counter por rota; o teste espera total e labels de baixa cardinalidade.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Temporality e agregação dependem do reader/exporter e da configuração do SDK de teste.

## Como verificar
Compare counter, histograma e conjunto de atributos na saída coletada e crie novo provider para cada caso.

## Conexões
- [[otel-resource-scope-instrumentation-identity]] — Veja também: OpenTelemetry: distinguir resource de instrumentation scope.
- [[otel-histogram-buckets-boundaries]] — Veja também: OpenTelemetry: testar histograma por limites e distribuição.

## Fontes
- [OpenTelemetry Java — SDK](https://opentelemetry.io/docs/languages/java/sdk/) — SDK Java, configuração e utilitários de teste; consultado em 2026-10-02.
- [OpenTelemetry — Metrics SDK](https://opentelemetry.io/docs/specs/otel/metrics/sdk/) — aggregation, views e exportação de métricas; consultado em 2026-10-02.
