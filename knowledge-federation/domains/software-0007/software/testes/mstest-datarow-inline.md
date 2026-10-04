---
id: software.testes.tranche15.000931
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://learn.microsoft.com/en-us/visualstudio/test/how-to-create-a-data-driven-unit-test?view=visualstudio", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: fornecer casos inline com DataRow

## Em uma frase
O atributo `[DataRow]` declara valores constantes para os parâmetros do teste, e cada linha gera uma execução independente identificada pelos dados.

## Por que importa
Casos de fronteira ficam visíveis no mesmo método, evitando funções duplicadas que divergem com o tempo.

## Como funciona
Aplique uma linha por combinação relevante, mantendo os valores legíveis e os parâmetros na mesma ordem das linhas.

## Exemplo
`[TestMethod] [DataRow(2, 3, 5)] [DataRow(-1, 1, 0)] public void Soma(int a, int b, int esperado) { ... }` cobre dois casos em uma função.

## Limites e trade-offs
`DataRow` aceita apenas constantes, e tipos como datas ou objetos complexos exigem outra fonte de dados; a quantidade de linhas também cresce rápido com muitas dimensões.

## Como verificar
Execute o método e confirme uma entrada por linha no relatório; remova uma linha e verifique que a contagem de casos caiu exatamente um.

## Conexões
- [[mstest-testclass-and-testmethod]] — Veja também: MSTest: reconhecer a estrutura de um teste.
- [[mstest-dynamicdata-provider]] — Veja também: MSTest: gerar dados com DynamicData.

## Fontes
- [Microsoft — Data-driven unit test](https://learn.microsoft.com/en-us/visualstudio/test/how-to-create-a-data-driven-unit-test?view=visualstudio) — DataRow, DynamicData, DataSource e acesso por TestContext; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
