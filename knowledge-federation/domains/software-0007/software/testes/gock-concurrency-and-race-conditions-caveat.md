---
id: software.testes.tranche25.001934
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

# Concorrência e condições de corrida: declarar mocks antes de disparar goroutines

## Em uma frase
Na subseção Race conditions em Tips, o README faz um alerta direto: se você estiver executando código concorrente, declare todos os seus mocks primeiro para evitar condições de corrida inesperadas ao configurar o gock ou interceptar clientes HTTP customizados, acrescentando que "gock is not fully thread-safe, but sensible parts are".

## Por que importa
Em Go é muito comum que o código sob teste dispare goroutines que fazem requisições HTTP em paralelo; se o próprio teste continuar chamando gock.New(...) ou gock.InterceptClient(...) enquanto essas goroutines já estão trafegando pelo transporte interceptado, podem ocorrer data races na configuração.

## Como funciona
Configure todos os mocks (gock.New...) e eventuais interceptações de clientes customizados na thread principal do teste antes de iniciar as goroutines ou o componente concorrente sob teste.

## Exemplo
Em um teste de worker pool que faz chamadas HTTP concorrentes, toda a cadeia de gock.New("http://server.com") é registrada de forma síncrona no início do teste antes de dar start nos workers.

## Limites e trade-offs
A ressalva "gock is not fully thread-safe, but sensible parts are" é literal dos mantenedores no README: rodar sob go test -race exige respeitar estritamente a separação entre fase de declaração dos mocks e fase de execução concorrente.

## Como verificar
Conferi a subseção Race conditions na seção Tips do README oficial.

## Conexões
- [[gock-ordering-concrete-before-generic]] — Veja também: Dica de precedência: declarar mocks mais concretos antes dos genéricos.
- [[gock-custom-http-client-intercept-and-restore]] — Veja também: Clientes customizados: gock.InterceptClient(client) uma vez e defer gock.RestoreClient(client).

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [Repositório oficial h2non/gock](https://github.com/h2non/gock) — Repositório oficial do gock no GitHub com código-fonte sem dependências externas e diretório _examples.; consultado em 2026-10-03.
