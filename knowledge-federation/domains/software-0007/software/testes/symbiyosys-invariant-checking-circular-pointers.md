---
id: software.testes.tranche26.001974
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

# Verificação de invariante estrutural: consistência entre contador auxiliar e diferença de ponteiros

## Em uma frase
Ainda em Verification properties, o tutorial mostra como amarrar um sinal auxiliar de contagem (count) aos ponteiros reais de leitura e escrita (raddr e waddr) de um buffer circular: calcula-se a distância com wrap-around via assign addr_diff = waddr >= raddr ? waddr - raddr : waddr + MAX_DATA - raddr; e afirma-se o invariante a_count_diff, exigindo que count == addr_diff ou que (count == MAX_DATA && addr_diff == 0).

## Por que importa
Um erro comum em verificação formal é escrever uma propriedade sobre um contador auxiliar (count <= MAX_DATA) que nunca pode falhar por construção do próprio contador, enquanto os ponteiros reais do circuito divergem silenciosamente; provar a equivalência a_count_diff conecta a especificação ao caminho de dados real.

## Como funciona
Sempre que introduzir registradores ou sinais auxiliares de modelagem no RTL para facilitar a escrita de asserções, adicione uma asserção de invariante que prove que o sinal auxiliar reflete exatamente o estado dos ponteiros ou máquinas de estado do circuito.

## Exemplo
Quando a fila circular de 16 posições está completamente cheia (count == MAX_DATA), waddr e raddr apontam para o mesmo endereço (addr_diff == 0), razão pela qual a segunda cláusula de a_count_diff trata explicitamente count == MAX_DATA && addr_diff == 0.

## Limites e trade-offs
É exatamente essa asserção a_count_diff que falha na tarefa demonstrativa nofullskip quando a lógica de proteção contra escrita com fila cheia é desabilitada no tutorial.

## Como verificar
Conferi o cálculo de addr_diff e a asserção a_count_diff na seção Verification properties do Getting started oficial.

## Conexões
- [[symbiyosys-sva-assert-and-past-operator]] — Veja também: Escrevendo propriedades temporais básicas em RTL: assert imediato e operador $past.
- [[symbiyosys-sby-file-tasks-and-default-tag]] — Veja também: O arquivo .sby, suas tarefas de verificação e a tag :default.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
