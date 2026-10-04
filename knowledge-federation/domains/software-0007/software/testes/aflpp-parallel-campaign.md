---
id: software.testes.tranche23.001719
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Campanha paralela: um -M main, N -S variantes e o mesmo -o

## Em uma frase
A seção de múltiplos cores do guia define a topologia canônica: um main fuzzer (-M main-$HOSTNAME com AFL_FINAL_SYNC=1) e um secondary (-S nome-qualquer) por core útil, todos compartilhando o mesmo diretório -o — nomes únicos por instância, o mesmo output para todas; e a doc marca um teto por máquina, "entre 32 e 64 cores", além do qual adicionar instâncias degrada o performance global.

## Por que importa
A prescrição que transforma "vários fuzzers iguais" em campanha séria está nos heterogenizadores: cada secondary deve variar — sanitizers em um, cmplog com pelo menos um seguindo transformações via -l 2AT em um ou dois, laf-intel em um a três (com a nota de que, para compartilhar resultados intermediários, o main tem que ser um deles), e o resto distribuído entre -Z (10% no cycling antigo), AFL_DISABLE_TRIM (50-70%), -P explore (40%) versus -P exploit (20%), e -a ascii/binary em 30%/30% quando usado.

## Como funciona
Os schedules de energia fecham o leque (-p explore default, fast, coe, lin, quad, exploit, rare — com o FAQ como leitura recomendada), e a doc recomenda o cache de casos de teste por ambiente AFL_TESTCACHE_SIZE entre 50 e 500 MB "if you have the RAM", mantendo os inputs de maior probabilidade em memória; para CI, AFL_CMPLOG_ONLY_NEW, AFL_FAST_CAL e AFL_NO_STARTUP_CALIBRATION encurtam o caminho até o primeiro mutante, e AFL_IGNORE_SEED_PROBLEMS pula seeds que crasham no import.

## Exemplo
Lance uma campanha de 4 instâncias no seu alvo com main -M e três -S (um ASAN, um cmplog -c, um plain com -p fast), todos no mesmo -o; as quatro pastas de instância dentro do -o compartilham o mesmo queue, confirmando o padrão descrito na seção.

## Limites e trade-offs
A repartição percentual da doc é heurística calibrada pela experiência do time, não derivada de benchmarks fechados — o guia lista os fuzzers compatíveis de outro ecossistema (Fuzzolic, symcc, Eclipser, FairFuzz, Angora...) e o -F para sincronizar com honggfuzz e libfuzzer -entropic=1, mas não prescreve a distribuição ótima para o seu alvo.

## Como verificar
Abra a seção 3c do fuzzing_in_depth e registre: teto 32-64, topologia -M/-S com AFL_FINAL_SYNC, os percentuais -Z/TRIM/-P/-a, a lista de power schedules, as variáveis de CI e a lista de fuzzers sync-able via -F.

## Conexões
- [[aflpp-dictionaries-memory]] — Veja também: Dicionários automáticos e o limite de memória que ninguém configura.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — índice da documentação](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md) — mapa dos guias: in-depth, binary-only, GUI, value profiling; consultado em 2026-10-03.
