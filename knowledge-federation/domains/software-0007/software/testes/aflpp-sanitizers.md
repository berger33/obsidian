---
id: software.testes.tranche23.001714
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

# Sanitizers de primeira classe — e a regra de um fuzzer por tipo

## Em uma frase
O guia dedica uma seção a sanitizers com a filosofia explícita: encontrar bugs "that would not necessarily result in a crash"; a doc enumera o suporte embutido com suas variáveis — AFL_USE_ASAN (use-after-free, NULL deref, overruns), AFL_USE_MSAN (leituras de memória não inicializada), AFL_USE_UBSAN (comportamento indefinido pelo padrão C/C++), AFL_USE_CFISAN (confusão de tipos, herdeiro da detecção anti-ROP), AFL_USE_TSAN (corridas) e AFL_USE_LSAN (vazamentos, com os hooks __AFL_LEAK_CHECK e as chaves __AFL_LSAN_OFF/ON).

## Por que importa
A decisão de policy embutida na doc é econômica: sanitizers "têm enorme impacto em CPU e RAM", e um único instance com ASAN basta porque os crashes sincronizam entre fuzzeres — rodar dois targets ASAN desperdiça um core; só em corpus saturado a doc libera até metade das instâncias com sanitizer, e cita o SAND como alternativa combinando sanitizers com throughput melhor.

## Como funciona
O guia grava as pegadinhas: ASAN e MSAN não podem coexistir (e ASAN+CFISAN frequentemente também não, por esquisitice do alvo); e LSAN/MSAN sinalizam com exit codes (23 e 86) em vez de abort, que o afl-fuzz lê como crash — falsos positivos se o alvo usa esses códigos por outros motivos.

## Exemplo
Compile um alvo AFL_USE_ASAN=1 e um AFL_USE_UBSAN=1, sincronize ambos na mesma campanha e compare os artefatos: os crashes do ASAN devem aparecer por sync sem precisar de campanha dedicada, exatamente como a seção argumenta.

## Limites e trade-offs
A seção cobre os seis tipos com suporte embutido, não qualquer sanitizer LLVM; e a doc recomenda experimentar combinações por alvo — a lista de incompatibilidades é orientativa, não exaustiva.

## Como verificar
Abra a seção 1c do fuzzing_in_depth e confirme as seis variáveis, a regra por instance, a nota saturada-meia, as referências a SAND e aos exit codes 23/86.

## Conexões
- [[aflpp-instrumentation-options]] — Veja também: cmplog/redqueen, laf-intel e allowlists de instrumentação.
- [[aflpp-target-modification]] — Veja também: Ajudar o alvo a ser fuzzável: checksums off e estático on.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — índice da documentação](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md) — mapa dos guias: in-depth, binary-only, GUI, value profiling; consultado em 2026-10-03.
