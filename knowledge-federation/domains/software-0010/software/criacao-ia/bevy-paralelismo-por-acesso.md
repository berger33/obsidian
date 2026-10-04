---
id: software.criacao_ia.tranche04.000322
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
fontes: ["https://bevy.org/learn/quick-start/getting-started/ecs/", "https://docs.rs/bevy_ecs/latest/bevy_ecs/schedule/struct.Schedule.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Bevy ECS: o paralelismo vem dos acessos declarados, não de threads manuais

## Em uma frase
Sistemas em Bevy rodam em paralelo sempre que seus acessos a componentes não conflitam — a unidade de concorrência é a assinatura de Query, não a gerência de threadpool.

## Por que importa
Um jogo com 30 sistemas onde cada um declara o que lê e escreve escala quase sozinho em múltiplos núcleos; um sistema que grava println desordenado na saída é a prova do modelo: o próprio quick-start avisa que a ordem dos prints pode variar porque os sistemas correm concorrentes. Trocar isso por mutex manuais anula o ganho.

## Como funciona
O agendador constrói um grafo de conflitos por sistema: dois sistemas que podem escrever o mesmo tipo de componente são serializados; leituras puras coexistem com leituras; escrita conflita com tudo no mesmo tipo. Não há anotação de thread para pedir — o tipo do parâmetro (Query<&T> vs. Query<&mut T>) é a política de concorrência. Para ordenar quando a concorrência natural não basta, usa-se chain ou sets, explicitamente.

## Exemplo
Os sistemas 'animar sprites' (lê Transform, escreve Sprite) e 'aplicar gravidade' (escreve Velocity) rodam em paralelo porque não se tocam; ao introduzir 'aterrissagem' que lê Sprite e escreve Velocity, o plano do frame muda sozinho — sem código novo de sincronização.

## Limites e trade-offs
Paralelo por acesso não ordena efeitos colaterais visíveis (prints, IO de arquivos, rand global): dois sistemas independentes podem produzir saída intercalada. Um único &mut em hot path serializa os vizinhos — a métrica certa é 'quantos sistemas ficam bloqueados por este tipo'. O modelo vale para o mundo ECS; comandos de render e áudio têm seus próprios agendadores.

## Como verificar
Compare o tempo de frame de um sistema pesado duplicado (leitura pura de &T) — se fosse lock manual, não escalaria. Insira uma escrita em &mut no mesmo tipo e observe a serialização no profiler de schedule. Testes de ordem: rode com 'available_parallelism' variável e confirme que o resultado da simulação independe da ordem dos sistemas independentes.

## Conexões
- [[bevy-startup-update-duas-momentos]] — Bevy ECS: Startup roda uma vez antes de tudo; Update é o loop.
- [[bevy-chain-ordenamento-minimo]] — Bevy ECS: use chain() onde a ordem importa, e só lá.

## Fontes
- [Bevy — Quick Start: ECS](https://bevy.org/learn/quick-start/getting-started/ecs/) — afirma que sistemas rodam em paralelo por padrão sempre que possível e ilustra com a ordem variável dos prints Consulta: 2026-10-04.
- [docs.rs — bevy_ecs::schedule::Schedule](https://docs.rs/bevy_ecs/latest/bevy_ecs/schedule/struct.Schedule.html) — referência da estrutura que materializa ordem e paralelismo dos sistemas Consulta: 2026-10-04.
