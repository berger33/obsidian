---
id: software.seguranca.tranche16.001533
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

# Taxonomia de Vazamentos de Memória (**Memory Leaks**) no Valgrind Memcheck: **`definitely lost`**, **`indirectly lost`**, **`possibly lost`** e **`still reachable`**

## Em uma frase
Ao encerrar um programa sob `valgrind --leak-check=full`, o relatório `LEAK SUMMARY` divide os blocos alocados com `malloc`/`new` que não foram liberados em **4 categorias distintas**: **`definitely lost`**, **`indirectly lost`**, **`possibly lost`** e **`still reachable`**. Qual é a diferença exata entre elas segundo a tabela de ponteiros da seção 4.2.10 do `mc-manual.html`?

## Por que importa
Tudo depende de se ainda existe algum ponteiro (` root-set`: registradores, stack ou variáveis globais) apontando para o bloco no momento em que o programa termina: **(1) `definitely lost` (Vazamento Confirmado Crítico!)** — **nenhum ponteiro** aponta mais para aquele bloco; o programa perdeu a referência e jamais conseguiria dar `free()` nele (causa exaustão de memória / DoS em daemons de longa duração!).

## Como funciona
**(2) `indirectly lost`** — blocos filhos (ex.: nós de uma árvore ou lista encadeada) que só eram alcançáveis através de um bloco pai que foi `definitely lost` (corrigir o pai corrige todos os filhos automaticamente!); **(3) `possibly lost`** — só existe um **ponteiro interior** apontando para o meio do bloco, e não para o início; e **(4) `still reachable`** — um ponteiro global/estático ainda aponta para o início do bloco quando `exit()` foi chamado!

## Exemplo
```bash
# Auditar vazamentos de memoria exigindo detalhamento completo (--show-leak-kinds=definite,indirect,possible) e quebrando o CI em leaks definitivos
valgrind \
  --leak-check=full \
  --show-leak-kinds=definite,indirect,possible \
  --errors-for-leak-kinds=definite,possible \
  --error-exitcode=1 \
  ./meu_servico --run-once
```

## Limites e trade-offs
Veja a combinação cirúrgica **`--errors-for-leak-kinds=definite,possible --error-exitcode=1`** acima: muitas bibliotecas do sistema (como `glib` ou `dlopen`) deixam caches globais `still reachable` ao sair do programa; configurando `--errors-for-leak-kinds=definite,possible`, o seu pipeline de CI/CD ignora blocos `still reachable` inofensivos na saída, mas **reprova automaticamente o build se surgir qualquer vazamento real (`definitely lost` ou `possibly lost`)**!

## Como verificar
E se você quiser gerar uma árvore visual de onde o seu programa está alocando e liberando mais memória ao longo do tempo (*Execution Trees*), passe **`--xtree-memory=allocs`** (ou `full`) para gerar um arquivo `xtmemory.kcg` visualizável no **`kcachegrind`**!

## Conexões
- [[valgrind-erros-memcheck-invalid-read-write-uninitialised-track-origins]] — Veja também: Interpretando Erros Críticos do **Memcheck**: `Invalid read/write`, `Use of uninitialised value` (**`--track-origins=yes`**), `Syscall param` e `Invalid free()` / `Mismatched free()`.
- [[valgrind-arquivos-supressao-gen-suppressions-ci-cd-bibliotecas-terceiros]] — Veja também: Gerenciando Falsos Positivos de Bibliotecas de Terceiros no Valgrind com **Suppression Files (`--gen-suppressions=all` e `--suppressions=arquivo.supp`)**.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.
- [[valgrind-perfilamento-heap-massif-dhat-otimizacao-memoria-dos]] — Referência cruzada direta com valgrind-perfilamento-heap-massif-dhat-otimizacao-memoria-dos.

## Fontes
- [The Valgrind Quick Start Guide (`valgrind.org/docs/manual/QuickStart.html`)](https://valgrind.org/docs/manual/QuickStart.html) — guia rápido oficial do Valgrind cobrindo preparação de programas (`-g -O1`) e execução sob a ferramenta padrão `Memcheck`; consultado em 2026-10-03.
- [Valgrind User Manual — Memcheck: a memory error detector (`mc-manual.html`)](https://valgrind.org/docs/manual/mc-manual.html) — manual técnico oficial do Memcheck detalhando erros de leitura/escrita inválida, bits `V` (*Valid-Value*) e `A` (*Valid-Address*), `--track-origins=yes`, taxonomia de leaks, `.supp`, `vgdb` e Memory Pools; consultado em 2026-10-03.
