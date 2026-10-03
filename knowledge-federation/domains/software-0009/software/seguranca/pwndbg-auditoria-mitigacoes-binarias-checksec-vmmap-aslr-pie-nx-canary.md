---
id: software.seguranca.tranche10.000942
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

# Pwndbg: Auditoria de Mitigações de Compilação (**`checksec`: RELRO, Stack Canary, NX, PIE, Fortify, CFI/CET**) e Mapeamento Virtual (**`vmmap`**, **`canary`**)

## Em uma frase
O primeiro comando executado ao abrir qualquer binário C/C++/Rust no Pwndbg é **`checksec`**, seguido de **`vmmap`** e **`canary`** (após iniciar o processo com `start`).

## Por que importa
O `checksec` inspeciona os cabeçalhos ELF (`PT_GNU_RELRO`, `PT_GNU_STACK`, `DT_BIND_NOW`, tabela de símbolos `__stack_chk_fail`) para reportar o estado das cinco defesas fundamentais do binário: **(1) RELRO** (*No / Partial / Full RELRO* — `Full RELRO` torna toda a **Global Offset Table (`.got.plt`)** somente-leitura na inicialização, bloqueando ataques de *GOT Overwrite*!), **(2) Stack Canary** (valor aleatório em `fs:0x28` no x86_64 verificado antes do `ret`), **(3) NX** (*No-eXecute* — impede execução de shellcode na stack/heap), **(4) PIE** (*Position Independent Executable* — permite que o **ASLR** randomize também o endereço base do próprio binário) e **(5) FORTIFY_SOURCE / SHSTK / IBT (Intel CET)**!

## Como funciona
Já o comando **`vmmap`** lista todas as páginas de memória virtual do processo com suas permissões exatas (`r-xp`, `rw-p`, **`rwxp`**), destacando em vermelho imediato qualquer região perigosa com permissão simultânea de **Escrita e Execução (`RWX`)**!

## Exemplo
```gdb
# Dentro do Pwndbg: auditar mitigacoes ELF (checksec), listar permissoes de paginas de memoria (vmmap) e inspecionar o Stack Canary atual
pwndbg> checksec
pwndbg> vmmap
pwndbg> canary
```

## Limites e trade-offs
O comando **`canary`** do Pwndbg localiza automaticamente o valor mestre do Stack Canary no Thread Control Block (`fs:0x28` em x86_64, sempre terminado em byte nulo `0x00` para dificultar vazamento via `strlen`/`printf`) e mostra todas as cópias dele atualmente presentes na stack!

## Como verificar
Em pipelines de CI/CD de binários C/C++ corporativos, valide sempre que todos os executáveis de produção saem compilados com `Full RELRO`, `Canary found`, `NX enabled` e `PIE enabled` (`-fPIE -pie -fstack-protector-strong -D_FORTIFY_SOURCE=3 -Wl,-z,relro,-z,now`).

## Conexões
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Veja também: **Pwndbg (`pwndbg/pwndbg`)**: Arquitetura Multi-Debugger (**GDB 12.1+ & LLDB 19+**) com Desmontagem/Emulação **Capstone + Unicorn** e Painel `context`.
- [[pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins]] — Veja também: Pwndbg para **Heap Exploitation (`glibc ptmalloc2` & `jemalloc`)**: Comandos **`heap`**, **`vis_heap_chunks` (`vis`)**, **`bins`**, **`tcache`**, **`arena`** e **`try_free`**.
- [[pwndbg-analise-got-plt-got-overwrite-relro-ret2plt-ret2libc]] — Referência cruzada direta com pwndbg-analise-got-plt-got-overwrite-relro-ret2plt-ret2libc.
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Referência cruzada direta com ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
