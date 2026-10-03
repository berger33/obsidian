---
id: software.testes.tranche23.001736
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

# Cenário = sequências = steps: a gramática do teste de carga

## Em uma frase
O Concepts fecha a hierarquia do benchmark com analogia de programação: o cenário consiste de uma ou mais sequências compostas de steps — "steps are similar to statements in programming language and sequences are an equivalent of blocks of code" — e, como um navegador real executa parte das operações em paralelo (imagens carregando concorrentes num page load), a sessão contém a qualquer momento uma ou mais sequence instances ativas, encerrando quando todas terminam para reciclar o usuário.

## Por que importa
A modelagem por instâncias de sequência é o que permite o branching realista: a doc exemplifica que, após avaliar uma condição, a sessão pode criar a instância de uma sequência segundo a lógica do ramo — o closed model de um script linear não tem como expressar isso.

## Como funciona
A Quickstart 1 mostra a materialização em YAML: scenario contém a sequência test, que contém um httpRequest com GET / e o helper sync: true mantendo a sequência bloqueada até o processamento da resposta — o comentário do arquivo oficial explica que o sync torna o request síncrono por decisão, não default.

## Exemplo
Escreva um cenário com duas sequências e uma condição que ramifica entre elas (a analogia if-block da doc); acompanhe no stats que o total de completions reflete só o ramo escolhido — prova de que as instâncias contam separadamente.

## Limites e trade-offs
O modelo de concorrência dentro da sessão (quantas sequence instances simultâneas por página simulada) tem limites práticos definidos pelo pool de sessions da nota própria; a doc de concepts descreve a semântica, os detalhes de API para custom steps vão ao quickstart 8 e à seção Extensions.

## Como verificar
Abra a subseção Scenario do Concepts e o bloco YAML anotado do Quickstart 1; confirme a analogia statements/blocks e o papel do helper sync.

## Conexões
- [[hyperfoil-sessions-prealloc]] — Veja também: Sessões pré-alocadas: o custo de não alocar no caminho quente.
- [[hyperfoil-first-run]] — Veja também: Do zero ao primeiro run: download, start-local, upload, run, stats.

## Fontes
- [Hyperfoil — Concepts](https://hyperfoil.io/docs/overview/concepts/) — controller e agents, fases, sessões e cenário/sequências/steps; consultado em 2026-10-03.
- [Hyperfoil — Quickstart 1: First benchmark](https://hyperfoil.io/docs/getting-started/quickstart1/) — download, start-local, upload, run e stats; consultado em 2026-10-03.
