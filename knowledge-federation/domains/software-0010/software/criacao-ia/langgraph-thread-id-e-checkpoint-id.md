---
id: software.criacao_ia.tranche03.000202
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
fontes: ["https://docs.langchain.com/oss/python/langgraph/checkpointers", "https://docs.langchain.com/oss/python/langgraph/use-time-travel"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# LangGraph: distinguir thread_id de checkpoint_id

## Em uma frase
`thread_id` identifica a sequência persistida de uma execução conversacional; `checkpoint_id` seleciona um snapshot específico dentro dessa sequência.

## Por que importa
Confundir os dois identificadores leva a retomar uma conversa errada, perder histórico ou depurar o estado atual quando a intenção era reproduzir um passo anterior. A distinção é especialmente importante em aplicações que mostram histórico, oferecem desfazer ou executam várias sessões em paralelo.

## Como funciona
Passe `thread_id` em `configurable` em toda invocação que deve continuar a mesma thread. Um checkpointer grava snapshots em limites de super-step e a API de histórico permite localizar cada snapshot, inclusive seu `checkpoint_id` e nós seguintes. Use o identificador do checkpoint ao pedir um ponto histórico; mantenha o identificador da thread para delimitar a cadeia. Um novo `thread_id` inicia outra cadeia, não é um alias do snapshot mais recente.

## Exemplo
Uma interface de suporte pode guardar `thread_id` por conversa. Ao abrir a tela de auditoria, ela lista snapshots dessa conversa e registra o `checkpoint_id` escolhido para replay. A operação de continuação usa a configuração histórica daquele snapshot, enquanto mensagens novas seguem na mesma thread quando esse for o fluxo pretendido.

## Limites e trade-offs
Um checkpoint é um retrato de estado, não uma cópia independente de todas as dependências externas. Retenção, serialização e consistência dependem do backend do checkpointer. Não exponha IDs como credenciais nem presuma que conhecer um identificador concede autorização sobre a thread.

## Como verificar
Crie duas threads e vários snapshots em cada uma. Confirme que trocar apenas o `thread_id` não carrega estado da outra conversa e que selecionar um `checkpoint_id` antigo retorna o snapshot esperado. Revise como IDs são persistidos e autorizados na API de produto.

## Conexões
- [[langgraph-interrupt-retomar-sem-repetir-efeitos]] — LangGraph: retomar interrupts sem duplicar efeitos colaterais.
- [[langgraph-time-travel-replay-ou-fork]] — LangGraph: escolher replay ou fork no time travel.

## Fontes
- [LangGraph — Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) — define threads, checkpoints, snapshots por super-step e configuração de `thread_id` Consulta: 2026-10-04.
- [LangGraph — Time travel](https://docs.langchain.com/oss/python/langgraph/use-time-travel) — mostra consulta do histórico e retomada a partir da configuração de checkpoint selecionada Consulta: 2026-10-04.
