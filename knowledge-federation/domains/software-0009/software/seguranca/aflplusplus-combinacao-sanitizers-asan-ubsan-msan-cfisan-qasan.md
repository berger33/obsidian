---
id: software.seguranca.tranche16.001524
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

# Potencializando a Detecção de Bugs Silenciosos no AFL++ com Sanitizers: **`AFL_USE_ASAN=1` (AddressSanitizer)**, **`AFL_USE_UBSAN=1`**, **`AFL_USE_CFISAN=1`** e **`AFL_USE_MSAN=1`**

## Em uma frase
Se o seu parser em C tiver um **Heap Buffer Overflow de 2 bytes (`off-by-one`)** ou um **Use-After-Free (`UAF`)** que sobrescreve uma região adjacente do `malloc` sem cruzar a fronteira de uma página de memória (`4 KB`) da MMU, o programa **NÃO sofrerá `SIGSEGV` (crash)**! Como fazer o AFL++ detectar instantaneamente qualquer leitura ou escrita fora dos limites de 1 único byte?

## Por que importa
Compilando o alvo com os **Sanitizers do LLVM/GCC** ativados pelas variáveis de ambiente do `afl-cc`: **`AFL_USE_ASAN=1` (*AddressSanitizer*)**, **`AFL_USE_UBSAN=1` (*UndefinedBehaviorSanitizer*)**, **`AFL_USE_MSAN=1` (*MemorySanitizer* para leitura de memória não inicializada)** e **`AFL_USE_CFISAN=1` (*Control Flow Integrity Sanitizer*)**!

## Como funciona
Quando `AFL_USE_ASAN=1` e `AFL_USE_UBSAN=1` estão ativos na compilação, o compilador cerca cada variável na stack e cada bloco no heap com *Redzones* envenenadas (*Shadow Memory*) e aborta imediatamente o programa na primeira tentativa de acesso inválido de 1 byte, integer overflow com sinal ou *double-free*, salvando a prova de conceito em `out/default/crashes/`!

## Exemplo
```bash
# Compilar o harness com AddressSanitizer (ASAN) e UndefinedBehaviorSanitizer (UBSAN) para capturar corrupcoes de memoria de 1 byte
export AFL_USE_ASAN=1
export AFL_USE_UBSAN=1
afl-clang-lto -O2 -g harness.c parser.c -o ./alvo.asan
```

## Limites e trade-offs
Por que a documentação oficial (`fuzzing_in_depth.md`) recomenda que, em uma campanha de fuzzing multicore com múltiplos processos (`-M` / `-S`), **apenas UMA instância secundária (`-S`) rode o binário com `ASAN` + `UBSAN`** enquanto as outras instâncias rodam o binário normal rápido e o CMPLOG? Porque o `AddressSanitizer` adiciona cerca de **2x de lentidão de CPU**; como todas as instâncias sincronizam seus novos caminhos descobertos entre si na pasta `-o sync_dir`, a instância ASAN testa automaticamente cada caminho novo descoberto pelas instâncias rápidas sem desacelerar o restante da frota!

## Como verificar
Atenção em sistemas 64 bits: o `ASAN` reserva ~20 Terabytes de memória virtual (*Shadow Memory*, sem usar RAM física real); por isso, o `afl-fuzz` moderno já desativa automaticamente o limite de memória virtual `-m` quando detecta `ASAN`.

## Conexões
- [[aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver]] — Veja também: Multiplicando a Velocidade em 20x no AFL++: **Persistent Mode (`__AFL_LOOP` / `LLVMFuzzerTestOneInput`)**, Memória Compartilhada (**`__AFL_INIT`**) e **Deferred Forkserver**.
- [[aflplusplus-engenharia-corpus-sementes-afl-cmin-afl-tmin-dicionarios]] — Veja também: Engenharia e Minimização de Corpus no AFL++: Destilação de Conjunto (**`afl-cmin`**), Minimização de Arquivo (**`afl-tmin`**) e Dicionários de Tokens (**`-x`** / **`AUTODICT`**).
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[aflplusplus-campanhas-paralelas-multicore-master-secondary-sync]] — Referência cruzada direta com aflplusplus-campanhas-paralelas-multicore-master-secondary-sync.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
