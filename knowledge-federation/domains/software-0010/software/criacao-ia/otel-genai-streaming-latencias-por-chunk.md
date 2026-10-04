---
id: software.criacao_ia.tranche03.000287
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI streaming: distinguir time to first chunk de cadência

## Em uma frase
`time_to_first_chunk` mede a espera até o primeiro chunk; `time_per_output_chunk` mede intervalos entre chunks seguintes, não a duração completa.

## Por que importa
Uma resposta streamada pode começar rápido e depois produzir tokens lentamente, ou iniciar tarde e fluir bem após o primeiro fragmento. Um único número de latência não distingue essas experiências e pode direcionar incorretamente otimizações de servidor ou rede.

## Como funciona
Use `gen_ai.client.operation.time_to_first_chunk` para o intervalo entre emitir o request e receber o primeiro chunk. Registre `gen_ai.client.operation.time_per_output_chunk` para cada chunk depois do primeiro, medindo do fim do chunk anterior ao fim do atual. A semconv recomenda ambos para chamadas streamadas e não recomenda em chamadas sem streaming; compare com `gen_ai.client.operation.duration` para observar tempo total.

## Exemplo
Uma completion termina em 6,8 segundos, recebe seu primeiro chunk após 0,45 s e tem intervalos posteriores de 0,07–0,11 s. Os três sinais apontam para boa latência inicial, cadência relativamente estável e duração total, sem tratar time-to-first como tempo por token.

## Limites e trade-offs
Proxies e buffers podem alterar quando o cliente observa chunks em comparação com quando o modelo os produziu. Os nomes dos sinais e buckets recomendados estão sob convenções em desenvolvimento, e resultados dependem de uma definição consistente de início e fim de chunk.

## Como verificar
Teste stream que atrasa só o primeiro chunk, outro que pausa entre chunks e um request não streamado. Confirme que a primeira mudança altera apenas time-to-first, os intervalos seguintes são registrados individualmente e o modo não streamado não emite essas métricas.

## Conexões
- [[otel-genai-token-counters-versus-histograms]] — OpenTelemetry GenAI token metrics: contadores de uso não são histogramas por operação.
- [[otel-genai-conteudo-opt-in-minimizacao]] — OpenTelemetry GenAI: minimizar conteúdo de prompt e resposta na telemetria.

## Fontes
- [OpenTelemetry GenAI — Client metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md) — define duration, time_to_first_chunk e time_per_output_chunk para client calls Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Model spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md) — documenta o atributo de resposta time_to_first_chunk em streams Consulta: 2026-10-04.
