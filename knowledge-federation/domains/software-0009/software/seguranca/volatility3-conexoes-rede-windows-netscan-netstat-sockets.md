---
id: software.seguranca.tranche06.000536
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

# Volatility 3: Reconstrução de Conexões de Rede e Sockets em Memória (`windows.netscan.NetScan` e `windows.netstat.NetStat`)

## Em uma frase
Os plugins **`windows.netscan.NetScan`** e **`windows.netstat.NetStat`** extraem da memória RAM todas as conexões TCP (`ESTABLISHED`, `SYN_SENT`, `CLOSE_WAIT`, `CLOSED`), portas TCP/UDP em escuta (`LISTENING`) e o **PID**, nome do processo proprietário e carimbo de tempo de criação do socket.

## Por que importa
Enquanto um log de firewall de borda mostra apenas que o IP `10.10.5.42` conectou-se ao IP externo `198.51.100.214:443`, o `netscan`/`netstat` na memória RAM do host revela exatamente **qual processo (`PID 4120 - rundll32.exe`)** abriu aquela conexão de saída.

## Como funciona
O `windows.netstat.NetStat` percorre as tabelas de partição e listas ativas da pilha TCP/IP (`tcpip.sys`), enquanto o `windows.netscan.NetScan` varre os pools de memória física procurando por *pool tags* de objetos de rede (`TcpE`, `TcpL`, `UdpA`), conseguindo recuperar inclusive conexões TCP que acabaram de ser fechadas mas cujas estruturas ainda residem na RAM.

## Exemplo
```bash
# Extrair conexoes ativas e recem-encerradas do dump de memoria Windows com seus respectivos PIDs e processos
vol -f /cases/memdumps/wkst-fin-09.raw windows.netstat.NetStat
vol -f /cases/memdumps/wkst-fin-09.raw windows.netscan.NetScan
```

## Limites e trade-offs
Estruturas de conexões antigas recuperadas por varredura de pool (`NetScan`) podem ter campos de ponteiro parcialmente sobrescritos; valide sempre os achados cruzando o `PID` retornado com `pstree` e `NetStat`.

## Como verificar
Cruze os IPs externos e portas encontradas em `NetScan` com a aba *Intelligence* do Timesketch/MISP e anote o `PID` responsável pelo tráfego.

## Conexões
- [[volatility3-inspecao-dlls-handles-ldrmodules-mutants-privs]] — Veja também: Volatility 3: Auditoria de DLLs Desvinculadas (`dlllist` vs `ldrmodules`), *Handles*/Mutexes (`handles`) e Tokens (`privs` / `getsids`).
- [[volatility3-registro-windows-memoria-hivelist-printkey-userassist-hashdump]] — Veja também: Volatility 3: Forense de Registro Windows em Memória (`hivelist`, `printkey`, `userassist`) e Auditoria de Credenciais (`hashdump` / `lsadump`).
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Referência cruzada direta com volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline.
- [[wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap]] — Referência cruzada direta com wireshark-arquitetura-dissecadores-separacao-privilegios-dumpcap.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
