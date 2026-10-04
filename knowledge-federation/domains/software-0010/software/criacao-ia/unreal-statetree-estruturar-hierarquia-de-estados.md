---
id: software.criacao_ia.tranche02.000151
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

# Unreal Engine: estruturar hierarquia de estados leves no StateTree

## Em uma frase
O StateTree é um sistema moderno de árvore de estados hierárquica de alta performance para tomada de decisão em agentes de gameplay.

## Por que importa
O StateTree combina a clareza de máquinas de estados com a flexibilidade de árvores hierárquicas, exigindo menos memória que Behavior Trees tradicionais.

## Como funciona
Crie um asset `StateTree` no Content Browser, defina estados raiz e filhos no editor visual, e vincule componentes `StateTreeComponent` em seus AI Controllers ou Pawns para executar a lógica.

## Exemplo
```text
// Hierarquia visual no editor de StateTree da Unreal Engine 5
Root
├── Idle (State)
│    └── Task: PlayAnimation (Idle)
├── Combat (State)
│    ├── Engage (State) -> Task: MoveToTarget
│    └── Attack (State) -> Task: TriggerAbility
└── Flee (State)
```

## Limites e trade-offs
A lógica de StateTree avalia transições com base em eventos e ticks; estados excessivamente aninhados sem condições de saída claras podem gerar loops de transição.

## Como verificar
Abra o painel de depuração do StateTree durante o modo PIE (*Play in Editor*) e verifique qual estado está ativo para cada entidade simulada no mundo.

## Conexões
- [[unreal-statetree-extrair-contexto-com-evaluators]] — Veja também: Unreal Engine: extrair contexto e dados de mundo com StateTree Evaluators.
- [[unreal-statetree-implementar-tasks-assincronas]] — Conexão temática direta com unreal-statetree-implementar-tasks-assincronas.
- [[godot-estruturar-maquina-de-estados-hierarquica]] — Conexão temática direta com godot-estruturar-maquina-de-estados-hierarquica.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
