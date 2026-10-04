---
id: software.criacao_ia.tranche04.000349
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: flags de render do shader espacial que economizam passes inteiros

## Em uma frase
render_mode no espacial controla comportamento de pipeline: shadows_disabled recebe mas não projeta, depth_draw_* decide quando o material se auto-ocultar resolve, skip_vertex_transform ignora a view-matriz e wireframe exige um toggle extra no Compatibility.

## Por que importa
Cada flag muda o que o render pass executa: um material de 'luz fake' sem sombra economiza o depth pass da sombra; um quad de pós-processamento com skip_vertex_transform evita multiplicação de matriz por vértice. Desconhecer as flags é pagar passes que o material já declarou não precisar.

## Como funciona
Escreva no header: 'render_mode shadows_disabled;' para objetos que não devem projetar (partículas, decals aditivos); depth_draw_always para transparentes que precisam de profundidade (água com reflexo correto), depth_draw_never para auto-composição previsível de sprites de UI 3D; cull_back/front para dupla-face barata; fog_disabled conforme a nota da página. Para ver wireframe num material em Compatibility, a página espacial documenta o pré-requisito de gerar malha com 'set_debug_generate_wireframes'.

## Exemplo
O plano de reflexo 'fake' de um piso: skip_vertex_transform + depth_draw_never + shadows_disabled compõe com a cena sem participar dos passes de sombra/depth — o profiler de render passa a mostrar o objeto fora do depth pass.

## Limites e trade-offs
As flags são do material, não do objeto: dois nós que precisam de 'com sombra' e 'sem sombra' do mesmo shader pedem dois materiais. skip_vertex_transform transfere a você a conta de projeção (posicionar o quad fullscreen é o caso de uso), e errar a conta é objeto 'sumindo em câmera Y'. O wireframe de debug não é universal: o pré-requisito documentado existe para fechar a lacuna do Compatibility.

## Como verificar
No render profiler (ou frame debugger), confirme que o objeto com shadows_disabled não aparece no passe de sombra; com depth_draw_always, ele aparece no depth de um transparente. Teste a combinação fog_disabled+blend_add no caso de blend. Rode o wireframe em Compatibility e em Forward+ para ver onde o toggle extra importa.

## Conexões
- [[godot-blend-modes-spatial]] — Godot 4: os blend modes do material espacial e o truque do fog em blend_add.
- [[godot-shader-matrizes-colunares]] — Godot 4: nas shaders, matrizes são colunares — m[1][0] é a segunda coluna, primeira linha.

## Fontes
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — tabela de render_mode do espacial (shadows, depth_draw, skip_vertex_transform, wireframe/Compatibility) Consulta: 2026-10-04.
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — o equivalente 2D (light_only e outros modos) para comparar famílias Consulta: 2026-10-04.
