---
id: software.criacao_ia.tranche01.000060
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

# Godot: validar navegação em movimento real

## Em uma frase

Um caminho calculado só é útil se o personagem conseguir segui-lo com sua física, aceleração e animações.

## Por que importa

Integração entre o motor de navegação e controle de gameplay expõe problemas que uma linha de debug isolada não revela.

## Como funciona

Execute consultas com corpo real, aplique movimento no ciclo de física e mantenha alvo e estado de parada sincronizados.

## Exemplo

Um personagem segue um corredor curvo, evita uma parede móvel e para no raio de interação sem empurrar outro ator.

## Limites e trade-offs

Pathfinding não escolhe estratégia, intenção ou animação; essas decisões precisam de sistemas separados.

## Como verificar

Teste cena sem obstáculo, caminho longo, bloqueio temporário e destino inalcançável; registre waypoint e motivo de parada.

## Conexões
- [[godot-escolher-navigationlayers-por-uso]] — Godot: escolher NavigationLayers por uso.
- [[blender-organizar-clips-como-actions]] — Blender: organizar clips como Actions.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
