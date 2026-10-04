---
id: software.seguranca.tranche16.001521
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

# Arquitetura do **AFL++ (`AFLplusplus/AFLplusplus`)**: Fuzzing Guiado por Cobertura (*Coverage-Guided Greybox Fuzzing*), Compilador **`afl-cc`** e Modos **`LTO` (`afl-clang-lto`)**, **`LLVM`** e **`GCC_PLUGIN`**

## Em uma frase
Por que o **AFL++ (`American Fuzzy Lop plus plus`)** se tornou o fuzzer guiado por cobertura padrão da indústria de segurança (e referência no Google FuzzBench) para encontrar vulnerabilidades críticas de corrupção de memória (`Heap Overflow`, `Use-After-Free`, `Integer Overflow`) em código C, C++ e Rust FFI?

## Por que importa
Como explica a documentação oficial (`fuzzing_in_depth.md`), diferente de um fuzzer cego (*blackbox*) que joga dados aleatórios na entrada sem saber o que aconteceu dentro do programa, o **AFL++ instrumenta cada aresta do grafo de fluxo de controle (*Edge Coverage*) durante a compilação usando o compilador unificado `afl-cc`**!

## Como funciona
A árvore de decisão oficial para escolher o modo do `afl-cc` é direta: **(1) Se você tem `clang/clang++ 11+`, use o Modo `LTO` (`afl-clang-lto` / `afl-clang-lto++`)** — como a instrumentação acontece na hora do link (*Link-Time Optimization*), o modo `LTO` atribui um ID único para cada aresta com **zero colisões de hash no bitmap de cobertura**!; **(2) Caso contrário (`clang 3.8+`), use o Modo `LLVM` (`afl-clang-fast` com `PCGUARD`)**; e **(3) Se só tiver GCC (`gcc 5+`), use o Modo `GCC_PLUGIN` (`afl-gcc-fast`)**!

## Exemplo
```bash
# Compilar uma biblioteca/programa alvo C/C++ com instrumentacao livre de colisoes (afl-clang-lto) e linkagem estatica (--disable-shared)
export CC=afl-clang-lto
export CXX=afl-clang-lto++
./configure --disable-shared
make clean all
```

## Limites e trade-offs
Por que o guia oficial (`README.md`) recomenda sempre passar **`--disable-shared`** no `./configure` ao compilar bibliotecas C/C++ para o AFL++? Porque se o binário de teste carregar uma versão `.so` dinâmica pré-instalada em `/usr/lib/` (que não foi compilada com `afl-cc`!), o AFL++ ficará completamente cego para os branches dentro da biblioteca! Ao compilar estaticamente (`--disable-shared`), 100% do código da biblioteca é instrumentado dentro do binário do harness!

## Como verificar
Lembre-se do aviso importante em `fuzzing_in_depth.md`: os antigos wrappers `afl-gcc` e `afl-clang` (baseados em montagem assembly antiga) foram removidos por obsolescência; use sempre `afl-cc` (`afl-clang-lto` ou `afl-clang-fast`).

## Conexões
- [[aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva]] — Veja também: Superando Magic Bytes e Checksums no AFL++: **`AFL_LLVM_CMPLOG=1` (*Redqueen / Input-to-State*)**, **`AFL_LLVM_LAF_ALL=1`** e Instrumentação Seletiva (**`AFL_LLVM_ALLOWLIST`**).
- [[aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver]] — Referência cruzada direta com aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver.
- [[valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits]] — Referência cruzada direta com valgrind-arquitetura-instrumentacao-binaria-vex-ir-memcheck-valid-bits.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
