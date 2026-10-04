---
id: software.seguranca.tranche16.001540
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

# Auditando Daemons Complexos no Valgrind: Seguindo Processos Filhos (**`--trace-children=yes`**), Vazamento de **File Descriptors (`--track-fds=yes`)** e Logs XML para CI

## Em uma frase
Quando você audita um servidor Unix real (como um servidor SSH, worker HTTP ou agente de segurança), ele frequentemente: **(1)** Cria processos filhos via `fork()` / `execve()`, e **(2)** Pode sofrer de **Vazamento de Descritores de Arquivo (*File Descriptor Leak* — sockets, pipes ou arquivos abertos com `open()`/`socket()` que nunca recebem `close()`)**, travando o servidor ao atingir `ulimit -n` (`Too many open files`)! Como configurar o Valgrind para auditar tudo isso automaticamente?

## Por que importa
Combinando três flags essenciais do Valgrind: **(1) `--trace-children=yes`** (faz o Valgrind continuar instrumentando processos filhos após `fork()` + `exec()`, com `--trace-children-skip='*/bin/sh,*/usr/bin/*'` para não perder tempo instrumentando utilitários externos!).

## Como funciona
**(2) `--track-fds=yes`** (ou `all`, que lista no final da execução todos os File Descriptors e Sockets deixados abertos com o stack trace exato de onde o `open()`/`socket()` foi chamado!); e **(3) `--log-file=valgrind-%p.log` / `--xml=yes --xml-file=valgrind-%p.xml`** (onde `%p` insere o PID de cada processo filho em um arquivo separado)!

## Exemplo
```bash
# Auditar um daemon multiprocesso rastreando vazamento de File Descriptors/Sockets (--track-fds=yes), processos filhos e gerando um log por PID (%p)
valgrind \
  --tool=memcheck \
  --leak-check=full \
  --track-fds=yes \
  --trace-children=yes \
  --trace-children-skip="/bin/*,/usr/bin/*" \
  --log-file="./valgrind-pid-%p.log" \
  ./meu_daemon --test-run
```

## Limites e trade-offs
Por que usar o especificador **`%p`** em `--log-file="./valgrind-pid-%p.log"` e `--xml-file="./valgrind-pid-%p.xml"` é obrigatório quando `--trace-children=yes` está ativo? Porque se o processo pai e 4 processos filhos escreverem ao mesmo tempo no mesmo arquivo de log sem `%p`, as linhas de saída (ou tags XML) ficarão embaralhadas e corrompidas! Com `%p`, cada processo ganha seu próprio relatório limpo!

## Como verificar
Com isso fechamos o grupo completo do **Valgrind** (`Memcheck`, `Helgrind`, `DRD`, `Massif`, `DHAT`) na Tranche 16!

## Conexões
- [[valgrind-perfilamento-heap-massif-dhat-otimizacao-memoria-dos]] — Veja também: Investigando **Negação de Serviço por Exaustão de Memória (Memory DoS)** e Uso de Heap com **`--tool=massif` (`ms_print`)** e **`--tool=dhat`** no Valgrind.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Referência cruzada direta com valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost.
- [[valgrind-arquivos-supressao-gen-suppressions-ci-cd-bibliotecas-terceiros]] — Referência cruzada direta com valgrind-arquivos-supressao-gen-suppressions-ci-cd-bibliotecas-terceiros.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
