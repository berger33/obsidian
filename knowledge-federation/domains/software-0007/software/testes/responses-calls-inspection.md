---
id: software.testes.tranche22.001638
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

# responses: o histórico em responses.calls

## Em uma frase
Depois do bloco, o mock mantém cada interação em responses.calls — o README usa len(responses.calls) como asserção de contagem e .calls[0].request.url para inspecionar o request original.

## Por que importa
Contar chamadas é tão importante quanto checar resposta: um cliente que refaz o mesmo GET dez vezes por retry loop passa em todo mock ingênuo.

## Como funciona
Padrão de coroutine async do material oficial: dentro de @responses.activate sobre async def, requests.get afirmado por respostas e por responses.calls[0].request.url == url esperada.

## Exemplo
No teste de exemplo, as asserções finais confirmam resp.json() == {"error": "not found"}, status_code 404 e o URL registrado na chamada — as três camadas do contrato.

## Limites e trade-offs
calls grava o que passou pelo mock ativo; com decorator e contexto aninhados, leia o histórico do objeto certo (responses.mock vs o rsps do bloco).

## Como verificar
Force um retry duplo no cliente sob teste e use len(responses.calls) == 2 para transformar a contagem em asserção de bug.

## Conexões
- [[responses-passthru]] — Veja também: responses: deixar alguns requests passarem.
- [[responses-callback]] — Veja também: responses: add_callback para respostas dinâmicas.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
