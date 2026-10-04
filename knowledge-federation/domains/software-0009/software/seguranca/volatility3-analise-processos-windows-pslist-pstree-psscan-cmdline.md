---
id: software.seguranca.tranche06.000533
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

# Volatility 3: Análise de Processos Windows (`pslist`, `pstree`, `psscan`, `cmdline`, `envars` e Detecção de *DKOM*)

## Em uma frase
A triagem inicial de um dump de memória Windows no Volatility 3 compara a lista duplamente encadeada ativa de processos do kernel (`windows.pslist.PsList` e `windows.pstree.PsTree`) com a varredura física de estruturas `_EPROCESS` na memória (`windows.psscan.PsScan`) e os argumentos de execução (`windows.cmdline.CmdLine`).

## Por que importa
Rootkits de kernel que utilizam **DKOM** (*Direct Kernel Object Manipulation*) desvinculam os ponteiros `Flink`/`Blink` da estrutura `_EPROCESS` na lista `ActiveProcessLinks` para ocultar o processo malicioso do Gerenciador de Tarefas e do `pslist`; porém, como a estrutura `_EPROCESS` precisa continuar na RAM para que suas threads sejam agendadas, o `psscan` a encontra.

## Como funciona
Cruzar `pstree` (hierarquia pai-filho `PPID -> PID`, timestamps de criação/saída e caminhos de imagem) com `cmdline` e `envars` revela imediatamente anomalias clássicas de intrusão, como `w3wp.exe` (IIS) ou `sqlservr.exe` gerando `cmd.exe` / `powershell.exe -enc ...`, ou `svchost.exe` rodando fora de `C:\Windows\System32\` e sem ter `services.exe` como pai.

## Exemplo
```bash
# Exportar arvore de processos, varredura fisica de _EPROCESS e linhas de comando em JSON para cruzamento
vol -r json -f /cases/memdumps/wkst-fin-09.raw windows.pstree.PsTree > /tmp/pstree.json
vol -r json -f /cases/memdumps/wkst-fin-09.raw windows.psscan.PsScan > /tmp/psscan.json
vol -f /cases/memdumps/wkst-fin-09.raw windows.cmdline.CmdLine
```

## Limites e trade-offs
Um processo que aparece em `psscan` mas não em `pslist` pode ser tanto um processo encerrado recentemente cuja memória ainda não foi sobrescrita (`ExitTime` preenchido) quanto um processo ativo oculto por DKOM (`ExitTime` zerado/inválido com threads ativas).

## Como verificar
Compare os conjuntos de PIDs ativos (`ExitTime == N/A`) entre `/tmp/psscan.json` e `/tmp/pstree.json` para confirmar ausência de ocultação DKOM.

## Conexões
- [[volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map]] — Veja também: Volatility 3: Geração de Tabelas de Símbolos **ISF** para Kernels Linux e macOS com `dwarf2json`.
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Veja também: Volatility 3: Detecção de Injeção de Código em Memória, *Reflective DLL* e *Process Hollowing* (`malfind`, `vadinfo` e `hollowprocesses`).
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.
- [[volatility3-inspecao-dlls-handles-ldrmodules-mutants-privs]] — Referência cruzada direta com volatility3-inspecao-dlls-handles-ldrmodules-mutants-privs.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
