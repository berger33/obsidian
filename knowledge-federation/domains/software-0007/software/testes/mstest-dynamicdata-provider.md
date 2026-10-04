---
id: software.testes.tranche15.000932
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

# MSTest: gerar dados com DynamicData

## Em uma frase
O atributo `[DynamicData]` referencia uma propriedade ou método que devolve uma coleção de linhas, permitindo dados calculados ou objetos tipados.

## Por que importa
Valores que dependem de lógica, cultura ou geração programática não cabem em atributos constantes e precisam de um provedor verificável.

## Como funciona
Declare o provedor como estático, devolva uma sequência de arrays ou objetos tipados e mantenha nomes claros para diagnosticar cada caso.

## Exemplo
`[DynamicData(nameof(Casos))]` aponta para uma propriedade estática que devolve tuplas com entrada e resultado esperado.

## Limites e trade-offs
O provedor roda durante a descoberta, então erro nele impede a suíte inteira de iniciar; dados gerados aleatoriamente sem semente tornam a falha irreproduzível.

## Como verificar
Introduza um caso inválido no provedor e confirme que o executor reporta o erro de descoberta com a origem correta.

## Conexões
- [[mstest-datarow-inline]] — Veja também: MSTest: fornecer casos inline com DataRow.
- [[mstest-lifecycle-order]] — Veja também: MSTest: respeitar a ordem do ciclo de vida.

## Fontes
- [Microsoft — Data-driven unit test](https://learn.microsoft.com/en-us/visualstudio/test/how-to-create-a-data-driven-unit-test?view=visualstudio) — DataRow, DynamicData, DataSource e acesso por TestContext; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
