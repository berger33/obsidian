---
id: software.criacao_ia.tranche03.000227
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
fontes: ["https://openai.github.io/openai-agents-python/agents/", "https://openai.github.io/openai-agents-python/results/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Agents SDK: normalizar saída tipada entre handoffs

## Em uma frase
`final_output` pode ser texto ou o objeto tipado do último agente e fica `None` quando o run termina sem saída final, por exemplo numa interrupção.

## Por que importa
Handoffs podem mudar qual agente conclui o run, então o chamador não pode inferir estaticamente uma única forma de resultado apenas a partir do agente inicial. Código que serializa `final_output` como se fosse sempre string pode quebrar justamente nos fluxos com especialista ou aprovação.

## Como funciona
Declare `output_type` por agente quando a aplicação depende de saída estruturada. No limite público, inspecione `last_agent`, `interruptions` e o estado de completude antes de converter o resultado. Se agentes finais usam schemas diferentes, normalize os resultados para um modelo de domínio comum no gerente ou camada de aplicação.

## Exemplo
Um especialista pode devolver `Diagnosis`, outro `AssetPlan`, mas a API de produto converte ambos a `JobOutcome` com campos de estado, resumo e artefatos. Quando há aprovação pendente, a API devolve estado `needs_review` em vez de tentar serializar `None` como resposta final.

## Limites e trade-offs
`output_type` estrutura formato, não torna conteúdo factual nem garante que todo run termine com objeto. Um handoff pode levar a tipo que o agente inicial não declarou; a aplicação precisa testar versões e erros de validação.

## Como verificar
Exercite saída normal, handoff para cada especialidade, tripwire de output, ferramenta terminal e aprovação pendente. Valide a conversão de Pydantic para JSON e o comportamento de schema desconhecido.

## Conexões
- [[agents-sdk-session-versus-responses-continuation]] — Agents SDK: escolher session local ou continuação server-side.
- [[agents-sdk-hosted-tool-search-deferred-loading]] — Agents SDK: adiar tool schemas com hosted tool search.

## Fontes
- [OpenAI Agents SDK — Agents](https://openai.github.io/openai-agents-python/agents/) — documenta `output_type` e possibilidade de saída estruturada Consulta: 2026-10-04.
- [OpenAI Agents SDK — Results](https://openai.github.io/openai-agents-python/results/) — define tipos possíveis de `final_output`, `last_agent` e resultado interrompido Consulta: 2026-10-04.
