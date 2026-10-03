---
id: software.testes.tranche25.001937
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/h2non/gock/master/README.md", "https://godoc.org/github.com/h2non/gock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Matching de parâmetros de URL com MatchParam

## Em uma frase
O exemplo TestMatchParams do README mostra como restringir um mock aos parâmetros de query string da URL: gock.New("http://foo.com").MatchParam("page", "1").MatchParam("per_page", "10").Reply(200).BodyString("foo foo") casa com uma requisição GET para "http://foo.com?page=1&per_page=10".

## Por que importa
Separar os parâmetros de query em chamadas MatchParam("chave", "valor") torna o teste imune à ordem de serialização dos parâmetros na URL e muito mais legível do que concatenar strings longas de query na rota.

## Como funciona
Declare o host em gock.New("http://foo.com"), encadeie uma chamada MatchParam(chave, valor) para cada parâmetro de paginação ou filtro esperado e verifique ao final com gock.IsDone() que a requisição com aqueles parâmetros ocorreu.

## Exemplo
No exemplo TestMatchParams do README, http.NewRequest("GET", "http://foo.com?page=1&per_page=10", nil) satisfaz simultaneamente MatchParam("page", "1") e MatchParam("per_page", "10").

## Limites e trade-offs
Se a requisição real omitir um dos parâmetros exigidos por MatchParam ou enviar valor divergente, o mock não casa e o cliente recebe erro de falta de match (a menos que outro mock ou rede real esteja ativo).

## Como verificar
Conferi o exemplo TestMatchParams no README oficial do repositório h2non/gock.

## Conexões
- [[gock-header-and-regex-matching]] — Veja também: Matching de cabeçalhos com expressões regulares: MatchHeader e HeaderPresent.
- [[gock-json-body-matching-and-reply]] — Veja também: Matching de payload e resposta JSON com Post, MatchType("json") e JSON(...).

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
