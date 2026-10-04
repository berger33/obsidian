---
id: software.criacao_ia.tranche04.000341
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

# Godot 4: cada tipo de shader tem seu conjunto de embutidos — a referência é o mapa

## Em uma frase
As built-ins de um shader Godot (VERTEX, LIGHT, FRAGCOORD, ALBEDO...) pertencem à família do shader — canvas_item, spatial, particles, sky — e declarar uma de outra família é erro, não sintoma de versão.

## Por que importa
O editor compila o texto do shader contra o tipo do material, e a lista de identidades disponíveis vem da página de referência correspondente. A confusão mais comum de port de 2D para 3D é escrever ALBEDO num shader canvas-item porque 'estava no tutorial' — a referência separada existe para matar esse tipo de caça-palavra em docs genéricos.

## Como funciona
Comece pela tabela da página oficial da família: as variáveis por estágio (vertex/fragment e, no espacial, light/forward_add), seus tipos e se são de leitura ou escrita. No canvas-item, VERTEX é posição em píxeles locais; no espacial, VERTEX move o vértice em espaço de view. Quando uma funcionalidade parece 'faltando', procure primeiro na outra família antes de assumir limitação do motor.

## Exemplo
Um dissolve em sprite 2D usa TEXSCREEN/TEXTURE e UV do fragment canvas-item; o mesmo efeito num mesh 3D troca o conjunto por ALBEDO/ALPHA do spatial. Guardar as duas páginas como referência do projeto evita as duas tentativas falhas.

## Limites e trade-offs
As famílias particles e sky compartilham convenções, mas não os conjuntos — a referência por página é obrigatória. Em shaders de partículas, dados de configuração chegam por canais específicos (como INSTANCE_CUSTOM no lado de partículas, documentado na referência canvas-item), não por uniforms inventadas. A disponibilidade de escrita de uma variável também muda por estágio — a tabela indica direção.

## Como verificar
Faça o inventário: liste as builtins usadas no seu material e confirme cada uma na página da família. No editor, use a busca da ajuda inline do shader e compare com a tabela — divergência é alerta de versão errada da doc. Adicione intencionalmente uma variável de outra família e confirme o erro de compilação apontando o nome.

## Conexões
- [[godot-canvas-vertex-px-locais]] — Godot 4: no canvas-item, VERTEX fala em píxeles locais — não em UV nem em mundo.

## Fontes
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — tabela de built-ins e escrita por estágio para shaders 2D Consulta: 2026-10-04.
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — mesma taxonomia para o conjunto 3D (ALBEDO, Metallic/Roughness, flags de render) Consulta: 2026-10-04.
