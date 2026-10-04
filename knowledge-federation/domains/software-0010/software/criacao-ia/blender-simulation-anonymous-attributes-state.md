---
id: software.criacao_ia.tranche03.000247
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Simulation Zone: declarar atributos anônimos no estado

## Em uma frase
Atributos anônimos não são propagados automaticamente pelos nós de Simulation; precisam ser explicitamente guardados no estado da simulação.

## Por que importa
Um atributo anônimo pode continuar acessível em links comuns de geometry nodes, mas a fronteira temporal não consegue inferir quais campos serão necessários em frames futuros. Uma graph que parece correta numa etapa pode perder silenciosamente um dado ao entrar ou sair da simulação.

## Como funciona
Inclua os valores que precisam atravessar frames entre os Simulation State items e direcione atributos para uma forma explicitamente armazenada. Lembre que o resultado só é acessado pelo Simulation Output e que dados iniciais conectados ao Simulation Input são avaliados uma vez no começo; valores externos aos nós da zona podem ser reavaliados por frame.

## Exemplo
Uma simulação de objetos em desgaste guarda o atributo anônimo `wear_amount` junto da geometria entre frames antes de usar o valor para deslocar vértices. Sem esse item de estado, a graph reaparece com valores ausentes apesar de link anônimo continuar desenhado no editor.

## Limites e trade-offs
A disponibilidade e compatibilidade dos itens de estado dependem de tipo, geometry e cache. Attribute anônimo não é substituto para uma interface nomeada externa, e o Simulation Zone não está disponível no Tool context.

## Como verificar
Inspecione valor no input, dentro da zona e no output em vários frames; limpe e reconstrua cache após alterar estado. Teste atributo nomeado e anônimo separadamente em geometry inicial e criada durante a simulação.

## Conexões
- [[blender-repeat-versus-simulation-zone]] — Blender Geometry Nodes: escolher Repeat ou Simulation Zone.
- [[blender-simulation-cache-bake-render]] — Blender Simulation Zone: gerenciar cache e bake para render.

## Fontes
- [Blender 5.2 LTS — Simulation Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html) — declara explicitamente que anonymous attributes não são propagados sem estado Consulta: 2026-10-04.
- [Blender 5.2 LTS — Attributes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html) — explica escopo e continuidade de atributos anônimos em geometry nodes Consulta: 2026-10-04.
