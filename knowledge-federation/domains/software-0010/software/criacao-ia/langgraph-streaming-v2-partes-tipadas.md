---
id: software.criacao_ia.tranche03.000207
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/streaming", "https://docs.langchain.com/oss/python/langgraph/event-streaming"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: usar partes tipadas no streaming v2

## Em uma frase
O formato `version=v2` entrega cada chunk de streaming com os campos discriminantes `type`, `ns` e `data`.

## Por que importa
O formato antigo varia conforme se solicita um modo, vários modos ou saída de subgrafo, levando consumidores a ramificar por tuplas e formas diferentes. Um discriminante estável simplifica renderização de mensagens, snapshots de estado e progresso sem confundir dados de modos distintos.

## Como funciona
Passe `version=v2` a `stream()` ou `astream()` numa versão compatível do LangGraph e selecione os modos necessários, como `updates`, `messages` e `custom`. Faça narrowing por `chunk['type']` antes de interpretar `data`; `ns` informa o namespace de subgrafo quando aplicável. A documentação atual requer LangGraph 1.1 ou posterior para esse formato e recomenda event streaming para novas aplicações que preferem projeções tipadas de nível superior.

## Exemplo
Um painel de execução pode anexar chunks de `updates` ao estado visível e encaminhar `custom` para uma barra de progresso. A branch para `messages` extrai token e metadados próprios; nenhuma delas tenta converter todos os payloads num único tipo genérico.

## Limites e trade-offs
O parâmetro de versão precisa corresponder ao SDK instalado e o formato padrão documentado ainda pode diferir. O chunk `data` varia por modo e a ordem temporal de dois modos pode afetar a interface. Streaming não significa que a execução foi persistida ou concluída.

## Como verificar
Fixe a versão de LangGraph no ambiente de CI, teste cada tipo de chunk esperado e valide subgrafos e múltiplos modos. Compare o comportamento de consumidor v1 e v2 antes de migrar uma integração pública.

## Conexões
- [[langgraph-functional-api-task-result-checkpoint]] — LangGraph Functional API: persistir resultados com @task.
- [[langgraph-event-streaming-projecoes-concorrentes]] — LangGraph: consumir projeções do event streaming v3.

## Fontes
- [LangGraph — Streaming](https://docs.langchain.com/oss/python/langgraph/streaming) — especifica o envelope v2, seus campos e compatibilidade mínima indicada Consulta: 2026-10-04.
- [LangGraph — Event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) — apresenta a camada de projeções tipadas recomendada para novos fluxos Consulta: 2026-10-04.
