---
id: software.testes.tranche22.001636
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

# responses: match() com matchers combináveis

## Em uma frase
Em vez de só bater URL, o parâmetro match recebe um iterável de callbacks que casam atributos do request; o módulo responses.matchers traz os prontos: json_params, urlencoded_params, query_param, query_string, kwargs do request, multipart/form-data, headers e fragment identifier.

## Por que importa
Testes de API POST que só verificam URL aceitam qualquer payload; o matcher transforma o corpo em parte do contrato testado — request errado não consome a resposta mockada.

## Como funciona
A deprecação histórica marca o caminho: json_params_matcher e urlencoded_params_matcher saíram do root para responses.matchers.* na 0.14.0, e match_querystring (0.17.0) foi substituído por query_param_matcher/query_string_matcher.

## Exemplo
matcher que falha em um dos critérios não casa o registro e a chamada vira ConnectionError — a lista de match funciona como conjunção.

## Limites e trade-offs
Matchers customizados são permitidos (o README encoraja criar o seu), mas cada um é código de teste que também precisa de teste.

## Como verificar
Registre um GET com match=(query_param_matcher({"page": "2"}),) e confirme que a chamada com outra query quebra o match.

## Conexões
- [[responses-parameters]] — Veja também: responses: o catálogo de parâmetros do Response.
- [[responses-passthru]] — Veja também: responses: deixar alguns requests passarem.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
