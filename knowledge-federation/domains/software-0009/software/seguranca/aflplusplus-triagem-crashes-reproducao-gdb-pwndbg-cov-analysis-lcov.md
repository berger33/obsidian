---
id: software.seguranca.tranche16.001530
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

# Triagem de Crashes (`out/default/crashes/`), Análise de Cobertura de Código (**`AFLplusplus/cov-analysis` / `llvm-cov`**) e Reprodução no **GDB / Pwndbg**

## Em uma frase
Quando a tela do `afl-fuzz` fica vermelha indicando **`saved crashes : 14`** dentro de `out/default/crashes/` (com arquivos nomeados como `id:000000,sig:06,src:000012,time:4520,execs:189400,op:havoc,rep:4`), como deduzir quais desses 14 arquivos representam bugs distintos, reproduzir a falha no **GDB / Pwndbg** e medir visualmente quais linhas do código-fonte ainda não foram alcançadas pelo fuzzer?

## Por que importa
Primeiro: para reproduzir qualquer crash salvo em `crashes/id:000000*`, basta passá-lo para o seu binário compilado com **`ASAN` (`./alvo.asan`)** ou dentro do **GDB + Pwndbg** (`gdb --args ./alvo.asan crashes/id:000000*`), que mostrará o *stack trace* exato da linha C/C++ onde ocorreu a corrupção de memória!

## Como funciona
Segundo: conforme destacado no item 6 do `README.md` oficial do AFL++, para medir exatamente quais linhas e branches do código-fonte o seu corpus alcançou, você compila uma cópia do alvo com cobertura do compilador (`-fprofile-instr-generate -fcoverage-mapping` no Clang ou `--coverage` no GCC) e usa a ferramenta parceira **`AFLplusplus/cov-analysis`** (ou `llvm-cov show`) sobre os arquivos da fila `out/default/queue/`!

## Exemplo
```bash
# Reproduzir todos os crashes encontrados pelo AFL++ contra o binario ASAN salvando o stack trace de cada falha para deduplicacao
for crash in ./out/default/crashes/id:*; do
  echo "=== Testando $crash ==="
  ./alvo.asan "$crash" 2>&1 | grep -E "(ERROR: AddressSanitizer|SUMMARY:|#0 )"
done
```

## Limites e trade-offs
Olhe que prático o loop de triagem acima: como o relatório do **AddressSanitizer** imprime a linha padronizada `SUMMARY: AddressSanitizer: heap-buffer-overflow parser.c:142 in decode_frame`, filtrar por `SUMMARY:` e `#0` agrupa instantaneamente 50 arquivos de crash pela função e linha exatas da causa-raiz!

## Como verificar
E antes de encerrar uma auditoria de código C/C++ com o AFL++, gere sempre o relatório HTML de cobertura (`llvm-cov` / `lcov`) sobre `out/default/queue/`: se uma função crítica de autenticação aparecer com 0 execuções em vermelho no relatório de cobertura, significa que o fuzzer está parando em alguma verificação anterior (ex.: checksum ou flag de configuração) que você pode destravar com um Custom Mutator ou nova semente!

## Conexões
- [[aflplusplus-fuzzing-servicos-rede-desocketing-preeny-afl-network-proxy]] — Veja também: Como Fazer Fuzzing de **Servidores de Rede (TCP/UDP Sockets)** no AFL++: *Desocketing* com `LD_PRELOAD` (`libdesock`), Persistent Harness e Isolamento de Estado.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Referência cruzada direta com aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
