---
id: software.testes.tranche26.001976
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

# Reexecução iterativa com a flag -f e seleção de tarefa na linha de comando

## Em uma frase
Ao demonstrar como provocar e inspecionar uma falha com o comando sby -f fifo.sby nofullskip, o Getting started destaca o papel da flag -f: ela sobrescreve automaticamente o diretório de saída existente da tarefa, o que é muito útil ao fazer ajustes no código RTL e reexecutar os testes para validar.

## Por que importa
Por segurança, o SymbiYosys cria um diretório de trabalho por tarefa (como fifo_nofullskip/) e evita apagar resultados anteriores sem permissão; durante o ciclo rápido de editar o Verilog e rodar o verificador de novo, passar -f evita ter de remover a pasta de saída manualmente a cada tentativa.

## Como funciona
Use sby -f <arquivo.sby> [nome_da_tarefa] durante o desenvolvimento interativo e em scripts de CI que reutilizam o diretório de checkout para garantir que a saída reflita sempre a última execução.

## Exemplo
O comando sby -f fifo.sby nofullskip executa apenas a tarefa nofullskip (que define a macro NO_FULL_SKIP omitindo a lógica rskip/wskip) e sobrescreve a pasta fifo_nofullskip/ se ela já existir.

## Limites e trade-offs
Como -f apaga os artefatos anteriores daquela tarefa (incluindo traces VCD e testbenches gerados), salve ou copie qualquer arquivo trace.vcd importante antes de rodar novamente com -f.

## Como verificar
Conferi o comando sby -f fifo.sby nofullskip e a explicação da flag -f na seção SymbiYosys do Getting started oficial.

## Conexões
- [[symbiyosys-sby-file-tasks-and-default-tag]] — Veja também: O arquivo .sby, suas tarefas de verificação e a tag :default.
- [[symbiyosys-unbounded-basecase-and-induction]] — Veja também: Verificação não limitada (unbounded): processos paralelos basecase e induction.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
