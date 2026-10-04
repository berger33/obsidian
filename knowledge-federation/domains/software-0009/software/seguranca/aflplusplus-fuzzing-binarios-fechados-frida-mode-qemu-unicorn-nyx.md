---
id: software.seguranca.tranche16.001527
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md", "https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fuzzing de Binários Sem Código-Fonte (**Binary-Only Targets**) no AFL++: **FRIDA Mode (`-O`)**, **QEMU Mode (`-Q`)**, **Unicorn Mode (`-U`)** e **Nyx Full-System (`-X`)**

## Em uma frase
Como usar o **AFL++** para fazer Fuzzing Guiado por Cobertura (*Coverage-Guided*) em uma biblioteca proprietária fechada (`.so` / `.dll`), em um binário ELF/Mach-O comercial sem código-fonte ou em uma rotina extraída de um firmware ARM/MIPS de roteador IoT?

## Por que importa
O AFL++ oferece a suíte mais avançada do mundo para binários fechados (`fuzzing_binary-only_targets.md`): **(1) `FRIDA Mode` (`afl-fuzz -O`)** — injeta o motor de instrumentação dinâmica `Stalker` do **Frida** diretamente no processo nativo (`x86_64`, `arm64`), suportando inclusive **Persistent Mode em binários fechados** (`AFL_FRIDA_PERSISTENT_ADDR=0x...`) e **CMPLOG (`AFL_FRIDA_CMPLOG=1`)**!

## Como funciona
**(2) `QEMU Mode` (`afl-fuzz -Q` / `qemuafl`)** — emula binários de arquiteturas diferentes (ex.: rodar um binário MIPS/ARM de roteador em um servidor `x86_64`) com `QASAN` (`AFL_USE_QASAN=1`, AddressSanitizer para binários fechados!); **(3) `Unicorn Mode` (`-U`)** para emular fragmentos de firmware bare-metal em memória; e **(4) `Nyx Mode` (`-X`)** para fuzzing de sistema inteiro com snapshots ultra-rápidos de VM KVM!

## Exemplo
```bash
# Executar fuzzing guiado por cobertura em um binario fechado sem codigo-fonte usando o FRIDA Mode (-O) em Persistent Mode
export AFL_FRIDA_PERSISTENT_ADDR=0x401250
export AFL_FRIDA_PERSISTENT_CNT=10000
afl-fuzz -O -i ./seeds -o ./out -- ./binario_proprietario @@
```

## Limites e trade-offs
Veja o poder das duas variáveis **`AFL_FRIDA_PERSISTENT_ADDR=0x401250`** e **`AFL_FRIDA_PERSISTENT_CNT=10000`** no **FRIDA Mode (`-O`)** acima: basta você abrir o binário fechado no **Ghidra** ou **Radare2**, descobrir o endereço hexadecimal `0x401250` da função interna `parse_packet()` e informar ao AFL++ — o FRIDA Mode fará um loop em memória executando apenas aquela função 10.000 vezes por fork sem precisar do código-fonte!

## Como verificar
E se o binário fechado tiver verificações de heap que você quer auditar no modo QEMU (`-Q`), ative **`export AFL_USE_QASAN=1`** (*QEMU AddressSanitizer*) para interceptar chamadas `malloc`/`free`/`memcpy` e detectar Heap Overflows e Use-After-Free mesmo sem código-fonte!

## Conexões
- [[aflplusplus-campanhas-paralelas-multicore-master-secondary-sync]] — Veja também: Escalando Campanhas Multicore no AFL++ (`-M` Principal e `-S` Secundários): Diversificando Estratégias (**`MOpt` `-L 0`**, **Power Schedules `-p`**, **`CMPLOG`** e **`ASAN`**).
- [[aflplusplus-custom-mutators-python-c-libprotobuf-mutator-structure-aware]] — Veja também: Fuzzing Consciente de Estrutura (**Structure-Aware / Grammar Fuzzing**) no AFL++: **Custom Mutators em C e Python (`AFL_CUSTOM_MUTATOR_LIBRARY` / `PYTHONPATH`)**.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
