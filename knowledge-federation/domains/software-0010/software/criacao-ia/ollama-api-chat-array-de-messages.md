---
id: software.criacao_ia.tranche05.000403
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
fontes: ["https://docs.ollama.com/api/chat", "https://docs.ollama.com/api/generate"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: representar a conversa em messages no endpoint chat

## Em uma frase
`POST /api/chat` recebe histórico como uma lista de mensagens com papel e conteúdo, ao contrário de `generate`, que recebe um campo de prompt.

## Por que importa
Manter turnos explícitos evita reconstruir a conversa em texto ad hoc e permite que o cliente decida qual histórico entregar em cada chamada.

## Como funciona
O corpo documentado exige `model` e `messages`; cada item representa uma mensagem e traz `role` e `content`. A resposta apresenta uma mensagem de assistant. O aplicativo mantém a política de retenção e escolhe quais turnos reenviar.

## Exemplo
Uma chamada envia uma única mensagem `{"role":"user","content":"Resuma este log"}`; na próxima interação, o cliente inclui os turnos anteriores que decidiu conservar.

## Limites e trade-offs
A existência do array não significa que o servidor guarde automaticamente o histórico de produto entre requisições. Não envie segredos ou conversas de outro usuário ao reutilizar uma lista persistida.

## Como verificar
Valide que o serializador preserva a ordem dos turnos, os papéis esperados e o conteúdo da resposta `message`; teste requisições sem histórico e com mais de um turno.

## Conexões
- [[ollama-api-generate-stream-e-done]] — Ollama API: tratar stream de generate até o marcador done.
- [[ollama-api-json-schema-structured-output]] — Ollama API: validar saídas estruturadas com format JSON Schema.

## Fontes
- [Ollama API — Generate a chat message](https://docs.ollama.com/api/chat) — Especifica `messages` como histórico em array e mostra a mensagem de resposta. Consulta: 2026-10-04.
- [Ollama API — Generate a response](https://docs.ollama.com/api/generate) — Distingue o formato `prompt` usado pelo endpoint de geração individual. Consulta: 2026-10-04.
