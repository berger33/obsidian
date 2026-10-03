---
id: software.seguranca.tranche10.000947
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

# Pwndbg para **Linux Kernel Exploitation & Research (`qemu-system`)**: Comandos **`kchecksec`**, **`kversion`**, **`slab` (SLUB)**, **`buddydump`** e **`pagewalk`**

## Em uma frase
O Pwndbg não é apenas um depurador de user-space: ele possui uma suíte inteira de comandos especializados para **Depuração e Pesquisa de Vulnerabilidades no Kernel Linux** anexado à stub GDB do **QEMU (`qemu-system-x86_64 -s -S`, porta `:1234`)**!

## Por que importa
Ao conectar no kernel (`target remote :1234`), o Pwndbg oferece: **`kversion`** e **`kcmdline`** (identificam a versão exata do kernel e parâmetros de boot como `kaslr`, `smep`, `smap`, `kpti`, `pti=on`), **`kchecksec`** (audita opções de hardening de compilação `CONFIG_*` do kernel!), **`kbase`** (localiza o endereço base do texto do kernel derrotando o `KASLR` na sessão de debug), **`kmod`** (lista módulos `.ko` carregados e seus endereços) e **`ksymaddr`**!

## Como funciona
Para vulnerabilidades de corrupção de memória no kernel (que quase sempre ocorrem no alocador **SLUB** ou no **Page Allocator**), os comandos **`slab`** (`slab list`, `slab info kmalloc-cg-1k`, `slab contains <addr>`) e **`buddydump`** inspecionam em detalhes todos os caches `kmem_cache`, *freelist pointers* e páginas físicas, enquanto **`pagewalk <va>`** percorre a hierarquia de **Page Tables (`PGD -> P4D -> PUD -> PMD -> PTE`)** mostrando os bits `NX`, `RW` e `User/Supervisor` de qualquer endereço virtual!

## Exemplo
```gdb
# Conectar o Pwndbg a uma VM do Kernel Linux rodando no QEMU (-s / :1234) e auditar caches SLUB e Page Tables
pwndbg> target remote 127.0.0.1:1234
pwndbg> kversion
pwndbg> kchecksec
pwndbg> slab info kmalloc-256
pwndbg> pagewalk $rip
```

## Limites e trade-offs
Por que o comando **`pagewalk <endereco>`** é indispensável ao depurar exploits ou rootkits de kernel? Porque ele mostra os bits físicos de cada nível da tabela de páginas (incluindo se a página está marcada como `User` — relevante para **SMEP / SMAP** — ou `Write` / `NX`), permitindo verificar instantaneamente técnicas de *Page Table Manipulation* (como *Dirty Pagetable*)!

## Como verificar
Sempre adicione `nokaslr` na linha `-append` do QEMU durante a fase inicial de desenvolvimento de PoCs de kernel para facilitar breakpoints em módulos antes de testar o bypass de KASLR.

## Conexões
- [[pwndbg-integracao-decompiladores-decomp2dbg-ghidra-ida-binja]] — Veja também: Pwndbg + **Ghidra / IDA / Binary Ninja (`decomp2dbg`)**: Sincronização em Tempo Real de **Código Decompilado C, Símbolos e Structs** no Terminal.
- [[pwndbg-inspecao-estado-processo-procinfo-fds-seccomp-rop-runtime]] — Veja também: Pwndbg: Inspeção de Estado do Processo (**`procinfo`**: UID/GID, **SELinux**, File Descriptors, Conexões), Filtros **Seccomp** e Busca **`rop` / `ropper`** em Runtime.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.
- [[pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins]] — Referência cruzada direta com pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
