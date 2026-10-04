---
id: software.criacao_ia.tranche03.000248
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Simulation Zone: gerenciar cache e bake para render

## Em uma frase
Simulation Zones são cacheadas durante playback e podem ser baked em disco para renderização fora de ordem dos frames.

## Por que importa
Um render farm costuma solicitar frames sem reproduzir a timeline sequencialmente, enquanto um cache local em memória pode desaparecer ou consumir muita RAM. Separar preview, cache e bake torna mais previsível renderizar um estado validado.

## Como funciona
Durante playback, confira a faixa roxa de frames válidos na timeline. Para prévia focada só no frame atual, o manual permite desativar Cache e economizar memória. Quando o resultado está pronto para render farm, bake em disco habilita frames não sequenciais. A operação bake abrange todas as simulations em todos os modifiers dos objetos selecionados.

## Exemplo
Antes de enviar uma sequência de destruição ao farm, selecione somente os objetos previstos, execute bake e confirme frames inicial/final. Um worker renderiza os frames 1, 50 e 100 fora de ordem e valida que cada imagem corresponde ao cache salvo.

## Limites e trade-offs
Bake pode atingir mais zones do que a selecionada visualmente, porque inclui simulações nos modifiers dos objetos selecionados. Atualizar geometry, parâmetros ou versão do graph pode invalidar resultados já baked; armazene o arquivo junto de seus assets e revisão.

## Como verificar
Faça cache, invalide um frame intermediário, rebake e renderize frames fora de ordem. Registre objetos selecionados, faixa baked, uso de memória e existência dos dados em disco ao reabrir o projeto.

## Conexões
- [[blender-simulation-anonymous-attributes-state]] — Blender Simulation Zone: declarar atributos anônimos no estado.
- [[blender-instancing-realize-atributos-custo]] — Blender Geometry Nodes: manter instâncias até precisar realizá-las.

## Fontes
- [Blender 5.2 LTS — Simulation Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html) — documenta cache em playback, opção de cache, bake em disco e escopo em objetos selecionados Consulta: 2026-10-04.
- [Blender 5.2 LTS — Geometry Nodes inspection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html) — explica que ferramentas de inspeção mostram dados da última avaliação Consulta: 2026-10-04.
