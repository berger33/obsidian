---
id: software.testes.tranche22.001633
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
fontes: ["https://github.com/getsentry/responses/blob/master/README.rst", "https://pypi.org/project/responses/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# responses: RequestsMock como contexto

## Em uma frase
Em vez de decorar a função inteira, o with responses.RequestsMock() as rsps registra no objeto do bloco (rsps.add(...)) — e fora do contexto os requests voltam a bater no servidor remoto de verdade.

## Por que importa
Escopo delimitado é o contrato: só o que está dentro do with enxerga o mock, e o README frisa que a comparação de requests fora do bloco "will hit the remote server".

## Como funciona
rsps.add(responses.GET, url, body="{}", status=200, content_type="application/json") é a forma completa documentada para o contexto.

## Exemplo
Fora do bloco, resp = requests.get(...) real — o snippet do README termina exatamente com essa demonstração de vazamento controlado.

## Limites e trade-offs
A forma de contexto cobra atenção ao retorno: esquecer o assert dentro do bloco deixa a verificação para onde o mock já foi desligado.

## Como verificar
Coloque um registro dentro do contexto e um requests fora, com um servidor local de escuta, e prove que o de fora não vê o mock.

## Conexões
- [[responses-shortcuts]] — Veja também: responses: atalhos por verbo HTTP.
- [[responses-connection-error]] — Veja também: responses: URL sem match é ConnectionError.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
