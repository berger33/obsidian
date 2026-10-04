---
id: software.criacao_ia.tranche01.000018
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

# Responses API: isolar conteúdo não confiável

## Em uma frase

Texto fornecido por usuários deve ser tratado como dado de entrada, não como instrução privilegiada do sistema.

## Por que importa

Separar conteúdo reduz a chance de uma solicitação embutida num arquivo ou diálogo desviar o objetivo do aplicativo.

## Como funciona

Delimite trechos citados, informe ao modelo como usá-los e não concatene texto externo em instruções confiáveis sem uma fronteira explícita.

## Exemplo

Um tutor pode explicar um script enviado pelo aluno sem obedecer a comentários que peçam revelar segredos ou alterar política.

## Limites e trade-offs

Delimitadores ajudam a organizar contexto, mas não são uma proteção infalível contra prompt injection.

## Como verificar

Inclua documentos maliciosos nos testes e confirme que segredos e ferramentas sensíveis são protegidos por controles fora do prompt.

## Conexões
- [[responses-api-criar-um-prompt-versionavel]] — Responses API: criar um prompt versionável.
- [[responses-api-tratar-falhas-e-repeticao]] — Responses API: tratar falhas e repetição.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
