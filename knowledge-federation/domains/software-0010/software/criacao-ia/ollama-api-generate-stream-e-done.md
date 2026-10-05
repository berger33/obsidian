---
id: software.criacao_ia.tranche05.000402
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
fontes: ["https://docs.ollama.com/api/generate", "https://docs.ollama.com/api/introduction"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: tratar stream de generate até o marcador done

## Em uma frase
`POST /api/generate` pode responder com fragmentos quando `stream` está ativo, e o consumidor deve reconhecer o evento final em vez de presumir que a primeira resposta é completa.

## Por que importa
A interface pode exibir texto progressivamente, mas precisa distinguir uma geração em andamento de uma geração concluída para liberar controles, persistir o resultado e relatar falhas com precisão.

## Como funciona
O endpoint documenta `stream` como booleano com padrão `true`, respostas parciais e o campo `done` que indica o fim. Defina `stream: false` quando a integração precisa de uma resposta única, ou processe cada registro do stream e finalize ao receber `done: true`.

## Exemplo
Um cliente de terminal acrescenta cada `response` à saída visível, mas só grava a resposta como concluída quando o registro final contém `done: true`; um teste também cobre `stream: false`.

## Limites e trade-offs
O tamanho e o número de fragmentos dependem do modelo e da entrada; não codifique uma quantidade fixa de eventos nem use a chegada de um fragmento de texto como sinal de término.

## Como verificar
Teste uma geração curta em modo streaming e outra com `stream: false`; confirme que o cliente não duplica texto, termina no indicador documentado e fecha corretamente a conexão.

## Conexões
- [[ollama-api-separar-base-url-local-cloud]] — Ollama API: diferenciar base URLs local e cloud antes de configurar o cliente.
- [[ollama-api-chat-array-de-messages]] — Ollama API: representar a conversa em messages no endpoint chat.

## Fontes
- [Ollama API — Generate a response](https://docs.ollama.com/api/generate) — Define o padrão de `stream`, respostas parciais e o campo final `done`. Consulta: 2026-10-04.
- [Ollama API — Introduction](https://docs.ollama.com/api/introduction) — Confirma a rota REST local usada no exemplo da chamada de geração. Consulta: 2026-10-04.
