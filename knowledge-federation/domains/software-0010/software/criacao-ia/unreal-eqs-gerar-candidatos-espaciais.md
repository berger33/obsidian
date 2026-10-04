---
id: software.criacao_ia.tranche01.000046
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

# Unreal EQS: gerar candidatos espaciais

## Em uma frase

Uma consulta EQS reúne candidatos por gerador antes de avaliá-los com critérios de ambiente.

## Por que importa

Buscar pontos candidatos cria decisões espaciais sem codificar coordenadas fixas para cada arena.

## Como funciona

Escolha gerador adequado, defina contexto do querier ou alvo e mantenha quantidade de amostras compatível com custo de execução.

## Exemplo

Para procurar cobertura, gere pontos em alcance ao redor do NPC e depois avalie visibilidade e distância do inimigo.

## Limites e trade-offs

Geradores podem produzir muitos pontos inválidos ou caros; coordenadas dependem de navegação e contexto corretos.

## Como verificar

Desenhe os itens gerados no debugger, compare com a geometria e confirme que a query retorna candidatos na situação esperada.

## Conexões
- [[unreal-escolher-aborts-de-observadores]] — Unreal: escolher aborts de observadores.
- [[unreal-eqs-selecionar-contextos-coerentes]] — Unreal EQS: selecionar contextos coerentes.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
