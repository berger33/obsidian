---
id: software.testes.tranche24.001853
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

# Then: a resposta predeterminada

## Em uma frase
O par simétrico: Then é definido na página da crate como "the configuration of HTTP responses in a mock server environment", e o exemplo oficial o usa com três encadeamentos — status(200), header("content-type", "text/html") e body("ohi") — enquanto o MockServer se descreve como o servidor que "intercepts HTTP requests and can be configured to return predetermined responses".

## Por que importa
Separar when e then em dois builders mantém a especificação do mock legível como contrato (entrada → saída), e é o que permite às mensagens de erro explicarem só a parte de entrada que falhou, já que a resposta esperada nunca precisou competir com a lógica do teste.

## Como funciona
Declare status, headers e corpo no closure then; o teste então confere os dois lados do contrato — status/parseamento no lado do cliente e assert() no lado do mock — cobrindo o que um stub de retorno fixo não cobre: o request como ele realmente saiu.

## Exemplo
O par do exemplo — then.status(200).header(content-type).body(ohi) — responde exatamente a um GET /translate?word=hello; para outro shape, o mock não matcheado fica silencioso e o assert ruidoso, que é o design inteiro.

## Limites e trade-offs
A lista de métodos completos do builder Then não é reproduzida na página da crate; os exemplos por método vivem na doc do struct, linkada da mesma página.

## Como verificar
A definição de Then e o uso com status/header/body vêm da documentação de itens e do exemplo oficial no docs.rs.

## Conexões
- [[httpmock-when-when]] — Veja também: When: as condições que o request tem que satisfazer.
- [[httpmock-assert-diagnostics]] — Veja também: O assert que vira laudo: diff do request mais parecido.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
