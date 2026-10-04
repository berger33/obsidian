---
id: software.testes.tranche23.001713
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

# cmplog/redqueen, laf-intel e allowlists de instrumentação

## Em uma frase
A seção de opções de instrumentação do guia oficial descreve duas famílias: laf-intel/COMPCOV — split de comparações de inteiros, strings, floats e switches, ativado com AFL_LLVM_LAF_ALL=1 antes de compilar, "importante se você não tem um corpus bom e grande" — e o cmplog/redqueen, "usualmente melhor que laf-intel": instrumenta o alvo para reportar valores comparados, com AFL_LLVM_CMPLOG=1 na compilação e consumo via -c, avisando que usar o mesmo binário para fuzz normal e cmplog custa uns 20% de performance, melhor compilando um segundo binário cmplog apontado por -c.

## Por que importa
A distinção importa porque as técnicas têm regimes opostos de custo: laf-intel incha o binário sempre, o cmplog cobra só quando um fuzzer o usa — daí a arquitetura recomendada de dois binários, documentada explicitamente no guia.

## Como funciona
A mesma seção cobre seleção cirúrgica de instrumentação: AFL_LLVM_ALLOWLIST=arquivo instrumenta só os nomes citados (filename ou fun: função — casando foo.cpp em qualquer subpasta) e AFL_LLVM_DENYLIST exclui, com a nota de que funções inline podem não casar com as listas.

## Exemplo
Prepare allowlist com o parser que você quer atacar, recompile e confira, comparando a bitmap de um seed antes e depois do filtro, que as bordas fora do parser sumiram — é a leitura prática do que a seção descreve.

## Limites e trade-offs
Os modos de cobertura adicional referenciados (context-sensitive, n-gram, neverzero counters) são listados como "less effective" na maioria dos casos pelo próprio guia, empurrados para links de README específicos — não existem prescrições simples para eles aqui.

## Como verificar
Abra a seção 1b do fuzzing_in_depth e confirme as duas técnicas, a variável LAFL_ALL (AFL_LLVM_LAF_ALL), o trade-off dos 20%, os dois caminhos de -c e as variáveis de allow/deny com a nota de inlining.

## Conexões
- [[aflpp-compiler-modes]] — Veja também: afl-cc: a árvore de decisão LTO, LLVM e GCC_PLUGIN.
- [[aflpp-sanitizers]] — Veja também: Sanitizers de primeira classe — e a regra de um fuzzer por tipo.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
