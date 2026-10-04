---
id: software.criacao_ia.tranche01.000044
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

# Unreal: encapsular ação em Tasks

## Em uma frase

Uma Task executa uma unidade de gameplay, como mover, aguardar ou iniciar animação, e informa o término à árvore.

## Por que importa

Tarefas pequenas podem ser testadas e reutilizadas sem esconder o fluxo completo de decisão.

## Como funciona

Dê à tarefa entradas explícitas, trate término normal e cancelamento, e evite misturar várias decisões de alto nível no mesmo nó.

## Exemplo

`MoveToCover` lê uma posição escolhida pelo EQS, inicia navegação e termina quando o AIController conclui ou falha o movimento.

## Limites e trade-offs

Se uma tarefa nunca notifica conclusão ou cancelamento, o ramo pode ficar preso e bloquear toda a árvore.

## Como verificar

Teste sucesso, caminho bloqueado, agente destruído e interrupção, observando que a árvore sempre recupera controle.

## Conexões
- [[unreal-usar-decorators-como-condicoes]] — Unreal: usar Decorators como condições.
- [[unreal-escolher-aborts-de-observadores]] — Unreal: escolher aborts de observadores.

## Fontes
- [Epic Games — Behavior Tree in Unreal Engine: Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---overview) — Apresenta estrutura de Behavior Trees, Blackboard e execução orientada a eventos na Unreal Engine. Consulta: 2026-10-04.
- [Epic Games — Environment Query System Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-quick-start-in-unreal-engine) — Mostra a criação e execução de consultas EQS para selecionar posições do ambiente. Consulta: 2026-10-04.
