---
id: software.seguranca.tranche10.000948
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

# Pwndbg: Inspeção de Estado do Processo (**`procinfo`**: UID/GID, **SELinux**, File Descriptors, Conexões), Filtros **Seccomp** e Busca **`rop` / `ropper`** em Runtime

## Em uma frase
Quando você está depurando um processo complexo (como um daemon de rede em container, um worker sandboxed com **Bubblewrap / Seccomp** ou um binário nativo em um celular Android via `gdbserver`), entender as restrições do sistema operacional sobre aquele processo é fundamental.

## Por que importa
O comando **`procinfo`** do Pwndbg lê `/proc/<pid>/status`, `/proc/<pid>/fd` e `/proc/<pid>/net` para exibir em uma única tela o PID, PPID, UID/GID efetivos, **Contexto SELinux / AppArmor**, capacidades Linux (`CapEff`), filtros Seccomp e **todos os File Descriptors abertos (incluindo arquivos, pipes e sockets TCP/UDP com IP:porta local e remota!)**!

## Como funciona
Além disso, os comandos **`rop`** e **`ropper`** integrados ao Pwndbg buscam gadgets ROP **diretamente nas páginas executáveis carregadas em tempo de execução no espaço de endereçamento real do processo** (incluindo todas as bibliotecas `.so` carregadas dinamicamente via `dlopen` que ferramentas estáticas não veem)!

## Exemplo
```gdb
# Inspecionar a identidade, contexto SELinux, capacidades e sockets abertos do processo (procinfo) e buscar gadgets ROP em runtime
pwndbg> procinfo
pwndbg> rop -- --grep "pop rdi"
```

## Limites e trade-offs
Essa busca de gadgets ROP em **Runtime (`rop` / `ropper` dentro do Pwndbg)** tem duas grandes vantagens sobre rodar a ferramenta fora do GDB: **(1)** ela já retorna os endereços reais somados com a base atual do ASLR/PIE de cada biblioteca `.so` carregada, e **(2)** ela filtra apenas páginas que o kernel realmente mapeou com permissão de execução (`r-xp`) no `vmmap`!

## Como verificar
Use `errno` no Pwndbg logo após o retorno de uma chamada de sistema ou função da `libc` para ver o código e a descrição de `errno` da thread atual.

## Conexões
- [[pwndbg-depuracao-kernel-linux-qemu-system-kchecksec-slab-pagewalk]] — Veja também: Pwndbg para **Linux Kernel Exploitation & Research (`qemu-system`)**: Comandos **`kchecksec`**, **`kversion`**, **`slab` (SLUB)**, **`buddydump`** e **`pagewalk`**.
- [[pwndbg-depuracao-binarios-go-rust-windbg-compatibility-layer]] — Veja também: Pwndbg: Depuração de Binários **Go (`go-dump`)**, Camada de Compatibilidade **WinDbg (`dd`, `dq`, `dps`, `eb`, `eq`)** e Suporte a **LLDB (`pwndbg-lldb`)**.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Referência cruzada direta com ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
