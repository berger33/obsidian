---
id: software.criacao_ia.tranche03.000201
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/interrupts", "https://docs.langchain.com/oss/python/langgraph/checkpointers"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: retomar interrupts sem duplicar efeitos colaterais

## Em uma frase
Um interrupt durável pausa o nó e, ao retomar, volta a executar a função do nó desde o início, não apenas a linha seguinte.

## Por que importa
Esse detalhe muda o desenho de aprovações humanas e confirmações de ações em jogos ou aplicativos: gravações, cobranças, envio de mensagens e chamadas de serviço feitas antes da pausa podem acontecer novamente. O checkpoint restaura o fluxo, mas não desfaz automaticamente um efeito externo já realizado.

## Como funciona
Compile o grafo com um checkpointer e forneça um `thread_id` estável. A função `interrupt()` entrega um payload serializável; uma execução posterior com `Command(resume=...)` fornece a resposta como valor de retorno do interrupt. Como a função do nó recomeça, mantenha antes da pausa apenas preparação repetível, ou proteja o efeito com uma chave de idempotência persistida fora do nó. Colocar a ação irreversível depois da decisão também simplifica a semântica.

## Exemplo
Em uma ferramenta de publicação, primeiro monte e valide o rascunho, depois interrompa para aprovação e somente então publique. Se a operação anterior à pausa reservar um recurso, grave um identificador único e consulte-o antes de reservar outra vez. No teste, retome duas vezes com o mesmo `thread_id` e confirme que o identificador do efeito não se duplica.

## Limites e trade-offs
Idempotência depende do contrato do serviço externo; um checkpointer não fornece transação distribuída com banco de dados, rede ou engine. Respostas do modelo e chamadas externas repetidas podem produzir resultados diferentes. Um payload de interrupt também não deve ser tratado como mecanismo de autorização.

## Como verificar
Inspecione a implementação do nó em torno de `interrupt()` e simule parada e retomada com o mesmo `thread_id`. Registre quantas vezes a função executa, quantas vezes o serviço é chamado e o comportamento após timeout entre o efeito remoto e a gravação local.

## Conexões
- [[langgraph-thread-id-e-checkpoint-id]] — LangGraph: distinguir thread_id de checkpoint_id.

## Fontes
- [LangGraph — Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — explica checkpoint, retomada com `Command` e reinício do nó que contém o interrupt Consulta: 2026-10-04.
- [LangGraph — Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) — define thread, checkpoint e recuperação de execução interrompida Consulta: 2026-10-04.
