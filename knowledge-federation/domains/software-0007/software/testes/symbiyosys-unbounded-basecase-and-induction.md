---
id: software.testes.tranche26.001977
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

# Verificação não limitada (unbounded): processos paralelos basecase e induction

## Em uma frase
O log de saída da tarefa nofullskip reproduzido no Getting started mostra como o SymbiYosys executa um unbounded model check (prova por k-induction) com o motor engine_0 (smtbmc boolector): ele roda os sub-processos engine_0.basecase e engine_0.induction e, assim que engine_0.basecase encontra a falha na asserção a_count_diff (returncode=1, Status: FAIL), o orquestrador encerra o processo de indução ("engine_0.induction: terminating process") e conclui com DONE (FAIL, rc=2).

## Por que importa
Na prova por indução temporal (k-induction), o caso base (basecase) procura contraexemplos alcançáveis a partir do estado inicial nos primeiros k ciclos, enquanto o passo indutivo (induction) tenta provar que se a propriedade vale por k ciclos quaisquer, vale no ciclo k+1; abortar a indução assim que o caso base acha um bug economiza tempo de CPU.

## Como funciona
Configure tarefas de prova não limitada no arquivo .sby para obter garantias além de uma janela fixa de ciclos, e observe no log se a falha veio do basecase (um bug real alcançável desde o reset, com trace concreto) ou da induction.

## Exemplo
No log oficial de fifo_nofullskip, em apenas 2 segundos de relógio o engine_0 (smtbmc boolector) retorna FAIL para o basecase na asserção a_count_diff, mata o processo engine_0.induction e encerra o sby com código de retorno rc=2.

## Limites e trade-offs
Em scripts de automação e CI, note que uma falha de verificação formal no sby retorna código de saída diferente de zero (rc=2 no log oficial de falha), listando no final "The following tasks failed: ['nofullskip']".

## Como verificar
Conferi a descrição da tarefa nofullskip e as linhas de log SBY [fifo_nofullskip] no Getting started oficial.

## Conexões
- [[symbiyosys-overwrite-flag-f-and-task-selection]] — Veja também: Reexecução iterativa com a flag -f e seleção de tarefa na linha de comando.
- [[symbiyosys-three-counterexample-artifacts]] — Veja também: Os três artefatos gerados em uma falha: trace.vcd, trace_tb.v e trace.smtc.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
