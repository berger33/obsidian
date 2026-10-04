---
id: software.criacao_ia.tranche03.000282
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
fontes: ["https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md", "https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-agent-spans.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenTelemetry GenAI: padronizar gen_ai.operation.name sem apagar a operação real

## Em uma frase
`gen_ai.operation.name` usa uma taxonomia de ações GenAI, não necessariamente o nome literal do endpoint ou método do SDK.

## Por que importa
Duas bibliotecas podem chamar a mesma ação de nomes diferentes, dificultando comparar latência, erro e custo. A taxonomia publicada inclui operações de inferência, embeddings, retrieval, agentes, ferramentas, memória e workflows, refletindo que uma execução de IA é maior que uma única chamada ao modelo.

## Como funciona
Quando um valor conhecido corresponde à ação — por exemplo `chat`, `generate_content`, `embeddings`, `retrieval`, `invoke_agent` ou `execute_tool` — a semconv indica que esse valor deve ser usado. Se um sistema específico tiver uma operação diferente, documente-a nas convenções próprias do sistema; instrumentações devem preferir o valor conhecido aplicável quando o nome customizado não estiver documentado.

## Exemplo
Uma chamada multimodal do Gemini pode usar `generate_content`; uma chamada de chat corresponde a `chat`; o passo que executa uma ferramenta é `execute_tool`, não uma segunda inferência. Um wrapper interno chamado `run_model_v4` não deve substituir o valor semântico apenas porque esse é o nome da função local.

## Limites e trade-offs
A lista e o status das convenções GenAI consultadas estão em desenvolvimento, e operações de SDK podem combinar várias ações sem equivalência um-para-um. Não converta automaticamente nomes customizados antigos sem verificar o que cada instrumentação mede.

## Como verificar
Compare eventos de uma operação simples e de um fluxo com agente; valide que a mesma ação mantém o mesmo operation.name entre providers e que ações diferentes não colapsam em `chat`.

## Conexões
- [[otel-genai-provider-name-perspectiva]] — OpenTelemetry GenAI: interpretar gen_ai.provider.name pela perspectiva da instrumentation.
- [[otel-genai-modelo-solicitado-versus-resposta]] — OpenTelemetry GenAI: separar modelo solicitado de modelo que respondeu.

## Fontes
- [OpenTelemetry GenAI — Model spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-spans.md) — lista nomes conhecidos de operação e critérios para valores específicos de sistemas Consulta: 2026-10-04.
- [OpenTelemetry GenAI — Agent spans, revisão b9ecbae](https://github.com/open-telemetry/semantic-conventions-genai/blob/b9ecbaef4ac462cc2b6f7f7763b2cff1d15d5400/docs/gen-ai/gen-ai-agent-spans.md) — distingue invoke_agent, invoke_workflow, plan e execute_tool no domínio de agentes Consulta: 2026-10-04.
