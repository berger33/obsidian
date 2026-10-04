---
id: software.testes.tranche26.001973
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html", "https://raw.githubusercontent.com/YosysHQ/sby/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Escrevendo propriedades temporais básicas em RTL: assert imediato e operador $past

## Em uma frase
Na seção Verification properties do Getting started, o tutorial demonstra duas formas fundamentais de asserção em Verilog/SystemVerilog verificadas pelo sby: um limite invariante imediato sobre um contador auxiliar — a_oflow: assert (count <= MAX_DATA); — e uma propriedade temporal que compara o valor atual de um sinal com seu valor no ciclo de clock anterior usando $past — a_counts, que exige por disjunção lógica que count seja 0, igual a $past(count), igual a $past(count) + 1 ou igual a $past(count) - 1.

## Por que importa
A expressão com $past(count) codifica de forma declarativa que a ocupação da fila nunca pode dar saltos maiores que 1 elemento por ciclo (exceto quando reseta diretamente para 0), capturando imediatamente bugs de incremento duplo ou underflow.

## Como funciona
Rotule cada asserção no código RTL (como a_oflow: e a_counts:) para que o log de falha do SymbiYosys indique pelo nome exato qual propriedade foi violada, e use $past(sinal) para relacionar estados entre ciclos consecutivos.

## Exemplo
Na propriedade a_counts do tutorial, pelo menos uma das quatro disjunções (zero por reset, igual ao ciclo anterior, +1 ou -1) precisa ser verdadeira em todos os ciclos de clock.

## Limites e trade-offs
Ao usar $past(sinal), lembre-se de cobrir o estado inicial ou de reset (como count == 0 na disjunção de a_counts) para evitar falsas falhas no primeiro ciclo de verificação.

## Como verificar
Conferi a seção Verification properties no Getting started oficial do SymbiYosys.

## Conexões
- [[symbiyosys-fifo-rtl-example-structure]] — Veja também: O exemplo canônico em fifo.sv: ponteiros circulares addr_gen e banco de registradores.
- [[symbiyosys-invariant-checking-circular-pointers]] — Veja também: Verificação de invariante estrutural: consistência entre contador auxiliar e diferença de ponteiros.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
