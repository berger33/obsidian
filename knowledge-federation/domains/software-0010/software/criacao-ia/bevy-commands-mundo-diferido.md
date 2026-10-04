---
id: software.criacao_ia.tranche04.000326
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/ecs/", "https://docs.rs/bevy/latest/bevy/ecs/system/struct.Commands.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: Commands é a fila de mutação estrutural adiada

## Em uma frase
Sistemas que precisam spawnar, inserir ou remover entidades e componentes mutam o mundo via Commands, que enfileira operações aplicadas quando o executor está num ponto seguro.

## Por que importa
Uma mutação estrutural no meio da iteração invalidaria a query que está rodando — em qualquer ECS. Bevy resolve por contrato de tipo: quem precisa criar entidades pede 'mut commands: Commands' e não toca no World diretamente. O adiamento é o que mantém as queries sem travas e o paralelismo honesto.

## Como funciona
Dentro do sistema, 'commands.spawn((A, B))', 'commands.entity(e).insert(C)', 'commands.entity(e).despawn()' e variantes retornam handles com 'get()' para encadear operações na mesma fila. O executor drena as filas em pontos definidos entre sistemas/frames. Consequência prática: a entidade referenciada pelo Entity retornado só passa a existir no mundo após o drain — ler imediatamente no mesmo sistema não encontra.

## Exemplo
O disparo de projétil: 'let bullet = commands.spawn((Pos, Vel)).id();' na bala, e 'commands.entity(shooter).insert(Recoil);' — as duas entidades novas só são visíveis no próximo ponto de aplicação, e o sistema de colisão as vê no frame seguinte.

## Limites e trade-offs
Comandos adiados não veem efeito uns dos outros no mesmo sistema: encadear spawn e depois 'query' o resultado falha; precisa de dois sistemas com um ponto de drenagem entre eles. Para mutações fora do fluxo normal (setup manual, testes, I/O pesado), existe acesso direto via 'world'/'World' e 'world_mut()' — as regras de segurança de sistema não valem ali, e a responsabilidade é sua. O padrão de fila é o que torna a API de spawn um custo de alocação por frame em massa — perfis que importam usam spawn_batch.

## Como verificar
Escreva um teste que faz spawn via Commands e update o App; confirme que só após update o query retorna a entidade. Compare tempo de frame com N=50k spawns via spawn vs. spawn_batch — a API alternativa existe porque o custo real. Rode o sistema com o drain manual para entender o ponto de aplicação.

## Conexões
- [[bevy-query-filtros-refinam-superficie]] — Bevy ECS: com With/Without você estreita o alvo sem quebrar o contrato de acesso.
- [[bevy-resources-valor-unico-mundo]] — Bevy ECS: resources são o valor-único do mundo, não mais um componente.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — usa Commands como o meio canônico de popular o World nos exemplos Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::system::Commands](https://docs.rs/bevy/latest/bevy/ecs/system/struct.Commands.html) — define a fila de operações de mundo e a aplicação adiada Consulta: 2026-10-04.
