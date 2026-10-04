---
id: software.criacao_ia.tranche04.000328
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/ecs/", "https://docs.rs/bevy/latest/bevy/ecs/component/trait.Component.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: componente é struct Rust com derive — a decomposição é o design

## Em uma frase
Componentes são tipos dados comuns anotados com #[derive(Component)]; o ganho do ECS vem de quebrá-los em peças pequenas que se recombinam entre entidades.

## Por que importa
O quick-start argumenta o motivo com um caso concreto: nomear 'Person' e 'Name' separados porque 'dogs should probably also have a name' — a decomposição permite que entidades diferentes compartilhem componentes sem herança, e o padrão 'forces you to break up your app data and logic into its core components'. Um componente monolito por entidade joga fora exatamente isso.

## Como funciona
Cada struct que representa um aspecto (Position, Velocity, Name) recebe 'Component'; entidades são chaves com uma coleção delas; queries pegam o produto cartesiano que interessa. As regras de registro são triviais (derive + spawn com tuple); o design é a pergunta: este campo muda de vida própria? Se sim, componente separado. Componentes-vazio para marcação funcionam (o marcador 'Person' do exemplo não tem campos) e são baratos em iteração quando combinados com &mut.

## Exemplo
O inimigo '(Position, Velocity, Hostile, Name)' e o NPC '(Position, Name)' compartilham Position e Name sem classe base; adicionar um terceiro aspecto não toca os sistemas existentes — só os queries que o pedem.

## Limites e trade-offs
Decompor até o átomo aumenta o custo de join em queries amplas — componentes que vivem e morrem juntos podem ser um só struct. Derivar Component é o contrato de tipo, não de persistência: salvar/carregar mundos exige reflexão/serialização além do derive. 'struct Entity(u64)' do quick-start lembra que a entidade é só um índice — lógica em cima de identidade exige cuidado com reciclo de slot.

## Como verificar
Um teste de regressão de design: adicione um tipo de entidade novo reusando componentes existentes sem modificar nenhum sistema — se precisa modificar, a decomposição falhou. Compare o iterado em query '&mut (A, B, C)' antes e depois de juntar A+B num só struct para medir o custo real de joins.

## Conexões
- [[bevy-resources-valor-unico-mundo]] — Bevy ECS: resources são o valor-único do mundo, não mais um componente.
- [[bevy-plugins-unidade-distribuicao]] — Bevy ECS: Plugin é a unidade de empacotamento, não de lógica.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — justifica a divisão de Person/Name e o papel do derive Component com exemplos diretos Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::component::Component](https://docs.rs/bevy/latest/bevy/ecs/component/trait.Component.html) — define o trait que transforma um tipo em componente Consulta: 2026-10-04.
