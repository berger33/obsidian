---
id: software.criacao_ia.tranche01.000020
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

# Responses API: avaliar geração com exemplos

## Em uma frase

Um conjunto versionado de entradas e expectativas torna possível detectar regressões de prompt sem depender de uma demonstração escolhida a dedo.

## Por que importa

Avaliação repetível evidencia variação em tarefas, idiomas e limites do produto antes que usuários encontrem mudanças inesperadas.

## Como funciona

Colete exemplos representativos, defina critérios qualitativos e métricas mensuráveis, e compare versões de prompt e modelo sob o mesmo protocolo.

## Exemplo

Uma ferramenta de quests mede se cada missão respeita o cenário, cabe no limite e evita contradizer fatos fornecidos pelo designer.

## Limites e trade-offs

Uma amostra pequena não prova qualidade geral e uma métrica automática pode premiar respostas longas ou superficiais.

## Como verificar

Revise erros qualitativamente, mantenha casos de borda e rode a avaliação sempre que atualizar prompt, modelo ou dados de contexto.

## Conexões
- [[responses-api-tratar-falhas-e-repeticao]] — Responses API: tratar falhas e repetição.
- [[function-calling-declarar-contrato-de-ferramenta]] — Function calling: declarar contrato de ferramenta.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
