---
id: software.testes.tranche21.001518
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

# freezegun: tempo correndo com tick e auto_tick

## Em uma frase
tick=True mantém o relógio andando a partir do instante congelado, e auto_tick_seconds avança o tempo uma quantidade fixa a cada chamada de now, sobrepondo-se ao tick.

## Por que importa
Relógios congelados revelam bugs de dependência de ordem; relógios que andam de forma previsível testam expiração por intervalo sem incerteza.

## Como funciona
Decore com tick para simular progresso, ou fixe auto_tick_seconds=15 quando cada consulta deverá avançar um quarto de minuto.

## Exemplo
O exemplo afirma que a segunda leitura difere da primeira exatamente por quinze segundos sob auto_tick.

## Limites e trade-offs
Sob auto_tick_seconds o parâmetro tick é ignorado, comportamento documentado; testes que dependem de ambas as premissas confundem a esteira.

## Como verificar
Leia now duas vezes sob auto_tick e afirme a diferença de segundos entre as leituras.

## Conexões
- [[freezegun-nice-inputs]] — Veja também: freezegun: datas legíveis e funções geradoras.
- [[freezegun-manual-ticks]] — Veja também: freezegun: avanço manual com o congelador vivo.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
