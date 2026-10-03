---
id: software.seguranca.tranche10.000953
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
fontes: ["https://raw.githubusercontent.com/sashs/Ropper/master/README.md", "https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ropper: Busca Avançada de Gadgets (**`--search`**, `--quality`, **`--stack-pivot`**, `-p` `pop-pop-ret`, `-j` `jmp reg`) e Filtro de **`--badbytes` (`-b`)**

## Em uma frase
Encontrar `80.000` gadgets em uma `libc.so.6` não ajuda se o seu gadget contiver efeitos colaterais que corrompem outros registradores ou se o próprio endereço de 64 bits do gadget contiver **Bytes Proibidos (*Badbytes*)** que quebram a função de entrada vulnerável!

## Por que importa
Por exemplo: se a vulnerabilidade é em `strcpy()` (que para no byte nulo **`0x00`**), `fgets()`/`scanf()` (que param em **`0x0a` `\n`**, **`0x0d` `\r`** ou **`0x20` espaço**), qualquer gadget cujo endereço contenha `0x0a` truncará o payload no meio! Ao passar **`-b 000a0d20` (`--badbytes 000a0d20`)** ao Ropper, **todo gadget cujo endereço (considerando o `-I <imagebase>`) contenha qualquer um desses bytes é descartado automaticamente**!

## Como funciona
Na flag **`--search <padrao>`** (onde `?` casa qualquer caractere e `%` casa qualquer string, ex.: `--search "mov [%], rdx"`), adicionar **`--quality 1`** restringe a saída aos gadgets mais limpos (que realizam a operação desejada e retornam imediatamente sem efeitos colaterais em outros registradores), enquanto **`--stack-pivot`**, **`-p` (`pop reg; pop reg; ret`)** e **`-j rsp`** encontram gadgets de controle de pilha!

## Exemplo
```bash
# Buscar gadgets que carregam RDI, RSI ou RDX sem conter badbytes (0x00, 0x0a, 0x0d) e com qualidade maxima (--quality 1)
ropper --file /cases/pwn/libc.so.6 \
  -I 0x00007ffff7c00000 \
  --badbytes 000a0d \
  --quality 1 \
  --search "pop r?i"
```

## Limites e trade-offs
Quando um overflow na stack é curto demais para caber uma ROP chain inteira (mas você controla um buffer maior na heap ou `.bss`), execute **`ropper --file binario --stack-pivot`** para listar todos os gadgets que movem ou trocam o registrador `rsp`/`esp` (`xchg rax, rsp; ret`, `leave; ret`, `mov rsp, rbp; ret`) para a nova pilha controlada!

## Como verificar
Use `--opcode ffe4` (com suporte a curingas `?`, ex.: `ffe?`) quando quiser buscar diretamente pelos bytes de máquina da instrução.

## Conexões
- [[ropper-inspecao-cabecalhos-mitigacoes-sec-nx-aslr-cfg-pe-elf]] — Veja também: Ropper: Inspeção de Cabeçalhos Binários (**`-i`, `-e`, `--imagebase`, `-s`, `-S`, `--imports`, `--symbols`**) e Filtro **Microsoft Control Flow Guard (`--cfg-only`)**.
- [[ropper-busca-semantica-pyvex-z3-solver-restricoes-registradores]] — Veja também: Ropper **`--semantic` (`PyVEX` + `Z3 Theorem Prover`)**: Busca Semântica de Gadgets por Efeito Matemático e Preservação de Registradores (`!reg`).
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Referência cruzada direta com ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes.
- [[pwndbg-busca-memoria-search-leakfind-telescope-cyclic-offset]] — Referência cruzada direta com pwndbg-busca-memoria-search-leakfind-telescope-cyclic-offset.

## Fontes
- [Ropper Official GitHub — Multi-Architecture ROP/JOP/SYS Gadget Finder, Semantic Search (PyVEX/Z3) & Python API (`RopperService`)](https://raw.githubusercontent.com/sashs/Ropper/master/README.md) — documentação oficial completa do Ropper cobrindo formatos ELF/PE/Mach-O/Raw, 10 arquiteturas, busca semântica Z3, geradores de ROP chains, badbytes e API `RopperService`; consultado em 2026-10-03.
- [Ropper Official CLI Entrypoint & Source (`Ropper.py`)](https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py) — código-fonte oficial de inicialização do Ropper e integração com `filebytes`; consultado em 2026-10-03.
