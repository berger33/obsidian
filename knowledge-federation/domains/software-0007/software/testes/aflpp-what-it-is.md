---
id: software.testes.tranche23.001710
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
fontes: ["https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AFL++: o fork superior ao AFL do Google, na série 5.03c

## Em uma frase
O README oficial se define como "a superior fork to Google's AFL — more speed, more and better mutations, more and better instrumentation, custom module support", mantém numeração de release (5.03c na página atual, com página de Releases) e credita a manutenção a Marc Heuse, Dominik Maier, Andrea Fioraldi e Heiko Eissfeldt, com o AFL original de Michal Zalewski.

## Por que importa
Fuzzing dirigido por cobertura é um campo onde a versão importa — o modo AFL++ para benchmarks do fuzzbench do Google (afl-clang-fast com AFL_LLVM_CMPLOG=1) existe porque o fork concentra as melhorias que depois são comparadas academicamente.

## Como funciona
O quick start do README fixa o fluxo mínimo em sete passos: compilar o alvo com afl-cc, obter inputs válidos (e dicionário para sintaxes verbosas como SQL e HTTP), rodar afl-fuzz com -i seeds -o saída e @@ para arquivo, investigar o vermelho na UI pela doc de status, tratar crashes e hangs em crashes/ e hangs/, usar as ferramentas parceiras de cobertura e — enfático — ler o fuzzing_in_depth para fuzzar de verdade.

## Exemplo
Compare a lista de features do README com a nota de comparação do fuzzbench: a prescrição para benchmarks (afl-clang-fast mais CMPLOG) revela as opções que o próprio time considera mais determinantes.

## Limites e trade-offs
O texto de "superior" é autoavaliação do mantenedor, não medida independente; e o guia abre a seção 0 com "common sense risks" — a doc avisa explicitamente que fuzzing pode degradar hardware, encher disco e que "shouldn't be fuzzing on systems where the prospect of data loss is not an acceptable risk".

## Como verificar
Abra o topo do README stable e confirme a descrição, a lista de mantenedores, a versão 5.03c e o parágrafo de recomendação do fuzzbench; confirme a seção 0 do guia in-depth.

## Conexões
- [[aflpp-license-docker-branches]] — Veja também: Licença AGPL com harness Apache, Docker pronto e branches stable/dev.

## Fontes
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
