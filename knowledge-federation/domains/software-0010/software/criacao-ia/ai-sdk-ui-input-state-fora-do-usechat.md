---
id: software.criacao_ia.tranche05.000451
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

# AI SDK UI: manter o estado do campo de entrada fora de useChat no AI SDK 5

## Em uma frase
A partir do AI SDK 5, `useChat` usa arquitetura baseada em transportes e não mantém internamente o estado do campo de entrada.

## Por que importa
Separar texto digitado do estado do histórico dá ao formulário liberdade de interação e evita depender de uma API de input removida na mudança arquitetural.

## Como funciona
Armazene o valor do input no componente e use `sendMessage({ text })` no submit; deixe `useChat` administrar mensagens, estado da requisição e streaming através do transport configurado.

## Exemplo
Um componente React usa `useState('')`, envia o texto por `sendMessage`, limpa o campo após a chamada e desabilita submit enquanto `status` não está `ready`.

## Limites e trade-offs
A referência destaca que essa mudança ocorreu no AI SDK 5.0; exemplos de versões anteriores podem expor `input` e `handleSubmit` que não correspondem à API atual.

## Como verificar
Confira a versão instalada do pacote, compile o formulário com os tipos atuais e teste input vazio, envio em andamento e resposta concluída.

## Conexões
- [[ai-sdk-ui-renderizar-uimessage-parts]] — AI SDK UI: renderizar UIMessage.parts por tipo em vez de presumir texto único.

## Fontes
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Registra a mudança de AI SDK 5 para transportes e remoção do estado interno de input. Consulta: 2026-10-04.
- [AI SDK UI — Chatbot](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot) — Mostra input local e chamada de `sendMessage` no exemplo atual de chat. Consulta: 2026-10-04.
