---
id: software.testes.tranche24.001855
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

# O handle Mock: observar contagens e remover mocks

## Em uma frase
O struct Mock é documentado como "a reference to a mock configuration stored on a MockServer... used for interacting with, monitoring, and managing a specific mock's lifecycle, such as observing call counts or removing the mock from the server" — a configuração declarada no closure when/then ganha um identificador vivo no teste.

## Por que importa
Isso abre a faixa de asserções entre o teste-puro (assert de 1 chamada) e o teste-caótico: contar chamadas progressivamente durante uma rotina de retry, remover um mock no meio do teste para simular o backend "morrendo", e recriar outro para ver o fallback do cliente.

## Como funciona
Guarde o retorno de server.mock(...) (ou server.create_mock) para consultar contagens e deletar o mock depois; para extensões menos comuns, a crate oferece o trait MockExt, definido na própria doc como o que "extends the Mock structure with some additional functionality, that is usually not required".

## Exemplo
Fluxo de teste de resiliência com um único servidor: mock ativo → cliente faz 3 tentativas → assert por contagem → remove o mock → novo mock de erro → confere o circuit breaker do cliente — tudo com o handle documentado.

## Limites e trade-offs
As chamadas exatas (métodos de contagem/remoção) estão na página do struct, não na frase de sumário; a nota cobre a capacidade declarada pela descrição do item da API.

## Como verificar
A descrição do Mock e a definição de MockExt vêm das listas de Structs e Traits da página oficial no docs.rs.

## Conexões
- [[httpmock-assert-diagnostics]] — Veja também: O assert que vira laudo: diff do request mais parecido.
- [[httpmock-record-playback]] — Veja também: Record and Playback: gravar o backend real para replay.

## Fontes
- [Crate httpmock 0.8.3 no docs.rs](https://docs.rs/httpmock/latest/httpmock/) — Documentação oficial da crate httpmock 0.8.3 no docs.rs com features, exemplo Getting Started, diagnóstico de assert e referência de structs.; consultado em 2026-10-03.
- [Repositório oficial httpmock/httpmock](https://github.com/httpmock/httpmock) — Repositório oficial do httpmock no GitHub com código-fonte, especificação de mocks em YAML, modo standalone e diretório de testes.; consultado em 2026-10-03.
