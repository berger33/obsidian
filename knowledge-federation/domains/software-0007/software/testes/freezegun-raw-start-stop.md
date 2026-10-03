---
id: software.testes.tranche21.001514
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

# freezegun: start e stop para fixtures

## Em uma frase
O objeto cru devolvido por freeze_time aceita start() e stop() manuais, a peça que permite ligar o congelamento em fixtures e setups compartilhados.

## Por que importa
Fixtures do pytest e setUp do unittest vivem fora do corpo do teste, exatamente onde decorator e contexto são desajeitados demais.

## Como funciona
Guarde freezer = freeze_time("2012-01-14 12:00:01"), chame start no setup, e stop no teardown para não contaminar o resto da suíte.

## Exemplo
A fixture de app pode iniciar o congelamento antes do teste e parar no yield seguinte automaticamente.

## Limites e trade-offs
Start sem stop correspondente deixa o relógio da suíte congelado em casos alheios; o par simétrico é regra, não sugestão.

## Como verificar
Pare o congelamento na finalização da fixture e confirme que o próximo teste do módulo começa com o relógio real.

## Conexões
- [[freezegun-context-manager]] — Veja também: freezegun: contexto para controlar a fronteira.
- [[freezegun-as-kwarg]] — Veja também: freezegun: receber o congelador como argumento.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
