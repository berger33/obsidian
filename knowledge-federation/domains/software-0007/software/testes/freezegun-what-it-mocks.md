---
id: software.testes.tranche21.001510
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://pypi.org/project/freezegun/", "https://github.com/spulec/freezegun"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# freezegun: o que a biblioteca congela

## Em uma frase
O freezegun congela o tempo dos testes simulando o módulo datetime: now, utcnow, today, time.time, localtime, gmtime e strftime devolvem o instante escolhido.

## Por que importa
Lógica de expiração, cobrança recorrente e janela de horário é justamente a que não pode depender do relógio da máquina que roda a esteira.

## Como funciona
Importe freeze_time do freezegun, declare o instante desejado e deixe o código de produção chamar datetime normalmente sob o congelamento.

## Exemplo
test() com @freeze_time("2012-01-14") afirma datetime.datetime.now() igual a 14 de janeiro de 2012.

## Limites e trade-offs
time.monotonic e perf_counter também ficam congeladas, mas sem garantia de valor absoluto — a biblioteca só preserva a variação temporal.

## Como verificar
Consulte os dois relógios (datetime e monotonic) dentro do congelamento e confirme que variam de acordo com o modo ativo.

## Conexões
- [[freezegun-decorator-basics]] — Veja também: freezegun: decorar o teste com o instante.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
