---
id: software.criacao_ia.tranche01.000055
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

# Godot: distinguir caminho de evasão local

## Em uma frase

Pathfinding escolhe uma rota até o alvo, enquanto avoidance tenta reduzir conflitos entre agentes em movimento local.

## Por que importa

Entender a separação evita esperar que desvio local corrija um caminho global bloqueado ou que mude o alvo do agente.

## Como funciona

Use consulta de caminho para progresso global e habilite evasão apenas para conflitos pertinentes; aplique a velocidade segura retornada ao corpo.

## Exemplo

Dois NPCs podem compartilhar corredor e reduzir velocidade para passar, mantendo o mesmo destino calculado no mapa.

## Limites e trade-offs

Evasão não garante passagem em geometria estreita nem atualiza por si só a rota quando o alvo muda.

## Como verificar

Compare cena com um agente e vários; confira velocidade segura, destino e caminho quando aparece congestionamento.

## Conexões
- [[godot-controlar-a-chegada-ao-waypoint]] — Godot: controlar a chegada ao waypoint.
- [[godot-aplicar-velocidade-de-avoidance]] — Godot: aplicar velocidade de avoidance.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
