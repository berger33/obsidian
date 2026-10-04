---
id: software.criacao_ia.tranche02.000146
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html", "https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity: compor fatores de saúde e distância em pontuações de ação

## Em uma frase
A composição de utilidades individuais através de multiplicação ou média ponderada gera decisões contextuais ricas e equilibradas.

## Por que importa
Avaliar fatores de forma isolada pode induzir o NPC a escolher uma ação que pontua bem em um critério, mas é inviável em outro.

## Como funciona
Combine pontuações parciais de utilidade utilizando operadores como a média geométrica ou produto compensado (`Score = U_saude * U_distancia * U_municao`) para garantir que utilidade zero em um fator crítico anule a ação.

## Exemplo
```csharp
// Calculando pontuacao composta de ataque a distancia
public float CalculateAttackScore(float healthUtil, float distUtil, float ammoUtil)
{
    // Se a municao for zero, o produto anula a possibilidade de ataque
    return healthUtil * distUtil * ammoUtil;
}
```

## Limites e trade-offs
O produto direto de múltiplos fatores pequenos pode resultar em números excessivamente baixos que dificultam comparações numéricas estáveis.

## Como verificar
Aplique normalização de raiz enésima quando combinar muitos fatores para manter as pontuações em uma escala intuitiva de 0 a 1.

## Conexões
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Veja também: Unity: avaliar decisões de NPCs com curvas de resposta em Utility AI.
- [[unity-navmesh-reconstruir-superficie-em-runtime]] — Veja também: Unity: reconstruir NavMeshSurface em tempo de execução.
- [[godot-selecionar-alvos-por-distancia-e-ameaca]] — Conexão temática direta com godot-selecionar-alvos-por-distancia-e-ameaca.
- [[unreal-statetree-extrair-contexto-com-evaluators]] — Conexão temática direta com unreal-statetree-extrair-contexto-com-evaluators.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
