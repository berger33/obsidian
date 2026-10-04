---
id: software.criacao_ia.tranche01.000058
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

# Godot: usar obstacles para geometria e fluxo

## Em uma frase

Obstáculos de navegação podem representar estruturas que alteram rotas ou evitar que agentes se aproximem de regiões locais.

## Por que importa

Diferenciar obstáculos estáticos e móveis ajuda a decidir se o mapa deve mudar globalmente ou apenas a evasão local.

## Como funciona

Escolha recurso e modo compatíveis com a finalidade, ajuste geometria e acompanhe a sincronização quando a obstrução altera o mapa.

## Exemplo

Uma barreira móvel temporária pode solicitar atualização de navegação; uma multidão pode usar avoidance sem reconstruir a malha inteira.

## Limites e trade-offs

Rebakes frequentes são caros, e o obstáculo de avoidance não substitui uma malha que representa passagem permanente bloqueada.

## Como verificar

Mova e remova o obstáculo em teste, verificando atualização de rota, custo e ausência de caminho através da área proibida.

## Conexões
- [[godot-particionar-avoidance-com-layers]] — Godot: particionar avoidance com layers.
- [[godot-escolher-navigationlayers-por-uso]] — Godot: escolher NavigationLayers por uso.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
