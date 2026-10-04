---
id: software.criacao_ia.tranche02.000147
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

# Unity: reconstruir NavMeshSurface em tempo de execução

## Em uma frase
O componente NavMeshSurface permite gerar e atualizar malhas de navegação em runtime para suportar cenários modulares e destrutíveis.

## Por que importa
Malhas de navegação estáticas impedem a movimentação correta de IA em jogos com mapas gerados proceduralmente ou obstáculos dinâmicos.

## Como funciona
Invoque o método assíncrono `navMeshSurface.UpdateNavMesh(navMeshSurface.navMeshData)` após instanciar novas salas ou remover pontes e paredes no cenário do jogo.

## Exemplo
```csharp
// Reconstruindo a superficie de navegacao em runtime no Unity
using Unity.AI.Navigation;
using UnityEngine;

public class DynamicDungeonNav : MonoBehaviour
{
    [SerializeField] private NavMeshSurface surface;

    public void OnLevelGenerated()
    {
        surface.BuildNavMesh();
    }
}
```

## Limites e trade-offs
Reconstruir superfícies de navegação completas a cada frame congela a thread principal; utilize recálculos localizados por fatias (*bounds*).

## Como verificar
Gere uma masmorra procedural e observe se os agentes calculam rotas válidas imediatamente após a conclusão do build do NavMesh.

## Conexões
- [[unity-utility-ai-compor-fatores-de-saude-e-distancia]] — Veja também: Unity: compor fatores de saúde e distância em pontuações de ação.
- [[unity-navmesh-atribuir-custos-por-area-de-terreno]] — Veja também: Unity: atribuir custos diferenciados por tipo de área no NavMesh.
- [[godot-preparar-malha-de-navegacao]] — Conexão temática direta com godot-preparar-malha-de-navegacao.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
