---
id: software.testes.tranche24.001851
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

# Getting Started: dev-dependency e o exemplo canônico

## Em uma frase
A página da crate define a entrada mínima: httpmock = "0.8.3" sob [dev-dependencies] no Cargo.toml, e o uso de cinco linhas: use httpmock::prelude::*;, let server = MockServer::start();, um mock com server.mock(|when, then| { when.method(GET).path("/translate").query_param("word", "hello"); then.status(200).header("content-type", "text/html").body("ohi"); }), a requisição real via reqwest contra server.url("/translate?word=hello") e as duas verificações (hello_mock.assert() e assert_eq!(response.status(), 200)).

## Por que importa
A forma do exemplo ensina mais que o texto: o mock é uma função com dois builder arguments — when descreve o request aceito, then descreve a resposta devolvida — e o handle retornado (Mock) é o objeto de verificação, mantendo especificação e asserção no mesmo escopo lexical.

## Como funciona
Para o primeiro teste de integração com HTTP no seu crate, copie o esqueleto: dev-dependency, prelude, start, mock com when/then, chamar o cliente apontando para server.url(...), e assert — sem threads, ports fixos ou fixtures externas.

## Exemplo
O header e o body de exemplo ("content-type: text/html", body "ohi") e o query_param esperado (word=hello) vêm literalmente da página — inclusive a pequena ironia do corpo de demonstração.

## Limites e trade-offs
A versão 0.8.3 é a documentada no docs.rs consultado; a API pode evoluir — o próprio link do docs.rs mantém permalink versionado para consulta exata.

## Como verificar
Todo o código de exemplo e o trecho de instalação vêm da seção Getting Started da página da crate.

## Conexões
- [[httpmock-what-it-is]] — Veja também: httpmock: simular serviços HTTP para testar clientes em Rust.
- [[httpmock-when-when]] — Veja também: When: as condições que o request tem que satisfazer.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
