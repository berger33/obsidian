---
id: software.criacao_ia.tranche04.000325
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/ecs/", "https://docs.rs/bevy/latest/bevy/ecs/system/struct.Query.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: com With/Without você estreita o alvo sem quebrar o contrato de acesso

## Em uma frase
Filtros de query (With, Without, Or) refinam quais entidades a iteração toca, sem alterar o que é lido — e o agendador continua enxergando os tipos reais.

## Por que importa
Iterar tudo e filtrar no corpo com if continua correto em resultado, mas paga o custo por cada entidade e não comunica intenção. Um filtro na assinatura documenta o recorte ('só Name de Person') e reduz iteração; o quick-start usa exatamente Query<&Name, With<Person>> para expressar 'todo Name cujo dono é Person'.

## Como funciona
O segundo parâmetro genérico de Query é o filtro: With<Marker> exige a presença, Without<Marker> a ausência, Or<(A, B)> a disjunção. Combine com os tipos lidos para manter o mínimo de superfície. Filtros não pedem permissão de escrita sobre o tipo filtrado — ler a presença de Marker via filtro não é ler seu valor; por isso With<Marker> funciona com marcador vazio sem custo de acesso. Para negação composta, Or com Without é o padrão documentado na referência.

## Exemplo
Dois sistemas sobre 'Sprite': um atualiza 'Sprite, With<Enemy>' e outro 'Sprite, With<Player>' não se serializam entre si, pois os conjuntos são disjuntos — o filtro vira informação de concorrência, não só economia.

## Limites e trade-offs
Filtros não são índices de arcabouço: o custo de teste por entidade existe e With em tipo raro pode iterar mais do que parece; a estrutura de índices é detalhe de versão. Or amplia o conjunto de leitura e, por isso, pode alargar o conflito no grafo de agendamento: filtrar é também uma declaração de alcance.

## Como verificar
Compare a contagem de iterações (um contador local no sistema) entre filtro na query e if no corpo com 100 mil entidades. Rode o par de sistemas do exemplo e confirme que ganham paralelismo quando os filtros ficam disjuntos. Mude Or para a conjunção e observe a mudança no profile — é a semântica de alcance funcionando.

## Conexões
- [[bevy-query-mutavel-unico-por-alvo]] — Bevy ECS: uma query &mut é o ponto único de escrita de um tipo.
- [[bevy-commands-mundo-diferido]] — Bevy ECS: Commands é a fila de mutação estrutural adiada.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — introduz Query<&Name, With<Person>> com a leitura literal da semântica Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::system::Query](https://docs.rs/bevy/latest/bevy/ecs/system/struct.Query.html) — documenta os tipos de filtro (With, Without, Or) e combinações Consulta: 2026-10-04.
