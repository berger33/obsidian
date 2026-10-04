---
id: software.seguranca.tranche10.000949
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

# Pwndbg: Depuração de Binários **Go (`go-dump`)**, Camada de Compatibilidade **WinDbg (`dd`, `dq`, `dps`, `eb`, `eq`)** e Suporte a **LLDB (`pwndbg-lldb`)**

## Em uma frase
Engenheiros de segurança modernos frequentemente precisam depurar binários compilados em **Go** (que usam convenções próprias de stack, fat-pointers de `slice` `{ptr, len, cap}` e `map` complexos em runtime sem seguir a ABI C tradicional) ou transitam entre ambientes Windows (**WinDbg**) e Linux/macOS (**GDB / LLDB**).

## Por que importa
O Pwndbg oferece suporte dedicado à **Depuração de Go**: ele interpreta os metadados de tipos embutidos pelo compilador Go para fazer dump legível de `slices`, `strings`, `structs` e `maps` complexos da linguagem Go!

## Como funciona
E para pesquisadores acostumados com a sintaxe clássica do **WinDbg** no Windows, o Pwndbg implementa uma **Camada Completa de Compatibilidade WinDbg**: você pode digitar diretamente comandos como **`dd`** (*display dwords*), **`dq`** (*display qwords*), **`dps`** (*display pointers and symbols*), **`da`/`du`** (*display ASCII/Unicode*) e **`eb`/`ed`/`eq`** (*enter/write bytes, dwords, qwords* na memória, ex.: `eb $rip 90` para escrever um `NOP`)!

## Exemplo
```gdb
# Usar comandos estilo WinDbg dentro do Pwndbg para inspecionar ponteiros/simbolos na stack (dps) e qwords (dq)
pwndbg> dps $rsp 10
pwndbg> dq $rdi 8
```

## Limites e trade-offs
Além do `pwndbg` sobre GDB no Linux, o executável **`pwndbg-lldb`** traz a mesma interface, o mesmo painel `context` e os mesmos comandos para o **LLDB 19+**, permitindo depurar binários **Mach-O nativos no macOS (Apple Silicon `arm64` / `x86_64`)** e targets iOS sem precisar reaprender comandos verbosos do LLDB!

## Como verificar
Consulte o guia `pwndbg` (que lista todos os comandos agrupados por categoria) ou `help <comando>` a qualquer momento.

## Conexões
- [[pwndbg-inspecao-estado-processo-procinfo-fds-seccomp-rop-runtime]] — Veja também: Pwndbg: Inspeção de Estado do Processo (**`procinfo`**: UID/GID, **SELinux**, File Descriptors, Conexões), Filtros **Seccomp** e Busca **`rop` / `ropper`** em Runtime.
- [[pwndbg-depuracao-cross-architecture-qemu-user-arm-mips-riscv-iot]] — Veja também: Pwndbg + **`qemu-user` (`qemu-arm`, `qemu-aarch64`, `qemu-mipsel`, `qemu-riscv64`)**: Depuração de Binários **IoT e Firmware Embarcado** em Estações `x86_64`.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
