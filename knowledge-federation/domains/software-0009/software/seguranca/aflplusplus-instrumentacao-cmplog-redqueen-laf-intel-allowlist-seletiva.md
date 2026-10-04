---
id: software.seguranca.tranche16.001522
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

# Superando Magic Bytes e Checksums no AFL++: **`AFL_LLVM_CMPLOG=1` (*Redqueen / Input-to-State*)**, **`AFL_LLVM_LAF_ALL=1`** e Instrumentação Seletiva (**`AFL_LLVM_ALLOWLIST`**)

## Em uma frase
Se uma função C começa com `if (magic == 0xdeadbeef)` ou `if (strcmp(buf, "CABECALHO_SECRETO") == 0)`, um fuzzer mutacional puro levaria bilhões de anos sorteando bytes até acertar os 4 ou 17 bytes de uma vez! Como o **AFL++** descobre e atravessa essas comparações complexas em poucos segundos?

## Por que importa
Usando a técnica **`CMPLOG` (*Redqueen / Input-to-State*), habilitada com `AFL_LLVM_CMPLOG=1`** (ou a divisão de comparações `laf-intel` via `AFL_LLVM_LAF_ALL=1`)!

## Como funciona
Como recomenda o `fuzzing_in_depth.md`: como o binário compilado com `AFL_LLVM_CMPLOG=1` registra todos os operandos de comparações (`cmp`, `memcmp`, `strcmp`, `switch`) e tem ~20% de overhead, a prática ideal é **compilar DOIS binários separados**: **(1) O binário principal rápido (`./alvo.norm`)** compilado apenas com `afl-clang-lto` e **(2) O binário auxiliar `./alvo.cmplog`** compilado com `AFL_LLVM_CMPLOG=1`, passando **`-c ./alvo.cmplog`** ao `afl-fuzz`!

## Exemplo
```bash
# Compilar um binario normal rapido e um binario dedicado CMPLOG (-c) restrito aos arquivos criticos via AFL_LLVM_ALLOWLIST
export AFL_LLVM_ALLOWLIST=./arquivos_parser.txt
afl-clang-lto -O3 harness.c parser.c -o ./alvo.norm
AFL_LLVM_CMPLOG=1 afl-clang-lto -O3 harness.c parser.c -o ./alvo.cmplog
afl-fuzz -i ./seeds -o ./out -c ./alvo.cmplog -- ./alvo.norm @@
```

## Limites e trade-offs
Veja também no exemplo acima a variável **`AFL_LLVM_ALLOWLIST=./arquivos_parser.txt`** (e sua irmã `AFL_LLVM_DENYLIST`): em programas gigantescos, você não quer que o fuzzer perca tempo explorando caminhos irrelevantes de inicialização ou CLI; colocando apenas os nomes dos arquivos ou funções (`fun: parse_packet`) no `arquivos_parser.txt`, o `afl-cc` instrumenta **exclusivamente o código que você quer auditar**, multiplicando a velocidade de execução e evitando poluição do bitmap!

## Como verificar
Para identificar estaticamente quais funções um harness consegue alcançar e gerar a `allowlist.txt` automaticamente, a documentação oficial recomenda a ferramenta parceira **`AFLplusplus/fuzz-reachability`**!

## Conexões
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Veja também: Arquitetura do **AFL++ (`AFLplusplus/AFLplusplus`)**: Fuzzing Guiado por Cobertura (*Coverage-Guided Greybox Fuzzing*), Compilador **`afl-cc`** e Modos **`LTO` (`afl-clang-lto`)**, **`LLVM`** e **`GCC_PLUGIN`**.
- [[aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver]] — Veja também: Multiplicando a Velocidade em 20x no AFL++: **Persistent Mode (`__AFL_LOOP` / `LLVMFuzzerTestOneInput`)**, Memória Compartilhada (**`__AFL_INIT`**) e **Deferred Forkserver**.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
