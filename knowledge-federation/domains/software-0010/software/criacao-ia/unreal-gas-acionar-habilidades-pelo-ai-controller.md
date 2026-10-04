---
id: software.criacao_ia.tranche02.000158
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

# Unreal Engine: acionar Gameplay Abilities a partir de decisões do AIController

## Em uma frase
O Gameplay Ability System (GAS) centraliza habilidades de combate, custos de atributos e cooldowns em uma arquitetura extensível.

## Por que importa
Acoplar mecânicas de ataque diretamente no código de movimentação da IA dificulta o compartilhamento de magias e golpes entre jogadores e NPCs.

## Como funciona
Faça o AI Controller emitir chamadas `TryActivateAbilityByClass()` ou disparar tags de evento de gameplay no `AbilitySystemComponent` do Pawn para acionar ataques e bloqueios.

## Exemplo
```cpp
// Acionando Gameplay Ability atraves do AbilitySystemComponent do NPC
if (UAbilitySystemComponent* ASC = Pawn->FindComponentByClass<UAbilitySystemComponent>())
{
    ASC->TryActivateAbilityByClass(HeavyAttackAbilityClass);
}
```

## Limites e trade-offs
Disparar habilidades sem checar se o NPC possui recursos (mana, estamina) suficientes ou se está sob efeito de atordoamento (*Stun*) gera falhas de execução silenciosas.

## Como verificar
Consulte as Gameplay Tags ativas no personagem antes de solicitar a ativação da habilidade para validar se o agente está livre para agir.

## Conexões
- [[unreal-mass-ai-processar-agentes-com-massentity]] — Veja também: Unreal Engine: simular multidões com arquitetura ECS MassEntity e Mass AI.
- [[unreal-motion-warping-alinhar-interacoes-fisicas]] — Veja também: Unreal Engine: alinhar pontos de contato e saltos com Motion Warping.
- [[unreal-statetree-implementar-tasks-assincronas]] — Conexão temática direta com unreal-statetree-implementar-tasks-assincronas.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Conexão temática direta com unity-utility-ai-avaliar-decisoes-com-curvas.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
