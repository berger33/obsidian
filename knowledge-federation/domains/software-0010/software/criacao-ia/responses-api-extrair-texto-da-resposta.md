---
id: software.criacao_ia.tranche01.000014
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
fontes: ["https://platform.openai.com/docs/guides/text", "https://platform.openai.com/docs/guides/prompt-engineering"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Responses API: extrair texto da resposta

## Em uma frase

A resposta pode conter diferentes itens, e uma aplicação deve distinguir o texto destinado à pessoa de metadados ou estados auxiliares.

## Por que importa

Consumir a saída sem percorrer corretamente a estrutura pode exibir conteúdo vazio, parcial ou de tipo inesperado.

## Como funciona

Use o SDK e os campos documentados para obter texto, mantendo tratamento separado para recusa, resposta incompleta e erro de transporte.

## Exemplo

Um chat renderiza apenas o texto final autorizado, enquanto registra de forma controlada a ocorrência de recusa sem expor detalhes internos.

## Limites e trade-offs

Nem toda resposta contém texto final; código que presume um campo não vazio pode quebrar quando a API retorna outra modalidade ou estado.

## Como verificar

Teste respostas normais, vazias, recusadas e incompletas e assegure que cada estado tenha comportamento de interface definido.

## Conexões
- [[responses-api-definir-o-objetivo-do-prompt]] — Responses API: definir o objetivo do prompt.
- [[responses-api-escolher-modelo-por-tarefa]] — Responses API: escolher modelo por tarefa.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
