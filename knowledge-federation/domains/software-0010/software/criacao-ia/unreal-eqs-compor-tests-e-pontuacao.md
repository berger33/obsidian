---
id: software.criacao_ia.tranche01.000048
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

# Unreal EQS: compor Tests e pontuação

## Em uma frase

Tests filtram ou pontuam itens candidatos por condições como navegação, distância e visibilidade, permitindo ranquear locais.

## Por que importa

Combinar filtros duros com preferências graduais evita que uma única métrica escolha posição inviável.

## Como funciona

Remova itens que violam requisitos essenciais e depois compare candidatos válidos por custos e pesos calibrados.

## Exemplo

A query exige que o ponto esteja no NavMesh e sem linha de visão do inimigo, preferindo os pontos próximos ao objetivo.

## Limites e trade-offs

Peso exagerado pode dominar demais critérios; um teste que deveria ser requisito pode ter sido configurado como score.

## Como verificar

Crie cenas em que cada critério discorda dos outros e inspecione valores e posição selecionada no EQS debugger.

## Conexões
- [[unreal-eqs-selecionar-contextos-coerentes]] — Unreal EQS: selecionar contextos coerentes.
- [[unreal-eqs-enviar-resultado-a-behavior-tree]] — Unreal EQS: enviar resultado à Behavior Tree.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
