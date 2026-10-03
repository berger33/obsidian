---
id: software.testes.tranche21.001516
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

# freezegun: congelar com deslocamento de fuso

## Em uma frase
O argumento tz_offset desloca o tempo congelado, aceitando horas inteiras ou um timedelta com minutos fracionários, e separa o que é utcnow do que é now local.

## Por que importa
Janela de expiração medida em UTC e dia contábil medido em horário local discordam justamente no midnight, onde vivem os bugs de data.

## Como funciona
Declare o instante e o offset juntos e afirme utcnow, now e date.today() cada um com sua semântica deslocada.

## Exemplo
@freeze_time("2012-01-14 03:21:34", tz_offset=-4) faz today() cair em 13 de janeiro, pois usa a hora local.

## Limites e trade-offs
O timedelta com minutos (como -3h30) aparece no exemplo e ajuda fusos meio-horários; esquecer o offset congela o fuso da máquina, não o do usuário.

## Como verificar
Mude apenas o tz_offset e confirme que utcnow permanece e now desloca o dia.

## Conexões
- [[freezegun-as-kwarg]] — Veja também: freezegun: receber o congelador como argumento.
- [[freezegun-nice-inputs]] — Veja também: freezegun: datas legíveis e funções geradoras.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
