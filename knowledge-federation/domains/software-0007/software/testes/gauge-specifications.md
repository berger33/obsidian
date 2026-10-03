---
id: software.testes.tranche20.001359
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://docs.gauge.org/writing-specifications", "https://docs.gauge.org/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gauge: escrever especificações em markdown

## Em uma frase
Uma especificação é um arquivo em formato markdown com cabeçalho próprio, uma ou mais seções de cenário e passos como itens de lista.

## Por que importa
Escrever o teste na linguagem do negócio deixa o documento legível por quem não programa e serve ao mesmo tempo como documentação viva.

## Como funciona
Nomeie a especificação pela funcionalidade, descreva cada cenário como um fluxo único e escreva passos curtos começando por verbo.

## Exemplo
A especificação de login pode declarar um cenário de acesso válido e outro de credencial incorreta, cada um com seus passos.

## Limites e trade-offs
Especificações extensas com dezenas de cenários dificultam a leitura, e passos que descrevem detalhes de implementação perdem o valor de linguagem comum.

## Como verificar
Leia a especificação em voz alta com alguém de produto e confirme que cada cenário descreve um comportamento reconhecível.

## Conexões
- [[gauge-steps-implementation]] — Veja também: Gauge: implementar passos no código.

## Fontes
- [Gauge — Escrever especificações](https://docs.gauge.org/writing-specifications) — sintaxe das especificações, tabelas de dados e conceitos; consultado em 2026-10-03.
- [Gauge — Visão geral](https://docs.gauge.org/overview) — conceitos de especificação, cenário, passo e conceito; consultado em 2026-10-03.
