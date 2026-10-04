---
id: software.criacao_ia.tranche01.000059
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

# Godot: escolher NavigationLayers por uso

## Em uma frase

NavigationLayers filtram quais regiões um agente considera ao consultar o mapa, permitindo superfícies específicas para classes de movimento.

## Por que importa

Um personagem que voa, nada ou atravessa portas pode precisar de possibilidades de rota diferentes de um pedestre.

## Como funciona

Atribua camadas às regiões e configure máscara de cada agente conforme locomotor e regra de gameplay.

## Exemplo

Um robô terrestre ignora uma plataforma de salto, enquanto um drone inclui caminhos em camada aérea preparada para seu movimento.

## Limites e trade-offs

As camadas não implementam animação nem física do modo de transporte; a locomação ainda precisa executar o trajeto.

## Como verificar

Compare consultas com máscaras diferentes e confira visualmente que cada personagem escolhe superfícies compatíveis.

## Conexões
- [[godot-usar-obstacles-para-geometria-e-fluxo]] — Godot: usar obstacles para geometria e fluxo.
- [[godot-validar-navegacao-em-movimento-real]] — Godot: validar navegação em movimento real.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
