---
id: software.testes.tranche22.001639
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

# responses: add_callback para respostas dinâmicas

## Em uma frase
Para respostas que dependem do request, responses.add_callback(metodo, url, callback=..., content_type=...) delega a geração da resposta a uma função que recebe o request e devolve a trinca (status, headers, corpo serializado).

## Por que importa
O mock deixa de ser tábua estática e vira um micro-servidor em memória: validador de payload, cálculo por request e request-id ecoado na resposta saem do mesmo callback.

## Como funciona
O exemplo documentado casa re.compile("http://calc.com/(sum|prod|pow|unsupported)") com um request_callback que lê request.body, reduz a lista de números pelo operador do path e devolve {"value": ...}.

## Exemplo
Como o callback recebe o request cru, é ali — não no registro — que se validam headers e corpo antes de fabricar a resposta.

## Limites e trade-offs
O contrato de retorno do callback (tupla de três) é manual: esquecer o dumps do json produz corpo em branco silencioso.

## Como verificar
Suba um teste que devolve 422 dentro do callback quando o payload é inválido, provando a validação com estado por request.

## Conexões
- [[responses-calls-inspection]] — Veja também: responses: o histórico em responses.calls.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
