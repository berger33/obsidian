---
id: software.testes.tranche22.001630
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

# responses: mockar o requests sem tocar na rede

## Em uma frase
O responses é uma biblioteca utilitária para simular (mock out) a biblioteca requests do Python, exigindo Python 3.8+ e requests >= 2.30.0, instalável com pip install responses.

## Por que importa
Clientes HTTP são o ponto de contato instável de todo teste de serviço; mockar na camada requests — e não no servidor — mantém o teste unitário sem socket, sem docker e sem porta.

## Como funciona
O modelo mental do README: registrar respostas mockadas e cobrir a função de teste com o decorator responses.activate, usando uma interface deliberadamente parecida com a do próprio requests.

## Exemplo
@responses.activate sobre test_simple(), um responses.add(responses.GET, url, json=..., status=404) e a chamada requests.get devolve o 404 inventado.

## Limites e trade-offs
Ele intercepta requests especificamente; httpx, urllib e sessões customizadas de outras bibliotecas não entram no mock — o escopo é declarado no nome.

## Como verificar
Quebre o ambiente de rede do teste (unset proxy, sem DNS) e confirme que a suíte com responses continua verde.

## Conexões
- [[responses-register-interface]] — Veja também: responses: add() com objeto ou argumentos diretos.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
