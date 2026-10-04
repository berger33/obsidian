---
id: software.criacao_ia.tranche03.000241
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: fields são avaliados no contexto do consumidor

## Em uma frase
Um field é uma função avaliada pelo nó de fluxo de dados consumidor, então a mesma árvore de field pode produzir valores diferentes em consumidores diferentes.

## Por que importa
Conexões de field parecem dados armazenados, mas muitas representam instruções que serão executadas mais tarde em cada elemento. Se a geometria mudar entre dois consumidores, campos como Position e Index podem ser reavaliados sobre nova topologia ou posição e não preservar o valor original.

## Como funciona
Identifique sockets de field e os nós de fluxo de dados que os consomem. Field nodes obtêm contexto de componente e domínio a partir da geometria do consumidor. Para manter um valor original após mudar geometry, avalie-o antes da transformação e capture o resultado como atributo anônimo; caso precise de um valor único, use Sample Index ou Attribute Statistic em vez de supor que field converte automaticamente em escalar.

## Exemplo
Uma graph armazena a posição inicial de cada ponto antes de deslocar a geometria. Se o mesmo nó Position alimentar outro Set Position depois da mudança, ele poderá ler a nova localização; capturar o valor inicial cria atributo que pode orientar a operação posterior.

## Limites e trade-offs
A avaliação concreta depende do componente e domain usados no consumidor. Não assuma avaliação eager só porque o field está conectado, nem que uma conexão visualmente igual tenha valor estático em toda a árvore.

## Como verificar
Conecte a mesma rede de Position a consumidores antes e depois de Set Position, compare resultados no Viewer e Capture Attribute e confira o domain selecionado em cada nó consumidor.

## Conexões
- [[blender-capture-attribute-antes-de-conversao]] — Blender: capturar fields antes de uma conversão de geometria.

## Fontes
- [Blender 5.2 LTS — Fields](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html) — define fields como funções e explica contexto de avaliação por data-flow node Consulta: 2026-10-04.
- [Blender 5.2 LTS — Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) — mostra como fixar resultado de um field em atributo anônimo na geometria Consulta: 2026-10-04.
