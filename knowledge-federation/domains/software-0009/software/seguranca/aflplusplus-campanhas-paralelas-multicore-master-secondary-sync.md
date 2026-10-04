---
id: software.seguranca.tranche16.001526
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

# Escalando Campanhas Multicore no AFL++ (`-M` Principal e `-S` Secundários): Diversificando Estratégias (**`MOpt` `-L 0`**, **Power Schedules `-p`**, **`CMPLOG`** e **`ASAN`**)

## Em uma frase
Se você tem um servidor de 8 ou 16 núcleos para rodar uma campanha de fuzzing com o AFL++, por que rodar 8 instâncias idênticas com exatamente as mesmas opções é um desperdício do potencial do AFL++?

## Por que importa
Porque a documentação oficial (`fuzzing_in_depth.md`) ensina a **Estratégia de Frota Heterogênea Cooperativa**: todas as instâncias compartilham o mesmo diretório de sincronização `-o ./sync_dir`, sendo **uma instância Principal (`-M fuzzer01`)** e **múltiplas instâncias Secundárias (`-S fuzzer02`, `-S fuzzer03`, ...)**, onde cada instância aplica uma **combinação diferente de binário compilado, mutador e Power Schedule (`-p`)**!

## Como funciona
Veja a distribuição recomendada para 4+ núcleos: **(1) `-M main`**: binário normal rápido (`afl-clang-lto`) com `-p fast` (default); **(2) `-S cmplog`**: binário normal com `-c ./alvo.cmplog` e `-p explore`; **(3) `-S asan`**: binário compilado com `AFL_USE_ASAN=1 AFL_USE_UBSAN=1` e `-p coe`; e **(4) `-S laf_mopt`**: binário compilado com `AFL_LLVM_LAF_ALL=1`, mutador PSO **`-L 0` (*MOpt*)** e `-p lin` ou `-p quad`!

## Exemplo
```bash
# Iniciar uma campanha paralela cooperativa no mesmo diretorio ./sync_dir e monitorar o progresso consolidado com afl-whatsup
AFL_TMPDIR=/dev/shm afl-fuzz -i ./seeds -o ./sync_dir -M main -- ./alvo.norm @@ >/dev/null 2>&1 &
AFL_TMPDIR=/dev/shm afl-fuzz -i ./seeds -o ./sync_dir -S cmplog -c ./alvo.cmplog -p explore -- ./alvo.norm @@ >/dev/null 2>&1 &
AFL_TMPDIR=/dev/shm afl-fuzz -i ./seeds -o ./sync_dir -S sani -p coe -- ./alvo.asan @@ >/dev/null 2>&1 &
afl-whatsup -s ./sync_dir
```

## Limites e trade-offs
Olhe o utilitário **`afl-whatsup ./sync_dir`** (e `afl-plot` para gerar gráficos HTML de evolução!) na última linha acima: ele lê os arquivos `fuzzer_stats` de todas as instâncias `-M` e `-S` em execução e imprime um painel consolidado mostrando a soma da velocidade total (`cumulative speed`), cobertura de bitmap combinada, tempo desde o último caminho novo e total de crashes encontrados!

## Como verificar
Antes de iniciar a campanha no Linux, execute **`sudo afl-system-config`** para ajustar automaticamente o `core_pattern` e os governors de frequência de CPU (`performance`) exigidos pelo `afl-fuzz`.

## Conexões
- [[aflplusplus-engenharia-corpus-sementes-afl-cmin-afl-tmin-dicionarios]] — Veja também: Engenharia e Minimização de Corpus no AFL++: Destilação de Conjunto (**`afl-cmin`**), Minimização de Arquivo (**`afl-tmin`**) e Dicionários de Tokens (**`-x`** / **`AUTODICT`**).
- [[aflplusplus-fuzzing-binarios-fechados-frida-mode-qemu-unicorn-nyx]] — Veja também: Fuzzing de Binários Sem Código-Fonte (**Binary-Only Targets**) no AFL++: **FRIDA Mode (`-O`)**, **QEMU Mode (`-Q`)**, **Unicorn Mode (`-U`)** e **Nyx Full-System (`-X`)**.
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva]] — Referência cruzada direta com aflplusplus-instrumentacao-cmplog-redqueen-laf-intel-allowlist-seletiva.
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Referência cruzada direta com aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
