---
id: software.testes.tranche23.001715
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

# Ajudar o alvo a ser fuzzável: checksums off e estático on

## Em uma frase
A seção "d) Modifying the target" ensina a intervenção canônica: remover (ou neutrar) verificações que bloqueiam o fuzzer — checksums, HMAC — dentro de blocos #ifdef FUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION, definição que todos os compiladores AFL++ ligam automaticamente, permitindo o hack "só no build de fuzz" em código usado em produção.

## Por que importa
Sem isso, o mutator briga com CRC em vez de explorar o formato: a seção argumenta que "say that the checksum or HMAC was fine" destrava o fuzzing em alvos de protocolo, com o ifdef garantindo que a produção continua com verificação ativa.

## Como funciona
A seção seguinte grava a regra de ouro da instrumentação com força incomum na doc: "avoid instrumenting shared libraries at all cost" — porque exige LD_LIBRARY_PATH e pode-se acabar fazendo make install de bibliotecas instrumentadas no sistema; o guia manda sempre compilar as bibliotecas instrumentadas como estáticas e linkar no alvo, com os exemplos por build system (CC/CXX configure, cmake com afl-cc, meson antes do primeiro comando, e exeptor para sistemas alienígenas).

## Exemplo
Numa lib de parse com CRC, envolva o teste do checksum no ifdef, instrumente tudo staticamente via CC=/caminho/afl-cc ./configure --disable-shared e confirme na bitmap de cobertura do afl-fuzz que as bordas após o checksum agora aparecem no mapa.

## Limites e trade-offs
Os exemplos por build system assumem que você controla o build do alvo; o guia não fornece caminho para binários de terceiros sem fonte — para targets binários, a seção separada fuzzing_binary-only_targets.md existe exatamente para isso, nota o índice docs/README.md.

## Como verificar
Abra as seções 1d e 1e do fuzzing_in_depth: o bloco ifdef, a regra #1 sobre shared libraries, e os trechos de configure/CMake/Meson; confira o pointer do docs/README.md para fuzzing_in_depth e binary-only.

## Conexões
- [[aflpp-sanitizers]] — Veja também: Sanitizers de primeira classe — e a regra de um fuzzer por tipo.
- [[aflpp-corpus-prep]] — Veja também: Corpus primeiro: afl-cmin, afl-merge e afl-tmin em sequência.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — índice da documentação](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md) — mapa dos guias: in-depth, binary-only, GUI, value profiling; consultado em 2026-10-03.
