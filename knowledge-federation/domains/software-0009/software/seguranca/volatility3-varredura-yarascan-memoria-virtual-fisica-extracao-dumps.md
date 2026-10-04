---
id: software.seguranca.tranche06.000540
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

# Volatility 3: Caça em Memória com Regras YARA (`yarascan.YaraScan` / `windows.vadyarascan.VadYaraScan`) e Extração de Arquivos (`dumpfiles`)

## Em uma frase
O Volatility 3 integra o motor **YARA** (e `yara-x` / `yara-python`) através dos plugins **`yarascan.YaraScan`** (varredura sobre a camada de memória física/virtual completa) e **`windows.vadyarascan.VadYaraScan`** (varredura focada nos espaços de endereçamento virtual VAD dos processos, atribuindo cada match diretamente ao `PID` e processo dono).

## Por que importa
Quando um malware utiliza criptografia ou empacotamento em disco, suas strings de configuração, chaves de API, URLs de C2 e opcodes de desencriptação ficam **desencriptados em claro na memória RAM** do processo em execução; varrer as regiões VAD com YARA encontra a ameaça instantaneamente.

## Como funciona
Uma vez identificado o processo ou objeto de arquivo mapeado em cache (`_FILE_OBJECT`), os plugins **`windows.dumpfiles.DumpFiles`** (que extrai arquivos do *Cache Manager* do Windows pelo `--virtaddr`, `--physaddr` ou `--pid`) e **`windows.pslist.PsList --pid <PID> --dump`** extraem o executável desempacotado da RAM para análise estática no Ghidra/CAPEv2.

## Exemplo
```bash
# Varrer o espaco VAD dos processos Windows com um arquivo de regras YARA e extrair o processo infectado
vol -f /cases/memdumps/wkst-fin-09.raw windows.vadyarascan.VadYaraScan \
  --yara-file /opt/secops/yara/cobaltstrike_beacon_memory.yar

mkdir -p /tmp/extracted-proc
vol -o /tmp/extracted-proc -f /cases/memdumps/wkst-fin-09.raw windows.pslist.PsList --pid 4120 --dump
```

## Limites e trade-offs
Sempre prefira **`windows.vadyarascan.VadYaraScan`** (com filtro `--pid` quando possível) em vez de `yarascan.YaraScan` bruto sobre a memória física inteira: o `VadYaraScan` respeita o mapeamento virtual contíguo de cada processo (não perdendo assinaturas que cruzam fronteiras de páginas físicas fragmentadas de 4 KB) e já informa a qual `PID` pertence o match.

## Como verificar
Calcule o SHA-256 dos artefatos extraídos em `/tmp/extracted-proc/` e submeta as regras YARA sobre os dumps extraídos para confirmar a assinatura.

## Conexões
- [[volatility3-forense-linux-rootkits-check-syscall-modules-bash-sockstat]] — Veja também: Volatility 3: Forense de Memória Linux — Processos, Histórico `bash`, Sockets (`sockstat`) e Detecção de Rootkits LKM (`check_syscall`, `check_modules`, `check_idt`).
- [[volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo]] — Referência cruzada direta com volatility3-deteccao-injecao-memoria-malfind-hollowprocesses-vadinfo.
- [[capev2-desempacotamento-dinamico-process-injection-unpacking]] — Referência cruzada direta com capev2-desempacotamento-dinamico-process-injection-unpacking.

## Fontes
- [Volatility 3 Official GitHub — Volatile Memory Extraction Framework](https://raw.githubusercontent.com/volatilityfoundation/volatility3/develop/README.md) — documentação oficial do Volatility 3 cobrindo ISF symbol tables, plugins Windows/Linux/macOS e uso da CLI; consultado em 2026-10-03.
- [Volatility dwarf2json Official GitHub — Linux & macOS ISF Generator](https://raw.githubusercontent.com/volatilityfoundation/dwarf2json/master/README.md) — documentação oficial do gerador de tabelas de símbolos ISF dwarf2json a partir de DWARF e System.map; consultado em 2026-10-03.
- [Volatility Software License & Foundation Reference](https://www.volatilityfoundation.org/license/vsl-v1.0) — referência institucional da Volatility Foundation; consultado em 2026-10-03.
