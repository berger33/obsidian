---
id: software.criacao_ia.tranche03.000203
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/use-time-travel", "https://docs.langchain.com/oss/python/langgraph/interrupts"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: escolher replay ou fork no time travel

## Em uma frase
Replay repete a execução a partir de um checkpoint; fork cria uma ramificação histórica com estado alterado, sem apagar a linha original.

## Por que importa
Usar o recurso certo evita interpretar uma reexecução como consulta passiva ao cache. Nós posteriores ao checkpoint executam novamente, então chamadas de modelo, APIs e interrupts podem retornar valores diferentes ou repetir efeitos externos. O fork é útil para explorar uma alternativa mantendo a história anterior.

## Como funciona
Use `get_state_history` para escolher o checkpoint. Para replay, invoque o grafo com a configuração daquele ponto; para fork, aplique `update_state` nesse checkpoint e continue com a nova configuração. `update_state` não rebobina nem modifica retroativamente a thread antiga: produz um novo checkpoint derivado. Em caminhos paralelos, informe `as_node` quando a origem do update não puder ser inferida sem ambiguidade.

## Exemplo
Num fluxo de geração de missão, repita desde o estado imediatamente anterior ao nó que escolhe a recompensa para observar o comportamento atual do modelo. Para comparar uma recompensa alternativa, faça fork com estado ajustado e execute a continuação separada; registre ambos os IDs de checkpoint no relatório de QA.

## Limites e trade-offs
Replay não é uma leitura de resultados armazenados e pode refazer operações externas. Interrupts acionam uma nova pausa e exigem nova resposta. O grafo precisa de checkpointer e os reducers continuam determinando como updates são combinados.

## Como verificar
Compare a sequência de nós antes e depois do checkpoint, inspecione `next` e os IDs gerados, e use um serviço de teste que conte chamadas externas. Confirme que o histórico da execução original continua disponível depois do fork.

## Conexões
- [[langgraph-thread-id-e-checkpoint-id]] — LangGraph: distinguir thread_id de checkpoint_id.
- [[langgraph-checkpointer-versus-store]] — LangGraph: separar checkpointer de store de longo prazo.

## Fontes
- [LangGraph — Time travel](https://docs.langchain.com/oss/python/langgraph/use-time-travel) — define replay, fork, `update_state`, `as_node` e repetição de nós posteriores Consulta: 2026-10-04.
- [LangGraph — Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — documenta a interação entre interrupções, checkpoint e nova retomada Consulta: 2026-10-04.
