---
id: software.criacao_ia.tranche01.000016
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

# Responses API: limitar o tamanho da saída

## Em uma frase

Limites explícitos de extensão ajudam a controlar interface, custo e tempo, mas precisam refletir a tarefa e não apenas um número arbitrário.

## Por que importa

Respostas ilimitadas podem ultrapassar o espaço de tela ou gerar conteúdo redundante; limites excessivos podem cortar explicações úteis.

## Como funciona

Defina o tamanho no formato e parâmetro suportados pela versão atual e especifique quais partes têm prioridade se houver pouco espaço.

## Exemplo

Um tooltip pede uma frase curta; uma documentação de migração solicita etapas, riscos e verificação, portanto precisa de orçamento maior.

## Limites e trade-offs

Limites de tokens não equivalem exatamente a palavras ou caracteres e uma resposta pode terminar incompleta.

## Como verificar

Verifique a extensão por tipo de conteúdo, trate respostas truncadas e monitore se o limite força omissão de informação essencial.

## Conexões
- [[responses-api-escolher-modelo-por-tarefa]] — Responses API: escolher modelo por tarefa.
- [[responses-api-criar-um-prompt-versionavel]] — Responses API: criar um prompt versionável.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
