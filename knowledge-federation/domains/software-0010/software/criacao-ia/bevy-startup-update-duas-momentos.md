---
id: software.criacao_ia.tranche04.000321
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

# Bevy ECS: Startup roda uma vez antes de tudo; Update é o loop

## Em uma frase
O app executa sistemas em schedules — Startup corre exatamente uma vez na inicialização, Update corre todo frame — e registrar o sistema no schedule errado muda o comportamento sem mudar uma linha de lógica.

## Por que importa
Inserir entidades com um sistema de setup no Update os recria a cada frame; fazer lógica de frame no Startup congela a simulação no primeiro tick. Como a distinção é só um argumento de 'add_systems', o erro típico de Bevy não é de sintaxe, é de momento — e a documentação canônica define o papel de cada schedule.

## Como funciona
Sistemas são funções Rust comuns; 'App::add_systems(schedule, sistema)' escolhe quando rodam. O quick-start define os Startup systems como exatamente-uma-vez, na largada, antes dos demais — o exemplo 'add_people' cria as entidades ali. Update é o schedule padrão do jogo. A partir daqui, schedules extras (FixedUpdate para física, RunFixedMainLoop e afins) seguem a mesma lógica: a pergunta de revisão é sempre 'este código pertence a qual momento do app?'.

## Exemplo
Um gerador de mundo coloca spawn de cenário em OnEnter/Startup, o consumo de input em Update e a simulação determinística em FixedUpdate — os três acessando os mesmos componentes, cada um no seu relógio.

## Limites e trade-offs
Startup corre uma vez — se o mundo pode ser reiniciado (novo mapa, respawn), o sistema precisa ser idempotente ou viver num schedule de transição, não no Startup. A ordem 'Startup antes de Update' vale para a largada; entre sistemas do mesmo schedule a ordem não é garantida sem configuração explícita. Schedules customizados têm suas próprias condições de disparo.

## Como verificar
Coloque um println com contagem em cada schedule e confirme: Startup exatamente 1, Update igual ao número de frames, FixedUpdate em ritmo próprio. Mude um spawn de Update para Startup e observe que ele deixa de repetir — o teste visual da regra. Para projetos, teste de integração com App::default().update() duas vezes cobre o contrato.

## Conexões
- [[bevy-paralelismo-por-acesso]] — Bevy ECS: o paralelismo vem dos acessos declarados, não de threads manuais.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — define Startup (exatamente uma vez, antes dos demais) e a função de add_systems Consulta: 2026-10-04.
- [docs.rs — bevy::app::App](https://docs.rs/bevy/latest/bevy/app/struct.App.html) — referência da API de registro de schedules e plugins Consulta: 2026-10-04.
