---
id: software.seguranca.tranche10.000943
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md", "https://pwndbg.re/stable/features/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pwndbg para **Heap Exploitation (`glibc ptmalloc2` & `jemalloc`)**: Comandos **`heap`**, **`vis_heap_chunks` (`vis`)**, **`bins`**, **`tcache`**, **`arena`** e **`try_free`**

## Em uma frase
Diagnosticar e explorar vulnerabilidades de corrupção de heap (**Heap Overflow, Use-After-Free (UAF), Double Free, House of Force/Spirit/Lore/Einherjar, Tcache Poisoning**) no GDB puro exigiria decodificar manualmente cabeçalhos `malloc_chunk` (`prev_size`, `size` com bits `PREV_INUSE`/`IS_MMAPPED`/`NON_MAIN_ARENA`, ponteiros `fd`/`bk` ofuscados por *Safe-Linking*) em hexadecimal.

## Por que importa
O Pwndbg possui o conjunto mais completo de comandos de introspecção de alocadores de memória (**glibc `ptmalloc2`** e **`jemalloc`**): **`heap`** (lista todos os chunks alocados e livres da arena), **`vis_heap_chunks` (ou atalho `vis`)** (desenha visualmente os chunks contíguos da heap com cores diferentes por chunk e marca quais pertencem a cada bin!), **`bins`** (exibe o estado completo de **`tcachebins`**, **`fastbins`**, **`unsortedbin`**, **`smallbins`** e **`largebins`** decodificando os ponteiros!) e **`tcache`**!

## Como funciona
Ainda mais impressionante: os comandos **`try_free <endereco>`** e **`find_fake_fast <endereco>`** simulam todas as verificações de integridade do `free()` da `glibc` antes de você chamá-lo e procuram regiões de memória que podem servir como um *fake chunk* válido!

## Exemplo
```gdb
# Dentro do Pwndbg: visualizar graficamente os chunks da heap (vis), inspecionar todas as listas de chunks livres (bins) e simular um free()
pwndbg> vis_heap_chunks 16
pwndbg> bins
pwndbg> try_free 0x5555555592a0
```

## Limites e trade-offs
Por que o comando **`try_free <addr>`** economiza horas de análise? Porque a `glibc` moderna possui dezenas de *security checks* dentro de `_int_free` (como `double free or corruption (top)`, `free(): invalid next size (fast)` ou falha de alinhamento de 16 bytes): `try_free` testa todas essas condições sem alterar o processo e diz exatamente se o `free(addr)` vai funcionar ou qual check da `glibc` vai abortar!

## Como verificar
Use `arena`, `mp` (`mp_` struct) e `top_chunk` para auditar o estado global do alocador em processos multi-thread.

## Conexões
- [[pwndbg-auditoria-mitigacoes-binarias-checksec-vmmap-aslr-pie-nx-canary]] — Veja também: Pwndbg: Auditoria de Mitigações de Compilação (**`checksec`: RELRO, Stack Canary, NX, PIE, Fortify, CFI/CET**) e Mapeamento Virtual (**`vmmap`**, **`canary`**).
- [[pwndbg-busca-memoria-search-leakfind-telescope-cyclic-offset]] — Veja também: Pwndbg: Introspecção de Ponteiros (**`telescope`**, **`search`**, **`leakfind`**, **`probeleak`**) e Cálculo de Offset de Buffer Overflow (**`cyclic`**).
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
