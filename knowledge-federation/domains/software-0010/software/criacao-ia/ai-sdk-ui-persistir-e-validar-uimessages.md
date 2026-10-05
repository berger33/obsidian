---
id: software.criacao_ia.tranche05.000454
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
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence", "https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: persistir UIMessage e validar tools e metadata antes de converter

## Em uma frase
Para persistência, armazene mensagens no formato `UIMessage` e valide mensagens recuperadas antes de convertê-las para a forma enviada ao modelo.

## Por que importa
A estrutura da interface inclui IDs, partes, metadados e estados de ferramenta; aceitar conteúdo salvo sem validar pode quebrar conversão ou reintroduzir payloads incompatíveis.

## Como funciona
Guarde o array completo de `UIMessage`, incluindo IDs estáveis para restauração. Antes de chamar `convertToModelMessages`, use `validateUIMessages` com schemas atuais de ferramentas, partes de dados e metadata.

## Exemplo
Uma rota carrega histórico por chat ID, valida tool calls contra o catálogo de ferramentas vigente, converte mensagens aprovadas e persiste a resposta final recebida pelo callback de stream.

## Limites e trade-offs
O tutorial de persistência declara que o exemplo simples não cobre autorização ou tratamento completo de erros; validação estrutural não prova que usuário possa acessar aquele chat.

## Como verificar
Teste mensagens antigas, ferramenta removida, metadata inválida e chat ID não autorizado; confirme que o backend falha de forma controlada sem encaminhar conteúdo inválido ao modelo.

## Conexões
- [[ai-sdk-ui-configurar-chat-transport]] — AI SDK UI: configurar endpoint e cabeçalhos no DefaultChatTransport.
- [[ai-sdk-ui-tools-execution-and-output]] — AI SDK UI: separar execução de tools server-side e client-side com addToolOutput.

## Fontes
- [AI SDK UI — Chatbot Message Persistence](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-message-persistence) — Recomenda formato UIMessage e validação via `validateUIMessages` para tools, metadata e data parts. Consulta: 2026-10-04.
- [AI SDK Core — UIMessage](https://ai-sdk.dev/docs/reference/ai-sdk-core/ui-message) — Documenta tipo de mensagem e campos preservados pela interface e persistência. Consulta: 2026-10-04.
