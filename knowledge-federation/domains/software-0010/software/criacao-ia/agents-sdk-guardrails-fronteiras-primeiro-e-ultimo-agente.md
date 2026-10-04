---
id: software.criacao_ia.tranche03.000224
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
fontes: ["https://openai.github.io/openai-agents-python/guardrails/", "https://openai.github.io/openai-agents-python/handoffs/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK guardrails: mapear fronteiras de primeiro e último agente

## Em uma frase
Input guardrails de agente rodam no primeiro agente da cadeia e output guardrails no agente que produz a saída final; tool guardrails cobrem chamadas de function tool guardadas.

## Por que importa
Numa orquestração multiagente, assumir que cada agente repete automaticamente a mesma checagem deixa lacunas. No modo paralelo padrão, a execução do agente pode começar enquanto input guardrail ainda avalia, permitindo consumo e efeitos antes de um tripwire.

## Como funciona
Desenhe verificações pelo limite que precisam proteger: bloqueio antes de qualquer trabalho pede `run_in_parallel=False`; validação por ferramenta usa input e output tool guardrails; revisão da resposta final usa output guardrail no agente final. Ferramentas locais MCP podem receber guardrails quando configuradas, mas handoffs não são cobertos por function-tool guardrails. Autorização do servidor MCP permanece no próprio servidor.

## Exemplo
Um pipeline de geração usa input guardrail bloqueante antes do primeiro modelo para rejeitar um projeto não autorizado, ferramenta de publicação com checagem por chamada, e output guardrail na resposta final. O triage agent não é considerado o agente final se transferir o controle para outro especialista.

## Limites e trade-offs
Um output guardrail valida resultado depois que a ferramenta já executou; não desfaz o efeito externo. Guardrails não substituem permissões do sistema, e o comportamento de persistência em falhas de tripwire deve ser examinado no fluxo de sessão.

## Como verificar
Teste primeira chamada, handoff, tool call, aprovação pendente e saída final; instrumente início da execução para confirmar que o guardrail bloqueante termina antes. Verifique que tools e handoffs aplicam autorização dentro dos respectivos callbacks.

## Conexões
- [[agents-sdk-on-handoff-autorizacao-antes-de-efeitos]] — Agents SDK: validar handoff input em on_handoff.
- [[agents-sdk-streaming-drenar-ate-fim]] — Agents SDK streaming: consumir eventos até o iterador terminar.

## Fontes
- [OpenAI Agents SDK — Guardrails](https://openai.github.io/openai-agents-python/guardrails/) — define fronteiras de input/output, execução paralela e tool guardrails Consulta: 2026-10-04.
- [OpenAI Agents SDK — Handoffs](https://openai.github.io/openai-agents-python/handoffs/) — confirma que handoff arguments exigem validação própria e não recebem tool guardrails Consulta: 2026-10-04.
