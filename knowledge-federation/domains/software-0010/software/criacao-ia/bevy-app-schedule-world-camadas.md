---
id: software.criacao_ia.tranche04.000330
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/", "https://docs.rs/bevy/latest/bevy/ecs/world/struct.World.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: App planeja, Schedule decide quando, World guarda o estado

## Em uma frase
A arquitetura do runtime é em três camadas — App agrega plugins e schedules, Schedule ordena sistemas num instante, World armazena entidades e resources — e entender a costura evita decisões de API no lugar errado.

## Por que importa
Dúvidas de projeto de engine ('onde marco ordem? onde salvo o estado?') são respostas de camada, não de sintaxe. Registrar sistema é App, definir precedência é Schedule, iterar e mutar dados é World — o quick-start mostra as três em uso desde o primeiro exemplo, com add_systems, schedules e comandos de World separados.

## Como funciona
'App::new().add_plugins(...).add_systems(Update, ...).run()' é a fachada: cada schedule (Update, Startup, FixedUpdate) tem seu grafo de sistemas. O World é o agregado de dados (tabelas por archetype, resources) que os sistemas recebem mutado; fora do agendamento, 'world.rs()' e acesso direto ao World existem para setup e teste, mas ignoram as convenções de paralelismo que os sistemas ganham de graça. A pergunta de revisão certa para cada adição: é configuração (App), é tempo (Schedule) ou é dado (World)?

## Exemplo
Carregar um save vira World-mutation no build do plugin de save; a reordenação dos sistemas pós-load é Schedule; o registro do sistema de autosave é App — três camadas, cada uma com seu tipo de mudança e seu lugar natural na revisão.

## Limites e trade-offs
Schedules têm políticas próprias (condições de execução, fix-rate) que não são globais ao app; confundir FixedUpdate com Update é o erro de camada com maior custo silencioso. Mutação direta do World em testes pode passar onde um sistema seria bloqueado — o 'teste verde' não implica 'sistema seguro'. A superfície do App muda entre releases do Bevy mais que as outras camadas; plugins que guardam referências a ele devem ser pequenos.

## Como verificar
Num fixture, faça a mesma operação pelas três portas (app, schedule, world direto) e compare o que compila/empana — o contraste ensina as fronteiras. Um teste que usa 'App::world_mut' na inicialização e depois roda update documenta onde a exceção de segurança é legítima. A revisão de código deveria ser capaz de classificar cada PR por camada; se não consegue, a arquitetura está vazando.

## Conexões
- [[bevy-plugins-unidade-distribuicao]] — Bevy ECS: Plugin é a unidade de empacotamento, não de lógica.

## Fontes
- [Bevy — Quick Start: Getting Started](https://bevy.org/learn/quick-start/getting-started/) — sequência oficial App → schedules → World que as notas de arquitetura seguem Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::world::World](https://docs.rs/bevy/latest/bevy/ecs/world/struct.World.html) — referência da camada de estado e do acesso direto fora de sistema Consulta: 2026-10-04.
