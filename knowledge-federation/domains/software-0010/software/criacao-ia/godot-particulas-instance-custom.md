---
id: software.criacao_ia.tranche04.000345
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

# Godot 4: INSTANCE_CUSTOM é o canal de dados por-partícula para o shader 2D

## Em uma frase
Em processos de partículas 2D, o float3 de custom data chega ao shader como INSTANCE_CUSTOM, com três canais semânticos definidos pela fonte de dados (rotação, fase, quadro no caso padrão).

## Por que importa
Partículas animam por CPU (process material) e por GPU (shader). O cano entre os dois é o buffer de custom data — sem usá-lo, todo movimento vira atribuição de transform por partícula no processo; com ele, rotação/tint/quadro vivem no shader. O erro típico é ler INSTANCE_CUSTOM sem configurar a fonte de dados correspondente, e o shader receber zero silencioso.

## Como funciona
No GPUParticles2D, configure o Custom Data com a fonte que produz o vetor (a referência 2D documenta o uso canônico com a grade de animação: x = rotação, y = fase, z = quadro no caso de 'Animation'). No shader canvas-item, leia INSTANCE_CUSTOM no fragment e derive o UV do quadro: 'uv = (quadro + fração(fase))/colunas' com o TEXTURE_PIXEL_SIZE ou tamanho do atlas definindo o passo. Mantenha as constantes do layout do atlas no material, não hardcoded no texto.

## Exemplo
Folhagem ao vento: um custom data 'Random' por partícula (x = offset de fase) alimenta o shader que ondula VERTEX — zero CPU por frame e o efeito é por-partícula, não por-emissor.

## Limites e trade-offs
O significado dos três canais não é fixo pela linguagem — é acordado entre a fonte de custom data e o shader; dois materiais lendo o mesmo buffer com suposições divergentes é o bug. O canal é um vec3 de 32 bits — contadores grandes de quadro/fase perdem precisão; e ele existe na via GPU do GPUParticles2D (no CPU process a via é outra).

## Como verificar
Um teste de leitura direta: 'COLOR = INSTANCE_CUSTOM.xyzx' — os três canais aparecem nas cores primárias com os valores esperados da fonte. Configure a fonte errada (ou nenhuma) e confirme o canal zerado — o diagnóstico do bug clássico. Meça o custo de processo de CPU vs. shader no alvo mínimo do jogo.

## Conexões
- [[godot-color-vertex-multipliers]] — Godot 4: COLOR em 2D é a trama de vértice × modulate × self_modulate.
- [[godot-shading-sem-cast-implicito]] — Godot 4: a shading language não faz cast implícito — e suas variáveis locais nascem sem inicializar.

## Fontes
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — documenta INSTANCE_CUSTOM e o mapeamento de canais no caso de grade de animação Consulta: 2026-10-04.
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — par 3D do mesmo mecanismo para GPUParticles3D Consulta: 2026-10-04.
