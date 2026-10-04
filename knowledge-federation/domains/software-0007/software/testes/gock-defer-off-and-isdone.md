---
id: software.testes.tranche25.001932
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

# Ciclo de vida no teste: defer gock.Off() e verificação de pendências com gock.IsDone()

## Em uma frase
Nas seções Tips (Testing e Disable gock traffic interception once done) e nos exemplos de código, o README recomenda declarar defer gock.Off() logo no início de cada função TestFoo(t *testing.T) para limpar mocks pendentes e desativar a interceptação ao término do teste, e usar gock.IsDone() ao final do teste para verificar que não restaram mocks pendentes não consumidos.

## Por que importa
Sem defer gock.Off(), um mock que deixou de ser consumido num teste que falhou cedo permanece ativo no pool global e pode interceptar requisições de testes subsequentes no mesmo pacote; já gock.IsDone() garante que o código sob teste realmente realizou todas as chamadas HTTP esperadas.

## Como funciona
Comece toda função de teste que usa gock com defer gock.Off(), declare os mocks em seguida, execute o código sob teste e encerre afirmando que gock.IsDone() é verdadeiro.

## Exemplo
Em todos os exemplos do README (TestSimple, TestMatchHeaders, TestMatchParams, TestMockSimple), a primeira linha da função é defer gock.Off() e a última linha verifica st.Expect(t, gock.IsDone(), true).

## Limites e trade-offs
Chamar gock.Off() limpa o estado global de interceptação, mas clientes http.Client customizados que sofreram interceptação explícita também devem ser restaurados com gock.RestoreClient(client), como explica a dica específica do README.

## Como verificar
Conferi as subseções Testing e Disable gock traffic interception once done e os exemplos do README oficial.

## Conexões
- [[gock-how-it-mocks-four-steps]] — Veja também: Como o gock funciona: RoundTripper, fila FIFO e modo de rede real opcional.
- [[gock-ordering-concrete-before-generic]] — Veja também: Dica de precedência: declarar mocks mais concretos antes dos genéricos.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
