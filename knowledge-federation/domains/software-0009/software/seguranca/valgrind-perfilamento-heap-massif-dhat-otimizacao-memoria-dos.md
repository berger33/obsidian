---
id: software.seguranca.tranche16.001539
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://valgrind.org/docs/manual/QuickStart.html", "https://valgrind.org/docs/manual/mc-manual.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Investigando **Negação de Serviço por Exaustão de Memória (Memory DoS)** e Uso de Heap com **`--tool=massif` (`ms_print`)** e **`--tool=dhat`** no Valgrind

## Em uma frase
Às vezes um servidor em C/C++ ou Rust **não possui nenhum Memory Leak** (ele libera 100% da memória antes de sair!), mas ao processar uma requisição específica de um cliente malicioso ele sofre um pico momentâneo de **8 GB de alocação no Heap**, acionando o **OOM Killer** do Linux e derrubando o serviço (**Denial of Service por Amplificação de Memória**)! Como descobrir exatamente qual função causou o pico de memória no Heap?

## Por que importa
Usando os dois profilers de Heap oficiais da suíte Valgrind: **`--tool=massif`** (acompanhado do visualizador **`ms_print`**) e **`--tool=dhat` (*Dynamic Heap Analysis Tool*)**!

## Como funciona
O **`massif`** tira snapshots periódicos da árvore de alocação do Heap (e opcionalmente da Stack com `--stacks=yes`) ao longo da execução, identificando o **Snapshot de Pico (`Peak`)** exato e desenhando um gráfico ASCII no terminal com `ms_print massif.out.<pid>`; já o **`dhat`** analisa cada bloco alocado medindo **quantas vezes cada byte alocado foi realmente lido ou escrito** (revelando blocos enormes alocados desnecessariamente que nunca são lidos!)!

## Exemplo
```bash
# Executar o profiler de Heap Massif (incluindo medicao de Stack com --stacks=yes) e imprimir o grafico de pico de memoria com ms_print
valgrind --tool=massif --stacks=yes --massif-out-file=./massif.out ./servidor_parser ./entrada_grande.bin
ms_print ./massif.out | head -n 45
```

## Limites e trade-offs
Olhe que recurso valioso do **`--tool=dhat`**: além de achar picos de memória, quando você abre o arquivo `dhat.out.<pid>` no visualizador `dh_view.html`, ele mostra métricas como **`zero-reads / zero-writes`** (memória alocada que nunca foi usada antes do `free()`!) e **`short-lived allocations`** (milhões de `malloc`/`free` minúsculos que degradam a CPU sob carga)!

## Como verificar
Use o `massif` sempre que o AFL++ encontrar uma entrada na pasta `hangs/` ou um caso de teste que consuma memória anormalmente alta para localizar a linha exata da amplificação de alocação.

## Conexões
- [[valgrind-deteccao-overflow-stack-globais-exp-sgcheck-limites]] — Veja também: Limitações Arquiteturais do Memcheck em **Arrays de Stack/Globais** e Como Auditar Overflows de Stack com **`exp-sgcheck` / AddressSanitizer**.
- [[valgrind-auditoria-daemons-fork-trace-children-file-descriptors-fds]] — Veja também: Auditando Daemons Complexos no Valgrind: Seguindo Processos Filhos (**`--trace-children=yes`**), Vazamento de **File Descriptors (`--track-fds=yes`)** e Logs XML para CI.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Referência cruzada direta com valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost.
- [[aflplusplus-triagem-crashes-reproducao-gdb-pwndbg-cov-analysis-lcov]] — Referência cruzada direta com aflplusplus-triagem-crashes-reproducao-gdb-pwndbg-cov-analysis-lcov.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
