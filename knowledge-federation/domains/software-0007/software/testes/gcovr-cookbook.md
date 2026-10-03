---
id: software.testes.tranche22.001657
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/index.html", "https://gcovr.com/en/stable/changelog.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: receitas de build difícil

## Em uma frase
O cookbook oficial resolve os casos recorrentes que fogem do flow canônico: cobertura de extensões C em Python, builds CMake out-of-source, suporte ao formato Keil uVision e como criar uma aplicação standalone do gcovr.

## Por que importa
Extensão C de Python é o exemplo máximo: dois toolchains (gcc com --coverage e pytest) e um relatório que ninguém sabe montar sem receita pronta.

## Como funciona
Cada uma das quatro entradas é uma seção ancorada da própria página do cookbook na doc 8.6, ligada da tabela de conteúdos.

## Exemplo
A menção a "How to collect coverage for C extensions" atende justamente o setup de testes de binding nativo, onde o build da extensão precisa herdar as flags de instrumentação.

## Limites e trade-offs
Receitas de cookbook envelhecem com as ferramentas citadas (versões de CMake e pytest); trate cada uma como receita testada na época da release da doc.

## Como verificar
Replique a receita CMake out-of-source num build seu e confira se o relatório resolve os caminhos sem -r manual.

## Conexões
- [[gcovr-gcov-parser]] — Veja também: gcovr: o parser do gcov por trás do número.
- [[gcovr-versions]] — Veja também: gcovr: ciclo de release visível na doc.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — Change Log](https://gcovr.com/en/stable/changelog.html) — datas de release da doc 8.6; consultado em 2026-10-03.
