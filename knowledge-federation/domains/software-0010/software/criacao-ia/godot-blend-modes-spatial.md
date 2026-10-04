---
id: software.criacao_ia.tranche04.000348
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: os blend modes do material espacial e o truque do fog em blend_add

## Em uma frase
render_mode blend_* escolhe como o fragment compõe com o framebuffer (mix, add, sub, mul, premultiplied alpha) — e a página documenta um caso em que fog e blend add brigam feio.

## Por que importa
Holograma, faísca e glass sem 'alpha mix' convencional se constroem com blend modes não-padrão; o bug correspondente aparece no ambiente: um objeto aditivo pintado com fog vira um bloco de névoa luminosa na borda do mapa. A doc do blend_add na página espacial recomenda explicitamente fog_disabled para esse caso.

## Como funciona
declare no header do shader: 'render_mode blend_add;' (ou blend_mix com alpha manual via ALPHA, blend_sub, blend_mul, blend_premultiplied_alpha para canais que já vêm pré-multiplicados — típico de efeitos exportados). Para transparentes aditivos num cenário com fog, feche o par: 'blend_add, fog_disabled'. A página também cobre os análogos de profundidade (depth_draw_*) e o modelo de render (shadows, cull), porque o header de render_mode é um conjunto, não uma flag isolada.

## Exemplo
O material de 'laser' (faíscas sobre céu claro) troca blend_mix por blend_add + fog_disabled: as faíscas somam sem halo de névoa, e o depth_draw_never do mesmo header evita que o plasma se auto-oculte.

## Limites e trade-offs
Modos aditivos multiplicativos exigem atenção ao pipeline de render (a doc do fog_disabled é o caso documentado; outros efeitos, como iluminação em aditivo, pedem teste por backend — a página separa o que muda entre Forward+, Mobile e Compatibility). premultiplied_alpha não é 'mais correto': é um contrato sobre o formato da origem. E render_mode é por material; a variação por preset no mesmo shader exige dois materiais.

## Como verificar
Um painel de matriz 3×2 dos cinco modos sobre o mesmo fundo (sólido, névoa, bloom) e o diff visual por backend de render — cada um é uma configuração real de shipping. No caso do fog: compare blend_add com/sem fog_disabled no mesmo cenário névoado; o doc claim é o delta. Render-test nos três backends para confirmar o que muda.

## Conexões
- [[godot-uniform-docs-inspector]] — Godot 4: o /** acima do uniform é documentação vira-inspetor, não comentário decorativo.
- [[godot-render-flags-sombras-wireframe]] — Godot 4: flags de render do shader espacial que economizam passes inteiros.

## Fontes
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — lista os render_mode de blend e a nota de fog_disabled para blend_add Consulta: 2026-10-04.
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — sintaxe do header render_mode e uniforms associadas Consulta: 2026-10-04.
