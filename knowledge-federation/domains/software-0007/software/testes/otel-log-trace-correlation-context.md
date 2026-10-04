---
id: software.testes.tranche09.000316
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
fontes: ["https://opentelemetry.io/docs/specs/otel/logs/data-model/", "https://opentelemetry.io/docs/concepts/context-propagation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: verificar correlação de logs com trace ativo

## Em uma frase
Modelo de logs OTel pode carregar trace ID e span ID quando um contexto válido está ativo durante a emissão.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Logs sem correlação em caminho assíncrono dificultam relacionar evento operacional à trace da requisição.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Capture log emitido no escopo de span e inspecione campos de trace/span no exporter ou bridge testado.

## Exemplo
Erro de cobrança é registrado dentro do span e o log do teste aponta para o mesmo trace ID da operação.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Correlação depende de bridge, logger e contexto; logs emitidos fora do escopo podem legitimamente não ter IDs.

## Como verificar
Teste logging síncrono e assíncrono, compare IDs e confirme que texto e atributos não contêm dados secretos.

## Conexões
- [[otel-histogram-buckets-boundaries]] — Veja também: OpenTelemetry: testar histograma por limites e distribuição.
- [[otel-cardinality-views-attribute-control]] — Veja também: OpenTelemetry: testar cardinalidade e views de métricas.

## Fontes
- [OpenTelemetry — Logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — campos de log e associação com trace/span; consultado em 2026-10-02.
- [OpenTelemetry — Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/) — propagação de contexto através de fronteiras de execução; consultado em 2026-10-02.
