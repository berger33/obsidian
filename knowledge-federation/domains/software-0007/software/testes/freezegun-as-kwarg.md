---
id: software.testes.tranche21.001515
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

# freezegun: receber o congelador como argumento

## Em uma frase
O parâmetro as_kwarg injeta o objeto do congelador no teste por nome, dando acesso ao time_to_freeze e aos controles de avanço dentro do corpo.

## Por que importa
Testes parametrizados sobre datas variadas querem ler ou mover a data-base em vez de digita-la duas vezes entre decorator e asserção.

## Como funciona
Decore com @freeze_time('2013-04-09', as_kwarg='frozen_time') e leia frozen_time.time_to_freeze.date() na verificação.

## Exemplo
kwargs.get('hello') na segunda variante do exemplo mostra o uso também com assinatura aberta.

## Limites e trade-offs
Acoplar o teste à estrutura interna do congelador pode quebrar em upgrades; prefira a data fixa quando ela bastar.

## Como verificar
Leia a data-base via kwarg e afirme contra datetime.date.today() para confirmar os dois caminhos.

## Conexões
- [[freezegun-raw-start-stop]] — Veja também: freezegun: start e stop para fixtures.
- [[freezegun-tz-offset]] — Veja também: freezegun: congelar com deslocamento de fuso.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
