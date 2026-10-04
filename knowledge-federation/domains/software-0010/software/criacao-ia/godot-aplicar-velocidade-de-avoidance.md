---
id: software.criacao_ia.tranche01.000056
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

# Godot: aplicar velocidade de avoidance

## Em uma frase

A evasão calcula uma velocidade preferível segura para reduzir colisões locais, mas o script precisa respeitar seu resultado.

## Por que importa

Ignorar a velocidade sugerida torna o agente visualmente ativo sem aproveitar a solução de prevenção de colisões.

## Como funciona

Envie velocidade desejada, aguarde a notificação documentada e use a velocidade segura ao mover o corpo no ciclo apropriado.

## Exemplo

Um personagem acelera em direção ao próximo waypoint e substitui a velocidade pelo retorno seguro antes de executar o movimento.

## Limites e trade-offs

O comportamento pode variar com frequência de atualização, raio, vizinhos e restrições físicas do personagem.

## Como verificar

Desenhe vetores desejado e seguro e teste cruzamentos, paredes próximas e agentes de velocidades distintas.

## Conexões
- [[godot-distinguir-caminho-de-evasao-local]] — Godot: distinguir caminho de evasão local.
- [[godot-particionar-avoidance-com-layers]] — Godot: particionar avoidance com layers.

## Fontes
- [Godot Docs — Introduction to 3D navigation](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html) — Apresenta mapas e malhas de navegação tridimensionais na Godot. Consulta: 2026-10-04.
- [Godot Docs — Using NavigationAgents](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_using_navigationagents.html) — Explica o uso e os cuidados de NavigationAgent para seguir caminho e evitar colisões. Consulta: 2026-10-04.
