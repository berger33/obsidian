---
id: software.testes.tranche09.000312
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
fontes: ["https://opentelemetry.io/docs/concepts/context-propagation/", "https://opentelemetry.io/docs/specs/otel/trace/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: preservar contexto em fronteira assíncrona

## Em uma frase
Contexto carrega informações como span atual entre componentes e precisa ser propagado quando execução atravessa threads ou tarefas assíncronas.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Sem propagação, spans filhos aparecem desconectados apesar de a chamada funcional completar corretamente.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Use mecanismo de contexto da biblioteca compatível e mantenha escopo encerrado após a tarefa, inclusive quando ocorre erro.

## Exemplo
Serviço inicia chamada assíncrona de dependência e o teste confirma parent span comum na trace exportada.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Propagação automática depende da instrumentação e executor; contexto global pode vazar entre testes concorrentes.

## Como verificar
Execute tarefas em paralelo com trace IDs distintos e confirme parentesco correto e restauração do contexto no teardown.

## Conexões
- [[otel-span-error-status-exception]] — Veja também: OpenTelemetry: testar exceção e status de span separadamente.
- [[otel-resource-scope-instrumentation-identity]] — Veja também: OpenTelemetry: distinguir resource de instrumentation scope.

## Fontes
- [OpenTelemetry — Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/) — propagação de contexto através de fronteiras de execução; consultado em 2026-10-02.
- [OpenTelemetry — Trace API](https://opentelemetry.io/docs/specs/otel/trace/api/) — spans, eventos, atributos e status de trace; consultado em 2026-10-02.
