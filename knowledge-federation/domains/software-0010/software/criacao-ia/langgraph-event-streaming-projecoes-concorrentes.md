---
id: software.criacao_ia.tranche03.000208
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/event-streaming", "https://docs.langchain.com/oss/python/langgraph/interrupts"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: consumir projeções do event streaming v3

## Em uma frase
Event streaming oferece projeções tipadas de uma execução, como `messages`, `values`, `subgraphs`, `interrupts` e `output`.

## Por que importa
Aplicações de agente costumam precisar mostrar texto parcial, estado final, subagentes e pedidos de aprovação na mesma tela. Ler um único fluxo bruto pode acoplar a aplicação ao formato interno do engine, enquanto projeções nomeadas separam usos e podem ser consumidas independentemente.

## Como funciona
Crie o fluxo por `stream_events(..., version=v3)` e selecione a projeção apropriada. O stream bruto representa eventos do protocolo; projeções integradas transformam esses eventos para consumidores da aplicação. Em código assíncrono, a documentação mostra consumidores independentes das projeções; use a operação de interleaving quando a ordem de chegada entre tipos diferentes precisar ser preservada. Continue drenando a execução e aguarde `output` para o resultado final.

## Exemplo
Uma interface pode iterar `stream.messages` para exibir texto e observar `stream.subgraphs` para revelar atividade de especialistas. Se `stream.interrupted` for verdadeiro, apresenta o conteúdo de `stream.interrupts`; após decisão humana, inicia outra chamada com `Command` e a configuração persistida.

## Limites e trade-offs
O event streaming foi introduzido em versão recente e nomes ou contratos podem mudar. Projeções consumidas separadamente não garantem uma ordenação global; para sequência exata, use os eventos brutos ou o mecanismo de interleaving documentado.

## Como verificar
Teste execução normal, uso de ferramenta, subgrafo, interrupção e cancelamento com a versão travada. Assegure que todos os consumidores terminem e que o resultado exposto à interface seja igual ao estado final retornado pelo grafo.

## Conexões
- [[langgraph-streaming-v2-partes-tipadas]] — LangGraph: usar partes tipadas no streaming v2.
- [[langgraph-schemas-entrada-saida-e-estado-privado]] — LangGraph: separar schemas de entrada, saída e estado interno.

## Fontes
- [LangGraph — Event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) — documenta versão v3, projeções, consumo concorrente e interleaving Consulta: 2026-10-04.
- [LangGraph — Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — mostra a forma de expor e retomar interrupts em event streaming Consulta: 2026-10-04.
