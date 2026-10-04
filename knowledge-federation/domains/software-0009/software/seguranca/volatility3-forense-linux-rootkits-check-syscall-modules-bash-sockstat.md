---
id: software.seguranca.tranche06.000539
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

# Volatility 3: Forense de Memória Linux — Processos, Histórico `bash`, Sockets (`sockstat`) e Detecção de Rootkits LKM (`check_syscall`, `check_modules`, `check_idt`)

## Em uma frase
Em servidores Linux e nós de containers, o namespace `linux.*` do Volatility 3 permite extrair processos (`linux.pslist.PsList`, `linux.pstree.PsTree`, `linux.psaux.PsAux`), variáveis de ambiente (`linux.envars.Envars`), conexões de rede (`linux.sockstat.Sockstat`), histórico de comandos em memória da shell (`linux.bash.Bash`) e detectar **Rootkits de Kernel LKM** (*Loadable Kernel Modules*).

## Por que importa
Mesmo que um invasor execute `unset HISTFILE` ou `history -c` ou apague `~/.bash_history`, as estruturas de alocação da biblioteca GNU `readline` dentro do espaço de memória do processo `/bin/bash` frequentemente ainda retêm os comandos digitados, recuperados por `linux.bash.Bash`.

## Como funciona
Para detecção de rootkits de kernel Linux (como Diamorphine, Reptile ou variantes eBPF/ftrace), os plugins **`linux.check_syscall.Check_syscall`** (verifica se ponteiros na `sys_call_table` foram desviados para fora do texto do kernel `_stext`–`_etext`), **`linux.check_modules.Check_modules`** (compara `/sys/module` `kset` com a lista `modules` para achar LKMs ocultos), **`linux.check_idt.Check_idt`** e **`linux.check_afinfo.Check_afinfo`** identificam ganchos de ocultação.

## Exemplo
```bash
# Recuperar comandos bash da RAM, sockets ativos e verificar integridade da sys_call_table e modulos LKM no Linux
vol -f /cases/memdumps/prod-k8s-node01.lime linux.bash.Bash
vol -f /cases/memdumps/prod-k8s-node01.lime linux.sockstat.Sockstat
vol -f /cases/memdumps/prod-k8s-node01.lime linux.check_syscall.Check_syscall
vol -f /cases/memdumps/prod-k8s-node01.lime linux.check_modules.Check_modules
```

## Limites e trade-offs
Para adquirir dumps de memória RAM de servidores Linux em resposta a incidentes de forma segura e sem precisar compilar módulos de kernel na máquina comprometida, ferramentas modernas como **Microsoft AVML** (*Acquire Volatile Memory for Linux*, escrita em Rust estático usando `/dev/crash`, `/proc/kcore` ou `/dev/mem`) geram arquivos `.lime` compatíveis diretamente com o Volatility 3.

## Como verificar
Execute `linux.check_syscall.Check_syscall` e `linux.check_modules.Check_modules` e confirme que nenhuma entrada da `sys_call_table` aparece marcada como `HOOKED`.

## Conexões
- [[volatility3-persistencia-servicos-callbacks-ssdt-drivers-windows]] — Veja também: Volatility 3: Detecção de Rootkits de Kernel Windows, Drivers Maliciosos (*BYOVD*), SSDT, Callbacks e Serviços (`svcscan`, `modules`, `driverscan`, `ssdt`, `callbacks`).
- [[volatility3-varredura-yarascan-memoria-virtual-fisica-extracao-dumps]] — Veja também: Volatility 3: Caça em Memória com Regras YARA (`yarascan.YaraScan` / `windows.vadyarascan.VadYaraScan`) e Extração de Arquivos (`dumpfiles`).
- [[volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map]] — Referência cruzada direta com volatility3-geracao-simbolos-linux-macos-dwarf2json-vmlinux-system-map.
- [[auditd-regras-modulos-kernel-mount-ptrace-time-change-mac]] — Referência cruzada direta com auditd-regras-modulos-kernel-mount-ptrace-time-change-mac.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
