---
id: software.testes.tranche18.001188
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://google.github.io/googletest/primer.html", "https://google.github.io/googletest/advanced.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: escolher entre asserção fatal e não fatal

## Em uma frase
As asserções fatais interrompem o caso no primeiro erro, enquanto as não fatais registram a falha e continuam a execução.

## Por que importa
Continuar depois de uma pré-condição violada produz erros derivados, e interromper em verificações independentes esconde informação útil.

## Como funciona
Use asserção fatal para pré-condições das quais o restante depende e não fatal para verificações independentes do mesmo caso.

## Exemplo
Se a criação do objeto falha, a asserção fatal interrompe antes de o teste usar um valor inválido nas verificações seguintes.

## Limites e trade-offs
O uso indiscriminado da forma não fatal espalha falhas em cascata, e a forma fatal demais reduz o diagnóstico de um caso com várias verificações.

## Como verificar
Introduza uma falha em pré-condição e confirme que o relatório mostra o ponto de interrupção correto.

## Conexões
- [[googletest-test-macros]] — Veja também: GoogleTest: declarar casos e suítes.
- [[googletest-comparisons]] — Veja também: GoogleTest: comparar valores com veredito claro.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — macros de caso, asserções, comparações e execução; consultado em 2026-10-03.
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
