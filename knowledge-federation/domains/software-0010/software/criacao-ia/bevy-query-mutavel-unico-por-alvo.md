---
id: software.criacao_ia.tranche04.000324
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

# Bevy ECS: uma query &mut é o ponto único de escrita de um tipo

## Em uma frase
Query<&mut T> pede acesso exclusivo aos componentes T do sistema; dentro do mesmo sistema, dois acessos mutáveis sobrepostos violam as regras de aliasing que a referência documenta.

## Por que importa
A segurança de dados do Bevy é compilada na assinatura: o compilador Rust impede duas &mut na mesma memória, e o runtime verifica a sobreposição entre queries de sistemas concorrentes. A regra 'um mutador por tipo' é o preço e a vantagem — você sabe, por assinatura, que ninguém mais está escrevendo ali enquanto o sistema roda.

## Como funciona
Para ler-e-escrever o mesmo componente no mesmo sistema, uma única query mutável cobre leitura e escrita (o iterador 'for mut name in &mut query' faz ambos). Para mover dados entre componentes A e B, a query dupla '&mut A, &B' é válida; '&mut A, &mut A' não é. O quick-start mostra o padrão de busca com break após a mutação — uma mutação, um dono, sem estado fantasma entre queries.

## Exemplo
O sistema de dano usa '(query_mut<&mut Health>, query<&EnemyTag>)': a escrita em Health fica num único canal de acesso; filtrar por EnemyTag na query mutável teria o mesmo efeito com um tipo a menos de empréstimo.

## Limites e trade-offs
Iterar '&mut query' ao mesmo tempo que se inspeciona o World por outro parâmetro pode esbarrar em regras de empréstimo que o compilador pega cedo demais — refatorar em dois sistemas resolve melhor que contornar. Query com Option<&mut T> não multiplica o direito de escrita; o empréstimo é do tipo. Acesso a um mesmo componente em dois schedules diferentes é serializado pelo executor, não unificado — um 'paralelo' aqui é uma ilusão.

## Como verificar
Duplique a query mutável num fixture e confirme o erro do borrow checker (é o contrato agindo). Rode o exemplo do quick-start e verifique que sem o 'mut' a atribuição não compila — a prova da direção do empréstimo. No profiler, um único &mut serializando 8 sistemas é um sinal de que a assinatura está dizendo algo útil sobre design.

## Conexões
- [[bevy-chain-ordenamento-minimo]] — Bevy ECS: use chain() onde a ordem importa, e só lá.
- [[bevy-query-filtros-refinam-superficie]] — Bevy ECS: com With/Without você estreita o alvo sem quebrar o contrato de acesso.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — define o padrão da query mutável (mut query, for mut name) e a iteração com break Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::system::Query](https://docs.rs/bevy/latest/bevy/ecs/system/struct.Query.html) — referência da API de Query, seus parâmetros e regras de empréstimo Consulta: 2026-10-04.
