---
id: software.seguranca.tranche07.000646
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

# Radare2 (`rafind2` & `rahash2`): Caça de Padrões Binários/ROP Gadgets e Cálculo de **Entropia por Blocos** para Detecção de *Packers* e Chaves

## Em uma frase
Os utilitários **`rafind2`** e **`rahash2`** (e a família de comandos **`/`** dentro do `r2`: `/x` hex, `/R` ROP gadgets, `/c` instruções assembly, `/k` constantes criptográficas) realizam buscas binárias e análise estatística de entropia.

## Por que importa
Dados comprimidos (como seções UPX/LZMA) ou blocos cifrados/chaves criptográficas possuem alta entropia de Shannon (próxima ao máximo teórico de **`8.0` bits por byte**), enquanto código nativo x86/ARM normal tem entropia entre `5.5` e `6.5`; o comando **`rahash2 -a entropy -b 4096 -B <arquivo>`** calcula a entropia de cada bloco de 4 KB do arquivo, localizando exatamente em qual offset está o payload cifrado ou a chave RSA/AES embutida.

## Como funciona
Dentro do `r2`, o comando **`/ca`** procura automaticamente por tabelas de constantes criptográficas conhecidas (S-Boxes de AES, constantes de inicialização de SHA-256, ChaCha20 `"expand 32-byte k"`, DES e Blowfish) no binário.

## Exemplo
```bash
# Calcular entropia global do binario e localizar tabelas de constantes criptograficas (AES/SHA/ChaCha20) via r2
rahash2 -a sha256,entropy /bin/ls
r2 -q -c "/ca" /bin/ls
```

## Limites e trade-offs
Quando uma amostra de malware apresenta entropia global `> 7.2` no `rahash2 -a entropy` e pouquíssimas funções importadas no `rabin2 -i` (ex.: apenas `LoadLibraryA`, `GetProcAddress`, `VirtualAlloc` e `VirtualProtect`), trata-se quase certamente de um binário empacotado (*packed*) que deve ser desempacotado no CAPEv2 ou via debugger.

## Como verificar
Use `rafind2 -X -s "http" amostra.bin` para exibir o hexdump contextualizado de todas as ocorrências de uma string ou sequência de bytes.

## Conexões
- [[radare2-comparacao-binarios-patch-diffing-radiff2-assinaturas-zignatures]] — Veja também: Radare2 (`radiff2` & Zignatures `z`): *Patch Diffing* de Binários (`-g`, `-AC`) e Reconhecimento de Funções com **Zignatures**.
- [[radare2-montador-desmontador-rasm2-rax2-analise-shellcode]] — Veja também: Radare2 (`rasm2` & `rax2`): Montagem/Desmontagem Multi-Arquitetura de **Shellcodes** e Conversão de Representações Numéricas/Binárias.
- [[radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings]] — Referência cruzada direta com radare2-triagem-binarios-rabin2-mitigacoes-nx-canary-pie-relro-strings.
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — Referência cruzada direta com capev2-desempacotamento-dinamico-process-injection-unpacking.

## Fontes
- [Radare2 Official GitHub — Libre Reversing Framework for Unix Geeks](https://raw.githubusercontent.com/radareorg/radare2/master/README.md) — documentação oficial do Radare2 cobrindo comandos fundamentais, arquitetura de bibliotecas e ecossistema de plugins r2pm (r2ghidra, r2frida, r2yara, r2pipe); consultado em 2026-10-03.
- [Radare2 Official Manual Page — radare2(1) CLI & Reversible Debugger](https://raw.githubusercontent.com/radareorg/radare2/master/man/radare2.1) — manual oficial radare2(1) cobrindo flags de linha de comando, modo sandbox, scripts QuickJS e checkpoints de depuração reversível (dts+/dtsc/dtsr); consultado em 2026-10-03.
- [The Official Radare2 Book](https://book.rada.re/) — livro oficial do projeto Radare2 cobrindo rabin2, radiff2, rasm2, ESIL e r2pipe; consultado em 2026-10-03.
