---
id: software.criacao_ia.tranche03.000206
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/functional-api", "https://docs.langchain.com/oss/python/langgraph/persistence"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph Functional API: persistir resultados com @task

## Em uma frase
Na Functional API, `@task` marca trabalho discreto cujo resultado pode ser recuperado do checkpoint quando um entrypoint é retomado.

## Por que importa
Separar chamadas demoradas de etapas que podem pausar evita refazer trabalho já concluído após uma interrupção. Isso é valioso para síntese de assets, compilação de um projeto ou requisições de dados usadas antes de solicitar aprovação humana. O benefício depende do resultado realmente ter sido salvo no checkpoint.

## Como funciona
Marque a função de trabalho com `@task` e coordene-a dentro de um `@entrypoint` compilado com checkpointer. Resolva o future da task e use seu resultado na etapa seguinte. Na retomada do entrypoint, o runtime pode reutilizar o resultado da task persistido para aquele checkpoint, enquanto a função do entrypoint percorre novamente o fluxo. Mantenha a task determinística ou idempotente quando efeitos externos não puderem ser repetidos.

## Exemplo
Gere uma prévia de textura numa task, apresente o hash da imagem num interrupt para aprovação e retome o entrypoint. O teste confirma que a imagem não é calculada de novo depois de retomar e que uma alteração de entrada cria uma execução com resultado novo.

## Limites e trade-offs
A função em memória do processo não substitui um backend persistente se o processo for reiniciado. Uma task só pode reaproveitar o que a implementação de checkpoint efetivamente registrou; cache não deve ser confundido com garantia de exactly-once para serviços externos.

## Como verificar
Use uma task de teste que incremente um contador e interrompa o entrypoint depois dela. Retome usando o mesmo thread e verifique a contagem, o resultado e o comportamento ao trocar o identificador de thread ou os dados de entrada.

## Conexões
- [[langgraph-supersteps-e-reducers-paralelos]] — LangGraph: combinar atualizações paralelas com reducers.
- [[langgraph-streaming-v2-partes-tipadas]] — LangGraph: usar partes tipadas no streaming v2.

## Fontes
- [LangGraph — Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api) — descreve `@entrypoint`, `@task`, checkpointing e recuperação de resultados ao retomar Consulta: 2026-10-04.
- [LangGraph — Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — distingue persistência de execução por checkpointer e durabilidade entre reinícios Consulta: 2026-10-04.
