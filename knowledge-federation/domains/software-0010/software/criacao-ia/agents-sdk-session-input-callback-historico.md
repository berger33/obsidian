---
id: software.criacao_ia.tranche03.000229
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
fontes: ["https://openai.github.io/openai-agents-python/sessions/", "https://openai.github.io/openai-agents-python/running_agents/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK Sessions: limitar histórico lido sem duplicar persistência

## Em uma frase
`session_input_callback` pode selecionar ou reordenar histórico para a próxima chamada do modelo sem gravar novamente itens antigos como entrada nova.

## Por que importa
Históricos longos encarecem turnos e podem incluir material irrelevante, enquanto filtros manuais mal posicionados duplicam mensagens na persistência. A callback de input ajuda a adaptar contexto sem mudar o repositório de histórico subjacente.

## Como funciona
A callback recebe cópias de `history` e `new_input` e devolve os itens finais para aquele turno. A Session ainda persiste os itens que pertencem ao novo turno. Use `SessionSettings(limit=N)` para limitar recuperação por execução, ou a callback para poda, reordenação e inclusão seletiva antes da chamada do modelo.

## Exemplo
Um assistente de pipeline mantém histórico completo no SQLite, mas envia ao modelo os dez itens mais recentes mais uma nota de resumo validada. O teste consulta o storage após duas chamadas e confirma que a antiga pergunta não foi inserida outra vez apenas porque a callback a incluiu no prompt.

## Limites e trade-offs
Filtrar o que o modelo vê não apaga o histórico armazenado nem constitui política de retenção. Uma callback pode remover dependências contextuais importantes; valide segurança, coerência de handoff e limite de tokens em cada tipo de sessão.

## Como verificar
Use sessão com itens marcados, registre entrada final do modelo e leia o storage antes e depois. Teste limite por run, callback com lista mutável e retomada de run interrompido.

## Conexões
- [[agents-sdk-hosted-tool-search-deferred-loading]] — Agents SDK: adiar tool schemas com hosted tool search.
- [[agents-sdk-tracing-flush-workers]] — Agents SDK tracing: descarregar spans antes de encerrar um job.

## Fontes
- [OpenAI Agents SDK — Sessions](https://openai.github.io/openai-agents-python/sessions/) — detalha callback de merge, cópias e persistência só de itens do turno novo Consulta: 2026-10-04.
- [OpenAI Agents SDK — Running agents](https://openai.github.io/openai-agents-python/running_agents/) — explica configuração de execução e filtros finais da entrada do modelo Consulta: 2026-10-04.
