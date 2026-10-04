---
id: software.testes.tranche21.001513
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

# freezegun: contexto para controlar a fronteira

## Em uma frase
O uso com with freeze_time("2012-01-14"): circunscreve o congelamento ao bloco, e fora dele o relógio volta ao normal.

## Por que importa
Quando o teste precisa observar o mesmo objeto antes e depois do instante simulado, o contexto marca a fronteira com precisão.

## Como funciona
Faça asserções do estado real antes do with, entre no congelamento para o comportamento datado e saia para confirmar a restauração.

## Exemplo
O padrão before-during-after aparece no próprio exemplo: agora fora do bloco difere da data congelada.

## Limites e trade-offs
Blocos aninhados somam estados de relógio; na dúvida de qual congelamento vence numa pilha profunda, prefira um decorator no caso inteiro.

## Como verificar
Afirme o relógio livre, o congelado e o livre novamente no mesmo teste e confirme as três fronteiras.

## Conexões
- [[freezegun-class-decorator]] — Veja também: freezegun: congelar uma classe de testes inteira.
- [[freezegun-raw-start-stop]] — Veja também: freezegun: start e stop para fixtures.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
