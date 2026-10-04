---
id: software.testes.tranche22.001631
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

# responses: add() com objeto ou argumentos diretos

## Em uma frase
O registro aceita dois formatos: instanciar responses.Response(method="PUT", url=...) e passar o objeto para responses.add, ou chamar add diretamente com os argumentos do Response (método, url, json, status).

## Por que importa
Em fixtures reutilizáveis vale montar Response como dado; no teste pontual, a forma direta de cinco argumentos é mais curta que a classe — a lib decide não forçar escolha.

## Como funciona
Ambos os formatos convivem no mesmo teste do README: rsp1 registrado como objeto e o GET 404 registrado inline, com asserções resp.json() == {"error": "not found"} e resp.status_code == 404.

## Exemplo
O objeto Response registrado sem corpo nem status devolve 200 vazio por padrão, como mostra a segunda chamada do exemplo (assert resp2.status_code == 200).

## Limites e trade-offs
json= e body= se excluem na prática: deixar os dois preenchidos confunde o leitor sobre qual resposta a suíte valida.

## Como verificar
Registre o mesmo método/url nas duas formas e compare as respostas — os dois caminhos devem casar a mesma chamada.

## Conexões
- [[responses-what-it-is]] — Veja também: responses: mockar o requests sem tocar na rede.
- [[responses-shortcuts]] — Veja também: responses: atalhos por verbo HTTP.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
