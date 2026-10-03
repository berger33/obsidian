---
id: software.seguranca.tranche10.000951
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

# **Ropper (`sashs/Ropper`)**: Arquitetura Multi-Formato (**ELF, PE, Mach-O, Raw**) e Busca de Gadgets **ROP, JOP e SYS** sobre **Capstone & `filebytes`**

## Em uma frase
Quando um binário nativo possui a mitigação **NX (*No-eXecute* / DEP)** habilitada, um atacante que controla a pilha (*Stack Buffer Overflow*) não pode simplesmente saltar para um shellcode injetado na stack porque as páginas de dados estão marcadas como não-executáveis (`rw-p`). A técnica padrão para reutilizar código já existente nas páginas executáveis (`r-xp`) do binário ou da `libc` é a **Programação Orientada a Retorno (*Return-Oriented Programming* — ROP)**.

## Por que importa
Criado por Sascha Schirra (`sashs/Ropper`, licença GPLv3), o **Ropper** é um analisador binário e buscador de gadgets escrito em Python sobre a biblioteca **`filebytes`** (que faz parsing nativo de **ELF, PE, Mach-O e arquivos Raw de firmware**) e o motor de desmontagem **Capstone Framework**.

## Como funciona
O Ropper suporta **10 arquiteturas de CPU** (`x86`, `x86_64`, `ARM`, `ARMTHUMB`, `ARM64`, `MIPS`, `MIPS64`, `PPC`, `PPC64`, `SPARC64`) e classifica as sequências encontradas em três tipos selecionáveis por **`--type`**: **`rop`** (gadgets terminados em instruções de retorno como `ret` / `ret imm`), **`jop`** (*Jump-Oriented Programming*, terminados em `jmp reg` / `call reg`) e **`sys`** (terminados em instruções de chamada de sistema como `syscall` / `int 0x80` / `svc #0`)!

## Exemplo
```bash
# Listar todos os gadgets ROP e SYS de ate 5 instrucoes (--inst-count 5) em um binario ELF x86_64
ropper --file /cases/pwn/vuln_service --type rop --inst-count 5
```

## Limites e trade-offs
Como o Ropper encontra gadgets que nem sequer existiam no código assembly original em arquiteturas de instruções de tamanho variável como `x86` e `x86_64`? Ele localiza cada byte `0xc3` (`ret`) na seção `.text` e desmonta de trás para frente deslocando byte a byte (incluindo *unaligned instructions* no meio de outras instruções legítimas)!

## Como verificar
Use `--clear-cache` se o arquivo binário em disco tiver sido recompilado e você quiser forçar o Ropper a reindexar os gadgets.

## Conexões
- [[ropper-inspecao-cabecalhos-mitigacoes-sec-nx-aslr-cfg-pe-elf]] — Veja também: Ropper: Inspeção de Cabeçalhos Binários (**`-i`, `-e`, `--imagebase`, `-s`, `-S`, `--imports`, `--symbols`**) e Filtro **Microsoft Control Flow Guard (`--cfg-only`)**.
- [[ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade]] — Referência cruzada direta com ropper-busca-avancada-gadgets-ppr-stack-pivot-badbytes-qualidade.
- [[pwndbg-inspecao-estado-processo-procinfo-fds-seccomp-rop-runtime]] — Referência cruzada direta com pwndbg-inspecao-estado-processo-procinfo-fds-seccomp-rop-runtime.

## Fontes
- [Ropper Official GitHub — Multi-Architecture ROP/JOP/SYS Gadget Finder, Semantic Search (PyVEX/Z3) & Python API (`RopperService`)](https://raw.githubusercontent.com/sashs/Ropper/master/README.md) — documentação oficial completa do Ropper cobrindo formatos ELF/PE/Mach-O/Raw, 10 arquiteturas, busca semântica Z3, geradores de ROP chains, badbytes e API `RopperService`; consultado em 2026-10-03.
- [Ropper Official CLI Entrypoint & Source (`Ropper.py`)](https://raw.githubusercontent.com/sashs/Ropper/master/Ropper.py) — código-fonte oficial de inicialização do Ropper e integração com `filebytes`; consultado em 2026-10-03.
