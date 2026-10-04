---
id: software.criacao_ia.tranche02.000159
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

# Unreal Engine: alinhar pontos de contato e saltos com Motion Warping

## Em uma frase
O Motion Warping distorce dinamicamente animações raiz (*Root Motion*) para garantir que mãos e pés alcancem posições exatas no mundo.

## Por que importa
Animações com trajetórias fixas resultam em golpes no ar ou mãos atravessando beiradas quando o alvo está a uma distância ligeiramente diferente.

## Como funciona
Adicione o componente `MotionWarpingComponent` no personagem e configure modificadores de salto ou ataque no Montage, informando a coordenada do alvo antes de iniciar a execução da animação.

## Exemplo
```cpp
// Configurando o ponto de impacto do Motion Warping no NPC
MotionWarpingComp->AddOrUpdateWarpTargetFromLocation(
    FName("VaultTarget"),
    LedgeEdgeLocation
);
```

## Limites e trade-offs
Distorções de escala exageradas provocam estiramento visual excessivo das pernas e braços do modelo durante a execução do warp.

## Como verificar
Posicione o personagem a diferentes distâncias da mureta e confirme visualmente que a animação de pulo conecta exatamente com o topo do obstáculo.

## Conexões
- [[unreal-gas-acionar-habilidades-pelo-ai-controller]] — Veja também: Unreal Engine: acionar Gameplay Abilities a partir de decisões do AIController.
- [[unreal-gameplay-debugger-inspecionar-ia-em-runtime]] — Veja também: Unreal Engine: inspecionar transições de IA com o Gameplay Debugger.
- [[unity-animation-rigging-ajustar-pes-com-two-bone-ik]] — Conexão temática direta com unity-animation-rigging-ajustar-pes-com-two-bone-ik.
- [[unreal-smart-objects-configurar-slots-de-interacao]] — Conexão temática direta com unreal-smart-objects-configurar-slots-de-interacao.
- [[blender-separar-movimento-in-place-e-root-motion]] — Conexão temática direta com blender-separar-movimento-in-place-e-root-motion.

## Fontes
- [Unreal Engine 5 Documentation — StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine) — Manual oficial do framework statetree, árvores de estados hierárquicas leves, evaluators e tasks. Consulta: 2026-10-04.
- [Unreal Engine 5 Documentation — Smart Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/smart-objects-in-unreal-engine) — Documentação cobrindo smart object definitions, slots de animação, subsistema de reserva e interação com ia. Consulta: 2026-10-04.
