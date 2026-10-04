---
id: software.criacao_ia.tranche03.000284
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI spans: medir a operação lógica incluindo retries

## Em uma frase
O span GenAI de inference representa a duração da operação lógica do cliente até a resposta completa, incluindo retries automáticos realizados dentro dela.

## Por que importa
Um span encerrado no primeiro chunk ou no primeiro erro transitório subestima a experiência observada pela aplicação. Contar cada retry como se fosse uma nova operação de negócio também pode inflar volume e confundir custo, erro e latência por pedido.

## Como funciona
Inicie o span quando a operação é iniciada e encerre quando a resposta for totalmente recebida ou a operação terminar por erro ou cancelamento. Para issue transitório com retry transparente, o span lógico deve abranger todo o período dos retries; instrumentação HTTP pode registrar tentativas em spans filhos distintos, sem mudar a unidade de operação GenAI.

## Exemplo
Uma chamada de chat tenta o provider por duas vezes após um timeout transitório e obtém a resposta na terceira tentativa. O span `chat {model}` cobre o tempo total; spans HTTP filhos podem mostrar cada tentativa, enquanto a métrica de operação registra a experiência completa do cliente.

## Limites e trade-offs
Uma semconv de client span não substitui visibilidade de tentativa, fila ou protocolo no servidor. O modelo local pode usar kind `INTERNAL`; uma chamada remota normalmente usa `CLIENT`, e a instrumentação do provider pode adicionar outros spans.

## Como verificar
Force um retry, um cancelamento e uma resposta streamada. Confirme horário de início/fim, estado de erro, kind e que a duração do span lógico cobre a sequência completa, não somente a primeira tentativa.

## Conexões
- [[otel-genai-modelo-solicitado-versus-resposta]] — OpenTelemetry GenAI: separar modelo solicitado de modelo que respondeu.
- [[otel-genai-agent-spans-client-internal-tool]] — OpenTelemetry GenAI agents: separar invocation remota, execução local e tool span.

## Fontes
- [OpenTelemetry GenAI — Model spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md) — define a duração do span de GenAI como operação lógica e inclui retries Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Client metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md) — define histogram de duração da operação GenAI do cliente Consulta: 2026-10-04.
