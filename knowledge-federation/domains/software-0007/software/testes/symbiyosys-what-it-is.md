---
id: software.testes.tranche26.001970
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
fontes: ["https://raw.githubusercontent.com/YosysHQ/sby/master/README.md", "https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# SymbiYosys (sby): driver de linha de comando para verificação formal de hardware sobre o Yosys

## Em uma frase
O README oficial define o SymbiYosys (sby) como um programa driver front-end para fluxos de verificação formal de hardware baseados no Yosys (yosyshq.net/yosys/), com documentação oficial em yosyshq.readthedocs.io/projects/sby/.

## Por que importa
Em verificação de RTL (Verilog e SystemVerilog), preparar scripts de síntese no Yosys, gerar modelos para motores formais, invocar solvers SMT/SAT e coletar ondas de contraexemplo envolve várias ferramentas encadeadas; o sby orquestra todo esse fluxo a partir de um único arquivo de configuração .sby.

## Como funciona
Escreva o módulo de hardware com propriedades formais (assert, assume, cover), defina as tarefas de verificação num arquivo .sby e execute o comando sby para acionar o Yosys e o solver escolhido.

## Exemplo
No tutorial Getting started da documentação oficial, os arquivos de exemplo ficam em docs/examples/fifo no repositório do sby e são verificados com um único comando sby fifo.sby.

## Limites e trade-offs
O SymbiYosys é o orquestrador front-end; a síntese para representação formal depende do Yosys e a decisão matemática depende dos motores e solvers instalados (como boolector via smtbmc).

## Como verificar
Conferi o primeiro parágrafo do README oficial em YosysHQ/sby e a nota introdutória do Getting started oficial.

## Conexões
- [[symbiyosys-isc-license-and-suites]] — Veja também: Licenciamento ISC e distribuição via OSS CAD Suite (gratuito) e Tabby CAD Suite.

## Fontes
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
