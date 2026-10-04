---
id: software.criacao_ia.tranche02.000154
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

# Unreal Engine: configurar Smart Object Definitions e slots de animação

## Em uma frase
Os Smart Objects anexam comportamentos e dados de animação diretamente aos objetos do mundo, em vez de codificá-los na IA do NPC.

## Por que importa
Permitir que o mundo informe aos NPCs como interagir com cadeiras, portas e máquinas torna a criação de comportamento altamente modular e extensível.

## Como funciona
Crie um asset `SmartObjectDefinition`, configure posições relativas dos slots de interação, tags de restrição e vincule as Gameplay Behaviors ou animações que o NPC executará ao usar o slot.

## Exemplo
```text
// Definicao de Smart Object para uma Cadeira de Taberna
SmartObjectDefinition: TavernChair
├── Slot 0: [Offset: (0, -40, 0), Yaw: 180]
│    └── Activity: SitAnimationBehavior
└── RequiredTags: [Pawn.Humanoid]
```

## Limites e trade-offs
Slots mal posicionados em relação à malha estática causam sobreposição de malhas ou flutuação de personagens durante a animação.

## Como verificar
Posicione o ator de Smart Object no cenário e inspecione as formas dos slots e eixos de orientação desenhados no viewport da Unreal Engine.

## Conexões
- [[unreal-statetree-implementar-tasks-assincronas]] — Veja também: Unreal Engine: implementar tarefas atômicas com StateTree Tasks.
- [[unreal-smart-objects-gerenciar-reservas-concorrentes]] — Veja também: Unreal Engine: gerenciar reservas concorrentes com Smart Object Subsystem.
- [[unreal-smart-objects-conectar-a-tarefas-do-statetree]] — Conexão temática direta com unreal-smart-objects-conectar-a-tarefas-do-statetree.
- [[unreal-motion-warping-alinhar-interacoes-fisicas]] — Conexão temática direta com unreal-motion-warping-alinhar-interacoes-fisicas.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
