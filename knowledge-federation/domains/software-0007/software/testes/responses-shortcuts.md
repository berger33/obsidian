---
id: software.testes.tranche22.001632
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

# responses: atalhos por verbo HTTP

## Em uma frase
Sete atalhos pré-preenchem o método do registro: responses.delete/get/head/options/patch/post/put aceitam os mesmos argumentos de add com o verbo já resolvido.

## Por que importa
get/post/put viram a maioria esmagadora dos mocks de API; o atalho corta o primeiro argumento repetido de toda suíte e reduz o risco de mockar o verbo errado.

## Como funciona
O exemplo oficial registra get, post e patch na mesma url com json={"type": "get"} etc. e afirma cada resposta pelo seu verbo respectivo.

## Exemplo
Os atalhos cobrem os verbos listados no README; métodos exóticos (PROPFIND, REPORT) voltam a exigir add com Response.

## Limites e trade-offs
Mismatch de verbo é silêncio: requests.get() chamado contra um responses.post() registrado gera ConnectionError, não "405"; o erro diz "sem match", não "verbo errado".

## Como verificar
Troque o verbo do atalho num teste seu e observe a ConnectionError substituindo a falha semântica esperada.

## Conexões
- [[responses-register-interface]] — Veja também: responses: add() com objeto ou argumentos diretos.
- [[responses-context-manager]] — Veja também: responses: RequestsMock como contexto.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
