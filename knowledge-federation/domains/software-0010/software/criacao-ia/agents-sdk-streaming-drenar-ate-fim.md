---
id: software.criacao_ia.tranche03.000225
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
fontes: ["https://openai.github.io/openai-agents-python/streaming/", "https://openai.github.io/openai-agents-python/results/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK streaming: consumir eventos até o iterador terminar

## Em uma frase
Um run iniciado por `Runner.run_streamed()` só está completo quando `stream_events()` termina, mesmo que o último token visível já tenha chegado.

## Por que importa
O SDK ainda pode concluir persistência de session, bookkeeping de aprovação ou compactação do histórico depois de emitir texto. Sair antecipadamente do iterador pode deixar o resultado sem `final_output`, interromper o trabalho ou fechar um transport compartilhado antes da resposta final.

## Como funciona
Consuma os eventos assíncronos até o iterator terminar e só então leia `is_complete`, `final_output`, interrupções ou estado. Escolha eventos brutos para deltas em tempo real e run-item events para marcos de alto nível, como ferramenta executada ou handoff. Se precisar interromper, use `cancel()` explicitamente e trate aprovação pendente como estado retomável, não como resposta concluída.

## Exemplo
Uma API WebSocket entrega deltas ao cliente enquanto acumula a resposta. Mesmo depois do evento de texto final, ela termina o loop, inspeciona `interruptions` e persiste `to_state()` quando necessário. O teste fecha o cliente antes da última atualização para garantir que o cancelamento seja registrado.

## Limites e trade-offs
Deltas podem não corresponder um a um a mensagens finais e a ordem varia entre superfície bruta e projeções. Drenar o stream não garante que um efeito de ferramenta tenha sucesso, nem dispensa tratamento de cancelamento e erros.

## Como verificar
Compare tempo do último delta com término do iterador, confirme `final_output` depois do término e verifique gravações de sessão e aprovação. Exercite cancelamento imediato, cancelamento após turno e exceção terminal do guardrail.

## Conexões
- [[agents-sdk-guardrails-fronteiras-primeiro-e-ultimo-agente]] — Agents SDK guardrails: mapear fronteiras de primeiro e último agente.
- [[agents-sdk-session-versus-responses-continuation]] — Agents SDK: escolher session local ou continuação server-side.

## Fontes
- [OpenAI Agents SDK — Streaming](https://openai.github.io/openai-agents-python/streaming/) — explica que a execução não conclui até o iterador terminar e lista pós-processamento Consulta: 2026-10-04.
- [OpenAI Agents SDK — Results](https://openai.github.io/openai-agents-python/results/) — define `final_output`, `is_complete` e resultados de runs interrompidos Consulta: 2026-10-04.
