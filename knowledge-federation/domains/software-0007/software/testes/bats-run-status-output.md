---
id: software.testes.tranche22.001563
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://bats-core.readthedocs.io/en/latest/writing-tests.html", "https://bats-core.readthedocs.io/en/latest/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: run captura status e saída

## Em uma frase
O helper run invoca seus argumentos como comando, guarda o código em $status, junta stdout e stderr em $output e sempre retorna 0 para que as asserções seguintes sejam executadas.

## Por que importa
Testar CLI exige inspecionar saída e código de erro sem abortar o teste antes da verificação; o run separa a execução bruta da checagem deliberada.

## Como funciona
Depois do run, afirme [ "$status" -eq 1 ] e compare $output; com a versão moderna, [ "${lines[0]}" = ... ] checa linha a linha e $BATS_RUN_COMMAND devolve o comando inteiro reconstruído.

## Exemplo
run foo nonexistent_filename seguido de [ "$output" = "foo: no such file 'nonexistent_filename'" ] documenta o contrato de erro do programa testado.

## Limites e trade-offs
run sem as flags de expectativa engole o fracasso do comando testado; o guia traz a entrada "run doesn't fail, although the same command without run does" justamente para esse mal-entendido.

## Como verificar
Use run -1 para exigir status 1, ou run ! para exigir status não zero, e veja o teste falhar sozinho se a expectativa não se cumprir.

## Conexões
- [[bats-errexit-assertions]] — Veja também: bats-core: cada linha viva é uma asserção.
- [[bats-setup-teardown]] — Veja também: bats-core: ganchos por teste e por arquivo.

## Fontes
- [Bats-core — Writing tests](https://bats-core.readthedocs.io/en/latest/writing-tests.html) — run, tags, setup/teardown, ganchos e armadilhas de escrita; consultado em 2026-10-03.
- [Bats-core — Usage](https://bats-core.readthedocs.io/en/latest/usage.html) — opções do CLI, formatters, relatórios e execução paralela; consultado em 2026-10-03.
