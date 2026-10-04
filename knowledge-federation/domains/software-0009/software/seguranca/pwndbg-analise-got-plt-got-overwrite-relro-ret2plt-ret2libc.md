---
id: software.seguranca.tranche10.000945
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

# Pwndbg: Inspeção da **Global Offset Table (`got`)** e **Procedure Linkage Table (`plt`)**, Resolução Lazy Binding (`_dl_runtime_resolve`) e *ret2libc*

## Em uma frase
Em binários ELF no Linux que chamam funções de bibliotecas compartilhadas (como `printf`, `puts`, `free` ou `system` da `libc.so.6`), o código chama um stub na seção **`.plt` (*Procedure Linkage Table*, somente-leitura e executável)**, que lê o endereço real da função armazenado na tabela **`.got.plt` (*Global Offset Table*)**.

## Por que importa
No Pwndbg, digitar simplesmente **`got`** (ou `got printf free`) executa uma análise completa dos símbolos dinâmicos importados: ele mostra o status de proteção **RELRO** do binário, o endereço exato de cada entrada na `.got.plt` e para onde ela aponta atualmente (quer ainda para o stub de *lazy resolution* na `.plt + 6` antes da primeira chamada, quer já para o endereço resolvido dentro da `libc.so.6`!)!

## Como funciona
Combinado com o comando **`plt`** (que lista todos os stubs `.plt` disponíveis no binário) e **`libcinfo`**, o analista tem em mãos todos os endereços necessários para diagnosticar ataques de *GOT Overwrite* (quando o binário tem *No RELRO* ou *Partial RELRO*) ou construir chamadas *ret2plt* / *ret2libc*!

## Exemplo
```gdb
# Inspecionar todas as entradas da Global Offset Table (got), listar os stubs da PLT (plt) e ver a versao/caminho da libc carregada
pwndbg> got
pwndbg> plt
pwndbg> vmmap libc
```

## Limites e trade-offs
Por que inspecionar a saída do comando **`got`** ajuda também na engenharia defensiva? Porque se `got` mostrar que os endereços de `.got.plt` residem em uma página de memória gravável (`rw-p` — *Partial RELRO*), qualquer primitiva de escrita arbitrária (*Write-What-Where*, como um Format String `%n` ou Use-After-Free) permite sobrescrever a entrada de `free@GOT` com o endereço de `system`! Ativar `-Wl,-z,relro,-z,now` (*Full RELRO*) move toda a GOT para uma página `r--p`!

## Como verificar
Verifique com `got -r` símbolos de bibliotecas carregadas além do executável principal.

## Conexões
- [[pwndbg-busca-memoria-search-leakfind-telescope-cyclic-offset]] — Veja também: Pwndbg: Introspecção de Ponteiros (**`telescope`**, **`search`**, **`leakfind`**, **`probeleak`**) e Cálculo de Offset de Buffer Overflow (**`cyclic`**).
- [[pwndbg-integracao-decompiladores-decomp2dbg-ghidra-ida-binja]] — Veja também: Pwndbg + **Ghidra / IDA / Binary Ninja (`decomp2dbg`)**: Sincronização em Tempo Real de **Código Decompilado C, Símbolos e Structs** no Terminal.
- [[ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade]] — Referência cruzada direta com ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade.

## Fontes
- [Pwndbg Official GitHub — GDB & LLDB Plug-in for Exploit Development, Reverse Engineering & Kernel Debugging](https://raw.githubusercontent.com/pwndbg/pwndbg/dev/README.md) — repositório oficial do Pwndbg cobrindo suporte dual GDB/LLDB, compatibilidade com QEMU user/system e matriz de arquiteturas; consultado em 2026-10-03.
- [Pwndbg Official Documentation — Features Overview (Context, Capstone/Unicorn Emulation, Heap Inspection, Decompiler Integration & Kernel)](https://pwndbg.re/stable/features/) — documentação oficial de funcionalidades do Pwndbg cobrindo emulação Unicorn, inspeção de heap `ptmalloc2`/`jemalloc`, `decomp2dbg`, SLUB/PageTables do kernel, `procinfo` e WinDbg; consultado em 2026-10-03.
