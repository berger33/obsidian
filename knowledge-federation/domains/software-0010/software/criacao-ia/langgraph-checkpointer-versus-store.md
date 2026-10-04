---
id: software.criacao_ia.tranche03.000204
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/persistence", "https://docs.langchain.com/oss/python/langgraph/stores"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: separar checkpointer de store de longo prazo

## Em uma frase
Checkpointer salva snapshots do estado de uma thread; Store mantém valores de aplicação que podem ser consultados entre threads.

## Por que importa
Colocar preferências permanentes do usuário no histórico de uma única conversa dificulta reutilização e controle de retenção. No sentido inverso, armazenar todo o estado transitório do grafo em um Store pode misturar conversas e apagar a semântica de retomada. As duas ferramentas resolvem escopos diferentes e podem coexistir.

## Como funciona
Compile o grafo com um checkpointer para estado de execução, interrupções, continuidade da conversa e time travel. Use um Store com namespace e chave para dados arbitrários compartilhados, como preferências ou fatos aprovados. O nó recebe o Store via runtime e decide explicitamente quais valores ler ou gravar. Escolha implementações persistentes em produção; os backends em memória são úteis para desenvolvimento e testes, mas não sobrevivem ao reinício do processo.

## Exemplo
Uma aplicação de criação de níveis pode manter as escolhas recentes da sessão no checkpoint e guardar o tema visual preferido do usuário num Store com namespace por conta. Ao iniciar uma conversa nova, a preferência pode ser consultada sem importar o estado transitório da thread anterior.

## Limites e trade-offs
Store não fornece automaticamente qualidade semântica, consentimento ou política de expiração para cada fato. Um checkpointer também não deve ser tratado como memória global. A forma de ordenação e consulta pode variar entre backends, então a lógica não deve depender da ordem de inserção sem teste.

## Como verificar
Teste duas threads com o mesmo usuário: o snapshot deve permanecer isolado por `thread_id`, enquanto o item do Store aparece somente no namespace previsto. Reinicie a aplicação usando um backend persistente e valide migração, retenção, limites de acesso e exclusão de dados.

## Conexões
- [[langgraph-time-travel-replay-ou-fork]] — LangGraph: escolher replay ou fork no time travel.
- [[langgraph-supersteps-e-reducers-paralelos]] — LangGraph: combinar atualizações paralelas com reducers.

## Fontes
- [LangGraph — Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — compara checkpointers de escopo thread e stores de dados entre threads Consulta: 2026-10-04.
- [LangGraph — Stores](https://docs.langchain.com/oss/python/langgraph/stores) — detalha namespaces, operações key-value e backends do Store Consulta: 2026-10-04.
