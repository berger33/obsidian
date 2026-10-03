---
id: software.testes.tranche25.001935
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

# Clientes customizados: gock.InterceptClient(client) uma vez e defer gock.RestoreClient(client)

## Em uma frase
Duas subseções de Tips tratam de instâncias próprias de http.Client: "Intercept an http.Client just once" explica que basta chamar gock.InterceptClient(client) uma única vez no início do cenário, e "Restore an http.Client after interception" recomenda chamar defer gock.RestoreClient(client) (junto de defer gock.Off()) para restaurar o cliente após o teste, observando em nota que isso não é necessário quando se usa http.DefaultClient ou http.DefaultTransport.

## Por que importa
Quando um cliente HTTP customizado possui seu próprio http.Transport (com timeouts ou pools de conexão próprios), ele não usa o http.DefaultTransport; gock.InterceptClient substitui o transporte desse cliente, e gock.RestoreClient devolve o transporte original ao final do teste para não vazar a interceptação se a instância do cliente for compartilhada.

## Como funciona
Se o código sob teste usa um *http.Client próprio, chame gock.InterceptClient(client) uma vez no setup do teste e registre defer gock.RestoreClient(client) logo após defer gock.Off(); se usa http.DefaultClient, apenas defer gock.Off() basta.

## Exemplo
O esqueleto idiomático mostrado no README para cliente customizado combina as duas linhas no topo do teste: defer gock.Off() e defer gock.RestoreClient(client).

## Limites e trade-offs
Chamar gock.InterceptClient repetidas vezes sobre a mesma instância de cliente no mesmo cenário é desnecessário e contraindicado pela própria dica do README.

## Como verificar
Conferi as subseções Intercept an http.Client just once e Restore an http.Client after interception no README oficial.

## Conexões
- [[gock-concurrency-and-race-conditions-caveat]] — Veja também: Concorrência e condições de corrida: declarar mocks antes de disparar goroutines.
- [[gock-header-and-regex-matching]] — Veja também: Matching de cabeçalhos com expressões regulares: MatchHeader e HeaderPresent.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
