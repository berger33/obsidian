---
id: software.testes.tranche23.001733
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
fontes: ["https://hyperfoil.io/docs/overview/concepts/", "https://hyperfoil.io/docs/overview/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Controller, agents e o Vert.x eventbus por trás

## Em uma frase
O modelo de distribuição documentado: Hyperfoil usa um líder e seguidores (leader-follower) com o Vert.x Event Bus como middleware de clustering — o Controller é o servidor Vert.x com API REST que tem o papel de líder: ao iniciar um benchmark, ele faz deploy dos agents conforme a definição do benchmark, empurra a definição para eles e orquestra as fases; os agents executam o benchmark e mandam estatísticas periodicamente, permitindo ao controller combinar e avaliar tudo on the fly; quando o benchmark termina, todos os agents terminam.

## Por que importa
Essa arquitetura separa política de execução: é por isso que rodar num único VM é "quite easy" (o controller embutido no CLI do Quickstart 1) e o mesmo modelo serve a cluster — "all communication between the controller and agents happens over Vert.x eventbus - therefore it is independent on the deployment type".

## Como funciona
A granularidade do que o controller sabe é declarada com franqueza: ele gerencia o estado de cada fase em cada agent — a unidade mais fina que ele entende — e não tem informação sobre o estado de cada usuário individual.

## Exemplo
Rode start-local no CLI e confirme na saída o controller ouvindo em 127.0.0.1 com porta alta (41621 no exemplo da doc): é exatamente o servidor REST com eventbus, apenas no mesmo processo.

## Limites e trade-offs
A doc não abre detalhes de segurança do canal controller-agent (autenticação, TLS) na página de concepts — deployment em rede confiável é o cenário ilustrado; o Architecture e o Controller API nas seções de doc existem para quem precisa do protocolo real.

## Como verificar
Abra a subseção Controller and agents do Concepts e confirme os papéis, o fluxo de deploy, as estatísticas periódicas e as duas frases de granularidade e independência de deployment.

## Conexões
- [[hyperfoil-open-system]] — Veja também: Modelo aberto contra coordinated omission: cada VU é uma máquina de estado.
- [[hyperfoil-phases]] — Veja também: Fases: workloads independentes, quatro estados, escala gradual.

## Fontes
- [Hyperfoil — Concepts](https://hyperfoil.io/docs/overview/concepts/) — controller e agents, fases, sessões e cenário/sequências/steps; consultado em 2026-10-03.
- [Hyperfoil — Overview](https://hyperfoil.io/docs/overview/) — licença, distribuição, acurácia e versatilidade do DSL; consultado em 2026-10-03.
