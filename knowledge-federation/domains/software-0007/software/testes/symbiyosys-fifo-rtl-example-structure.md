---
id: software.testes.tranche26.001972
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

# O exemplo canônico em fifo.sv: ponteiros circulares addr_gen e banco de registradores

## Em uma frase
A página Getting started da documentação oficial apresenta o exemplo completo usado para ensinar a ferramenta (localizado em docs/examples/fifo/fifo.sv): um buffer FIFO de até 16 palavras de 8 bits (MAX_DATA=16) composto por duas instâncias de um gerador/contador de endereços síncrono com reset assíncrono (module addr_gen, para waddr e raddr que voltam a 0 ao atingir MAX_DATA-1) e um banco de registradores reg [7:0] data [MAX_DATA-1:0] com escrita síncrona e leitura assíncrona (assign rdata = data[raddr]).

## Por que importa
Em uma fila circular em hardware, os ponteiros de leitura e escrita dão a volta ao atingir MAX_DATA-1; qualquer erro sutil na lógica de fila cheia ou vazia dessincroniza os ponteiros e corrompe a ordem FIFO — um alvo clássico onde testes dirigidos deixam escapar cantos de wrap-around que a verificação formal pega em segundos.

## Como funciona
Estude os arquivos em docs/examples/fifo do repositório YosysHQ/sby para ver como instrumentar um módulo RTL real com sinais auxiliares de contagem e asserções de verificação sem alterar o comportamento funcional do circuito.

## Exemplo
No fifo.sv, o módulo addr_gen incrementa addr em posedge clk quando en está ativo e faz wrap-around para 0 quando addr == MAX_DATA-1.

## Limites e trade-offs
O código RTL por si só apenas descreve os registradores e ponteiros; para que o SymbiYosys verifique que a fila nunca perde a sincronia, é preciso declarar propriedades explícitas sobre os sinais do módulo.

## Como verificar
Conferi a seção First In, First Out (FIFO) buffer em yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html.

## Conexões
- [[symbiyosys-isc-license-and-suites]] — Veja também: Licenciamento ISC e distribuição via OSS CAD Suite (gratuito) e Tabby CAD Suite.
- [[symbiyosys-sva-assert-and-past-operator]] — Veja também: Escrevendo propriedades temporais básicas em RTL: assert imediato e operador $past.

## Fontes
- [SymbiYosys — Getting started (documentação oficial)](https://yosyshq.readthedocs.io/projects/sby/en/latest/quickstart.html) — Tutorial oficial Getting started do SymbiYosys com o exemplo FIFO em fifo.sv, asserções assert e $past, tarefas em fifo.sby com :default, flag -f, log de falha rc=2 com basecase/induction, trace.vcd/trace_tb.v/trace.smtc e inspeção no GTKWave.; consultado em 2026-10-03.
- [SymbiYosys (sby) — README oficial](https://raw.githubusercontent.com/YosysHQ/sby/master/README.md) — README oficial do SymbiYosys com definição como driver front-end sobre o Yosys, licença ISC, licenças individuais dos solvers e distribuição via OSS CAD Suite e Tabby CAD Suite.; consultado em 2026-10-03.
