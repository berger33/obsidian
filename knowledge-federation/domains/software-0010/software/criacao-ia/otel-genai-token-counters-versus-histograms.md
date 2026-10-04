---
id: software.criacao_ia.tranche03.000286
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-token-metrics.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI token metrics: contadores de uso não são histogramas por operação

## Em uma frase
As convenções separam contadores monotônicos de consumo de tokens de histogramas que mostram a distribuição por operação.

## Por que importa
Somar percentis de operações como se fossem faturamento produz totais errados; por outro lado, contar dimensões detalhadas de cache como tokens adicionais duplica subconjuntos. Instrumentar os dois grupos com semânticas explícitas permite estimar gasto e observar outliers sem confundir as perguntas.

## Como funciona
As métricas `gen_ai.client.inference.usage.*` são os instrumentos primários para acompanhar uso ao longo do tempo e aproximação de custo; se o provider informa contagem faturada e consumida, a convenção pede reportar a faturada. `gen_ai.client.inference.operation.input_tokens` e `...output_tokens` são histogramas de distribuição, úteis para percentis e extremos, não para total ou custo. Cache e reasoning são subconjuntos dos totais; tokens de uso são divididos por `gen_ai.token.modality`, enquanto os histogramas por operação não devem ser particionados por modalidade para percentis sem sentido.

## Exemplo
Para uma request com 300 tokens de entrada, sendo 40 de cache e 200 de imagem, o contador total continua sendo 300; as métricas detalhadas podem explicar cache e modalidade sem adicioná-los novamente. Use p95 do histograma para observar requests grandes, mas não como total de tokens faturados.

## Limites e trade-offs
Tokens podem não estar disponíveis, ser estimados ou usar unidades específicas de provider. Modality `unknown` é preferível a inventar uma separação quando provider e instrumentation não conseguem determiná-la de modo confiável.

## Como verificar
Com uma fixture multimodal que inclui tokens de cache, confira a inclusão nos totais e subconjuntos. Compare o somatório de contadores com dados billed do provider e valide que consultas de percentil usam os histogramas sem quebrar modality.

## Conexões
- [[otel-genai-agent-spans-client-internal-tool]] — OpenTelemetry GenAI agents: separar invocation remota, execução local e tool span.
- [[otel-genai-streaming-latencias-por-chunk]] — OpenTelemetry GenAI streaming: distinguir time to first chunk de cadência.

## Fontes
- [OpenTelemetry GenAI — Inference token metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-token-metrics.md) — define counters de uso, histogramas por operação, subsets de cache/reasoning e cautela de modality Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Client metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md) — separa token instruments das métricas de duração de operação Consulta: 2026-10-04.
