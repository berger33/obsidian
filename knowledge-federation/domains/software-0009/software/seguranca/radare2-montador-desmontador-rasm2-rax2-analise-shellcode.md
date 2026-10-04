---
id: software.seguranca.tranche07.000647
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/radareorg/radare2/master/README.md", "https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1", "https://book.rada.re/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Radare2 (`rasm2` & `rax2`): Montagem/Desmontagem Multi-Arquitetura de **Shellcodes** e Conversão de Representações Numéricas/Binárias

## Em uma frase
Os utilitários **`rasm2`** (montador e desmontador standalone multi-arquitetura) e **`rax2`** (calculadora e conversor de bases, endianness, strings, hex e floats) permitem inspecionar e testar *shellcodes* extraídos de exploits, PCAPs ou dumps de memória do Volatility 3 diretamente no terminal.

## Por que importa
Quando o plugin `windows.malfind` do Volatility 3 ou um alerta do Suricata captura uma sequência hexadecimal de bytes suspeitos (`fc4883e4f0e8c0000000...`), rodar `rasm2 -a x86 -b 64 -d "<hex>"` desmonta instantaneamente os bytes em instruções assembly legíveis sem precisar criar um arquivo ELF/PE.

## Como funciona
O `rasm2` suporta `-a <arch>` (`x86`, `arm`, `mips`, `ppc`, `riscv`, `avr`), `-b <bits>` (`16`, `32`, `64`), `-e` (big-endian), `-d` (disassemble), `-E` (converte as instruções para expressões **ESIL**) e `-f <arquivo>` (lê bytes binários brutos de um arquivo).

## Exemplo
```bash
# Desmontar um stub de shellcode x86-64 hexadecimal com rasm2 e converter expressoes/endianness com rax2
rasm2 -a x86 -b 64 -d "4831c05048bb2f62696e2f2f7368534889e7504889e2574889e6b03b0f05"
rax2 -S <<< "CorpSec2026"
```

## Limites e trade-offs
Para abrir um arquivo de shellcode binário bruto (`shellcode.bin`) no próprio `r2` com análise completa e grafo visual, passe a arquitetura e bits na linha de comando: **`r2 -a x86 -b 64 -A shellcode.bin`**.

## Como verificar
Verifique na saída do `rasm2` acima a reconstrução da string `/bin//sh` (`0x68732f2f6e69622f`) e a chamada `syscall` (`0f 05`) com `al = 0x3b` (`execve`).

## Conexões
- [[radare2-busca-padroes-rafind2-rahash2-entropia-secoes-empacotamento]] — Veja também: Radare2 (`rafind2` & `rahash2`): Caça de Padrões Binários/ROP Gadgets e Cálculo de **Entropia por Blocos** para Detecção de *Packers* e Chaves.
- [[radare2-automacao-scripting-r2pipe-python-javascript-qjs]] — Veja também: Radare2 (`r2pipe` & QuickJS `-j`): Automação Programática de Engenharia Reversa em Python e JavaScript Nativo.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Referência cruzada direta com radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao.
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Referência cruzada direta com volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
