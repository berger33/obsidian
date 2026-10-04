---
id: software.testes.tranche09.000313
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
fontes: ["https://opentelemetry.io/docs/concepts/instrumentation/libraries/", "https://opentelemetry.io/docs/specs/otel/trace/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: distinguir resource de instrumentation scope

## Em uma frase
Resource identifica a entidade que produz telemetria, enquanto instrumentation scope identifica biblioteca ou componente de instrumentação.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Confundir os dois pode atribuir versão de biblioteca ao serviço ou duplicar nomes de serviço entre sinais.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Configure resource e scope de forma separada e valide os metadados exportados junto ao span ou métrica.

## Exemplo
Dois componentes compartilham service.name, mas expõem scopes e versões de instrumentação distintos no exporter.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Atributos disponíveis variam por SDK e pipeline; não assuma que todo backend preserva metadados iguais.

## Como verificar
Inspecione resource e scope em sinal de teste e compare configuração com o deployment esperado.

## Conexões
- [[otel-context-propagation-async-boundary]] — Veja também: OpenTelemetry: preservar contexto em fronteira assíncrona.
- [[otel-inmemory-metrics-reader-aggregation]] — Veja também: OpenTelemetry: testar agregação de métricas em memória.

## Fontes
- [OpenTelemetry — Instrumentation libraries](https://opentelemetry.io/docs/concepts/instrumentation/libraries/) — instrumentação, API/SDK e geração de telemetria; consultado em 2026-10-02.
- [OpenTelemetry — Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/) — spans, eventos, atributos e status de trace; consultado em 2026-10-02.
