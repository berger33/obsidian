---
id: software.criacao_ia.tranche01.000043
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

# Unreal: usar Decorators como condições

## Em uma frase

Decorators controlam se um nó ou ramo pode executar, usando condições, observadores ou limites definidos pela árvore.

## Por que importa

Condições nomeadas tornam regras visíveis e evitam duplicar verificações dentro de tarefas distintas.

## Como funciona

Associe cada decorator a uma condição pequena, indique quais Blackboard keys observa e configure interrupção compatível com a prioridade desejada.

## Exemplo

Um decorator permite perseguir somente quando `HasLineOfSight` é verdadeiro e interrompe o ramo se a visão for perdida.

## Limites e trade-offs

Muitos decorators encadeados tornam a árvore difícil de entender; observadores mal configurados podem causar oscilação.

## Como verificar

Force estados verdadeiro e falso durante a execução e confirme ativação, saída e retorno da tarefa esperados.

## Conexões
- [[unreal-compor-sequence-e-selector]] — Unreal: compor Sequence e Selector.
- [[unreal-encapsular-acao-em-tasks]] — Unreal: encapsular ação em Tasks.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
