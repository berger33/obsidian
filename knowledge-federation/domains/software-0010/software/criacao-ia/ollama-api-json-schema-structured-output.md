---
id: software.criacao_ia.tranche05.000404
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
fontes: ["https://docs.ollama.com/api/generate", "https://docs.ollama.com/api/chat"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: validar saídas estruturadas com format JSON Schema

## Em uma frase
Os endpoints `generate` e `chat` aceitam `format` com `json` ou um objeto de JSON Schema, mas o consumidor ainda precisa validar o resultado no limite da aplicação.

## Por que importa
Respostas livres são frágeis para automação; declarar a forma esperada torna erros de parsing observáveis e reduz a necessidade de extrair campos por heurística textual.

## Como funciona
Envie o valor `json` ou o objeto de schema no campo `format` do endpoint escolhido. Use instruções coerentes com o esquema, faça parse do texto recebido e trate conteúdo incompleto, campos ausentes e resposta não válida como falhas do contrato.

## Exemplo
Um extrator de tarefas envia um schema com `title` e `priority`, parseia `response` ou `message.content` e rejeita o resultado se a validação local apontar propriedade ausente.

## Limites e trade-offs
O schema limita a forma pretendida da saída, não prova que os valores sejam verdadeiros nem elimina diferenças entre modelos. Não execute uma ação de negócio sem validar tipo, enumerações e permissões.

## Como verificar
Crie testes com resposta válida, propriedade ausente, enumeração desconhecida e JSON malformado; registre a falha de validação sem substituir silenciosamente por valores padrão.

## Conexões
- [[ollama-api-chat-array-de-messages]] — Ollama API: representar a conversa em messages no endpoint chat.
- [[ollama-api-embeddings-lote-e-truncamento]] — Ollama API: gerar embeddings em lote e escolher a política de truncamento.

## Fontes
- [Ollama API — Generate a response](https://docs.ollama.com/api/generate) — Documenta `format` como `json` ou objeto JSON Schema para geração. Consulta: 2026-10-04.
- [Ollama API — Generate a chat message](https://docs.ollama.com/api/chat) — Confirma o mesmo campo de formato estruturado no endpoint de chat. Consulta: 2026-10-04.
