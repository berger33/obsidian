---
id: software.testes.tranche23.001716
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

# Corpus primeiro: afl-cmin, afl-merge e afl-tmin em sequência

## Em uma frase
A segunda parte do guia é um ritual de três ferramentas para o insumo do afl-fuzz: coletar o máximo de entradas válidas possível de qualquer fonte (a doc sugere bugs reportados, test suites, downloads aleatórios, dados de unit test — e o diretório testcases/ do repo); deduplicar com afl-cmin -i INPUTS -o INPUTS_UNIQUE mantendo só o que produz caminho novo, com @@ para alvo por arquivo e stdin como default sem @@; e opcionalmente minimizar cada arquivo com afl-tmin num loop (paralelizável com GNU parallel), porque "the shorter the input files... the better the fuzzing".

## Por que importa
A doc chama a deduplicação de "highly recommended" com razão mensurável: corpus cheio de duplicatas desacelera a campanha inteira antes da primeira mutação, e cmin é barato comparado a horas de fuzzing desperdiçado.

## Como funciona
Para campanhas que continuam um corpus existente, a mesma seção apresenta o afl-merge como caminho do meio — análogo ao -merge=1 do libFuzzer: adiciona só o que cobre caminho novo sem minimizar o output; a sintaxe aceita CORPUS NOVAS... sem flags.

## Exemplo
Rode afl-cmin no seu seed atual contra o alvo instrumentado e meça a redução de contagem de arquivos; depois afl-tmin em um arquivo grande do corpus para ver o tamanho colapsar mantendo o mesmo caminho de cobertura.

## Limites e trade-offs
A minimização por arquivo (tmin) é marcada como "rather optional" pela própria doc — o custo é linear ao tamanho do corpus; e afl-cmin precisa do alvo compilado para a forma de input correta (stdin ou arquivo via @@), senão deduplica com base em execução quebrada.

## Como verificar
Abra as seções 2a, 2b e 2c do fuzzing_in_depth e confirme o exemplo do loop tmin, as duas sintaxes do merge e as frases de recomendação citadas.

## Conexões
- [[aflpp-target-modification]] — Veja também: Ajudar o alvo a ser fuzzável: checksums off e estático on.
- [[aflpp-run-basics]] — Veja também: Executando afl-fuzz: system-config, -i/-o, @@ e resume por traço.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — índice da documentação](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/README.md) — mapa dos guias: in-depth, binary-only, GUI, value profiling; consultado em 2026-10-03.
