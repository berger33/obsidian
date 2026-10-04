---
id: software.criacao_ia.tranche01.000030
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://platform.openai.com/docs/guides/function-calling", "https://platform.openai.com/docs/guides/structured-outputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ferramentas: testar exceções e falhas de execução

## Em uma frase

Uma integração robusta precisa responder a ferramenta indisponível, argumento inválido e resultado vazio sem travar o ciclo da aplicação.

## Por que importa

A falha pode ocorrer depois que o modelo formulou uma chamada; o produto precisa preservar estado e informar limites claramente.

## Como funciona

Converta exceções em erro tipado e mínimo, decida se uma nova tentativa é segura e mantenha correlação com a chamada original.

## Exemplo

Se o serviço de inventário falha, o jogo mantém o estado confirmado e informa que a informação não pôde ser consultada.

## Limites e trade-offs

Repetir automaticamente pode duplicar alteração ou cobrar duas vezes se o serviço concluiu mas a resposta se perdeu.

## Como verificar

Simule falha antes e depois do commit e prove que repetição, recuperação e apresentação ao usuário seguem a política definida.

## Conexões
- [[function-calling-minimizar-dados-retornados]] — Function calling: minimizar dados retornados.
- [[ml-agents-estruturar-um-agent]] — ML-Agents: estruturar um Agent.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
