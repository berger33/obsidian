---
id: software.criacao_ia.tranche01.000012
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

# Responses API: separar instruções e entrada

## Em uma frase

Instruções do desenvolvedor definem comportamento estável do aplicativo, enquanto a entrada do usuário expressa a solicitação daquela interação.

## Por que importa

Separação ajuda a manter regras de produto consistentes sem misturá-las a conteúdo imprevisível enviado pela pessoa usuária.

## Como funciona

Mantenha política e formato em instruções de desenvolvedor e passe o pedido do usuário como entrada distinta, com limites claros de confiança.

## Exemplo

Num gerador de diálogos, a regra de não alterar nomes canônicos fica nas instruções e a cena solicitada continua sendo entrada do jogador.

## Limites e trade-offs

Um prompt não é uma barreira de autorização: conteúdo adversarial pode tentar substituir regras ou induzir ações fora do escopo.

## Como verificar

Teste instruções com pedidos conflitantes e confirme que permissões e validações críticas existem também no código do aplicativo.

## Conexões
- [[responses-api-iniciar-uma-chamada-de-texto]] — Responses API: iniciar uma chamada de texto.
- [[responses-api-definir-o-objetivo-do-prompt]] — Responses API: definir o objetivo do prompt.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
