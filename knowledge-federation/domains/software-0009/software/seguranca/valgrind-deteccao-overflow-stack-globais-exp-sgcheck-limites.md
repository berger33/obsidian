---
id: software.seguranca.tranche16.001538
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

# Limitações Arquiteturais do Memcheck em **Arrays de Stack/Globais** e Como Auditar Overflows de Stack com **`exp-sgcheck` / AddressSanitizer**

## Em uma frase
Por que é fundamental que todo engenheiro de segurança saiba o que o **Valgrind Memcheck** detecta com perfeição (**Heap Overflows, Use-After-Free, Double-Free, Memory Leaks e Uninitialised Values**) e o que o **Memcheck NÃO consegue detectar por design (Overflows entre variáveis adjacentes na Stack ou no segmento `.bss`/`.data` global)**?

## Por que importa
Porque na arquitetura do Memcheck (`mc-manual.html`), como ele opera sobre o binário já compilado sem alterar o layout da stack frame gerada pelo compilador, ele intercepta todas as chamadas de **Heap (`malloc`, `calloc`, `realloc`, `free`, `new`, `delete`)** colocando *Redzones* entre os blocos do heap, mas **não pode inserir Redzones no meio de duas variáveis locais `char buf[16]; int admin = 0;` já alocadas lado a lado na Stack**!

## Como funciona
Para auditar especificamente ultrapassagens de limites de arrays na **Stack e em Variáveis Globais**, a suíte Valgrind criou a ferramenta experimental **`--tool=exp-sgcheck` (*Stack and Global Array Check*)**, e no fluxo moderno de compilação utiliza-se o **`AddressSanitizer` (`-fsanitize=address`)**!

## Exemplo
```bash
# Combinar na bateria de testes de seguranca C/C++ o Valgrind Memcheck (para Heap, Leaks e Uninitialised Bits) e compilacao com ASAN (para Stack/Globals)
valgrind --tool=memcheck --leak-check=full --track-origins=yes --error-exitcode=1 ./teste_unidade_valgrind
gcc -g -O1 -fsanitize=address,undefined teste_unidade.c -o ./teste_unidade_asan && ./teste_unidade_asan
```

## Limites e trade-offs
Veja na dupla de comandos acima por que rodar **ambos** (`Valgrind Memcheck` + binário `-fsanitize=address,undefined`) na sua pipeline de CI/CD de projetos C/C++ é o padrão ouro de engenharia de segurança: **(1)** O **ASAN/UBSAN** captura instantaneamente overflows em arrays de Stack e variáveis Globais (porque insere *Redzones* na stack durante a compilação), enquanto **(2)** O **Valgrind Memcheck** captura usos de memória não inicializada (`V-bits`), leaks detalhados e erros dentro de bibliotecas `.so` externas pré-compiladas!

## Como verificar
Nunca rode um binário já compilado com `-fsanitize=address` **dentro** do Valgrind: como ambos tentam substituir o `malloc`/`free` e mapear *Shadow Memory*, eles entram em conflito; mantenha um alvo de build limpo para o Valgrind e outro para o ASAN!

## Conexões
- [[valgrind-concorrencia-data-races-deadlocks-helgrind-drd-pthreads]] — Veja também: Caçando **Race Conditions (*Data Races*)** e **Deadlocks** em Programas Multithreaded C/C++ com **`--tool=helgrind`** e **`--tool=drd`** no Valgrind.
- [[valgrind-perfilamento-heap-massif-dhat-otimizacao-memoria-dos]] — Veja também: Investigando **Negação de Serviço por Exaustão de Memória (Memory DoS)** e Uso de Heap com **`--tool=massif` (`ms_print`)** e **`--tool=dhat`** no Valgrind.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.
- [[valgrind-erros-memcheck-invalid-read-write-uninitialised-track-origins]] — Referência cruzada direta com valgrind-erros-memcheck-invalid-read-write-uninitialised-track-origins.
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Referência cruzada direta com aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
