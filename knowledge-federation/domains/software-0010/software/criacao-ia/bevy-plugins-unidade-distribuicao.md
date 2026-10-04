---
id: software.criacao_ia.tranche04.000329
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/plugins/", "https://docs.rs/bevy/latest/bevy/app/struct.App.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: Plugin é a unidade de empacotamento, não de lógica

## Em uma frase
Um Plugin agrupa a instalação coesa de um sistema — seus recursos, schedules e handlers — e 'add_plugins' compõe o app; DefaultPlugins é o próprio pacote de engine.

## Por que importa
Bevy deliberadamente não tem herança de engine: o app cresce por composição. Sem a unidade Plugin, cada integração vira dez linhas espalhadas no main, impossíveis de reusar entre jogos ou desligar. O quick-start de Plugins trata isso como estrutura primária de organização, não estilo.

## Como funciona
Implemente 'impl Plugin for MeuPlugin { fn build(&self, app: &mut App) { ... } }' e registre com 'add_plugins((ModoA, ModoB))' em tupla. O build recebe o app mutável: inicialize recursos, registre tipos de asset, adicione sistemas nos schedules. Configurações viram campos do plugin struct (o padrão de 'MyPlugin { resolution }'), o que permite dois jogos lendo o mesmo crate com presets diferentes. Subconjuntos mínimos para código sem render (servidor dedicado, testes, headless CI) é o benefício documentado do modelo.

## Exemplo
O plugin de lobby expõe 'LobbyPlugin { max_slots: 8 }'; o mesmo crate roda no jogo completo com DefaultPlugins e num headless de teste com 'MinimalPlugins + LobbyPlugin', sem mudar o plugin.

## Limites e trade-offs
Ordem de add_plugins importa quando plugins escrevem no mesmo estado de app; 'build' roda na ordem dada — dependências implícitas entre plugins são a fragilidade que o padrão não resolve por si. Plugin não é sandbox: pode tocar qualquer parte do app, e o compiler não avisa sobre dois plugins competindo pelo mesmo resource. O ganho de composição em crates separados pressupõe versionar as interfaces de tipo (componentes compartilhados viram API pública).

## Como verificar
Teste unitário: App::new().add_plugins(MinimalPlugins).add_plugins(LobbyPlugin::default()).update() e assert no estado — a granularidade de plugin deve ser testável sem janela. Verifique que desligar o plugin da UI não quebra a simulação: se quebra, a coesão vazou. Rode o headless de CI com o mesmo plugin do cliente: é o cenário de origem da regra.

## Conexões
- [[bevy-componente-struct-derive]] — Bevy ECS: componente é struct Rust com derive — a decomposição é o design.
- [[bevy-app-schedule-world-camadas]] — Bevy ECS: App planeja, Schedule decide quando, World guarda o estado.

## Fontes
- [Bevy — Quick Start: Plugins](https://bevy.org/learn/quick-start/getting-started/plugins/) — página oficial que define a função de plugin e o padrão de composição Consulta: 2026-10-04.
- [docs.rs — bevy::app::App](https://docs.rs/bevy/latest/bevy/app/struct.App.html) — a superfície de add_plugins/DefaultPlugins na API Consulta: 2026-10-04.
