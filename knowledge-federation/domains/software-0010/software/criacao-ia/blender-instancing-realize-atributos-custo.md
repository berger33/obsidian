---
id: software.criacao_ia.tranche03.000249
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: manter instâncias até precisar realizá-las

## Em uma frase
Instance on Points cria referências eficientes a geometry compartilhada; Realize Instances materializa cópias para processamento individual, com possível custo alto.

## Por que importa
Manter objetos como instâncias evita duplicar dados base, mas certos nós precisam de geometry real para operações por elemento. Realizar cedo em uma floresta de meshes complexos pode multiplicar memória e trabalho sem necessidade.

## Como funciona
Use Instance on Points e mantenha a geometria instanciada enquanto transformações comuns e atributos no instance domain bastarem. Insira Realize Instances somente antes do nó que exige dados materializados. A realização propaga atributos do instance domain; se um atributo existir tanto na geometry base quanto na instância, o valor da base tem precedência.

## Exemplo
Distribua milhares de props como instâncias, ajuste rotação e escala por ponto, e só realize um subconjunto selecionado antes de deformar individualmente cada malha. A equipe verifica quais atributos de variação ficam no instance domain e quais sobrevivem à materialização.

## Limites e trade-offs
Realize Instances pode degradar muito o desempenho com numerosas instâncias de geometry complexa. Instâncias aninhadas têm profundidade configurável e volumes múltiplos recebem tratamento especial; não assuma cópia integral para todo componente.

## Como verificar
Compare tempo e memória antes e depois de realizar, confira quantidade de elementos e instâncias aninhadas, e inspecione atributos de mesmo nome em base e instância para confirmar precedência.

## Conexões
- [[blender-simulation-cache-bake-render]] — Blender Simulation Zone: gerenciar cache e bake para render.
- [[blender-viewer-domain-spreadsheet-debug]] — Blender Geometry Nodes: inspecionar fields com Viewer e domain explícito.

## Fontes
- [Blender 5.2 LTS — Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) — explica referências de geometry, atributos do instance domain e instancing aninhado Consulta: 2026-10-04.
- [Blender 5.2 LTS — Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) — documenta custo, propagação e precedência de atributos ao realizar Consulta: 2026-10-04.
