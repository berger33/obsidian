---
id: software.criacao_ia.tranche02.000149
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

# Unity: mesclar animações procedurais usando a PlayableGraph API

## Em uma frase
A PlayableGraph API oferece controle de baixo nível sobre a árvore de avaliação de animações e áudio no Unity.

## Por que importa
Criar nós customizados no grafo possibilita mesclar animações pré-gravadas com dados procedurais de física sem a rigidez do Animator Controller tradicional.

## Como funciona
Instancie um `PlayableGraph`, conecte nós `AnimationClipPlayable` a um `AnimationMixerPlayable` e envie o resultado para o `AnimationPlayableOutput` associado ao componente Animator.

## Exemplo
```csharp
// Exemplo basico de montagem de PlayableGraph em C#
using UnityEngine;
using UnityEngine.Animations;
using UnityEngine.Playables;

public class SimplePlayableMixer : MonoBehaviour
{
    private PlayableGraph graph;
    [SerializeField] private AnimationClip clipA;
    [SerializeField] private AnimationClip clipB;

    void Start()
    {
        graph = PlayableGraph.Create("CustomAnimationGraph");
        var output = AnimationPlayableOutput.Create(graph, "AnimationOutput", GetComponent<Animator>());
        var mixer = AnimationMixerPlayable.Create(graph, 2);
        output.SetSourcePlayable(mixer);
        // Conectar clips e iniciar grafo
        graph.Play();
    }
}
```

## Limites e trade-offs
Grafos instanciados devem ser explicitamente destruídos com `graph.Destroy()` no evento `OnDestroy` para evitar vazamentos de memória na engine.

## Como verificar
Altere os pesos das portas do mixer em tempo real e verifique se as poses dos dois clips se fundem suavemente sem jittering.

## Conexões
- [[unity-navmesh-atribuir-custos-por-area-de-terreno]] — Veja também: Unity: atribuir custos diferenciados por tipo de área no NavMesh.
- [[unity-ia-visualizar-decisoes-com-gizmos-de-cena]] — Veja também: Unity: visualizar sensores e scores de utilidade com Gizmos de cena.
- [[unity-animation-rigging-montar-rigbuilder]] — Conexão temática direta com unity-animation-rigging-montar-rigbuilder.
- [[godot-sincronizar-ia-com-animationtree]] — Conexão temática direta com godot-sincronizar-ia-com-animationtree.
- [[unreal-sequencer-animar-com-tracks-e-keyframes]] — Conexão temática direta com unreal-sequencer-animar-com-tracks-e-keyframes.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
