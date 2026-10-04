---
id: software.criacao_ia.tranche03.000242
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: capturar fields antes de uma conversão de geometria

## Em uma frase
Capture Attribute avalia fields na geometria de entrada e armazena seus valores num atributo anônimo acessível na geometria de saída do próprio nó.

## Por que importa
Conversões entre curvas, malhas, pontos e instâncias podem remover o contexto necessário para recomputar um field. Capturar previamente um parâmetro de spline ou outra propriedade preserva um dado útil para nós posteriores e evita reavaliar num domínio que já não existe.

## Como funciona
Ligue geometry à entrada e escolha explicitamente domain e tipos dos Capture Items. O field é avaliado para elementos selecionados; elementos não selecionados recebem valor padrão do tipo. O atributo novo só existe na geometria de saída do nó e não pode ser lido por nós upstream ou geometry sibling; nós downstream acessam o output do mesmo Capture Attribute.

## Exemplo
Para cortar segmentos regulares numa curva convertida em tubo, capture o parâmetro da spline nos pontos de controle antes de Curve to Mesh. A conversão transfere o atributo para vértices do tubo, onde filtros posteriores conseguem usar a distância original para remover partes.

## Limites e trade-offs
O resultado depende de domain, seleção e regras de interpolação dos nós seguintes. Capture Attribute armazena temporariamente, não cria necessariamente um atributo nomeado persistente para materiais ou outros sistemas.

## Como verificar
Visualize antes e depois da conversão com Viewer e Spreadsheet, alterne Selection e confirme valores default em elementos não capturados. Tente conectar a um nó irmão para verificar o limite de escopo.

## Conexões
- [[blender-geometry-nodes-field-contexto-avaliacao]] — Blender Geometry Nodes: fields são avaliados no contexto do consumidor.
- [[blender-anonymous-versus-named-attributes]] — Blender Geometry Nodes: escolher atributo anônimo ou nomeado.

## Fontes
- [Blender 5.2 LTS — Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) — define domínio, seleção, escopo do atributo e exemplo de conversão curve-to-mesh Consulta: 2026-10-04.
- [Blender 5.2 LTS — Fields](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html) — explica avaliação contextual e mudança de resultados após transformações Consulta: 2026-10-04.
