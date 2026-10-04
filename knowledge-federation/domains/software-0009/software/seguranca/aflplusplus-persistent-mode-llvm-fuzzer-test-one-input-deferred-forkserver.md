---
id: software.seguranca.tranche16.001523
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

# Multiplicando a Velocidade em 20x no AFL++: **Persistent Mode (`__AFL_LOOP` / `LLVMFuzzerTestOneInput`)**, Memória Compartilhada (**`__AFL_INIT`**) e **Deferred Forkserver**

## Em uma frase
Por que executar um binário tradicional via `fork()` + leitura de arquivo em disco para cada caso de teste limita o fuzzer a ~1.000–3.000 execuções por segundo (`execs/s`), enquanto um harness em **Persistent Mode + Shared Memory Testcases** no AFL++ ultrapassa facilmente **50.000 a 200.000 `execs/s` por núcleo de CPU**?

## Por que importa
Porque no modo padrão o AFL++ precisa fazer uma chamada de sistema `fork()` para cada entrada testada! Já no **Persistent Mode**, o processo filho **permanece vivo em um loop (`while (__AFL_LOOP(10000))`)** testando 10.000 entradas seguidas dentro do mesmo processo antes de reiniciar, e recebe os bytes de entrada diretamente de um ponteiro de **Memória Compartilhada (`__AFL_FUZZ_TESTCASE_BUF`)** sem nenhuma syscall `open()`/`read()` no sistema de arquivos!

## Como funciona
Melhor ainda: o compilador `afl-cc` suporta nativamente a assinatura padrão do **libFuzzer (`int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size)`)** — basta escrever essa função de 5 linhas e compilar com `afl-clang-lto` para ganhar **Persistent Mode + Shared Memory + In-Memory Fuzzing** automaticamente!

## Exemplo
```c
// Escrever um harness universal compativel com AFL++ Persistent Mode (Shared Memory) e libFuzzer usando LLVMFuzzerTestOneInput
#include <stdint.h>
#include <stddef.h>
#include "meu_parser.h"

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if (size < 4) return 0;
    parse_mensagem_rede(data, size);
    return 0;
}
```

## Limites e trade-offs
Qual cuidado fundamental você deve tomar ao escrever a função `LLVMFuzzerTestOneInput` (ou o loop `while (__AFL_LOOP(10000))`) em **Persistent Mode**? **Resetar qualquer estado global e liberar (`free`) toda memória alocada antes de retornar da função!** Se a função `parse_mensagem_rede` alterar variáveis globais de uma iteração para a outra, o comportamento deixará de ser determinístico (`stability < 90%` na tela do `afl-fuzz`); e se vazar memória a cada chamada, o processo atingirá o limite de RAM em segundos!

## Como verificar
E se você estiver fuzzando um binário existente que possui uma inicialização pesada (como carregar arquivos de configuração ou tabelas grandes) antes de ler a entrada? Basta inserir **`__AFL_INIT();`** no código logo após a inicialização pesada (**Deferred Forkserver**), para que o forkserver congele o processo no ponto exato em que já está pronto para receber os dados!

## Conexões
- [[aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva]] — Veja também: Superando Magic Bytes e Checksums no AFL++: **`AFL_LLVM_CMPLOG=1` (*Redqueen / Input-to-State*)**, **`AFL_LLVM_LAF_ALL=1`** e Instrumentação Seletiva (**`AFL_LLVM_ALLOWLIST`**).
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Veja também: Potencializando a Detecção de Bugs Silenciosos no AFL++ com Sanitizers: **`AFL_USE_ASAN=1` (AddressSanitizer)**, **`AFL_USE_UBSAN=1`**, **`AFL_USE_CFISAN=1`** e **`AFL_USE_MSAN=1`**.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost]] — Referência cruzada direta com valgrind-deteccao-memory-leaks-definitely-indirectly-possibly-lost.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
