---
id: software.testes.tranche26.001979
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

# Depuração visual do contraexemplo com GTKWave e arquivos de configuração .gtkw

## Em uma frase
No fechamento da seção SymbiYosys do Getting started, o tutorial recomenda instalar o GTKWave (gtkwave.sourceforge.net, visualizador VCD em código aberto) e mostra o comando para inspecionar o contraexemplo gerado junto de um arquivo de layout de sinais pré-configurado: gtkwave fifo_nofullskip/engine_0/trace.vcd noskip.gtkw, revelando visualmente o ciclo exato em que data_count e addr_diff divergem.

## Por que importa
Ler valores hexadecimais de dezenas de sinais de hardware em log textual é improdutivo; abrir o trace.vcd no GTKWave já com um arquivo .gtkw versionado no repositório destaca imediatamente os sinais relevantes (clock, reset, enables, ponteiros e contadores) na tela.

## Como funciona
Crie e versione no repositório um arquivo .gtkw com os sinais principais do módulo organizados e, ao receber uma falha do sby, execute gtkwave <pasta_da_tarefa>/engine_0/trace.vcd <layout.gtkw> para inspecionar os ciclos que antecedem a violação da asserção.

## Exemplo
No exemplo do tutorial, abrir fifo_nofullskip/engine_0/trace.vcd com noskip.gtkw mostra que escrever com a fila cheia sem a lógica de rskip sobrescreve o dado mais antigo sem avançar o ponteiro de leitura, quebrando a igualdade entre data_count e addr_diff.

## Limites e trade-offs
O GTKWave é uma ferramenta gráfica de inspeção local; em pipelines de CI sem tela, arquive a pasta da tarefa (contendo trace.vcd e trace_tb.v) como artefato do build para que o engenheiro possa abri-la localmente com o .gtkw.

## Como verificar
Conferi a nota inicial sobre GTKWave e o comando gtkwave fifo_nofullskip/engine_0/trace.vcd noskip.gtkw no Getting started oficial.

## Conexões
- [[symbiyosys-three-counterexample-artifacts]] — Veja também: Os três artefatos gerados em uma falha: trace.vcd, trace_tb.v e trace.smtc.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
