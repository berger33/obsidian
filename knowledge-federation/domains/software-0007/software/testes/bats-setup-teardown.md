---
id: software.testes.tranche22.001564
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
fontes: ["https://bats-core.readthedocs.io/en/latest/writing-tests.html", "https://bats-core.readthedocs.io/en/latest/tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: ganchos por teste e por arquivo

## Em uma frase
A dupla setup e teardown funciona como pre- e pós-gancho de cada caso, e a documentação dedica uma seção do tutorial a evitar setups caros repetidos a cada teste.

## Por que importa
Criar fixture em todo caso sai caro em suítes grandes; conhecer a granularidade dos ganchos deixa o setup por arquivo quando o estado é compartilhado e o por teste quando não é.

## Como funciona
Declare setup no topo do arquivo para preparar TMPDIR ou instalar um binário de teste; rode o gancho inverso para limpar, confiando que o processo isolado de cada teste não vaza estado.

## Exemplo
setup { mkdir -p "$BATS_TEST_TMPDIR/fixtures"; cp fixture.txt "$BATS_TEST_TMPDIR"; } dá a cada caso um diretório temporário virgem.

## Limites e trade-offs
Como cada teste roda em processo próprio, variáveis exportadas em setup não sobrevivem entre casos — e o gancho também não roda em código fora de @test.

## Como verificar
Force um teste a escrever em arquivo fora de BATS_TEST_TMPDIR e veja o segundo caso herdá-lo; depois mova para o tmpdir e confirme o isolamento.

## Conexões
- [[bats-run-status-output]] — Veja também: bats-core: run captura status e saída.
- [[bats-tagging]] — Veja também: bats-core: tags, filtros e modo foco.

## Fontes
- [Bats-core — Writing tests](https://bats-core.readthedocs.io/en/latest/writing-tests.html) — run, tags, setup/teardown, ganchos e armadilhas de escrita; consultado em 2026-10-03.
- [Bats-core — Tutorial](https://bats-core.readthedocs.io/en/latest/tutorial.html) — primeiro teste, setup, output, limpeza e suítes multifiles; consultado em 2026-10-03.
