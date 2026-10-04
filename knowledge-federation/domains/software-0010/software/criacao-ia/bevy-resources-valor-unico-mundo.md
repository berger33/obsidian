---
id: software.criacao_ia.tranche04.000327
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/resources/", "https://docs.rs/bevy/latest/bevy/ecs/world/struct.World.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: resources são o valor-único do mundo, não mais um componente

## Em uma frase
Um Resource é uma instância única por tipo, armazenada no World e acessível via Res/ResMut — o lugar certo para estado global do app, não para dado repetido por entidade.

## Por que importa
Colocar contagem global de kills em 'componente de um player-fantasma' é um hack que surge do desconhecimento do mecanismo de resource. O quick-start de Resources define o modelo: valor único por programa, 'a value that is unique per program'; e o tipo da assinatura (Res<T> vs. ResMut<T>) diz ao executor quem pode escrever.

## Como funciona
Defina 'struct Score(u32);', registre com 'app.init_resource::<Score>()' (ou insert_resource com valor inicial) e acesse nos sistemas por parâmetro Res<Score> para ler, ResMut<Score> para escrever. O registro é obrigatório: um sistema pedindo Res<T> sem T no mundo é erro de runtime, não de tipo. O trade-off documentado na página de recursos: recursos têm acesso mais lento que componentes para uso em massa por entidade — componente por entidade, resource por app.

## Exemplo
Configuração de simulação (dt alvo, dificuldade) e contadores agregados rodam como resources; posição e saúde por entidade permanecem componentes. Um 'Res<Config>' em dez sistemas dá leitura paralela trivial, porque ninguém escreve.

## Limites e trade-offs
Res<T> com escrita esparsa ainda concorre: um ResMut em sistema lento serializa os leitores até o fim do sistema — o custo de um mutador de resource é maior que o de um mutador de componente raro. Resources não têm change-detection automática como a de componentes para todos os padrões; estado que precisa de eventos explícitos deve ser modeled como evento. O World guarda um resource por tipo — dois 'config' exigem dois tipos novos, não dois nomes.

## Como verificar
Um teste: App com init_resource, sistema que incrementa, asserção do valor pós-update. Remova o init_resource e confirme o panic claro (a falta é registrada como erro). Para o perfil: um ResMut escrito a cada frame com dez leitores; o time dos leitores deve mover quando o mutador passa a componente.

## Conexões
- [[bevy-commands-mundo-diferido]] — Bevy ECS: Commands é a fila de mutação estrutural adiada.
- [[bevy-componente-struct-derive]] — Bevy ECS: componente é struct Rust com derive — a decomposição é o design.

## Fontes
- [Bevy — Quick Start: Resources](https://bevy.org/learn/quick-start/getting-started/resources/) — página oficial que define resource como valor único por programa e a dupla Res/ResMut Consulta: 2026-10-04.
- [docs.rs — bevy::ecs::world::World](https://docs.rs/bevy/latest/bevy/ecs/world/struct.World.html) — o armazenamento onde componentes e resources vivem; documenta get_resource/get_resource_mut Consulta: 2026-10-04.
