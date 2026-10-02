---
id: software.testes.tranche09.000311
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
fontes: ["https://opentelemetry.io/docs/specs/otel/trace/api/", "https://opentelemetry.io/docs/languages/java/sdk/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: testar exceção e status de span separadamente

## Em uma frase
Registrar uma exceção como evento e marcar status de span são operações distintas que dependem do código instrumentado.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Um teste que só vê log da exception pode deixar span finalizado como sucesso e métricas de erro ausentes.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Force falha conhecida e examine eventos, status e duração do span conforme convenção implementada.

## Exemplo
Timeout da dependência produz exception event e marca resultado do span como erro sem registrar credencial ou payload sensível.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. SDK não converte automaticamente todo objeto Exception em status de erro em qualquer instrumentação.

## Como verificar
Compare caminho de sucesso e falha e valide o span exportado depois que escopo e operação terminarem.

## Conexões
- [[otel-inmemory-span-exporter-assertions]] — Veja também: OpenTelemetry: inspecionar spans com exporter em memória.
- [[otel-context-propagation-async-boundary]] — Veja também: OpenTelemetry: preservar contexto em fronteira assíncrona.

## Fontes
- [OpenTelemetry — Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/) — spans, eventos, atributos e status de trace; consultado em 2026-10-02.
- [OpenTelemetry Java — SDK](https://opentelemetry.io/docs/languages/java/sdk/) — SDK Java, configuração e utilitários de teste; consultado em 2026-10-02.
