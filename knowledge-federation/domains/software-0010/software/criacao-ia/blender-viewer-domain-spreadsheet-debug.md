---
id: software.criacao_ia.tranche03.000250
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: inspecionar fields com Viewer e domain explícito

## Em uma frase
Viewer visualiza dados intermediários em geometry nodes, enquanto seu domain determina como um field é avaliado e quais colunas aparecem na Spreadsheet.

## Por que importa
Um valor pode parecer incorreto porque foi calculado num domain diferente do esperado, e olhar apenas o objeto final não mostra onde a mudança aconteceu. Viewer e Spreadsheet permitem verificar geometria intermediária e valores por elemento, desde que a graph tenha sido avaliada.

## Como funciona
Conecte Geometry primeiro e depois o field ao Viewer para visualização direta. Deixe Auto quando a inferência de domain funcionar ou selecione explicitamente Face Corner/Point quando não funcionar. A Spreadsheet mostra atributos do domain selecionado; Viewer funciona no contexto Modifier, não Tool. Socket inspection em geral reflete a última avaliação e requer que o node esteja ligado ao Group Output.

## Exemplo
Ao avaliar noise numa malha, conecte geometry e campo ao Viewer, selecione o domain de vertices e compare o gradiente no viewport com a coluna numérica no Spreadsheet. Pinar o Viewer mantém dados visíveis ao alternar seleção de objeto.

## Limites e trade-offs
Viewer não tem outputs e não altera a geometria final. Valores podem estar desatualizados se a graph não foi reavaliada; Viewer não é mecanismo de render final ou persistência de dados.

## Como verificar
Altere deliberadamente o domain, atualize a avaliação e compare coluna, viewport e output do Group. Confirme ordem dos sockets, contexto Modifier e que node de interesse está no caminho avaliado.

## Conexões
- [[blender-instancing-realize-atributos-custo]] — Blender Geometry Nodes: manter instâncias até precisar realizá-las.

## Fontes
- [Blender 5.2 LTS — Viewer Node](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) — define visualização, seleção automática/manual de domain e comportamento de Spreadsheet Consulta: 2026-10-04.
- [Blender 5.2 LTS — Inspection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html) — explica valores da última avaliação e exigência de conexão ao Group Output Consulta: 2026-10-04.
