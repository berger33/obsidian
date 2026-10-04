---
id: software.seguranca.tranche07.000644
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

# Radare2: Emulação Segura com **ESIL (*Evaluable Strings Intermediate Language*)** (`aei`, `aeim`, `aes`, `aeso` e `emu.str=true`)

## Em uma frase
**ESIL (*Evaluable Strings Intermediate Language*)** é a representação intermediária em notação polonesa reversa (Forth-like) do Radare2 projetada especificamente para **emular instruções de máquina passo a passo em memória virtual**, sem executar o binário real no processador host.

## Por que importa
Ao ativar **`e emu.str=true`** (ou **`e asm.emu=true`**) antes de imprimir o disassembly de uma função (`pdf`), o motor ESIL simula a execução linear das instruções e anota automaticamente ao lado de cada linha o valor calculado dos registradores, endereços de ponteiros resolvidos e strings construídas dinamicamente na pilha (*stack strings*)!

## Como funciona
Para emulação interativa controlada, a sequência **`aei`** (inicializa a VM ESIL), **`aeim`** (aloca a pilha virtual da VM), **`aeip`** (sincroniza o Program Counter do ESIL com o endereço atual) e **`aes`** (*step*) / **`aeso`** (*step over*) permite executar trechos de desofuscação de malware em qualquer arquitetura.

## Exemplo
```bash
# Ativar a anotacao de emulacao ESIL (emu.str=true) ao desmontar a funcao de entrada para resolver ponteiros calculados
r2 -q -A -e emu.str=true -c "s entry0; pd 25" /bin/ls
```

## Limites e trade-offs
A emulação ESIL ocorre inteiramente dentro de buffers de memória alocados pelo próprio `r2` (`aeim`): chamadas de sistema (`syscall`) ou chamadas para bibliotecas externas não tocam o kernel do host, tornando o ESIL 100% seguro para desofuscar shellcodes hostis.

## Como verificar
Configure `e asm.esil=true` temporariamente para visualizar a expressão ESIL exata gerada para cada instrução da arquitetura analisada.

## Conexões
- [[radare2-analise-fluxo-controle-aaa-grafos-cfg-xrefs-decompiler-pdg]] — Veja também: Radare2 (`r2`): Análise de Código (`aaa`), Grafos de Fluxo de Controle (`agf` / `agfj`), Referências Cruzadas (`axt` / `axf`) e Descompilação (`pdg`).
- [[radare2-comparacao-binarios-patch-diffing-radiff2-assinaturas-zignatures]] — Veja também: Radare2 (`radiff2` & Zignatures `z`): *Patch Diffing* de Binários (`-g`, `-AC`) e Reconhecimento de Funções com **Zignatures**.
- [[radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins]] — Referência cruzada direta com radare2-arquitetura-framework-engenharia-reversa-cli-core-plugins.
- [[ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware]] — Referência cruzada direta com ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
