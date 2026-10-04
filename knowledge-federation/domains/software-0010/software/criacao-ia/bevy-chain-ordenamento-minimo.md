---
id: software.criacao_ia.tranche04.000323
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/ecs/", "https://docs.rs/bevy/latest/bevy/app/struct.App.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: use chain() onde a ordem importa, e só lá

## Em uma frase
A ordem entre sistemas do mesmo schedule é definida pelos seus acessos; quando dois sistemas independentes em acesso precisam de sequência lógica, '.chain()' força a ordem listada.

## Por que importa
O exemplo canônico do quick-start diz exatamente isso: 'update_people' precisa rodar antes de 'greet_people' para que o nome alterado apareça no cumprimento — sem chain, a ordem é indefinida. Inverter a relação nos dados é mais barato e mais robusto, mas quando a dependência é de efeito (não de leitura/escrita de componente), a ordem explícita é a ferramenta honesta.

## Como funciona
Aplique .chain() no tuple de sistemas no add_systems — a sequência do tuple vira restrição de precedência. Use na menor granularidade que resolve: chain entre os dois sistemas que disputam, não entre os dez do módulo. A alternativa preferida quando possível é remodelar: um sistema que produz o componente que o outro consome já ordena via acessos; chain é para o resíduo de dependências invisíveis ao tipo.

## Exemplo
O pipeline de AI decide-algo e aplica-algo compartilham apenas um recurso de decisão: o par '(decidir, aplicar).chain()' elimina a corrida sem trocar o tipo do recurso.

## Limites e trade-offs
Chain demais recompõe a serialização que o modelo ECS evita por design: cada par acorrentado reduz o paralelismo do schedule. A restrição é intra-schedule — sistemas em schedules diferentes (Update vs. FixedUpdate) não se alinham com chain, exigem fix-first ou transições explícitas. Ordem não é contrato de persistência entre versões de API; prefira invariantes de dados sempre que possível.

## Como verificar
Rode o exemplo do quick-start com e sem chain e observe a diferença na saída. Adicione um teste que perturbe a ordem de registro e afirme o invariant (nome greetado = nome atualizado). Se o profiler mostrar 'sistemas em série' crescendo, conte as chains — é a métrica de dívida de ordenamento.

## Conexões
- [[bevy-paralelismo-por-acesso]] — Bevy ECS: o paralelismo vem dos acessos declarados, não de threads manuais.
- [[bevy-query-mutavel-unico-por-alvo]] — Bevy ECS: uma query &mut é o ponto único de escrita de um tipo.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — introduz .chain() com a motivação literal do caso update/greet Consulta: 2026-10-04.
- [docs.rs — bevy::app::App](https://docs.rs/bevy/latest/bevy/app/struct.App.html) — superfície do add_systems que recebe os tuples e a configuração de ordem Consulta: 2026-10-04.
