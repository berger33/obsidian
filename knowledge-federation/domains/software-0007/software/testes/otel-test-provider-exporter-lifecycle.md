---
id: software.testes.tranche09.000318
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
fontes: ["https://opentelemetry.io/docs/languages/java/sdk/", "https://opentelemetry.io/docs/concepts/instrumentation/libraries/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: isolar exporter e provider entre testes

## Em uma frase
Exporters e providers de teste acumulam ou fecham recursos segundo o lifecycle do SDK usado.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. State compartilhado deixa spans e pontos antigos aparecerem em assertions seguintes, especialmente com execução paralela.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Crie provider/exporter por fixture, encerre-o no teardown e evite compartilhar variáveis globais capturadas por múltiplos testes.

## Exemplo
Uma fixture cria SDK in-memory individual; dois testes paralelos emitem spans e cada um consulta apenas sua execução.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Encerramento e força de flush variam por implementação; não dependa de ordem de limpeza não documentada.

## Como verificar
Execute testes paralelos e repetidos, confirme contagem inicial vazia e recursos fechados após cada fixture.

## Conexões
- [[otel-cardinality-views-attribute-control]] — Veja também: OpenTelemetry: testar cardinalidade e views de métricas.
- [[otel-semconv-versioned-attributes]] — Veja também: OpenTelemetry: versionar assertions de semantic conventions.

## Fontes
- [OpenTelemetry Java — SDK](https://opentelemetry.io/docs/languages/java/sdk/) — SDK Java, configuração e utilitários de teste; consultado em 2026-10-02.
- [OpenTelemetry — Instrumentation libraries](https://opentelemetry.io/docs/concepts/instrumentation/libraries/) — instrumentação, API/SDK e geração de telemetria; consultado em 2026-10-02.
