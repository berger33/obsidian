---
id: software.testes.tranche26.001978
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

# Os três artefatos gerados em uma falha: trace.vcd, trace_tb.v e trace.smtc

## Em uma frase
O log de falha da tarefa fifo_nofullskip no Getting started mostra exatamente os três arquivos que o motor engine_0 grava no diretório da tarefa quando uma asserção falha: (1) o arquivo de ondas VCD em engine_0/trace.vcd ("Writing trace to VCD file"), (2) um testbench em Verilog reproduzível em engine_0/trace_tb.v ("Writing trace to Verilog testbench") e (3) um arquivo de restrições SMT em engine_0/trace.smtc ("Writing trace to constraints file").

## Por que importa
Cada um desses três artefatos resolve uma etapa do fluxo de engenharia de hardware: trace.vcd abre direto num visualizador de ondas para inspeção visual imediata; trace_tb.v permite simular o contraexemplo exato em qualquer simulador Verilog padrão da equipe; e trace.smtc permite transformar ou fixar restrições formais.

## Como funciona
Quando uma tarefa do sby falhar com Status: FAIL, localize o caminho impresso em "counterexample trace: <tarefa>/engine_0/trace.vcd" para abrir as ondas, ou passe engine_0/trace_tb.v ao simulador RTL do projeto para reproduzir o bug fora do verificador formal.

## Exemplo
No exemplo do tutorial, o sumário final aponta diretamente o arquivo de ondas gerado: counterexample trace: fifo_nofullskip/engine_0/trace.vcd, ao lado de engine_0/trace_tb.v e engine_0/trace.smtc.

## Limites e trade-offs
Esses três arquivos só são gerados quando o solver encontra um trace concreto (como uma falha no basecase/BMC ou um alvo atingido no modo cover); quando todas as asserções passam no BMC, não há contraexemplo a gravar.

## Como verificar
Conferi o bloco de log de saída da tarefa nofullskip na seção SymbiYosys do Getting started oficial.

## Conexões
- [[symbiyosys-unbounded-basecase-and-induction]] — Veja também: Verificação não limitada (unbounded): processos paralelos basecase e induction.
- [[symbiyosys-gtkwave-waveform-debugging]] — Veja também: Depuração visual do contraexemplo com GTKWave e arquivos de configuração .gtkw.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
