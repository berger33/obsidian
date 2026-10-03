---
id: software.seguranca.tranche10.000941
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

# **Pwndbg (`pwndbg/pwndbg`)**: Arquitetura Multi-Debugger (**GDB 12.1+ & LLDB 19+**) com Desmontagem/Emulação **Capstone + Unicorn** e Painel `context`

## Em uma frase
**Pwndbg** (`pwndbg/pwndbg`, licença MIT, originalmente criado por Zach Riggle) é o plug-in modular em Python 3 para **GDB (`pwndbg`) e LLDB (`pwndbg-lldb`)** projetado especificamente para pesquisa de vulnerabilidades de corrupção de memória, engenharia reversa de binários nativos (ELF, Mach-O, firmware embarcado) e depuração do kernel Linux (`qemu-system`).

## Por que importa
Enquanto projetos legados (`gdbinit`, `peda.py`, `gef.py`) eram scripts monolíticos em um único arquivo, o Pwndbg possui uma arquitetura limpa com tipagem estática que integra os motores **Capstone** (desmontagem multi-arquitetura) e **Unicorn Engine** (emulação de CPU em tempo real!).

## Como funciona
A cada parada do depurador (*breakpoint* ou *single-step*), o comando **`context`** imprime um painel unificado e colorido por tipo de memória (código executável, heap, stack, RWX) exibindo **Registradores (com desreferenciação recursiva de ponteiros *telescope*)**, **Disassembly anotado com emulação de saltos e argumentos de funções**, **Stack**, **Backtrace** e **Expressões Monitoradas (`contextwatch`)**!

## Exemplo
```bash
# Iniciar o Pwndbg sobre um binario ELF local, verificar as mitigacoes de compilacao (checksec) e parar em main
pwndbg -q /cases/pwn/vuln_service -ex "checksec" -ex "start"
```

## Limites e trade-offs
Por que a emulação integrada do **Unicorn Engine** no painel Disassembly do Pwndbg muda o jogo durante o single-stepping? Porque antes mesmo de você executar uma instrução de desvio condicional (`je`, `jne`, `b.eq`), de tabela de saltos (`jmp rax`) ou uma cadeia **ROP (`ret`)**, o Pwndbg emula as próximas instruções em background, avalia as flags da CPU e **mostra visualmente se o salto será tomado ou não e quais argumentos (`rdi`, `rsi`, `rdx`) estão sendo passados para `memcpy`, `strcpy` ou `syscall`**!

## Como verificar
Divida as seções do `context` em múltiplos painéis do `tmux` usando o comando `contextoutput` ou ative o modo nativo GDB TUI com `layout pwndbg`.

## Conexões
- [[pwndbg-auditoria-mitigacoes-binarias-checksec-vmmap-aslr-pie-nx-canary]] — Veja também: Pwndbg: Auditoria de Mitigações de Compilação (**`checksec`: RELRO, Stack Canary, NX, PIE, Fortify, CFI/CET**) e Mapeamento Virtual (**`vmmap`**, **`canary`**).
- [[pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins]] — Referência cruzada direta com pwndbg-inspecao-heap-glibc-ptmalloc2-vis-bins-tcache-fastbins.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
