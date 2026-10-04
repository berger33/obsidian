---
id: software.testes.tranche26.001975
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

# O arquivo .sby, suas tarefas de verificação e a tag :default

## Em uma frase
A seção SymbiYosys do Getting started explica que o sby usa um arquivo .sby (no exemplo, fifo.sby) para definir um conjunto de tarefas (tasks) de verificação: no tutorial são quatro — basic (bounded model check do design), nofullskip (demonstração de modelo com falha usando unbounded model check), cover (modo cover testando declarações cover) e noverific (teste de fallback para o frontend Verilog padrão) —, onde o uso da tag :default indica que apenas basic e cover devem rodar por padrão quando nenhuma tarefa é especificada na linha de comando (sby fifo.sby).

## Por que importa
Agrupar múltiplas configurações de verificação num único arquivo .sby permite manter no mesmo lugar o check rápido padrão de CI (:default com BMC e cover), testes de falha conhecidos e variações de frontend, sem espalhar vários arquivos de script pelo diretório.

## Como funciona
Defina as tarefas nomeadas dentro do arquivo .sby, associe a tag :default às tarefas que devem passar sempre na rotina padrão (sby projeto.sby) e invoque tarefas específicas pelo nome na linha de comando quando quiser executá-las isoladamente.

## Exemplo
Rodar simplesmente sby fifo.sby executa as tarefas marcadas com :default (basic e cover), que o tutorial destaca que devem passar todas se a instalação do sby e dos solvers estiver correta.

## Limites e trade-offs
Tarefas que não fazem parte do grupo :default (como nofullskip, criada propositalmente para falhar na demonstração) só rodam quando seu nome é passado explicitamente após o arquivo .sby.

## Como verificar
Conferi a descrição das quatro tarefas de fifo.sby e da tag :default na seção SymbiYosys do Getting started oficial.

## Conexões
- [[symbiyosys-invariant-checking-circular-pointers]] — Veja também: Verificação de invariante estrutural: consistência entre contador auxiliar e diferença de ponteiros.
- [[symbiyosys-overwrite-flag-f-and-task-selection]] — Veja também: Reexecução iterativa com a flag -f e seleção de tarefa na linha de comando.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
