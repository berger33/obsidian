---
id: software.criacao_ia.tranche03.000230
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
fontes: ["https://openai.github.io/openai-agents-python/tracing/", "https://openai.github.io/openai-agents-python/running_agents/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK tracing: descarregar spans antes de encerrar um job

## Em uma frase
O processador padrão de tracing exporta em background, então uma tarefa curta pode terminar antes de a trace aparecer no destino.

## Por que importa
Workers long-lived costumam manter a fila de spans aberta entre jobs, mas um consumidor pode interpretar atraso como perda. Encerrar o processo logo após a execução também torna importante verificar que a trace terminou e foi exportada depois do span externo.

## Como funciona
O SDK rastreia por padrão o run e spans de modelo, agentes, tools, guardrails e handoffs. Em tarefas de fundo que exigem garantia de entrega imediata, encerre o contexto `trace()` e então chame `flush_traces()` num bloco `finally`. O flush espera a exportação dos dados atualmente buffered; sem requisito de latência, exportação periódica padrão pode bastar.

## Exemplo
Um worker de build executa o agente dentro de uma trace nomeada, grava resultado e sai do contexto; no `finally`, descarrega spans mesmo se a etapa de build levantar uma exceção. Dashboards correlacionam o `group_id` de várias tentativas sem usar trace ID como autorização.

## Limites e trade-offs
Tracing não está disponível para organizações sujeitas a política Zero Data Retention documentada. Um flush não recupera eventos nunca gravados nem remove dados já bufferizados quando tracing é desativado. Inspecione processors customizados e política de dados antes de enviar conteúdo sensível.

## Como verificar
Teste execução normal e exceção em worker reiniciado logo após o job. Confirme que o flush ocorre depois do fechamento da trace, monitore falhas de exportação e verifique o comportamento sob tracing desabilitado e política ZDR.

## Conexões
- [[agents-sdk-session-input-callback-historico]] — Agents SDK Sessions: limitar histórico lido sem duplicar persistência.

## Fontes
- [OpenAI Agents SDK — Tracing](https://openai.github.io/openai-agents-python/tracing/) — descreve exportação em background e uso de `flush_traces()` após o contexto Consulta: 2026-10-04.
- [OpenAI Agents SDK — Running agents](https://openai.github.io/openai-agents-python/running_agents/) — explica ciclo de execução, erro e cancelamento que podem encerrar um job Consulta: 2026-10-04.
