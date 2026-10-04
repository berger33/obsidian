---
id: software.testes.tranche25.001930
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
fontes: ["https://raw.githubusercontent.com/h2non/gock/master/README.md", "https://github.com/h2non/gock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gock: mocking HTTP versátil e sem dependências para clientes net/http em Go

## Em uma frase
O README oficial descreve o gock como uma biblioteca de mocking HTTP versátil para Go que funciona com qualquer implementação baseada em net/http da biblioteca padrão, fortemente inspirada pelo nock (Node.js), com um porte irmão em Python chamado pook (github.com/h2non/pook), distribuída sob licença MIT e livre de dependências externas ("Dependency free").

## Por que importa
Em Go, muitos clientes HTTP de terceiros e da própria aplicação usam net/http por baixo; interceptar no nível do transporte padrão evita criar interfaces artificiais para cada cliente externo e sem adicionar dependências transitivas ao módulo.

## Como funciona
Instale com go get -u github.com/h2non/gock, declare as expectativas com a DSL fluente gock.New("http://foo.com").Get("/bar").Reply(200) antes de executar o código sob teste e limpe com defer gock.Off().

## Exemplo
No exemplo TestSimple do README, uma chamada direta à biblioteca padrão — http.Get("http://foo.com/bar") — é interceptada e respondida pelo gock com status 200 e corpo JSON {"foo":"bar"} sem tocar na rede real.

## Limites e trade-offs
O gock intercepta chamadas que passam por http.DefaultTransport ou por um http.Transport/http.Client interceptado; clientes que abrem conexões TCP brutas fora de net/http não passam pelo interceptador.

## Como verificar
Conferi a abertura, a seção Features e a seção Installation no README oficial do repositório h2non/gock.

## Conexões
- [[gock-how-it-mocks-four-steps]] — Veja também: Como o gock funciona: RoundTripper, fila FIFO e modo de rede real opcional.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [Repositório oficial h2non/gock](https://github.com/h2non/gock) — Repositório oficial do gock no GitHub com código-fonte sem dependências externas e diretório _examples.; consultado em 2026-10-03.
