---
id: software.criacao_ia.tranche02.000155
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

# Unreal Engine: gerenciar reservas concorrentes com Smart Object Subsystem

## Em uma frase
O Smart Object Subsystem gerencia a descoberta espacial e a reserva exclusiva de slots para evitar que múltiplos NPCs tentem usar o mesmo objeto.

## Por que importa
Concorrência não tratada em pontos de interação provoca NPCs sobrepostos na mesma cadeira ou tentando abrir a mesma porta simultaneamente.

## Como funciona
Utilize `USmartObjectSubsystem::FindSmartObjects()` para buscar slots disponíveis dentro de um raio e execute `Claim()` ou `MarkSlotAsOccupied()` para reservar o slot antes de iniciar a caminhada.

## Exemplo
```cpp
// Buscando e reservando slot no Smart Object Subsystem
FSmartObjectRequestFilter Filter;
Filter.ActivityRequirements = GameplayTagContainer;
FSmartObjectClaimHandle ClaimHandle = SmartObjectSubsystem->Claim(RequestResult);
```

## Limites e trade-offs
Reservar um slot e nunca liberá-lo após uma morte ou interrupção do NPC bloqueia aquele ponto de interação permanentemente no jogo.

## Como verificar
Gere múltiplos agentes simultâneos disputando uma única cadeira e valide visualmente se apenas o primeiro agente que realizou o claim ocupa o assento.

## Conexões
- [[unreal-smart-objects-configurar-slots-de-interacao]] — Veja também: Unreal Engine: configurar Smart Object Definitions e slots de animação.
- [[unreal-smart-objects-conectar-a-tarefas-do-statetree]] — Veja também: Unreal Engine: conectar navegação a Smart Objects via StateTree Tasks.
- [[godot-usar-obstacles-para-geometria-e-fluxo]] — Conexão temática direta com godot-usar-obstacles-para-geometria-e-fluxo.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
