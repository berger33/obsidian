---
id: software.criacao_ia.tranche04.000344
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

# Godot 4: COLOR em 2D é a trama de vértice × modulate × self_modulate

## Em uma frase
No canvas-item fragment, COLOR nasce como produto da cor por-vértice com os multiplicadores do nó, e escrever nele multiplica — não substitui — a leitura final da textura.

## Por que importa
Sprites com vértices coloridos (gradientes de mesh 2D, tesselação) interagem com o shader de um jeito que quem só conhece 'COLOR = branco fixo' não espera: um self_modulate no nó escurece a saída do seu shader de forma invisível no código do shader. Saber a origem de COLOR é o mínimo para 'meu shader ignora o fade do nó' não virar caçada.

## Como funciona
A página de referência define COLOR como o valor composto do vértice (cor por-vértice × modulate × self_modulate). No fragment, ele é legível para modular efeitos e escrevível para tint final — mas lembre que a escrita compõe sobre o que já veio, e as regras de blend do material (mix/mul/add na referência spatial têm análogos) decidem o resto. Para tint seletivo, multiplique só o canal desejado em vez de substituir RGB inteiro.

## Exemplo
Um shader de flash de dano em sprite: 'COLOR.rgb = mix(COLOR.rgb, vec3(1.0), flash_amount)' preserva gradientes por-vértice do mesh e o fade do nó — substituir COLOR por branco puro aniquila ambos os efeitos visuais.

## Limites e trade-offs
CanvasItems sem cores por-vértice recebem COLOR = branco × modulates — o bug simétrico é esperar que o shader 'veja' um modulate animado quando o nó usa material de outra árvore de canvas. No espacial, o análogo de escrita de cor é ALBEDO com regras próprias (e a modulação por-light é outro estágio). TEXTURE × COLOR é a ordem do sample 2D padrão — inverter a ordem das multiplicações não comuta com sRGB.

## Como verificar
Monte um mesh 2D com gradiente por-vértice, anime modulate no nó e confirme no frame capture que ambos chegam ao COLOR do shader (escreva 'COLOR' direto na tela e inspecione). Toggle do self_modulate deve escurecer o efeito igualmente — prova da composição. O teste de fade de entrada (alpha) pega o uso de COLOR.a corretamente.

## Conexões
- [[godot-tempo-time-rollover-pause]] — Godot 4: TIME é tempo de render em segundos, com rolover e sem pause.
- [[godot-particulas-instance-custom]] — Godot 4: INSTANCE_CUSTOM é o canal de dados por-partícula para o shader 2D.

## Fontes
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — define a composição de COLOR a partir de cor de vértice e modulates do nó Consulta: 2026-10-04.
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — regras de operadores e tipos usados nas expressões de cor Consulta: 2026-10-04.
