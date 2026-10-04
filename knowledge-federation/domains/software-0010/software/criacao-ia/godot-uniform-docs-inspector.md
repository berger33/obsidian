---
id: software.criacao_ia.tranche04.000347
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: o /** acima do uniform é documentação vira-inspetor, não comentário decorativo

## Em uma frase
Um comentário de documentação antes de 'uniform' no shader aparece como tooltip na interface do material — o metadado de interface mora no código do shader, não num config separado.

## Por que importa
Material é asset: quem ajusta o efeito é designer/artist no editor, não o autor do shader. Sem hint de unidade ('intensidade em 0..1', 'cor em espaço linear', 'tamanho em pixels'), o material vira caixa-preta e o ajuste vira tentativa-e-erro. A doc da linguagem registra esse recurso de anotação explicitamente.

## Como funciona
Escreva '/** Descrição curta do efeito. */' imediatamente acima da linha do uniform. Combine com as opções de anotação do próprio shader ('source_color' para campo de cor com seletor de cor, 'hint_range' para sliders com limites, 'group' para agrupamento) — a página lista as anotações de uniform válidas e seus efeitos no inspetor. Mantenha as strings de tooltip no inglês do código e a localização, se houver, fora do shader.

## Exemplo
O 'Bloom' expõe: /** Limiar de brilho em luminância linear */ uniform float threshold : hint_range(0.5, 5.0) = 1.2; — o artista passa a ver slider com unidade, e o threshold fora do range deixa de ser caso de bug report.

## Limites e trade-offs
A anotação só alcança o inspetor de material; nada obriga o código do shader a respeitar o range (clamp interno continua sendo responsabilidade do autor). /** fora da posição exata (acima do uniform) não renderiza no inspetor — a sensibilidade a posição é do parser. Tooltip em shader não substitui documentação do preset quando o efeito tem múltiplos uniforms dependentes.

## Como verificar
Abra o inspetor do material e confirme tooltip e slider para cada uniform anotado do efeito — é o teste do designer. Mova o /** uma linha e veja o hint sumir: fixa a regra de posição no seu time. Uma revisão de 'shader publicado' deveria exigir range anotado em toda uniform de usuário.

## Conexões
- [[godot-shading-sem-cast-implicito]] — Godot 4: a shading language não faz cast implícito — e suas variáveis locais nascem sem inicializar.
- [[godot-blend-modes-spatial]] — Godot 4: os blend modes do material espacial e o truque do fog em blend_add.

## Fontes
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — documenta os comentários de documentação virando tooltips do inspetor Consulta: 2026-10-04.
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — página onde as anotações de uniforms de materiais 3D operam Consulta: 2026-10-04.
