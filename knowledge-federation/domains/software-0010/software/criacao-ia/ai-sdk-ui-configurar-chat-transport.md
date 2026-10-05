---
id: software.criacao_ia.tranche05.000453
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
fontes: ["https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat", "https://ai-sdk.dev/docs/ai-sdk-ui/chatbot"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: configurar endpoint e cabeçalhos no DefaultChatTransport

## Em uma frase
O `DefaultChatTransport` centraliza endpoint, credenciais, cabeçalhos e preparação de requisição, em vez de embutir detalhes de rede no formulário.

## Por que importa
Uma fronteira de transporte clara facilita alternar ambiente, autenticação e payload sem espalhar configuração por cada botão ou componente.

## Como funciona
Passe `transport` a `useChat` e configure `api`, `credentials`, `headers`, `body` ou `fetch`; use `prepareSendMessagesRequest` quando o backend espera estrutura específica para mensagem e ID do chat.

## Exemplo
Um cliente escolhe `/api/chat`, envia cookie com `credentials: 'include'` e adiciona um `chatId` ao corpo na função de preparação da requisição.

## Limites e trade-offs
Valores definidos por request podem combinar com configuração de transporte; valide no servidor corpo, usuário e identificador em vez de confiar no que o browser envia.

## Como verificar
Inspecione uma requisição no teste de integração, confira URL, método, credenciais e shape do JSON, e valide que headers não são enviados a um host não confiável.

## Conexões
- [[ai-sdk-ui-renderizar-uimessage-parts]] — AI SDK UI: renderizar UIMessage.parts por tipo em vez de presumir texto único.
- [[ai-sdk-ui-persistir-e-validar-uimessages]] — AI SDK UI: persistir UIMessage e validar tools e metadata antes de converter.

## Fontes
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Lista opções de DefaultChatTransport e callbacks de preparação da requisição. Consulta: 2026-10-04.
- [AI SDK UI — Chatbot](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot) — Apresenta a configuração do endpoint via transport no fluxo atual de `useChat`. Consulta: 2026-10-04.
