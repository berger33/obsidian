---
id: software.testes.tranche21.001517
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

# freezegun: datas legíveis e funções geradoras

## Em uma frase
O parser usa dateutil por baixo, aceitando textos como "Jan 14th, 2012", e freeze_time recebe ainda uma função ou um gerador como fonte de datas.

## Por que importa
A data legível aproxima o teste do relatório de bug, e a geradora permite varrer uma sequência de anos no mesmo bloco de congelamento.

## Como funciona
Escreva o instante na forma humana dentro do decorator e, para séries, passe um gerador de datetimes consumido a cada congelamento.

## Exemplo
No exemplo, o gerador dos anos 2010 e 2011 entrega um valor por novo with, e a terceira chamada elevaria StopIteration.

## Limites e trade-offs
Formatos ambíguos como "03/04/2012" passam pelo gosto do parser, não do seu calendário; datas críticas pedem forma ISO explícita.

## Como verificar
Alterne um with por elemento do gerador e confirme o avanço da data-base a cada entrada no bloco.

## Conexões
- [[freezegun-tz-offset]] — Veja também: freezegun: congelar com deslocamento de fuso.
- [[freezegun-tick-modes]] — Veja também: freezegun: tempo correndo com tick e auto_tick.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
