---
id: software.testes.tranche22.001562
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
fontes: ["https://github.com/bats-core/bats-core/blob/master/README.md", "https://bats-core.readthedocs.io/en/latest/gotchas.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: cada linha viva é uma asserção

## Em uma frase
Os testes Bats rodam sob errexit: o teste termina na primeira linha com status de saída diferente de zero, de modo que toda linha que sobrevive foi verificada.

## Por que importa
Em shell não existe exceção por igualdade, então a semântica de "falhou, aborta" transforma qualquer comando em asserção implícita e reduz a verbosidade dos casos.

## Como funciona
Escreva os passos como comandos encadeados e termine com o teste booleano desejado, por exemplo um [ "$x" = "esperado" ]; não é preciso envolto nada em assert.

## Exemplo
[ "$(foo)" = "bar" ] dentro do bloco @test reprova o teste se foo imprimir qualquer outra coisa, e nenhuma linha seguinte é executada.

## Limites e trade-offs
Há pegadinhas conhecidas: negações com ! e compostos entre colchetes duplos ou aritméticos em certos contextos não chegam a falhar o teste, como a própria página de gotchas lista nos títulos.

## Como verificar
Reproduza um teste com uma linha falsa no meio e confirme que o caso para ali; depois compare com as entradas de gotchas sobre colchetes duplos e ! true.

## Conexões
- [[bats-test-syntax]] — Veja também: bats-core: a suíte é um script Bash.
- [[bats-run-status-output]] — Veja também: bats-core: run captura status e saída.

## Fontes
- [Bats-core — README oficial](https://github.com/bats-core/bats-core/blob/master/README.md) — proposta TAP, história do fork e licença MIT; consultado em 2026-10-03.
- [Bats-core — Gotchas](https://bats-core.readthedocs.io/en/latest/gotchas.html) — armadilhas documentadas: run, colchetes duplos, load e file descriptor 3; consultado em 2026-10-03.
