---
id: software.seguranca.tranche06.000534
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md", "https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md", "https://www.volatilityfoundation.org/license/vsl-v1.0"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Volatility 3: Detecção de Injeção de Código em Memória, *Reflective DLL* e *Process Hollowing* (`malfind`, `vadinfo` e `hollowprocesses`)

## Em uma frase
Para detectar malwares *fileless* e beacons injetados na memória de processos legítimos (como `explorer.exe`, `svchost.exe` ou `lsass.exe`), o Volatility 3 inspeciona a árvore **VAD** (*Virtual Address Descriptor*) de cada processo com os plugins **`windows.malfind.Malfind`**, **`windows.vadinfo.VadInfo`** e **`windows.hollowprocesses.HollowProcesses`**.

## Por que importa
Quando um injetor aloca memória privada em outro processo via `VirtualAllocEx` com permissão **`PAGE_EXECUTE_READWRITE` (`RWX`)** (ou altera para `PAGE_EXECUTE_READ` após gravar shellcode/PE sem arquivo de imagem mapeado em disco `FileObject` associado à VAD), o `malfind` sinaliza a região, exibe o *hexdump* e o *disassembly* das primeiras instruções assembly e permite extrair o payload com `--dump`.

## Como funciona
Se os primeiros bytes da região `VAD` privada executável contiverem o cabeçalho `MZ` (`4d 5a`) e `PE` (`50 45 00 00`), ou um *stub* de salto assembly (`eb ...` / `e8 ...` / `48 89 ...`), trata-se quase certamente de uma DLL refletida ou shellcode injetado em memória.

## Exemplo
```bash
# Detectar regioes de memoria privadas executaveis (RWX) suspeitas e extrair os payloads injetados para disco
mkdir -p /tmp/malfind-dumps
vol -o /tmp/malfind-dumps -f /cases/memdumps/wkst-fin-09.raw windows.malfind.Malfind --dump
```

## Limites e trade-offs
Navegadores modernos (Chrome/Edge V8, Firefox SpiderMonkey) e runtimes `.NET` CLR / Java JVM utilizam compilação **JIT** (*Just-In-Time*), que aloca legitimamente páginas privadas `PAGE_EXECUTE_READWRITE` sem arquivo em disco; diferencie JIT legítimo de malware verificando a presença de cabeçalhos `MZ`/strings de C2 e escaneando os dumps com YARA.

## Como verificar
Inspecione os arquivos `.dmp` gerados em `/tmp/malfind-dumps` com `file` e `yara` para identificar a família exata do payload injetado.

## Conexões
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Veja também: Volatility 3: Análise de Processos Windows (`pslist`, `pstree`, `psscan`, `cmdline`, `envars` e Detecção de *DKOM*).
- [[volatility3-inspecao-dlls-handles-ldrmodules-mutants-privs]] — Veja também: Volatility 3: Auditoria de DLLs Desvinculadas (`dlllist` vs `ldrmodules`), *Handles*/Mutexes (`handles`) e Tokens (`privs` / `getsids`).
- [[volatility3-varredura-yarascan-memoria-virtual-fisica-extracao-dumps]] — Referência cruzada direta com volatility3-varredura-yarascan-memoria-virtual-fisica-extracao-dumps.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
