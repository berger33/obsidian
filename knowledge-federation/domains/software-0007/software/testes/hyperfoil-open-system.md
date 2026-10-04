---
id: software.testes.tranche23.001732
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
fontes: ["https://hyperfoil.io/docs/overview/", "https://hyperfoil.io/", "https://hyperfoil.io/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Modelo aberto contra coordinated omission: cada VU é uma máquina de estado

## Em uma frase
O Overview é pedagógico sobre o problema: benchmarks medem o que acontece com milhares de usuários concorrentes cada um fazendo loads espaçados, mas drivers tradicionais simplificam para dezenas de VUs executando um request após outro ou com atrasos mínimos — o Closed System Model — o que produz latências enviesadas e deixa de disparar condições patológicas (queues estourando), problema conhecido como coordinated omission (com o slide How Not to Measure Latency linkado em dois lugares do site).

## Por que importa
Escolher Hyperfoil por acurácia é escolher o Open System Model: "virtual users are completely independent until it runs out of resources", e o estouro de recurso é gravado como resultado, não escondido pelo pacing do driver.

## Como funciona
A implementação descrita: um state-machine por VU, todas as requisições executadas assincronamente — a casa da baixa alocação (destaque low-allocation da página inicial) é o preço de manter milhares de máquinas de estado sem o GC virar fonte de ruído.

## Exemplo
Reproduza o argumento: rode o mesmo alvo com um driver de closed model clássico e com o Hyperfoil sob saturação; a latência p99 do primeiro melhora artificialmente porque os usuários lentos param de emitir requests — o viés documentado na seção Accuracy.

## Limites e trade-offs
O documento do Overview descreve o modelo e cita o problema com link para o slide de Gil Tene; não fornece um estudo comparativo próprio com números — a vantagem quantitativa do open model depende do alvo, da carga e do que o seu driver de comparação faz com o backpressure.

## Como verificar
Abra a seção Accuracy do Overview e a bullet accurate da página inicial; confirme a frase do state-machine por VU e os dois links coordinated omission.

## Conexões
- [[hyperfoil-apache-license]] — Veja também: Software livre para benchmarks auditáveis, Apache 2.0.
- [[hyperfoil-leader-follower]] — Veja também: Controller, agents e o Vert.x eventbus por trás.

## Fontes
- [Hyperfoil — Overview](https://hyperfoil.io/docs/overview/) — licença, distribuição, acurácia e versatilidade do DSL; consultado em 2026-10-03.
- [Hyperfoil — página inicial oficial](https://hyperfoil.io/) — definição e destaques distributed, accurate, versatile, low-allocation; consultado em 2026-10-03.
- [Hyperfoil — índice da documentação](https://hyperfoil.io/docs/) — nove seções: overview, quickstarts, user guide, API REST, extensions; consultado em 2026-10-03.
