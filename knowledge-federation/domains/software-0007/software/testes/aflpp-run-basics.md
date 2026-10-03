---
id: software.testes.tranche23.001717
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

# Executando afl-fuzz: system-config, -i/-o, @@ e resume por traço

## Em uma frase
Antes de qualquer run, o guia manda rodar sudo afl-system-config — que reconfigura o sistema para performance de fuzzing e sem o qual o afl-fuzz bails — com o fallback documentado AFL_SKIP_CPUFREQ=1 quando não há root; em Docker, a doc recomenda passar --cpuset-cpus com cores livres ou AFL_NO_AFFINITY, porque cada container vê só seus cores e todos os afl-fuzz mirariam o mesmo core sem isso.

## Por que importa
O afl-system-config e sua contraparte permanente afl-persistent-config vêm com a nota de honestidade rara: melhoram a performance "but also decrease your system protection against attacks" — firewall forte e SSH único são a condição recomendada pela doc para usá-los.

## Como funciona
O comando canônico é afl-fuzz -i input -o output -- bin/target -someopt @@, com -o criado se preciso, e para retomar uma campanha troca-se o input pelo traço: afl-fuzz -i - -o output ... — os mesmos flags podem mudar entre reinícios ("even change them by selecting a different power schedule") sem perder o queue; o guia também prescreve tela/detach (screen -dmS afl-main -- afl-fuzz -M main-$HOSTNAME...) para SSH resiliente.

## Exemplo
Reinicie uma campanha com -i - e confira que o fuzzer anuncia o import do queue existente (a doc orienta AFL_IMPORT_FIRST=1 para importar primeiro os casos dos outros fuzzers, alertando que isso atrasa o start com muitos fuzzers/seeds).

## Limites e trade-offs
Os scripts de system config são Linux (o guia fala em sudo e iostat); e o trade-off de segurança citado não é opcional — a doc recomenda os scripts e o hardening junto; quem não aceita o risco fica com CPU throttling que a seção 0 prevê.

## Como verificar
Abra as seções 3a e 0 do fuzzing_in_depth: afl-system-config, cpuset/AFL_NO_AFFINITY, o comando canônico, o truque do -i - e a nota dos persistent configs.

## Conexões
- [[aflpp-corpus-prep]] — Veja também: Corpus primeiro: afl-cmin, afl-merge e afl-tmin em sequência.
- [[aflpp-dictionaries-memory]] — Veja também: Dicionários automáticos e o limite de memória que ninguém configura.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
