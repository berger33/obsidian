---
id: software.testes.tranche25.001938
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

# Matching de payload e resposta JSON com Post, MatchType("json") e JSON(...)

## Em uma frase
O exemplo TestMockSimple do README demonstra como usar o helper JSON tanto na expectativa de entrada quanto na resposta simulada: gock.New("http://foo.com").Post("/bar").MatchType("json").JSON(map[string]string{"foo": "bar"}).Reply(201).JSON(map[string]string{"bar": "foo"}).

## Por que importa
Observe a posição de Reply(201) na cadeia fluente: tudo o que vem antes de Reply (Post("/bar"), MatchType("json") e o primeiro JSON(...)) define o que a requisição enviada pelo cliente deve conter; tudo o que vem depois de Reply(201) (o segundo JSON(...)) define o que o servidor simulado devolverá.

## Como funciona
Antes de chamar Reply(status), encadeie o método HTTP (Post, Put, etc.), MatchType("json") e JSON(estruturaEsperada) para validar o corpo de envio; depois de Reply(status), encadeie JSON(estruturaDeResposta) ou BodyString(...) para montar o retorno.

## Exemplo
Em TestMockSimple, http.Post("http://foo.com/bar", "application/json", bytes.NewBuffer([]byte(`{"foo":"bar"}`))) casa com MatchType("json") e JSON(map[string]string{"foo": "bar"}) e recebe status 201 com corpo `{"bar":"foo"}`.

## Limites e trade-offs
A seção Features do README também lista helpers embutidos para XML além de JSON; certifique-se de que o Content-Type enviado pelo cliente seja compatível quando usar MatchType("json").

## Como verificar
Conferi o exemplo TestMockSimple e a seção Features no README oficial.

## Conexões
- [[gock-query-params-matching]] — Veja também: Matching de parâmetros de URL com MatchParam.
- [[gock-ttl-persistence-delays-and-filters]] — Veja também: Recursos avançados da lista de Features: persistência/TTL, atrasos, filtros/maps e compatibilidade.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
