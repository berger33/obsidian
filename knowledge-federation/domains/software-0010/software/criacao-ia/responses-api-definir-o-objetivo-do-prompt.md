---
id: software.criacao_ia.tranche01.000013
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

# Responses API: definir o objetivo do prompt

## Em uma frase

Prompts orientados por tarefa especificam quem usa a função, o que deve ser produzido e quais características tornam a saída utilizável.

## Por que importa

Objetivos explícitos reduzem respostas decorativas que parecem completas, mas não encaixam no formato e no fluxo do produto.

## Como funciona

Escreva a tarefa com verbo observável, público, contexto suficiente e critérios de sucesso; remova adjetivos que não possam ser testados.

## Exemplo

Para resumir bug reports, peça causa provável, passos de reprodução e incertezas em campos separados, sem solicitar uma solução inventada.

## Limites e trade-offs

Instruções detalhadas ainda podem ser interpretadas de modo inconsistente entre modelos e versões.

## Como verificar

Avalie o prompt com exemplos típicos, casos adversariais e entradas incompletas, comparando a saída com uma rubrica escrita.

## Conexões
- [[responses-api-separar-instrucoes-e-entrada]] — Responses API: separar instruções e entrada.
- [[responses-api-extrair-texto-da-resposta]] — Responses API: extrair texto da resposta.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
