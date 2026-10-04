---
id: software.criacao_ia.tranche01.000054
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

# Godot: controlar a chegada ao waypoint

## Em uma frase

Distâncias de chegada determinam quando o agente considera o destino próximo o suficiente para avançar ou concluir o caminho.

## Por que importa

Tolerância muito pequena provoca oscilação perto de pontos; tolerância ampla faz personagem cortar curvas ou parar cedo.

## Como funciona

Ajuste distância ao alvo e ao caminho conforme tamanho do corpo, velocidade e precisão necessária, mantendo parâmetros compreensíveis.

## Exemplo

Um robô grande recebe margem maior para contornar corredor, enquanto um cursor controlado com precisão usa tolerância menor.

## Limites e trade-offs

Os valores não substituem física do personagem; velocidade, aceleração e colisões influenciam a aproximação observada.

## Como verificar

Teste em curvas apertadas e destinos junto à parede, medindo oscilação, sobrepassagem e distância real de parada.

## Conexões
- [[godot-sincronizar-consultas-com-o-mapa]] — Godot: sincronizar consultas com o mapa.
- [[godot-distinguir-caminho-de-evasao-local]] — Godot: distinguir caminho de evasão local.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
