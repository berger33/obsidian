---
id: software.criacao_ia.tranche02.000143
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

# Unity: orientar cabeça e olhar com Multi-Aim Constraint

## Em uma frase
A restrição Multi-Aim Constraint direciona a rotação da cabeça, pescoço e olhos do personagem para pontos de interesse no cenário.

## Por que importa
Personagens que mantêm o olhar fixo no vazio parecem estáticos e desconectados dos eventos e companheiros ao seu redor.

## Como funciona
Adicione uma `MultiAimConstraint` na cadeia de ossos da cabeça, defina o alvo como a posição do jogador e ajuste os limites de rotação angular para evitar torções excessivas no pescoço.

## Exemplo
```csharp
// Atribuindo o alvo do jogador ao componente MultiAimConstraint
[SerializeField] private MultiAimConstraint headAimConstraint;

public void LookAtTarget(Transform targetTransform)
{
    var data = headAimConstraint.data.sourceObjects;
    data.Clear();
    data.Add(new WeightedTransform(targetTransform, 1.0f));
    headAimConstraint.data.sourceObjects = data;
}
```

## Limites e trade-offs
Mudar o alvo abruptamente faz a cabeça do personagem girar instantaneamente em alta velocidade, quebrando a ilusão de peso orgânico.

## Como verificar
Interpole a coordenada do target com `Vector3.SmoothDamp` para garantir movimentos oculares e de cabeça naturais.

## Conexões
- [[unity-animation-rigging-ajustar-pes-com-two-bone-ik]] — Veja também: Unity: ajustar pés em terrenos inclinados com Two-Bone IK.
- [[unity-animation-rigging-suavizar-com-damp-transform]] — Veja também: Unity: suavizar movimento de armas e acessórios com Damp Transform.
- [[unity-animation-rigging-montar-rigbuilder]] — Conexão temática direta com unity-animation-rigging-montar-rigbuilder.
- [[godot-calcular-cone-de-visao-com-area3d-e-dot-product]] — Conexão temática direta com godot-calcular-cone-de-visao-com-area3d-e-dot-product.
- [[audio-ia-mapear-visemas-a-blend-shapes-faciais]] — Conexão temática direta com audio-ia-mapear-visemas-a-blend-shapes-faciais.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
