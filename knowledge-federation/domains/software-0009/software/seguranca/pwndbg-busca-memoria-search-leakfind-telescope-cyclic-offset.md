---
id: software.seguranca.tranche10.000944
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

# Pwndbg: Introspecção de Ponteiros (**`telescope`**, **`search`**, **`leakfind`**, **`probeleak`**) e Cálculo de Offset de Buffer Overflow (**`cyclic`**)

## Em uma frase
Quatro comandos de análise de memória do Pwndbg são utilizados a todo instante durante o triage de um *crash* (`SIGSEGV`) ou a construção de um exploit: **`telescope` (`tele`)**, **`search`**, **`leakfind` / `probeleak`** e **`cyclic`**!

## Por que importa
O **`telescope <endereco> [N]`** desreferencia recursivamente cadeias de ponteiros (por exemplo, `0x7fffffffe100 -> 0x555555558010 -> 0x7ffff7dd56a0 (puts) <- "Hello"`), revelando imediatamente o que cada endereço na stack ou nos registradores aponta.

## Como funciona
O comando **`search`** localiza strings (`search -t string "/bin/sh"`), ponteiros (`search -p 0x7ffff7...`), inteiros ou sequências de bytes hexadecimais (`search -x deadbeef`) filtrando por região mapeada (ex.: `search "/bin/sh" libc` ou `search -w` apenas em páginas graváveis); enquanto **`leakfind`** e **`probeleak`** descobrem cadeias de ponteiros que podem ser usadas para vazar o endereço base da `libc` ou do binário (derrotando o **ASLR**)!

## Exemplo
```gdb
# Gerar um padrao De Bruijn de 200 bytes (cyclic), descobrir o offset exato que sobrescreveu RIP/RSP e buscar "/bin/sh" na libc
pwndbg> cyclic 200
pwndbg> cyclic -l 0x6161616c6161616b
pwndbg> search -t string "/bin/sh" libc
```

## Limites e trade-offs
Entenda como o padrão **De Bruijn (`cyclic`)** calcula em 1 segundo o tamanho exato do buffer antes do endereço de retorno (`RIP`): como toda subsequência de 4 ou 8 bytes gerada por `cyclic 200` é matematicamente única, quando o programa sofre `SIGSEGV` tentando saltar para `0x6161616c6161616b` (`kaaa` / `kaaal...`), rodar **`cyclic -l $rsp`** (ou `cyclic -l 0x6161616c6161616b`) informa a distância exata em bytes até o controle do ponteiro de instrução!

## Como verificar
Use `hexdump <addr> <count>` no Pwndbg para inspecionar buffers binários com destaque de caracteres ASCII e códigos de cores.

## Conexões
- [[pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins]] — Veja também: Pwndbg para **Heap Exploitation (`glibc ptmalloc2` & `jemalloc`)**: Comandos **`heap`**, **`vis_heap_chunks` (`vis`)**, **`bins`**, **`tcache`**, **`arena`** e **`try_free`**.
- [[pwndbg-analise-got-plt-got-overwrite-relro-ret2plt-ret2libc]] — Veja também: Pwndbg: Inspeção da **Global Offset Table (`got`)** e **Procedure Linkage Table (`plt`)**, Resolução Lazy Binding (`_dl_runtime_resolve`) e *ret2libc*.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.
- [[ropper-geracao-automatica-rop-chains-execve-mprotect-ret2libc]] — Referência cruzada direta com ropper-geracao-automatica-rop-chains-execve-mprotect-ret2libc.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
