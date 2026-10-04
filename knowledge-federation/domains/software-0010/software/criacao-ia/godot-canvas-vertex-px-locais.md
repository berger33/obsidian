---
id: software.criacao_ia.tranche04.000342
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: no canvas-item, VERTEX fala em píxeles locais — não em UV nem em mundo

## Em uma frase
A variável VERTEX num shader 2D é a posição do vértice em píxeles no espaço local do objeto, o que muda como se escreve deslocamento, ondulação e máscaras espaciais.

## Por que importa
Portar um shader de tela-normalizada (UV 0..1) direto para canvas-item produz deslocamentos invisíveis ou absurdos: somar 0.01 em VERTEX move 0.01 pixel. Inversamente, máscaras de 'onde estou?' por posição exigem converter de volta, e a referência define a origem/escala — o resto é matemática.

## Como funciona
Trate VERTEX como entrada de leitura no vertex (posição local em px) e como saída de escrita para deslocar o vértice. Para trabalhar em unidades normalizadas, derive-as você mesmo a partir de tamanho (por exemplo, via TEXTURE_PIXEL_SIZE, que a própria referência define como 1/tamanho da textura). Em fragment, a posição no render target vem de FRAGCOORD, não de VERTEX. Escrita em VERTEX no fragment não existe — é regra de estágio da tabela.

## Exemplo
Uma ondulação de água num sprite: 'VERTEX += vec2(sin(TIME*3.0 + UV.y*20.0), 0.0) * amplitude' com amplitude em píxeles definidos, não em fração — e o teste visual é a amplitude não mudar com o tamanho da textura.

## Limites e trade-offs
O espaço local acompanha transforms do nó (a referência 2D define localidade; escala no CanvasItem entra antes do shader ver). Em objetos com region/atlas, a UV pode não cobrir 0..1 — usar UV como proxy de posição é fonte de bugs, prefira a geometria. Deslocar VERTEX altera também a área coberta pelo fill, com custo em overdrawing.

## Como verificar
Num quad de textura 100×100, some 10 em VERTEX e meça 10 px de deslocamento na tela com câmera 1:1 — a escala está correta. Compare o comportamento com escala do nó para confirmar o enquadramento local. Render test com region ativo mostra por que UV não substitui posição.

## Conexões
- [[godot-shader-builtins-por-familia]] — Godot 4: cada tipo de shader tem seu conjunto de embutidos — a referência é o mapa.
- [[godot-tempo-time-rollover-pause]] — Godot 4: TIME é tempo de render em segundos, com rolover e sem pause.

## Fontes
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — define VERTEX (píxeles locais) e TEXTURE_PIXEL_SIZE e as direções por estágio Consulta: 2026-10-04.
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — linguagem comum (tipos, operadores) usada dentro de qualquer família Consulta: 2026-10-04.
