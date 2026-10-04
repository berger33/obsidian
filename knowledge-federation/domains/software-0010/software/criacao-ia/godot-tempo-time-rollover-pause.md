---
id: software.criacao_ia.tranche04.000343
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: TIME é tempo de render em segundos, com rolover e sem pause

## Em uma frase
O uniform built-in TIME avança em segundos multiplicado pelo time_scale, dá rollover num limite configurável e continua correndo com a árvore pausada — três detalhes que viram artefatos quando ignorados.

## Por que importa
Efeitos cíclicos (brilho, ruído animado, scanline) usam fmod/sin de TIME: um rolover em 3600 s produz um hitch anual quase invisível no dev e dramático em eventos longos (maratonas, idle games). E 'o menu pausou mas a lava continua fluindo' é o segundo sintoma clássico, porque TIME não congela com get_tree().paused.

## Como funciona
Para ciclos, conte com o rollover: a página da referência indica o limite default (3600 s) configurável em rendering/limits/time/time_rollover_secs. Se o efeito precisa congelar com o pause, a alternativa documentada no próprio texto é usar um uniform global animado por um script (que você congela junto com o pause), em vez do built-in. Para sincronia entre materiais na mesma tela, o uniform global é a via correta independentemente do problema.

## Exemplo
O shader de portal anima com TIME e o hitch de rollover aparece exatamente em 1 h de demo — a correção de produção é subir o limite para 24 h na tela de configuração e mover sincronia fina para um global uniform atualizado no _process.

## Limites e trade-offs
Um global uniform animado por script não roda em materiais dentro de CanvasLayers customizados com seu próprio processo, nem sobrevive a shaders que rodam fora de frame (compute não é caso aqui). Aumentar o limite de rollover não elimina a quantização de float32 em segundos grandes — precisão de 'sin de tempo' degrada antes do wrap.

## Como verificar
Configure time_rollover_secs baixo (ex.: 10), observe o wrap num efeito cíclico e confirme que o hitch coincide com o valor. Pause a árvore com get_tree().paused e registre que TIME do material segue avançando — a página documenta o comportamento e o workaround. Em performance, compare o custo de global uniform vs. built-in no seu alvo móvel.

## Conexões
- [[godot-canvas-vertex-px-locais]] — Godot 4: no canvas-item, VERTEX fala em píxeles locais — não em UV nem em mundo.
- [[godot-color-vertex-multipliers]] — Godot 4: COLOR em 2D é a trama de vértice × modulate × self_modulate.

## Fontes
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — define TIME (segundos × time_scale, rollover, pausa) e aponta o workaround de uniform global Consulta: 2026-10-04.
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — mesmo built-in TIME para shaders 3D, com as mesmas ressalvas Consulta: 2026-10-04.
