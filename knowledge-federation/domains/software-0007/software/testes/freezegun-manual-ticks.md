---
id: software.testes.tranche21.001519
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

# freezegun: avanço manual com o congelador vivo

## Em uma frase
Usando o contexto como gerenciador, o objeto frozen_datetime permite tick() de um segundo e tick(delta=...) com o salto desejado, e chamá-lo devolve o instante atual congelado.

## Por que importa
Verificar comportamento a cada segundo, minuto ou hora dentro de um mesmo teste pede um avanço sob comando, não um relógio correndo sozinho.

## Como funciona
Abra with freeze_time(inicial) as frozen_datetime, ligue os ticks ao passo a passo da ação testada e afirme o relógio via frozen_datetime().

## Exemplo
O exemplo acumula um segundo, depois dez, conferindo a igualdade com o timedelta esperado em cada marca.

## Limites e trade-offs
Ticks manuais avançam o relógio mas não disparam por si os timers agendados pela biblioteca padrão; não espere que um sleep atrasado acorde sozinho.

## Como verificar
Avance com dois ticks de tamanhos diferentes e confirme a data resultante a cada salto aplicado.

## Conexões
- [[freezegun-tick-modes]] — Veja também: freezegun: tempo correndo com tick e auto_tick.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
