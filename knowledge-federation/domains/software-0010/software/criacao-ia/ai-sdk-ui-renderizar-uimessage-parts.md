---
id: software.criacao_ia.tranche05.000452
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
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/chatbot", "https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: renderizar UIMessage.parts por tipo em vez de presumir texto único

## Em uma frase
`UIMessage.parts` pode conter texto, ferramentas, resultados e outros dados, então a interface deve renderizar cada parte por seu tipo.

## Por que importa
Reduzir toda mensagem a uma string perde estados de ferramentas e conteúdo que não é texto, além de limitar extensões futuras da conversa.

## Como funciona
Percorra `message.parts`, faça branch por `part.type` e desenhe componentes apropriados para texto, tool invocation e outros tipos aceitos. Use `message.role` e `message.id` para organizar a apresentação.

## Exemplo
Uma mensagem assistant renderiza parágrafos para `text`, um card de confirmação para `tool-askForConfirmation` e um resultado estruturado para uma parte de ferramenta concluída.

## Limites e trade-offs
Tipos e estados disponíveis dependem das ferramentas e schemas habilitados; mensagens persistidas antigas podem exigir validação ou migração antes do render.

## Como verificar
Crie fixtures com texto simples, chamada de ferramenta, resultado e erro; confirme que cada tipo é exibido sem descartar partes desconhecidas silenciosamente.

## Conexões
- [[ai-sdk-ui-input-state-fora-do-usechat]] — AI SDK UI: manter o estado do campo de entrada fora de useChat no AI SDK 5.
- [[ai-sdk-ui-configurar-chat-transport]] — AI SDK UI: configurar endpoint e cabeçalhos no DefaultChatTransport.

## Fontes
- [AI SDK UI — Chatbot](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot) — Recomenda `parts` no lugar de `content` e enumera texto e chamadas/resultados de ferramentas. Consulta: 2026-10-04.
- [AI SDK Core — UIMessage](https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message) — Descreve a estrutura e os tipos de partes de mensagens exibidas na interface. Consulta: 2026-10-04.
