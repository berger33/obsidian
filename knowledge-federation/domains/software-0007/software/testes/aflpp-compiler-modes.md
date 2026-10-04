---
id: software.testes.tranche23.001712
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
fontes: ["https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# afl-cc: a árvore de decisão LTO, LLVM e GCC_PLUGIN

## Em uma frase
O guia in-depth formaliza a escolha do compilador de instrumentação: um fluxo de decisão que começa em clang/clang++ 11+ (modo LTO, afl-clang-lto), cai para clang 3.8+ (modo LLVM, afl-clang-fast) e depois para gcc 5+ com suporte a plugin (GCC_PLUGIN, afl-gcc-fast), encerrando com "GAME OVER! Install gcc-plugin-dev ou llvm-dev" quando nada existe; o aviso na página é seco — afl-gcc e afl-clang puros foram removidos por obsolescência.

## Por que importa
A escolha do modo não é estética: o guia recomenda explicitamente o LLVM mais novo possível ("anything below 9 is not recommended"), e o LTO tem um pré-requisito que a mesma seção documenta — usar llvm-ar e llvm-ranlib — porque o modo opera na link-time optimization.

## Como funciona
O afl-cc é um compilador central com symlink por modo (afl-clang-fast++, afl-gcc-fast etc.), variável de ambiente AFL_CC_COMPILER=MODE ou flags --afl-MODE dentro de CFLAGS; a mesma centralidade explica por que o guia recomenda exportar AFL_QUIET=1 quando o build não tolera stderr e AFL_NOOPT=1 para a fase de configure.

## Exemplo
Instale o LLVM mais novo do seu SO e rode a árvore de decisão do guia contra seu alvo; o README da seção de instrumentação (instrumentation/README.lto.md etc., referenciada pelo guia) orienta os detalhes de cada modo.

## Limites e trade-offs
As flags AFL++-específicas de compilação não são aceitas no afl-cc comum ("no AFL++ specific command-line options... fairly broad use of environment variables") — quem vem do afl-clang legado precisa reaprender por variáveis de ambiente e -hh.

## Como verificar
Abra a seção 1a do fuzzing_in_depth (fluxo de decisão e meios de seleção de modo) e o parágrafo de nota afl-gcc/afl-clang removidos.

## Conexões
- [[aflpp-license-docker-branches]] — Veja também: Licença AGPL com harness Apache, Docker pronto e branches stable/dev.
- [[aflpp-instrumentation-options]] — Veja também: cmplog/redqueen, laf-intel e allowlists de instrumentação.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
