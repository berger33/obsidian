---
id: software.criacao_ia.tranche02.000150
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

# Unity: visualizar sensores e scores de utilidade com Gizmos de cena

## Em uma frase
A renderização de Gizmos e Handles na Scene View permite inspecionar raios de percepção e pontuações de ações durante o jogo.

## Por que importa
Diagnosticar por que uma IA tomou uma decisão inesperada torna-se muito mais rápido quando os dados internos são desenhados diretamente no mundo do jogo.

## Como funciona
Implemente o método `OnDrawGizmosSelected()` desenhando esferas nos raios de visão, linhas até os alvos identificados e rótulos de texto com a utilidade calculada.

## Exemplo
```csharp
// Desenhando cone de visao e status de combate no Unity Editor
void OnDrawGizmosSelected()
{
    Gizmos.color = Color.yellow;
    Gizmos.DrawWireSphere(transform.position, detectionRadius);
    if (currentTarget != null)
    {
        Gizmos.color = Color.red;
        Gizmos.DrawLine(transform.position, currentTarget.position);
    }
}
```

## Limites e trade-offs
O desenho excessivo de Gizmos complexos pode reduzir a taxa de quadros do editor durante a reprodução da cena no modo Play.

## Como verificar
Utilize `OnDrawGizmosSelected` em vez de `OnDrawGizmos` para renderizar apenas os dados visuais do NPC selecionado no momento.

## Conexões
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Veja também: Unity: mesclar animações procedurais usando a PlayableGraph API.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Conexão temática direta com unity-utility-ai-avaliar-decisoes-com-curvas.
- [[godot-depurar-vetores-de-ia-com-draw-line]] — Conexão temática direta com godot-depurar-vetores-de-ia-com-draw-line.
- [[unreal-gameplay-debugger-inspecionar-ia-em-runtime]] — Conexão temática direta com unreal-gameplay-debugger-inspecionar-ia-em-runtime.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
