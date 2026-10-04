---
id: software.criacao_ia.tranche03.000221
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
fontes: ["https://openai.github.io/openai-agents-python/multi_agent/", "https://openai.github.io/openai-agents-python/tools/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK: escolher Agent.as_tool ou handoff

## Em uma frase
Com `Agent.as_tool()`, o agente gerente conserva o controle da conversa; com handoff, o especialista escolhido passa a ser o agente ativo do restante do turno.

## Por que importa
Ambos os padrões delegam trabalho, mas diferem em quem sintetiza a resposta e conduz a interação seguinte. Escolher a forma errada pode produzir respostas desconexas, uma hierarquia de aprovação difícil de auditar ou contexto duplicado entre agente coordenador e especialista.

## Como funciona
Use agentes como tools para pedir tarefas delimitadas e reunir várias contribuições sob uma resposta final do gerente. Use handoffs para encaminhar a conversa a um especialista cuja voz e instruções devem governar a continuação. O gerente pode combinar as duas técnicas. Avalie também contexto compartilhado, histórico passado ao especialista e guardrails do caminho.

## Exemplo
Um assistente de produção pode chamar `TextureReviewer.as_tool()` para receber uma lista de defeitos e incorporar os itens num plano único. Para um pedido de suporte que deve ser respondido diretamente por especialista de faturamento, o agente de triagem faz handoff para esse agente.

## Limites e trade-offs
O padrão de orquestração não é política de segurança nem garante qualidade da delegação. Um especialista como tool pode receber input e contexto de execução conforme configuração; handoff pode manter histórico, salvo se um filtro ou configuração o alterar.

## Como verificar
Registre agente ativo, itens gerados, respostas de especialistas e handoffs. Compare número de chamadas, contexto visível e autor da resposta final em uma avaliação para cada forma de delegação.

## Conexões
- [[agents-sdk-handoff-destino-fixo]] — Agents SDK handoff: modelar destinos como roteamento explícito.

## Fontes
- [OpenAI Agents SDK — Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) — compara explicitamente controle do gerente em Agent-as-tool com transferência por handoff Consulta: 2026-10-04.
- [OpenAI Agents SDK — Tools](https://openai.github.io/openai-agents-python/tools/) — documenta `Agent.as_tool()` e as categorias de tools do SDK Consulta: 2026-10-04.
