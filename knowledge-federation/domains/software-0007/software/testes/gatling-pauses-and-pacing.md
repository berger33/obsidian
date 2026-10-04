---
id: software.testes.tranche17.001062
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.gatling.io/reference/script/core/scenario/", "https://docs.gatling.io/concepts/scenario/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: representar o tempo de pensamento

## Em uma frase
As pausas inserem intervalos entre ações, e a função de ritmo ajusta a espera para manter uma frequência estável de transações por usuário.

## Por que importa
Sem pausas o teste simula usuários impacientes, e com pausas fixas cria um padrão sincronizado que não corresponde ao uso real.

## Como funciona
Use pausas com faixa de variação entre ações e a função de ritmo quando cada usuário precisa completar um número de voltas em um período.

## Exemplo
Um cenário de leitura pode variar a espera entre duas e cinco segundos, aproximando o intervalo da consulta real.

## Limites e trade-offs
Pausas longas reduzem a pressão exercida, e a função de ritmo pode compensar atrasos internos de forma inesperada se o alvo for mal dimensionado.

## Como verificar
Compare duas execuções, com e sem pausas, e observe o efeito na taxa efetiva e no número de voltas concluídas por usuário.

## Conexões
- [[gatling-feeders]] — Veja também: Gatling: alimentar cenários com dados externos.
- [[gatling-assertions]] — Veja também: Gatling: reprovar a execução com asserções.

## Fontes
- [Gatling — Pauses](https://docs.gatling.io/reference/script/core/scenario/) — pausas entre ações e função de ritmo por usuário virtual; consultado em 2026-10-03.
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — encadeamento de ações, pausas e nomeação de requisições na jornada; consultado em 2026-10-03.
