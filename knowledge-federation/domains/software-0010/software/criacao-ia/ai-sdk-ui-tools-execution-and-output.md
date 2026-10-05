---
id: software.criacao_ia.tranche05.000455
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage", "https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: separar execução de tools server-side e client-side com addToolOutput

## Em uma frase
As ferramentas podem executar no servidor, no cliente ou exigir confirmação, e resultados do cliente retornam ao chat por `addToolOutput`.

## Por que importa
O lugar da execução define permissões, interação humana e quem pode acessar dados; apresentar todos os tool calls como se fossem apenas texto esconde esse fluxo.

## Como funciona
Implemente ferramentas server-side com `execute`, trate ferramentas client-side em `onToolCall`, mostre aprovação quando necessário e envie o resultado com `addToolOutput`. Configure `sendAutomaticallyWhen` se outra rodada deve começar após todos os resultados.

## Exemplo
Uma busca privada roda no backend, uma ferramenta de confirmação aparece como card no browser e uma geolocalização client-side retorna resultado só após consentimento explícito.

## Limites e trade-offs
Uma chamada de ferramenta do modelo não é autorização para executar uma ação. Faça checagem de usuário e entradas no limite que efetivamente realiza a operação.

## Como verificar
Teste ferramenta automática, ferramenta que exige aprovação, erro e saída; confirme que cada saída usa o `toolCallId` certo e que a submissão automática ocorre apenas quando desejado.

## Conexões
- [[ai-sdk-ui-persistir-e-validar-uimessages]] — AI SDK UI: persistir UIMessage e validar tools e metadata antes de converter.
- [[ai-sdk-ui-retomar-streams-com-storage]] — AI SDK UI: implementar retomada de stream com persistência e endpoint GET.

## Fontes
- [AI SDK UI — Chatbot Tool Usage](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage) — Explica os três padrões de execução, `addToolOutput` e ressubmissão automática. Consulta: 2026-10-04.
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Define callbacks `onToolCall`, `addToolOutput` e `sendAutomaticallyWhen`. Consulta: 2026-10-04.
