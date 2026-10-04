---
id: software.seguranca.tranche06.000538
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

# Volatility 3: Detecção de Rootkits de Kernel Windows, Drivers Maliciosos (*BYOVD*), SSDT, Callbacks e Serviços (`svcscan`, `modules`, `driverscan`, `ssdt`, `callbacks`)

## Em uma frase
Ataques avançados utilizam **BYOVD** (*Bring Your Own Vulnerable Driver*) ou rootkits de kernel para desativar callbacks de telemetria de EDRs, instalar serviços ocultos ou interceptar chamadas de sistema no kernel Windows.

## Por que importa
O Volatility 3 audita a integridade do kernel Windows através de **`windows.svcscan.SvcScan`** (serviços registrados no *Service Control Manager*), **`windows.modules.Modules`** vs **`windows.driverscan.DriverScan`** (comparando a lista encadeada `PsLoadedModuleList` com objetos `_DRIVER_OBJECT` na memória física), **`windows.ssdt.SSDT`** (tabela de despacho de syscalls `KeServiceDescriptorTable`) e **`windows.callbacks.Callbacks`**.

## Como funciona
O plugin `windows.callbacks.Callbacks` lista todas as rotinas de notificação de kernel registradas via `PsSetCreateProcessNotifyRoutine`, `PsSetCreateThreadNotifyRoutine`, `PsSetLoadImageNotifyRoutine` e filtros de registro `CmRegisterCallback`: se um driver desconhecido registrou um callback ou se um atacante zerou os callbacks legítimos do agente EDR na memória do kernel, a manipulação fica evidente.

## Exemplo
```bash
# Auditar servicos, drivers carregados, tabela SSDT e callbacks de kernel em busca de BYOVD/Rootkits
vol -f /cases/memdumps/wkst-fin-09.raw windows.svcscan.SvcScan
vol -f /cases/memdumps/wkst-fin-09.raw windows.ssdt.SSDT
vol -f /cases/memdumps/wkst-fin-09.raw windows.callbacks.Callbacks
```

## Limites e trade-offs
Na tabela `windows.ssdt.SSDT` de sistemas Windows 64-bit modernos protegidos pelo *PatchGuard* (KPP), todas as entradas nativas devem apontar exclusivamente para os módulos `ntoskrnl.exe` ou `win32k.sys`; qualquer entrada apontando para um driver de terceiros ou endereço órfão indica comprometimento de kernel.

## Como verificar
Verifique na saída do `windows.ssdt.SSDT` que nenhum símbolo aponta para fora de `ntoskrnl` / `win32k` e revise todos os drivers não-Microsoft listados em `DriverScan`.

## Conexões
- [[volatility3-registro-windows-memoria-hivelist-printkey-userassist-hashdump]] — Veja também: Volatility 3: Forense de Registro Windows em Memória (`hivelist`, `printkey`, `userassist`) e Auditoria de Credenciais (`hashdump` / `lsadump`).
- [[volatility3-forense-linux-rootkits-check-syscall-modules-bash-sockstat]] — Veja também: Volatility 3: Forense de Memória Linux — Processos, Histórico `bash`, Sockets (`sockstat`) e Detecção de Rootkits LKM (`check_syscall`, `check_modules`, `check_idt`).
- [[volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline]] — Referência cruzada direta com volatility3-analise-processos-windows-pslist-pstree-psscan-cmdline.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
