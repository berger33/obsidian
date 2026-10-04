---
id: software.criacao_ia.tranche03.000285
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-agent-spans.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI agents: separar invocation remota, execução local e tool span

## Em uma frase
As convenções GenAI distinguem invocation remota de agente (`CLIENT`), execução do agente no mesmo processo (`INTERNAL`) e execução de ferramenta (`execute_tool`).

## Por que importa
Sem essa separação, um trace não mostra se o atraso está no serviço de agente, no raciocínio local, numa inferência ou numa ferramenta externa. IDs transientes de instância também geram falsa identidade e atrapalham comparar execuções do mesmo agente hospedado.

## Como funciona
Para agente remoto, use operação `invoke_agent` e kind `CLIENT`; para agente implementado no próprio processo, a convenção descreve kind `INTERNAL` e associa o span à entidade `gen_ai.main_agent`. Ferramentas possuem operação própria `execute_tool`. Em agente hospedado, `gen_ai.agent.id` deve representar um identificador estável dado pelo provider; evitar IDs de objetos em memória que mudam a cada invocação.

## Exemplo
Uma chamada remota a um agente hospedado aparece como `invoke_agent` com seu identificador de recurso; dentro de um agente local, uma etapa invoca `execute_tool` para consultar um catálogo. A inferência subsequente, se instrumentada, continua representada como operação de inferência distinta.

## Limites e trade-offs
Nem toda framework expõe uma identidade estável, e nem toda integração oferece os mesmos pontos de instrumentação. A documentação observada está em desenvolvimento; não inferir um vínculo causal ou tipo de span que a instrumentação não registra.

## Como verificar
Monte um fluxo remoto e outro local; verifique kind, operation.name, entidade associada e parentage real no trace. Confirme que um agent instance novo não altera o id estável do agente hospedado.

## Conexões
- [[otel-genai-span-logico-retries]] — OpenTelemetry GenAI spans: medir a operação lógica incluindo retries.
- [[otel-genai-token-counters-versus-histograms]] — OpenTelemetry GenAI token metrics: contadores de uso não são histogramas por operação.

## Fontes
- [OpenTelemetry GenAI — Agent spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-agent-spans.md) — especifica invoke_agent remoto/local, execute_tool e entidade gen_ai.main_agent Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Agent metrics, revisão 8ffdf56](https://github.com/open-telemetry/semantic-conventions-genai/blob/8ffdf568e1b4391a99adb081db16e8102e36918e/docs/gen-ai/gen-ai-metrics.md) — define métricas próprias para duração de agente, inference calls e tool calls Consulta: 2026-10-04.
