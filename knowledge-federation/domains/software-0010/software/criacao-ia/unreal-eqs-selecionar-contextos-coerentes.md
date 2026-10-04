---
id: software.criacao_ia.tranche01.000047
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
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview", "https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal EQS: selecionar contextos coerentes

## Em uma frase

Contexto define de quem ou de que local a query parte e influencia a relevância dos itens gerados.

## Por que importa

Contexto incorreto pode fazer uma consulta parecer válida mas gerar posições relativas a outro ator.

## Como funciona

Use o AI querier, alvo percebido ou conjunto explícito de atores conforme o objetivo e confirme qual posição alimenta cada gerador.

## Exemplo

Uma busca por distância ao inimigo usa o ator inimigo como referência, enquanto a navegação usa o NPC como solicitante.

## Limites e trade-offs

Contexto nulo, removido ou trocado durante gameplay pode invalidar itens e resultados previamente calculados.

## Como verificar

Troque o alvo durante a query e confira debug visual, contexto selecionado e item final armazenado no Blackboard.

## Conexões
- [[unreal-eqs-gerar-candidatos-espaciais]] — Unreal EQS: gerar candidatos espaciais.
- [[unreal-eqs-compor-tests-e-pontuacao]] — Unreal EQS: compor Tests e pontuação.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
