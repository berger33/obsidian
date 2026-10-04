---
id: software.criacao_ia.tranche03.000205
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/graph-api", "https://docs.langchain.com/oss/python/langgraph/checkpointers"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: combinar atualizações paralelas com reducers

## Em uma frase
Nós ativados no mesmo super-step podem executar em paralelo, e reducers definem como suas atualizações sobre um canal compartilhado são aplicadas.

## Por que importa
Duas ramificações podem concluir em ordem não determinística. Se ambas escreverem no mesmo campo sem uma regra de combinação apropriada, o grafo pode rejeitar a atualização ou produzir um estado que não representa o resultado desejado. O reducer faz parte do contrato de estado, não é apenas uma otimização.

## Como funciona
Defina o schema de estado por canal e associe reducers para campos que recebem contribuições concorrentes. Uma lista pode usar concatenação, enquanto contadores e mapas podem exigir funções específicas com propriedades de associatividade. Após o super-step, o runtime consolida as escritas e cria o checkpoint correspondente. Se o valor final precisar ser determinístico, projete a redução para não depender da ordem de chegada.

## Exemplo
Um agente que consulta três fontes em paralelo pode devolver um item por resultado e usar um reducer de concatenação no canal `evidence`. Se a ordem for importante, inclua índice de fonte nos itens e ordene numa etapa seguinte em vez de supor que tarefas paralelas terminam numa sequência fixa.

## Limites e trade-offs
Um reducer não coordena transações externas nem remove duplicatas por si só. Funções de redução mutáveis ou não determinísticas podem dificultar replay e teste. Alterar o schema sem migração pode tornar checkpoints antigos incompatíveis.

## Como verificar
Execute as ramificações em ordem variável e injete falhas em uma delas. Verifique o valor consolidado, duplicatas e retomada após falha, além de comparar um checkpoint salvo com o schema de estado que o consumirá.

## Conexões
- [[langgraph-checkpointer-versus-store]] — LangGraph: separar checkpointer de store de longo prazo.
- [[langgraph-functional-api-task-result-checkpoint]] — LangGraph Functional API: persistir resultados com @task.

## Fontes
- [LangGraph — Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) — define estado, canais, reducers e execução em super-steps Consulta: 2026-10-04.
- [LangGraph — Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) — explica checkpoints de limite de super-step e escritas de tarefas paralelas Consulta: 2026-10-04.
