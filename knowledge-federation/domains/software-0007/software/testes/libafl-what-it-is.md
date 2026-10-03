---
id: software.testes.tranche24.001800
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md", "https://github.com/AFLplusplus/LibAFL"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LibAFL: encaixe o seu fuzzador em Rust

## Em uma frase
O README define o LibAFL como "Advanced Fuzzing Library - Slot your own fuzzers together and extend their features using Rust": uma coleção de peças reutilizáveis de fuzzadores que entrega "muitos dos benefícios de um fuzzer pronto, sendo completamente customizável".

## Por que importa
A tese do projeto inverte a relação usual com ferramentas: em vez de configurar um binário existente, você compõe o fuzzador como dependência de biblioteca — o que abre espaço para políticas de mutação, feedbacks e arquiteturas que o fuzzer pronto nunca expôs.

## Como funciona
Os blocos de construção (executors, feedbacks, mutators, corpora) vivem no crate principal; o código comum de instrumentação de alvos e os wrappers de compilador têm crates próprios, e os exemplos em fuzzers/ mostram as combinações canônicas.

## Exemplo
Um fuzzador novo é um projeto cargo que depende de libafl: o exemplo inprocess/libfuzzer_libpng multicore — apontado como o mais bem testado — é a referência de partida que o README recomenda ler primeiro.

## Limites e trade-offs
"Completely customizable" descreve a arquitetura, não uma API garantida: a superfície da biblioteca evolui, e o README marca o livro oficial como "WIP" — a leitura de código dos exemplos é parte do contrato.

## Como verificar
A definição e a frase de benefício/customização estão na abertura do README oficial do repositório.

## Conexões
- [[libafl-llmp-scaling]] — Veja também: LLMP: escala quase linear por núcleo e TCP entre máquinas.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
