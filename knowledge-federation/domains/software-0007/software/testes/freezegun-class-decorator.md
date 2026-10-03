---
id: software.testes.tranche21.001512
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

# freezegun: congelar uma classe de testes inteira

## Em uma frase
Aplicado à classe, o decorator congela o tempo em cada callable testável, servindo tanto a TestCase do unittest quanto a classes comuns de teste.

## Por que importa
Suites inteiras sobre a mesma data-base ganham o congelamento num único lugar, e casos novos herdam a premissa sem lembrar do decorator.

## Como funciona
Decore a classe MyTests com a data e escreva os métodos como sempre, confiando que agora dentro deles o relógio está parado na premissa.

## Exemplo
@freeze_time("1955-11-12") sobre a classe vale para test_the_class e para os próximos casos que chegarem.

## Limites e trade-offs
O README avisa que para classes comuns a abordagem pode não funcionar em todo caso; testes com setups complexos pedem verificação.

## Como verificar
Adicione um método novo à classe decorada e confirme que ele também enxerga a data congelada sem decorator próprio.

## Conexões
- [[freezegun-decorator-basics]] — Veja também: freezegun: decorar o teste com o instante.
- [[freezegun-context-manager]] — Veja também: freezegun: contexto para controlar a fronteira.

## Fontes
- [freezegun — página no PyPI](https://pypi.org/project/freezegun/) — README oficial com uso, fusos, tick e limites; consultado em 2026-10-03.
- [freezegun — repositório oficial](https://github.com/spulec/freezegun) — código-fonte, testes e releases do projeto; consultado em 2026-10-03.
