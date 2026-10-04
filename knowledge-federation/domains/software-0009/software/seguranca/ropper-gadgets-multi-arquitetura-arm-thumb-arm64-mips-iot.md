---
id: software.seguranca.tranche10.000957
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

# ROP Multi-Arquitetura no Ropper: Peculiaridades de Gadgets em **ARM32 / Thumb (`pop {pc}` / `bx lr`)**, **ARM64 (`AArch64` `ldp` / `ret`)** e **MIPS (`jr $ra`)**

## Em uma frase
Explorar vulnerabilidades em roteadores, câmeras IP e dispositivos móveis exige compreender que **gadgets ROP em arquiteturas RISC (`ARM`, `ARM64`, `MIPS`) são estruturalmente muito diferentes do `x86_64`** — e o Ropper modela essas diferenças nativamente na flag **`-a` (`--arch`)**!

## Por que importa
Em **ARM de 32 bits (`-a ARM` vs `-a ARMTHUMB`)**, não existe uma instrução `ret` dedicada: uma função retorna quer desempilhando valores diretamente para o contador de programa **`pop {r0, r1, r4, pc}`** (o gadget perfeito de ROP em ARM!), quer copiando o *Link Register* (`bx lr` / `mov pc, lr`). Além disso, como um processador ARM pode alternar para o conjunto de instruções **Thumb de 16 bits** simplesmente saltando para um **endereço ímpar (`endereco | 1`)**, mudar `-a ARM` para **`-a ARMTHUMB`** no Ropper revela milhares de gadgets de 2 bytes extras no mesmo binário!

## Como funciona
Em **ARM64 (`-a ARM64`)**, as instruções têm tamanho fixo de 4 bytes alinhados, os argumentos vão em `x0–x7`, e os gadgets carregam pares de registradores via **`ldp x19, x20, [sp, #16]; ldp x29, x30, [sp], #32; ret`** (onde **`x30` (`lr`)** é o registrador para onde a instrução `ret` salta!); já em **MIPS (`-a MIPS`)**, todo salto possui um **Branch Delay Slot** (a instrução localizada *após* o `jr $ra` ou `jalr $t9` é executada antes do salto se concretizar!)!

## Exemplo
```bash
# Comparar os gadgets encontrados no mesmo binario embarcado ARM32 nos modos ARM (32-bit) e ARMTHUMB (16-bit)
ropper --file /cases/iot/rootfs/usr/bin/device_daemon --arch ARM --search "pop {%pc}"
ropper --file /cases/iot/rootfs/usr/bin/device_daemon --arch ARMTHUMB --search "pop {%pc}"
```

## Limites e trade-offs
Sempre que estiver analisando um binário de 32 bits para processadores ARM (`ELF 32-bit LSB arm`), execute o Ropper **duas vezes** — uma com **`--arch ARM`** e outra com **`--arch ARMTHUMB`** (lembrando de somar `+ 1` ao endereço do gadget Thumb ao colocá-lo na pilha para ativar o bit Thumb do `CPSR`)!

## Como verificar
Combine a busca de gadgets ARM/MIPS no Ropper com a depuração dinâmica no **Pwndbg + `qemu-user`**.

## Conexões
- [[ropper-montador-desmontador-keystone-capstone-asm-disasm-strings]] — Veja também: Ropper como Canivete Suíço de Opcodes: Montagem **Keystone (`--asm`)**, Desmontagem **Capstone (`--disasm`)** e Busca de Strings/Hex (`--string`, `--section`).
- [[ropper-automacao-api-python-ropperservice-integracao-pwntools]] — Veja também: Automação de Exploits em Python com **`RopperService` (`from ropper import RopperService`)**: Busca Programática de Gadgets e Integração com Scripts.
- [[ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes]] — Referência cruzada direta com ropper-arquitetura-busca-gadgets-rop-jop-sys-capstone-filebytes.
- [[pwndbg-depuracao-cross-architecture-qemu-user-arm-mips-riscv-iot]] — Referência cruzada direta com pwndbg-depuracao-cross-architecture-qemu-user-arm-mips-riscv-iot.

## Fontes
- [Ropper Official GitHub — Multi-Architecture ROP/JOP/SYS Gadget Finder, Semantic Search (PyVEX/Z3) & Python API (`RopperService`)](https://raw.githubusercontent.com/sashs/Ropper/master/README.md) — documentação oficial completa do Ropper cobrindo formatos ELF/PE/Mach-O/Raw, 10 arquiteturas, busca semântica Z3, geradores de ROP chains, badbytes e API `RopperService`; consultado em 2026-10-03.
- [Ropper Official CLI Entrypoint & Source (`Ropper.py`)](https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py) — código-fonte oficial de inicialização do Ropper e integração com `filebytes`; consultado em 2026-10-03.
