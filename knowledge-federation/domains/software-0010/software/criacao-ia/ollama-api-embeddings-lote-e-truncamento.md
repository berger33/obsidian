---
id: software.criacao_ia.tranche05.000405
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
fontes: ["https://docs.ollama.com/api/embed", "https://docs.ollama.com/api/introduction"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Ollama API: gerar embeddings em lote e escolher a política de truncamento

## Em uma frase
`POST /api/embed` aceita uma string ou uma lista de textos, e o campo `truncate` define se entradas além da janela são cortadas ou resultam em erro.

## Por que importa
O lote pode reduzir chamadas em pipelines de indexação, mas truncamento silencioso pode produzir vetores que representam apenas uma parte do documento.

## Como funciona
Envie `model` e `input`; quando `input` é uma lista, a resposta contém um vetor por entrada. O padrão documentado de `truncate` é verdadeiro; configure falso quando a aplicação precisa detectar entradas acima do contexto e dividi-las explicitamente.

## Exemplo
Um indexador manda uma lista com três trechos, verifica que retornaram três embeddings e, em modo de auditoria, usa `truncate: false` para encaminhar trechos grandes à etapa de chunking.

## Limites e trade-offs
O endpoint não define sua estratégia de segmentação semântica nem garante dimensões iguais entre modelos. Confirme as dimensões esperadas antes de gravar os vetores no índice escolhido.

## Como verificar
Teste string e array, confira a cardinalidade do campo `embeddings` e compare o comportamento documentado com `truncate: true` e `false` em uma entrada propositalmente longa.

## Conexões
- [[ollama-api-json-schema-structured-output]] — Ollama API: validar saídas estruturadas com format JSON Schema.
- [[ollama-api-pull-acompanhar-progresso]] — Ollama API: acompanhar o progresso do pull sem fixar mensagens de status.

## Fontes
- [Ollama API — Generate embeddings](https://docs.ollama.com/api/embed) — Especifica entrada string/array, truncamento e resposta com embeddings. Consulta: 2026-10-04.
- [Ollama API — Introduction](https://docs.ollama.com/api/introduction) — Fornece a base URL oficial a usar no exemplo local. Consulta: 2026-10-04.
