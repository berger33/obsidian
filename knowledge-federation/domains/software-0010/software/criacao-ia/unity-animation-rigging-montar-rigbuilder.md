---
id: software.criacao_ia.tranche02.000141
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

# Unity: montar componente RigBuilder e camadas de restrição

## Em uma frase
O pacote Animation Rigging permite aplicar restrições procedurais dinâmicas sobre esqueletos durante a execução do jogo no Unity.

## Por que importa
Ajustes procedurais corrigem poses capturadas para adaptar o personagem a irregularidades do cenário e empunhaduras de armas.

## Como funciona
Adicione o componente `RigBuilder` na raiz do GameObject do personagem e crie GameObjects filhos contendo componentes `Rig` e restrições específicas (Two-Bone IK, Multi-Aim, Damp Transform).

## Exemplo
```csharp
// Exemplo de configuracao de RigBuilder em C# no Unity
using UnityEngine;
using UnityEngine.Animations.Rigging;

public class CharacterRigSetup : MonoBehaviour
{
    [SerializeField] private RigBuilder rigBuilder;
    [SerializeField] private Rig aimRig;

    public void SetAimRigWeight(float weight)
    {
        aimRig.weight = Mathf.Clamp01(weight);
    }
}
```

## Limites e trade-offs
O cálculo de múltiplas camadas de rigging em muitos personagens simultâneos impacta o desempenho de CPU em plataformas mobile.

## Como verificar
Ajuste os pesos (`weight`) das camadas de Rig dinamicamente para desativar restrições desnecessárias quando o personagem estiver inativo.

## Conexões
- [[unity-animation-rigging-ajustar-pes-com-two-bone-ik]] — Veja também: Unity: ajustar pés em terrenos inclinados com Two-Bone IK.
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Conexão temática direta com unity-animation-rigging-orientar-olhar-com-multi-aim.
- [[blender-validar-o-rig-antes-de-exportar]] — Conexão temática direta com blender-validar-o-rig-antes-de-exportar.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
