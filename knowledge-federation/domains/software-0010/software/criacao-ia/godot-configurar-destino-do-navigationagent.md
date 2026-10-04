---
id: software.criacao_ia.tranche01.000052
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

# Godot: configurar destino do NavigationAgent

## Em uma frase

NavigationAgent recebe um alvo e expõe informação do caminho para um personagem implementar seu movimento.

## Por que importa

O agente planeja rota, mas o script de gameplay ainda precisa aplicar velocidade e mover o corpo corretamente.

## Como funciona

Atualize o alvo quando ele mudar, consulte o próximo ponto com a frequência documentada e direcione o personagem com a física do projeto.

## Exemplo

Um guarda define posição do jogador como alvo e orienta seu CharacterBody3D para o waypoint seguinte a cada passo de física.

## Limites e trade-offs

Alvo inatingível ou corpo que não se move para o waypoint pode fazer o agente recalcular continuamente.

## Como verificar

Registre destino, waypoint, posição e velocidade e confirme que a distância ao próximo ponto diminui sem atravessar colisores.

## Conexões
- [[godot-preparar-malha-de-navegacao]] — Godot: preparar malha de navegação.
- [[godot-sincronizar-consultas-com-o-mapa]] — Godot: sincronizar consultas com o mapa.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
