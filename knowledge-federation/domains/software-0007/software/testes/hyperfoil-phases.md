---
id: software.testes.tranche23.001734
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://hyperfoil.io/docs/overview/concepts/", "https://hyperfoil.io/docs/getting-started/quickstart1/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fases: workloads independentes, quatro estados, escala gradual

## Em uma frase
O Concepts documenta que um benchmark consiste de várias fases; fases podem rodar independentemente uma da outra simulando cargas de grupos de usuários diferentes (o exemplo: visitors versus admins) e, dentro de uma fase, todos os usuários executam o mesmo cenário (exemplo: logar, vender todo o estoque, sair); fases também são o instrumento de escala — buscar throughput máximo significa agendar várias iterações da mesma fase aumentando gradualmente o número de usuários.

## Por que importa
Enumerar os estados da fase é o que torna o plano do teste auditável: not running (scheduled), running, finished e terminated — finished significa que novos cenários não começam, mas os usuários já iniciados completam; terminated fecha tudo com todas as estatísticas coletadas e nenhuma requisição futura.

## Como funciona
A doc também fixa quem manda: o estado da fase em cada agent é gerido pelo Controller, e a fase é a unidade de trabalho mais fina que ele compreende — o resto (por usuário) é invisível por design.

## Exemplo
Declare duas fases com atOnce distintos (1 e 10 usuários) no seu YAML e acompanhe pelo comando run a tabela de status por fase, observando a transição dos quatro estados no output.

## Limites e trade-offs
O Concepts lista os estados e a semântica de controle; a sintaxe completa de agendamento (ramp, spike, for duration) mora na seção de phases do User Guide — que a própria doc remete aos quickstarts 4 e 5 — e o modelo por sessão não é o único formato de fase descrito lá.

## Como verificar
Abra a subseção Phases do Concepts oficial e confirme o exemplo visitors/admins, os quatro estados com suas frases e a frase da granularidade do controller.

## Conexões
- [[hyperfoil-leader-follower]] — Veja também: Controller, agents e o Vert.x eventbus por trás.
- [[hyperfoil-sessions-prealloc]] — Veja também: Sessões pré-alocadas: o custo de não alocar no caminho quente.

## Fontes
- [Hyperfoil — Concepts](https://hyperfoil.io/docs/overview/concepts/) — controller e agents, fases, sessões e cenário/sequências/steps; consultado em 2026-10-03.
- [Hyperfoil — Quickstart 1: First benchmark](https://hyperfoil.io/docs/getting-started/quickstart1/) — download, start-local, upload, run e stats; consultado em 2026-10-03.
