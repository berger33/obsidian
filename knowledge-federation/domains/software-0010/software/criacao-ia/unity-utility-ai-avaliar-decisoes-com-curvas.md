---
id: software.criacao_ia.tranche02.000145
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

# Unity: avaliar decisões de NPCs com curvas de resposta em Utility AI

## Em uma frase
A arquitetura Utility AI utiliza curvas matemáticas de resposta para atribuir valores de utilidade a cada ação possível do NPC.

## Por que importa
Árvores de decisão tradicionais tornam-se difíceis de calibrar e manter quando múltiplos fatores contínuos precisam ser ponderados simultaneamente.

## Como funciona
Mapeie variáveis de entrada (saúde normalizada, munição, distância) em valores de utilidade entre 0.0 e 1.0 utilizando objetos `AnimationCurve` editáveis diretamente no Inspector do Unity.

## Exemplo
```csharp
// Avaliando utilidade de curar-se com base na saude atual via AnimationCurve
[SerializeField] private AnimationCurve healthUtilityCurve;

public float EvaluateHealUtility(float currentHealth, float maxHealth)
{
    float healthPercent = Mathf.Clamp01(currentHealth / maxHealth);
    return healthUtilityCurve.Evaluate(healthPercent);
}
```

## Limites e trade-offs
Curvas mal calibradas podem gerar empates frequentes entre ações ou levar o NPC a hesitar entre comportamentos opostos a cada tick.

## Como verificar
Selecione a ação com maior utilidade e confira se a curva produz comportamentos proporcionais ao perigo enfrentado pelo agente.

## Conexões
- [[unity-animation-rigging-suavizar-com-damp-transform]] — Veja também: Unity: suavizar movimento de armas e acessórios com Damp Transform.
- [[unity-utility-ai-compor-fatores-de-saude-e-distancia]] — Veja também: Unity: compor fatores de saúde e distância em pontuações de ação.
- [[unity-ia-visualizar-decisoes-com-gizmos-de-cena]] — Conexão temática direta com unity-ia-visualizar-decisoes-com-gizmos-de-cena.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
