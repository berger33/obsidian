---
id: software.seguranca.tranche16.001525
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

# Engenharia e Minimização de Corpus no AFL++: Destilação de Conjunto (**`afl-cmin`**), Minimização de Arquivo (**`afl-tmin`**) e Dicionários de Tokens (**`-x`** / **`AUTODICT`**)

## Em uma frase
Se você coletar na internet 5.000 arquivos `.png` ou `.xml` de até 2 MB cada e jogá-los diretamente na pasta `-i seeds` do `afl-fuzz`, sua campanha de fuzzing será um desastre de lentidão! Como preparar e destilar matematicamente um **Corpus de Sementes (`Seed Corpus`) enxuto e de máxima cobertura** usando as ferramentas oficiais do AFL++?

## Por que importa
Aplicando o pipeline de 2 etapas documentado em `fuzzing_in_depth.md`: **(Etapa 1 — Destilação de Conjunto com `afl-cmin` / `afl-cmin.bash`)** e **(Etapa 2 — Minimização de Bytes de cada Arquivo com `afl-tmin`)**!

## Como funciona
Primeiro, o **`afl-cmin`** executa o seu binário instrumentado sobre os 5.000 arquivos candidatos e seleciona o **menor subconjunto de arquivos (ex.: 45 arquivos) que atinge exatamente os mesmos 100% de arestas de código que os 5.000 originais** (descartando 4.955 arquivos redundantes!). Segundo, o **`afl-tmin`** pega cada um dos 45 arquivos sobreviventes e **remove byte por byte tudo o que não altera o caminho de execução**, reduzindo os arquivos ao menor tamanho possível (< 1 KB)!

## Exemplo
```bash
# Destilar um conjunto de sementes redundantes com afl-cmin e minimizar os bytes de uma semente individual com afl-tmin
afl-cmin -i ./sementes_brutas -o ./sementes_unicas -- ./alvo.norm @@
for f in ./sementes_unicas/*; do
  afl-tmin -i "$f" -o "./seeds/$(basename "$f")" -- ./alvo.norm @@
done
```

## Limites e trade-offs
E quando você está auditando um protocolo baseado em texto ou gramática estruturada (como SQL, JSON, XML, HTTP, JavaScript ou PDF)? Se você compilar com **`afl-clang-lto`**, o compilador já extrai automaticamente todas as strings literais e tokens do código-fonte do programa alvo e as injeta no binário via **`AUTODICT`** — e você ainda pode passar dicionários adicionais da pasta `dictionaries/` com **`-x dictionaries/json.dict`**!

## Como verificar
Como alerta o `fuzzing_in_depth.md` na seção *Common sense risks*: configure sempre **`export AFL_TMPDIR=/ramdisk`** apontando para uma montagem `tmpfs` em RAM para evitar bilhões de escritas físicas que desgastam SSDs e reduzem a performance.

## Conexões
- [[aflplusplus-combinacao-sanitizers-asan-ubsan-msan-cfisan-qasan]] — Veja também: Potencializando a Detecção de Bugs Silenciosos no AFL++ com Sanitizers: **`AFL_USE_ASAN=1` (AddressSanitizer)**, **`AFL_USE_UBSAN=1`**, **`AFL_USE_CFISAN=1`** e **`AFL_USE_MSAN=1`**.
- [[aflplusplus-campanhas-paralelas-multicore-master-secondary-sync]] — Veja também: Escalando Campanhas Multicore no AFL++ (`-M` Principal e `-S` Secundários): Diversificando Estratégias (**`MOpt` `-L 0`**, **Power Schedules `-p`**, **`CMPLOG`** e **`ASAN`**).
- [[aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard]] — Referência cruzada direta com aflplusplus-arquitetura-coverage-guided-fuzzing-afl-cc-lto-llvm-pcguard.
- [[scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids]] — Referência cruzada direta com scapy-fuzzing-protocolos-fuzz-randfield-teste-robustez-parsers-ids.

## Fontes
- [AFL++ Official GitHub Repository (`AFLplusplus/AFLplusplus`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/README.md) — repositório oficial do fuzzer guiado por cobertura AFL++ cobrindo `afl-cc`, `afl-fuzz`, análise de cobertura e reprodução de crashes; consultado em 2026-10-03.
- [AFL++ Official In-Depth Fuzzing Guide (`docs/fuzzing_in_depth.md`)](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/docs/fuzzing_in_depth.md) — guia técnico oficial do AFL++ detalhando modos `LTO`/`LLVM`/`GCC_PLUGIN`, `AFL_LLVM_CMPLOG=1`, `AFL_LLVM_LAF_ALL=1`, `AFL_LLVM_ALLOWLIST`, Persistent Mode, `afl-cmin`/`afl-tmin` e campanhas multicore; consultado em 2026-10-03.
