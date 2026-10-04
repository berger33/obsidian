---
id: software.criacao_ia.tranche01.000051
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html", "https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot: preparar malha de navegação

## Em uma frase

Uma malha de navegação descreve regiões nas quais um agente pode planejar deslocamento evitando geometria considerada obstáculo.

## Por que importa

Separar superfície caminhável de colisão visual ajuda o motor a encontrar caminhos válidos sem codificar rotas fixas.

## Como funciona

Marque fontes de geometria e regiões navegáveis, configure a montagem do mapa e aguarde a sincronização antes de consultar caminhos.

## Exemplo

Uma arena com paredes usa malha que cobre pisos acessíveis e exclui fossos e áreas decorativas sem superfície caminhável.

## Limites e trade-offs

Malha desatualizada, escala incorreta ou geometria ausente pode criar atalhos e caminhos que atravessam obstáculos.

## Como verificar

Visualize a malha no editor e compare pontos do caminho calculado com o piso e colisores da cena.

## Conexões
- [[unreal-depurar-a-decisao-do-npc-em-runtime]] — Unreal: depurar a decisão do NPC em runtime.
- [[godot-configurar-destino-do-navigationagent]] — Godot: configurar destino do NavigationAgent.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
