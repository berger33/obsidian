---
id: software.criacao_ia.tranche01.000057
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

# Godot: particionar avoidance com layers

## Em uma frase

Camadas e máscaras permitem decidir quais agentes consideram outros agentes como vizinhos para evitar colisões.

## Por que importa

Grupos diferentes, como aliados, multidões e projéteis, nem sempre precisam influenciar a mesma decisão local.

## Como funciona

Defina bitmasks coerentes em cada agente e documente quais categorias enxergam ou ignoram durante o cálculo.

## Exemplo

NPCs aliados podem coordenar passagem entre si, enquanto um efeito visual sem colisão não entra na lista de vizinhos.

## Limites e trade-offs

Máscara incorreta pode causar colisões ou cálculos desnecessários; mudar categorias sem testar cria comportamento assimétrico.

## Como verificar

Monte pares com camadas distintas e confirme pelo debug e movimento quais agentes são tratados como vizinhos.

## Conexões
- [[godot-aplicar-velocidade-de-avoidance]] — Godot: aplicar velocidade de avoidance.
- [[godot-usar-obstacles-para-geometria-e-fluxo]] — Godot: usar obstacles para geometria e fluxo.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
