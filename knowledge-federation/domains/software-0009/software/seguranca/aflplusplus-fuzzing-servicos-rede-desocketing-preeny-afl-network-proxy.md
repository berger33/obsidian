---
id: software.seguranca.tranche16.001529
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

# Como Fazer Fuzzing de **Servidores de Rede (TCP/UDP Sockets)** no AFL++: *Desocketing* com `LD_PRELOAD` (`libdesock`), Persistent Harness e Isolamento de Estado

## Em uma frase
Servidores de rede (como servidores DNS, HTTP, MQTT, RTSP, FTP ou daemons customizados) normalmente abrem uma porta com `socket()` -> `bind()` -> `listen()` -> `accept()` e ficam esperando conexões de rede em um loop infinito — o que impede o uso direto do `afl-fuzz` (que alimenta dados via `stdin` ou arquivo `@@` e espera o processo processar a entrada)!

## Por que importa
Como a documentação oficial do AFL++ (`best_practices.md#fuzzing-a-network-service`) recomenda adaptar um servidor de rede para rodar a dezenas de milhares de execuções por segundo no AFL++?

## Como funciona
Existem duas abordagens graduais: **(Abordagem 1 — Ideal quando você tem o código-fonte: Extrair a função de processamento do pacote/requisição para um `LLVMFuzzerTestOneInput`)**, chamando diretamente o parser de protocolo em memória sem abrir nenhum socket! E **(Abordagem 2 — Rápida sem reescrever a rede: *Desocketing* via `LD_PRELOAD` ou `AFL_PRELOAD`)**, onde uma biblioteca compartilhada intercepta as syscalls `socket()`, `bind()`, `listen()`, `accept()`, `recv()` e redireciona tudo de forma transparente para ler da entrada padrão **`stdin` (`fd 0`)**!

## Exemplo
```bash
# Executar um daemon de rede no AFL++ redirecionando as chamadas socket/accept/recv para stdin via AFL_PRELOAD (Desocketing)
export AFL_PRELOAD=/usr/local/lib/libdesock.so
afl-fuzz -i ./seeds_pacotes -o ./out -- ./servidor_protocolo --foreground
```

## Limites e trade-offs
Por que usar **`export AFL_PRELOAD=/caminho/libdesock.so`** em vez de `LD_PRELOAD` comum na linha de comando? Porque se você exportar `LD_PRELOAD`, o próprio binário `afl-fuzz` (e o shell que o invoca) também carregará a biblioteca de interceptação de sockets! Já a variável **`AFL_PRELOAD`** é aplicada pelo AFL++ **exclusivamente ao processo filho do programa alvo**!

## Como verificar
Além de `AFL_PRELOAD`, ao testar servidores de rede lembre-se de passar a flag `-f` / `--foreground` (para que o daemon não faça `daemon()` / `fork()` em background fugindo do forkserver do AFL++) e substituir geradores de números aleatórios (`rand()`/`getrandom()`) por valores fixos para manter 100% de determinismo em handshakes criptográficos!

## Conexões
- [[aflplusplus-custom-mutators-python-c-libprotobuf-mutator-structure-aware]] — Veja também: Fuzzing Consciente de Estrutura (**Structure-Aware / Grammar Fuzzing**) no AFL++: **Custom Mutators em C e Python (`AFL_CUSTOM_MUTATOR_LIBRARY` / `PYTHONPATH`)**.
- [[aflplusplus-triagem-crashes-reproducao-gdb-pwndbg-cov-analysis-lcov]] — Veja também: Triagem de Crashes (`out/default/crashes/`), Análise de Cobertura de Código (**`AFLplusplus/cov-analysis` / `llvm-cov`**) e Reprodução no **GDB / Pwndbg**.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver]] — Referência cruzada direta com aflplusplus-persistent-mode-llvm-fuzzer-test-one-input-deferred-forkserver.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
