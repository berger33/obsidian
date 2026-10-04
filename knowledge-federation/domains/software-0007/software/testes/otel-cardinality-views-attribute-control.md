---
id: software.testes.tranche09.000317
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
fontes: ["https://opentelemetry.io/docs/specs/otel/metrics/sdk/", "https://opentelemetry.io/docs/specs/otel/metrics/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# OpenTelemetry: testar cardinalidade e views de métricas

## Em uma frase
Views e limites do SDK podem alterar agregação de atributos para conter crescimento de séries métricas.

## Por que importa
Testes de observabilidade verificam os dados produzidos pela aplicação antes de depender de um collector ou backend remoto. Atributo com ID de usuário ou URL dinâmica pode criar cardinalidade alta e custo de armazenamento descontrolado.

## Como funciona
Use SDK e exporters de memória em testes curtos, inspecione nomes, atributos, status e valores, e isole providers entre casos. Gere observações com valores variados e confirme que a configuração mantém somente dimensões permitidas.

## Exemplo
Milhares de IDs de pedido são removidos ou agregados conforme view, enquanto região permitida continua separando contadores.

## Limites e trade-offs
Representação final depende de SDK, exporter, pipeline e convenções semânticas; teste local não prova ingestão, retenção ou consulta no backend. Política de overflow e limites variam com SDK; teste não substitui medição de cardinalidade no collector/backend.

## Como verificar
Inspecione pontos após coleta em carga sintética e confirme atributo removido, limite aplicado e sinal de overflow.

## Conexões
- [[otel-log-trace-correlation-context]] — Veja também: OpenTelemetry: verificar correlação de logs com trace ativo.
- [[otel-test-provider-exporter-lifecycle]] — Veja também: OpenTelemetry: isolar exporter e provider entre testes.

## Fontes
- [OpenTelemetry — Metrics SDK](https://opentelemetry.io/docs/specs/otel/metrics/sdk/) — aggregation, views e exportação de métricas; consultado em 2026-10-02.
- [OpenTelemetry — Metrics API](https://opentelemetry.io/docs/specs/otel/metrics/api/) — instrumentos e observações de métricas; consultado em 2026-10-02.
