---
id: software.criacao_ia.tranche02.000148
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

# Unity: atribuir custos diferenciados por tipo de área no NavMesh

## Em uma frase
A atribuição de custos diferenciados por tipo de área orienta o pathfinding do NavMeshAgent a preferir caminhos mais seguros ou rápidos.

## Por que importa
Agentes que ignoram o tipo de terreno atravessam fogo, lama e pântanos quando esses caminhos são geometricamente mais curtos.

## Como funciona
Defina camadas de área como *Water*, *Mud* ou *Danger* nas configurações de navegação com custos elevados (ex.: 5.0 vs. 1.0 para chão plano) e aplique essas áreas em modificadores de volume.

## Exemplo
```csharp
// Ajustando a mascara de areas de navegacao permitidas para o agente
NavMeshAgent agent = GetComponent<NavMeshAgent>();
// Desativar a area de perigo (Danger) da mascara de travessia do agente
int dangerAreaIndex = NavMesh.GetAreaFromName("Danger");
agent.areaMask &= ~(1 << dangerAreaIndex);
```

## Limites e trade-offs
Custos de área afetam apenas o cálculo de rota do NavMeshAgent; não impedem que o agente seja empurrado para dentro da área perigosa por física.

## Como verificar
Posicione uma poça tóxica com custo alto entre o NPC e o jogador e confirme se o agente dá a volta pelo caminho limpo.

## Conexões
- [[unity-navmesh-reconstruir-superficie-em-runtime]] — Veja também: Unity: reconstruir NavMeshSurface em tempo de execução.
- [[unity-playablegraph-mesclar-animacoes-procedurais]] — Veja também: Unity: mesclar animações procedurais usando a PlayableGraph API.
- [[godot-escolher-navigationlayers-por-uso]] — Conexão temática direta com godot-escolher-navigationlayers-por-uso.
- [[godot-aplicar-velocidade-de-avoidance]] — Conexão temática direta com godot-aplicar-velocidade-de-avoidance.

## Fontes
- [Unity Animation Rigging Package Manual](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/index.html) — Documentação oficial do componente rigbuilder, restrições procedurais twoboneik, multi-aim e damptransform. Consulta: 2026-10-04.
- [Unity Animation Rigging — TwoBoneIKConstraint](https://docs.unity3d.com/Packages/com.unity.animation.rigging@1.3/manual/constraints/TwoBoneIKConstraint.html) — Referência técnica detalhando parâmetros de ik, targets polares e ajuste dinâmico em superfícies. Consulta: 2026-10-04.
