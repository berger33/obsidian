---
id: software.criacao_ia.tranche02.000142
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

# Unity: ajustar pés em terrenos inclinados com Two-Bone IK

## Em uma frase
A restrição Two-Bone IK adapta dinamicamente a posição dos pés e quadris conforme a inclinação do terreno sob o personagem.

## Por que importa
Pés que flutuam no ar ou afundam na geometria do solo em rampas e escadas degradam a qualidade visual da movimentação.

## Como funciona
Configure restrições `TwoBoneIKConstraint` para cada perna, vinculando quadril, joelho e pé. Dispare raycasts para baixo a partir dos pés para encontrar a altura do solo e reposicionar o target do IK.

## Exemplo
```csharp
// Ajustando a posicao do target do pe com base no impacto do raycast
RaycastHit hit;
if (Physics.Raycast(footTransform.position + Vector3.up, Vector3.down, out hit, 2.0f, groundLayer))
{
    leftFootIKTarget.position = hit.point + Vector3.up * footOffset;
    leftFootIKTarget.rotation = Quaternion.FromToRotation(Vector3.up, hit.normal) * footTransform.rotation;
}
```

## Limites e trade-offs
Configurações inadequadas do nó polar (*pole target*) podem fazer os joelhos dobrarem para trás ou em ângulos anatômicos bizarros.

## Como verificar
Teste a caminhada do personagem em rampas íngremes e escadarias no Scene View para validar o alinhamento das solas dos pés.

## Conexões
- [[unity-animation-rigging-montar-rigbuilder]] — Veja também: Unity: montar componente RigBuilder e camadas de restrição.
- [[unity-animation-rigging-orientar-olhar-com-multi-aim]] — Veja também: Unity: orientar cabeça e olhar com Multi-Aim Constraint.
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Conexão temática direta com unity-playablegraph-mesclar-animacoes-procedurais.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
