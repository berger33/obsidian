---
id: software.seguranca.tranche06.000537
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

# Volatility 3: Forense de Registro Windows em Memória (`hivelist`, `printkey`, `userassist`) e Auditoria de Credenciais (`hashdump` / `lsadump`)

## Em uma frase
Como o sistema operacional Windows mantém os arquivos de colmeia do Registro (*Registry Hives*: `SYSTEM`, `SOFTWARE`, `SAM`, `SECURITY`, `NTUSER.DAT`, `Amcache.hve`) mapeados e cacheados na memória RAM pelo *Configuration Manager*, o Volatility 3 pode inspecioná-los diretamente na RAM com **`windows.registry.hivelist.HiveList`**, **`windows.registry.printkey.PrintKey`** e **`windows.registry.userassist.UserAssist`**.

## Por que importa
Permite investigar chaves de persistência (`Run` / `RunServices`), serviços recém-modificados ou chaves voláteis em memória (como `HKLM\HARDWARE` ou alterações ainda não descarregadas para o disco) mesmo quando a análise é feita exclusivamente sobre um dump de RAM.

## Como funciona
Para auditoria de exposição de credenciais e resposta a incidentes, os plugins de registro (`windows.hashdump.Hashdump`, `windows.cachedump.Cachedump` e `windows.lsadump.Lsadump`) demonstram exatamente quais hashes locais SAM, credenciais de domínio cacheadas (*MSCASH2 / DCC2*) e segredos LSA estavam residentes na memória no momento da captura.

## Exemplo
```bash
# Listar todas as colmeias de Registro mapeadas na RAM e inspecionar a chave Run de persistencia
vol -f /cases/memdumps/wkst-fin-09.raw windows.registry.hivelist.HiveList
vol -f /cases/memdumps/wkst-fin-09.raw windows.registry.printkey.PrintKey \
  --key "Software\Microsoft\Windows\CurrentVersion\Run"
```

## Limites e trade-offs
Para proteger servidores Windows contra extração de credenciais da memória RAM (`lsass.exe` e LSA Secrets), habilite **Windows Defender Credential Guard** (isolamento baseado em virtualização VBS / `LsaIso.exe`) e `RunAsPPL` (*Protected Process Light* para o `lsass.exe`).

## Como verificar
Execute `windows.registry.printkey.PrintKey` apontando para o offset da colmeia `SOFTWARE` ou `NTUSER.DAT` e verifique os valores e carimbos `LastWriteTime` da chave.

## Conexões
- [[volatility3-conexoes-rede-windows-netscan-netstat-sockets]] — Veja também: Volatility 3: Reconstrução de Conexões de Rede e Sockets em Memória (`windows.netscan.NetScan` e `windows.netstat.NetStat`).
- [[volatility3-persistencia-servicos-callbacks-ssdt-drivers-windows]] — Veja também: Volatility 3: Detecção de Rootkits de Kernel Windows, Drivers Maliciosos (*BYOVD*), SSDT, Callbacks e Serviços (`svcscan`, `modules`, `driverscan`, `ssdt`, `callbacks`).
- [[volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins]] — Referência cruzada direta com volatility3-arquitetura-forense-memoria-ram-isf-symbols-plugins.
- [[impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa]] — Referência cruzada direta com impacket-extracao-credenciais-secretsdump-ntds-sam-lsa-dcsync-defesa.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
