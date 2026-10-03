---
id: software.testes.tranche24.001850
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://docs.rs/httpmock/latest/httpmock/", "https://github.com/httpmock/httpmock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# httpmock: simular serviços HTTP para testar clientes em Rust

## Em uma frase
A crate se resume na linha de sumário do docs.rs: "HTTP mocking library that allows you to simulate responses from HTTP-based services" — uma biblioteca que sobe um servidor de mentira controlado pelo próprio teste, em vez de exigir um backend real ou stub de trait interpolado no meio do código de produção.

## Por que importa
Em Rust não há herança para "estender o servidor"; mockar HTTP por baixo (trait do cliente) cobra abstração generalizada no design da aplicação. O httpmock corta o problema pelo lado de fora: o código sob teste faz requisições HTTP verdadeiras contra um servidor local que só existe durante o teste — zero intrusão no design.

## Como funciona
O teste cria um MockServer, declara mocks com pares when/then, aponta o cliente de produção para a URL devolvida pelo servidor e verifica chamadas e respostas — tudo dentro do mesmo processo de teste.

## Exemplo
O exemplo do Getting Started é exatamente esse fluxo: MockServer::start(); server.mock(|when, then| ...); get(&server.url("/translate?word=hello")); hello_mock.assert(); e assert_eq na resposta 200.

## Limites e trade-offs
A biblioteca intercepta no nível da rede local; código que fixa URLs absolutas de produção sem injeção de base URL continua difícil de testar — a nota presume o padrão usual de passar o server.url ao cliente.

## Como verificar
A definição vem do summary da crate; a lista completa de features vem da seção Features da página oficial no docs.rs.

## Conexões
- [[httpmock-getting-started]] — Veja também: Getting Started: dev-dependency e o exemplo canônico.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
