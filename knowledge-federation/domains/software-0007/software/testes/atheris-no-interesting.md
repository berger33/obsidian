---
id: software.testes.tranche23.001754
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://llvm.org/docs/LibFuzzer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# "No interesting inputs were found": a porta de entrada mais comum

## Em uma frase
A seção homônima do README documenta o erro — ERROR: no interesting inputs were found. Is the code instrumented for coverage? — com o mecanismo exato: ele aparece quando as duas primeiras chamadas a TestOneInput não produziram nenhum evento de cobertura, e isso acontece mesmo com instrumentação existente, por exemplo quando o TestOneInput é nontrivial e a cobertura instrumentada não é alcançada nos dois primeiros inputs.

## Por que importa
É a falha de configuração mais frequente de quem começa, e entendê-la economiza horas: o motor não está dizendo que a lib é imutável, está dizendo que não viu sinal de vida nos dois primeiros ensaios.

## Como funciona
As três receitas listadas são instrumentar o próprio TestOneInput com instrument_func, usar instrument_all, ou mover a função TestOneInput para dentro de um módulo instrumentado — todas garantindo que a execução de entrada em si emita eventos de cobertura.

## Exemplo
Reproduza o erro adiantando um return condicional cedo no seu harness, depois aplique a primeira receita do README sobre TestOneInput e confirme que a inicialização passa — a correção vem da lista oficial, não de chute.

## Limites e trade-offs
A página trata o sintoma de instrumentação, não de harness lento demais ou do parser que rejeita tudo silenciosamente — se as duas primeiras chamadas cobrem linhas mas o corpus ainda não cresce, o diagnóstico migra para a qualidade do alvo, fora do escopo desta seção.

## Como verificar
Abra a subseção Why am I getting No interesting inputs were found do README oficial e confirme a explicação das duas chamadas e as três correções na ordem dada.

## Conexões
- [[atheris-instrumentation-modes]] — Veja também: Três granularidades de instrumentação — e as pegadinhas de cada uma.
- [[atheris-coverage-viz]] — Veja também: Ver cobertura linha a linha com coverage.py e -atheris_runs.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [LLVM — libFuzzer documentation](https://llvm.org/docs/LibFuzzer.html) — motor base de cargo-fuzz e Atheris: corpus, -merge=1, requisitos do fuzz target; consultado em 2026-10-03.
