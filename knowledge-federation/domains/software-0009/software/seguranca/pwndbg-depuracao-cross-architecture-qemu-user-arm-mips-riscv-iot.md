---
id: software.seguranca.tranche10.000950
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

# Pwndbg + **`qemu-user` (`qemu-arm`, `qemu-aarch64`, `qemu-mipsel`, `qemu-riscv64`)**: Depuração de Binários **IoT e Firmware Embarcado** em Estações `x86_64`

## Em uma frase
Como depurar dinamicamente no seu computador Linux `x86_64` um binário `httpd` ou `upnpd` extraído do firmware de um roteador **MIPS**, de uma câmera IP **ARM32** ou de um controlador industrial **RISC-V**?

## Por que importa
Combinando a emulação de espaço de usuário do **QEMU (`qemu-mipsel-static`, `qemu-arm-static`, `qemu-aarch64-static`, `qemu-riscv64-static`, versão 8.1+)** na flag **`-g <porta>`** com o **`pwndbg` (compilado com `gdb-multiarch`)**!

## Como funciona
Quando você inicia o binário do firmware com `qemu-arm-static -L ./squashfs-root -g 1234 ./squashfs-root/usr/sbin/httpd` e conecta o Pwndbg com `target remote 127.0.0.1:1234`, o Pwndbg utiliza a **API `vFile` do QEMU 8.1+** para reconstruir o `vmmap`, detecta automaticamente a arquitetura (`ARM` / `Thumb` / `MIPS` / `AArch64` / `RISC-V`) no motor Capstone/Unicorn e exibe todos os registradores (`$r0–$r15`, `$lr`, `$pc`, `$sp` ou `$a0–$a7`, `$ra`) e argumentos de função no painel `context`!

## Exemplo
```bash
# Terminal 1: Emular um binario ARM64 extraido de um firmware IoT com qemu-aarch64 aguardando o Pwndbg na porta 1234
qemu-aarch64-static -L /cases/iot/rootfs -g 1234 /cases/iot/rootfs/usr/bin/device_daemon

# Terminal 2: Conectar o Pwndbg ao gdbstub do qemu-user e iniciar a analise dinamica multi-arquitetura
pwndbg -q /cases/iot/rootfs/usr/bin/device_daemon -ex "target remote 127.0.0.1:1234"
```

## Limites e trade-offs
Observe na tabela oficial de compatibilidade do Pwndbg: utilize sempre **QEMU 8.1 ou superior** ao depurar com `qemu-user`, pois versões antigas do QEMU não expunham a API `vFile` necessária para que o comando `vmmap` do Pwndbg leia os mapas de memória do processo emulado.

## Como verificar
Para binários ARM de 32 bits que alternam entre modo **ARM (32-bit)** e modo **Thumb (16-bit)** via `bx` / `blx`, o Pwndbg inspeciona automaticamente o bit `T` do registrador `CPSR` para desmontar o conjunto de instruções correto.

## Conexões
- [[pwndbg-depuracao-binarios-go-rust-windbg-compatibility-layer]] — Veja também: Pwndbg: Depuração de Binários **Go (`go-dump`)**, Camada de Compatibilidade **WinDbg (`dd`, `dq`, `dps`, `eb`, `eq`)** e Suporte a **LLDB (`pwndbg-lldb`)**.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Referência cruzada direta com ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
