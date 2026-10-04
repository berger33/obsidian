---
id: software.criacao_ia.tranche03.000289
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/5ca9052bc796ef1e497200b1d558fd87a201f335/docs/gen-ai/gen-ai-events.md", "https://opentelemetry.io/docs/specs/otel/logs/data-model/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI evaluation.result: correlacionar resultado ao output avaliado

## Em uma frase
O evento `gen_ai.evaluation.result` deve se ligar ao span da operação GenAI avaliada quando possível, ou usar response.id como correlação alternativa.

## Por que importa
Uma pontuação sem identidade da resposta pode ser associada à geração errada quando há retries, várias choices ou avaliações assíncronas. Modelar avaliação como evento separado conserva a distinção entre produzir uma resposta e julgar sua qualidade.

## Como funciona
Use o nome obrigatório `gen_ai.evaluation.result`; registre `gen_ai.evaluation.name` para indicar a métrica avaliada e score label/value quando aplicável. A convenção recomenda parentear o evento no span GenAI alvo; se o span id não estiver disponível, registre `gen_ai.response.id` quando possível. O label deve ter baixa cardinalidade e a lista de rótulos precisa ser documentada pelo evaluator.

## Exemplo
Um avaliador offline publica `gen_ai.evaluation.result` ligado ao trace da resposta que pontuou como relevante. Se avaliação ocorrer em outro job sem span original, inclui response.id e nome/versionamento da avaliação para relacioná-la ao registro de inference.

## Limites e trade-offs
Eventos e suas semconv estão em desenvolvimento e podem não estar implementados em todas as linguagens. Explanation textual pode ser extensa ou conter dados sensíveis; score não substitui o output avaliado e a correlação por ID depende de disponibilidade e escopo de retenção.

## Como verificar
Gere duas respostas e dois eventos de avaliação em ordem diferente; confirme parentage ou response.id correto, que labels pertencem a conjunto controlado e que métricas de pontuação não multiplicam spans de inference.

## Conexões
- [[otel-genai-conteudo-opt-in-minimizacao]] — OpenTelemetry GenAI: minimizar conteúdo de prompt e resposta na telemetria.
- [[otel-genai-conventions-development-status]] — OpenTelemetry GenAI semconv: interpretar o status Development antes de fixar integração.

## Fontes
- [OpenTelemetry GenAI — Events, revisão 5ca9052](https://github.com/open-telemetry/semantic-conventions-genai/blob/5ca9052bc796ef1e497200b1d558fd87a201f335/docs/gen-ai/gen-ai-events.md) — define nome, atributos, parentage e response.id para gen_ai.evaluation.result Consulta: 2026-10-04.
- [OpenTelemetry — Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) — define eventos como LogRecords e os campos de contexto de trace/span Consulta: 2026-10-04.
