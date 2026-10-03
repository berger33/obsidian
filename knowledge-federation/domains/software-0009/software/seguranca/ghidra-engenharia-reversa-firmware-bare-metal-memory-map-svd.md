---
id: software.seguranca.tranche07.000637
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
fontes: ["https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md", "https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md", "https://github.com/NationalSecurityAgency/ghidra/security/advisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Ghidra: Engenharia Reversa de **Firmware Embarcado / Bare-Metal** (Descoberta de *Base Address*, *Memory Map* MMIO e Arquivos CMSIS **SVD**)

## Em uma frase
Ao contrário de executáveis Linux ELF ou Windows PE (cujos cabeçalhos informam ao Ghidra exatamente a arquitetura, o endereço base de carregamento e os segmentos), uma imagem bruta de **firmware embarcado / bare-metal** extraída de uma memória Flash SPI (`.bin`) não possui cabeçalho: cabe ao analista configurar o processador, o **Base Address** e o **Memory Map** de registradores periféricos (**MMIO**).

## Por que importa
Se um firmware ARM Cortex-M3/M4 foi compilado para rodar a partir da Flash física no endereço `0x08000000` (padrão STM32), mas for importado no Ghidra no endereço padrão `0x00000000`, todos os ponteiros absolutos para strings, tabelas de salto e funções apontarão para o vazio.

## Como funciona
Após identificar o endereço base correto (inspecionando a tabela de vetores de interrupção inicial do ARM onde a primeira word é o `Initial_SP` `0x2000xxxx` na SRAM e a segunda word é o `Reset_Handler` `0x0800xxxx | 1`), importar o arquivo **CMSIS-SVD (*System View Description*, `.svd`)** do fabricante do microcontrolador mapeia automaticamente todos os registradores de hardware (`UART`, `SPI`, `I2C`, `GPIO`, `DMA`, `CRYP`) no `Memory Map` do Ghidra.

## Exemplo
```python
# Logica em Python para estimar o Base Address de um firmware ARM Cortex-M inspecionando a Vector Table inicial
import struct

with open("/cases/firmware/stm32_dump.bin", "rb") as f:
    sp_init, reset_vec = struct.unpack("<II", f.read(8))
print(f"Initial SP (SRAM): 0x{sp_init:08x} | Reset_Handler: 0x{reset_vec & ~1:08x}")
```

## Limites e trade-offs
No ARM Cortex-M, os endereços na tabela de vetores têm o bit menos significativo (`bit 0 = 1`) ligado para indicar o modo de conjunto de instruções **Thumb**; o endereço real da função é `reset_vec & ~1`.

## Como verificar
No `Memory Map` do Ghidra, crie o segmento de SRAM (`0x20000000`, `RW` volátil) e aplique os periféricos MMIO (`0x40000000`) para que o descompilador mostre `USART1->DR` em vez de `*(volatile uint *)0x40011004`.

## Conexões
- [[ghidra-identificacao-funcoes-estaticas-functionid-fidb-bsim]] — Veja também: Ghidra: Reconhecimento de Bibliotecas Estáticas com **FunctionID (`fidb`)** e Busca Vetorial de Similaridade Comportamental com **BSim**.
- [[ghidra-emulacao-pcode-emulatorhelper-desofuscacao-strings-malware]] — Veja também: Ghidra: Emulação Segura de Código com **`EmulatorHelper`** (Execução de P-Code para Desofuscação de Strings sem Executar o Malware).
- [[ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos]] — Referência cruzada direta com ghidra-arquitetura-sre-descompilador-sleigh-pcode-projetos.
- [[radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao]] — Referência cruzada direta com radare2-emulacao-esil-desofuscacao-calculo-estado-sem-execucao.

## Fontes
- [NSA Ghidra Official GitHub — Software Reverse Engineering Framework](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/README.md) — documentação oficial do NSA Ghidra cobrindo arquitetura SRE, instalação, build e avisos de segurança; consultado em 2026-10-03.
- [NSA Ghidra Official PyGhidra Documentation — CPython 3 Integration](https://raw.githubusercontent.com/NationalSecurityAgency/ghidra/master/Ghidra/Features/PyGhidra/README.md) — documentação oficial do módulo PyGhidra para execução de scripts Ghidra nativos em CPython 3 e modo headless; consultado em 2026-10-03.
- [NSA Ghidra Official Security Advisories](https://github.com/NationalSecurityAgency/ghidra/security/advisories) — avisos oficiais de segurança e recomendações de isolamento do projeto Ghidra; consultado em 2026-10-03.
