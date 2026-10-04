---
id: software.seguranca.tranche06.000535
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

# Volatility 3: Auditoria de DLLs Desvinculadas (`dlllist` vs `ldrmodules`), *Handles*/Mutexes (`handles`) e Tokens (`privs` / `getsids`)

## Em uma frase
Para investigar como um processo interage com o sistema e detectar técnicas furtivas de ocultação de bibliotecas no espaço de usuário (*PEB Unlinking*), o Volatility 3 disponibiliza **`windows.dlllist.DllList`**, **`windows.ldrmodules.LdrModules`**, **`windows.handles.Handles`**, **`windows.privs.Privs`** e **`windows.getsids.GetSids`**.

## Por que importa
O comando `dlllist` lê as três listas duplamente encadeadas na **PEB** (*Process Environment Block* no userland: `InLoadOrderLinks`, `InMemoryOrderLinks`, `InInitializationOrderLinks`). Como a PEB fica na memória do próprio processo, um malware pode remover sua DLL dessas três listas; porém, o plugin **`ldrmodules`** cruza a PEB contra as estruturas **VAD** do kernel (que o userland não pode falsificar), exibindo `False` nas três colunas da PEB quando uma DLL mapeada foi ocultada.

## Como funciona
Já o plugin `windows.handles.Handles` lista todos os arquivos abertos, chaves de registro, processos, threads e **Mutants (Mutexes)** (excelentes indicadores de famílias de malware), enquanto `windows.privs.Privs` revela quais privilégios de token (`SeDebugPrivilege`, `SeImpersonatePrivilege`, `SeTcbPrivilege`) foram habilitados.

## Exemplo
```bash
# Comparar listas da PEB contra a arvore VAD do kernel (ldrmodules) e listar apenas Mutexes do processo suspeito
vol -f /cases/memdumps/wkst-fin-09.raw windows.ldrmodules.LdrModules --pid 4120
vol -f /cases/memdumps/wkst-fin-09.raw windows.handles.Handles --pid 4120 | grep Mutant
```

## Limites e trade-offs
Note que o próprio executável principal do processo (`.exe`) normalmente aparece com `InInit = False` no `ldrmodules` (pois o `.exe` não tem rotina `DllMain` de inicialização de DLL); o sinal clássico de DLL oculta ou injetada é uma biblioteca que aparece na VAD com **`InLoad = False`, `InInit = False` e `InMem = False`** simultaneamente.

## Como verificar
Verifique na saída do `LdrModules` qualquer região mapeada cujo caminho ou presença nas três listas da PEB seja `False False False`.

## Conexões
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Veja também: Volatility 3: Detecção de Injeção de Código em Memória, *Reflective DLL* e *Process Hollowing* (`malfind`, `vadinfo` e `hollowprocesses`).
- [[volatility3-conexoes-rede-windows-netscan-netstat-sockets]] — Veja também: Volatility 3: Reconstrução de Conexões de Rede e Sockets em Memória (`windows.netscan.NetScan` e `windows.netstat.NetStat`).
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Referência cruzada direta com volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
