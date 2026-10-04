---
id: software.criacao_ia.tranche02.000156
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine", "https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal Engine: conectar navegação a Smart Objects via StateTree Tasks

## Em uma frase
Integrar o StateTree com Smart Objects permite que NPCs encontrem interações ambientais de forma orgânica durante rotinas de ócio e trabalho.

## Por que importa
Vincular o subsistema de Smart Objects ao fluxo de decisão automatiza o ciclo completo de busca, navegação, reserva e interação.

## Como funciona
Configure uma StateTree Task `FindSmartObject` que consulta o subsistema por tags (ex.: `WorkStation`), reserva o slot e direciona a task seguinte `MoveToSmartObjectSlot` até as coordenadas do slot.

## Exemplo
```text
// Fluxo de tarefas no StateTree para interagir com o ambiente
State: UseWorkbench
├── Task: FindSmartObject (Tag: Interact.Workbench)
├── Task: MoveToSmartObjectSlot
└── Task: ExecuteSmartObjectBehavior (Hammering)
```

## Limites e trade-offs
Se o caminho até o Smart Object estiver bloqueado, o NPC precisa abortar a reserva e buscar outro slot sem congelar a árvore de decisão.

## Como verificar
Bloqueie deliberadamente o trajeto até o objeto e verifique se a tarefa falha graciosamente e transiciona para o estado de busca alternativa.

## Conexões
- [[unreal-smart-objects-gerenciar-reservas-concorrentes]] — Veja também: Unreal Engine: gerenciar reservas concorrentes com Smart Object Subsystem.
- [[unreal-mass-ai-processar-agentes-com-massentity]] — Veja também: Unreal Engine: simular multidões com arquitetura ECS MassEntity e Mass AI.
- [[unreal-statetree-implementar-tasks-assincronas]] — Conexão temática direta com unreal-statetree-implementar-tasks-assincronas.
- [[unity-navmesh-reconstruir-superficie-em-runtime]] — Conexão temática direta com unity-navmesh-reconstruir-superficie-em-runtime.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
