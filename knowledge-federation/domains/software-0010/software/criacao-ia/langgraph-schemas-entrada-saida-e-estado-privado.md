---
id: software.criacao_ia.tranche03.000209
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/graph-api", "https://docs.langchain.com/oss/python/langgraph/use-graph-api"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: separar schemas de entrada, saída e estado interno

## Em uma frase
Um grafo pode expor schemas menores de entrada e saída e manter canais privados no schema interno compartilhado pelos nós.

## Por que importa
Em fluxos extensos, detalhes intermediários, chaves de cache e resultados parciais não deveriam virar automaticamente contrato público. Separar as superfícies reduz acoplamento entre consumidores e implementação e permite que um nó passe informação a outro sem aceitar esse campo da entrada externa.

## Como funciona
Defina o schema interno com os canais usados pelos nós e declare `input_schema` e `output_schema` como subconjuntos explícitos ao construir `StateGraph`. Os nós continuam retornando updates de estado que passam pelos reducers. Use tipos compatíveis e valide campos obrigatórios na fronteira; o limite do schema é um contrato de dados, não uma política de autorização.

## Exemplo
Um grafo de criação de arte pode aceitar `brief` como entrada, manter `prompt_normalized` e `asset_hash` em schema privado, e devolver apenas `asset_url` e `validation_status`. Teste que o cliente não consiga sobrescrever a chave interna enviando-a no objeto de entrada.

## Limites e trade-offs
Schemas distintos não escondem dados que o grafo exponha por logs, streaming ou checkpoints. O suporte a modelos de estado e comportamento de validação varia entre `TypedDict`, dataclasses e Pydantic; a documentação alerta para diferenças de desempenho e validação.

## Como verificar
Inspecione o schema de entrada e a saída compilada, envie campos desconhecidos e confira a política adotada, e percorra cada canal privado em nós e reducers. Teste serialização de checkpoints após mudanças de schema.

## Conexões
- [[langgraph-event-streaming-projecoes-concorrentes]] — LangGraph: consumir projeções do event streaming v3.
- [[langgraph-politica-retencao-checkpoints]] — LangGraph: planejar retenção e limpeza de checkpoints.

## Fontes
- [LangGraph — Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) — descreve schemas múltiplos, canais privados e tipos de estado Consulta: 2026-10-04.
- [LangGraph — Use the Graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) — mostra como declarar contratos explícitos de entrada e saída Consulta: 2026-10-04.
