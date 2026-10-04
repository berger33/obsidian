---
id: software.criacao_ia.tranche03.000283
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/openai.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI: separar modelo solicitado de modelo que respondeu

## Em uma frase
`gen_ai.request.model` descreve o modelo pedido, enquanto `gen_ai.response.model` registra, quando conhecido, o modelo que efetivamente gerou a resposta.

## Por que importa
Aliases, roteamento de provider, deployments e modelos fine-tuned podem fazer o nome configurado divergir do modelo retornado. Sobrescrever o valor pedido com o valor observado elimina evidência útil para investigar routing, qualidade ou migrações graduais.

## Como funciona
Registre o nome exato enviado ao provider em `gen_ai.request.model` quando ele é disponibilizado; para modelo fine-tuned, a recomendação é usar um nome mais específico que o base model. Se a resposta informa um modelo efetivo, registre-o separadamente em `gen_ai.response.model`. Não fabrique o campo de resposta quando o provider não revela esse dado.

## Exemplo
O cliente solicita o alias `model-prod`, mas a resposta indica uma revisão concreta `model-2026-09-30`. Armazene o alias em request.model e a revisão informada em response.model, permitindo consultar mudanças de deployment sem reescrever o intent original.

## Limites e trade-offs
Nem todo provider retorna a identidade final e alguns deployments não expõem alias estável. A semconv trata response.model como recomendado e request.model como condicional à disponibilidade, portanto ausência não é automaticamente evidência de erro.

## Como verificar
Use uma resposta simulada com identidade efetiva diferente da solicitada e confira ambos atributos no span e nas métricas. Em agent span, não preencha request.model se o agente permite múltiplos modelos ou seleção dinâmica.

## Conexões
- [[otel-genai-operation-name-taxonomia]] — OpenTelemetry GenAI: padronizar gen_ai.operation.name sem apagar a operação real.
- [[otel-genai-span-logico-retries]] — OpenTelemetry GenAI spans: medir a operação lógica incluindo retries.

## Fontes
- [OpenTelemetry GenAI — Model spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md) — define campos separados para modelo pedido e modelo de resposta Consulta: 2026-10-04.
- [OpenTelemetry GenAI — OpenAI conventions, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/openai.md) — aplica as convenções ao provider OpenAI e mostra campos de request e response Consulta: 2026-10-04.
