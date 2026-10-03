---
id: software.seguranca.tranche10.000946
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

# Pwndbg + **Ghidra / IDA / Binary Ninja (`decomp2dbg`)**: Sincronização em Tempo Real de **Código Decompilado C, Símbolos e Structs** no Terminal

## Em uma frase
Depurar um binário *stripped* (sem símbolos de depuração DWARF, onde `nm` não retorna nomes de funções) apenas lendo assembly no terminal é cansativo quando você já renomeou as funções, variáveis locais e estruturas no seu decompilador estático (**NSA Ghidra**, **IDA Pro** ou **Binary Ninja**).

## Por que importa
Conforme destacado na documentação oficial de *Features* do Pwndbg, o Pwndbg possui **Integração Nativa com Decompiladores (via `decomp2dbg`)**!

## Como funciona
Quando conectado ao **Ghidra** (ou IDA/Binary Ninja/angr-management), o Pwndbg adiciona uma nova seção **`decompiler`** diretamente ao painel `context` do terminal: a cada *step* no GDB/LLDB, o Pwndbg consulta o decompilador, resolve o endereço considerando o deslocamento do ASLR/PIE, **exibe o código C decompilado no terminal destacando a linha exata onde o `RIP`/`PC` está parado, e importa automaticamente para o GDB os nomes de funções, variáveis de stack e globais que você renomeou no Ghidra**!

## Exemplo
```gdb
# Dentro do Pwndbg: conectar ao plugin decomp2dbg rodando no Ghidra/IDA/Binary Ninja para exibir o codigo C decompilado no context
pwndbg> decomp2dbg
pwndbg> set context-sections "regs disasm decompiler code stack backtrace"
```

## Limites e trade-offs
Essa sincronização bidirecional une o melhor da análise estática (**Ghidra** reconstruindo tipos C e fluxo de controle) com a análise dinâmica (**Pwndbg** mostrando os valores reais em memória e registradores a cada instrução)!

## Como verificar
Quando o binário possuir código-fonte C/C++ ou símbolos DWARF próprios compilados com `-g`, o Pwndbg exibe automaticamente a seção `code` com realce de sintaxe sem precisar de decompilador externo.

## Conexões
- [[pwndbg-analise-got-plt-got-overwrite-relro-ret2plt-ret2libc]] — Veja também: Pwndbg: Inspeção da **Global Offset Table (`got`)** e **Procedure Linkage Table (`plt`)**, Resolução Lazy Binding (`_dl_runtime_resolve`) e *ret2libc*.
- [[pwndbg-depuracao-kernel-linux-qemu-system-kchecksec-slab-pagewalk]] — Veja também: Pwndbg para **Linux Kernel Exploitation & Research (`qemu-system`)**: Comandos **`kchecksec`**, **`kversion`**, **`slab` (SLUB)**, **`buddydump`** e **`pagewalk`**.
- [[pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto]] — Referência cruzada direta com pwndbg-arquitetura-debugger-gdb-lldb-capstone-unicorn-contexto.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
