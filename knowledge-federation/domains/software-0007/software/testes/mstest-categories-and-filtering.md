---
id: software.testes.tranche15.000938
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
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: classificar testes para seleção

## Em uma frase
Atributos de categoria e propriedade rotulam testes para filtragem no executor, permitindo selecionar subconjuntos por tipo ou risco.

## Por que importa
Rodar tudo em cada verificação encarece o feedback, e a seleção sem critério declarado tende a excluir casos por conveniência.

## Como funciona
Marque casos com categorias estáveis, documente o significado de cada uma e use filtros na linha de comando para montar os conjuntos.

## Exemplo
`[TestCategory(\"Smoke\")]` permite executar apenas o conjunto rápido em validações intermediárias, mantendo a suíte completa para o fechamento.

## Limites e trade-offs
Categorias viram nomes mágicos se ninguém as mantiver, e filtros errados podem deixar de executar testes importantes sem que o pipeline perceba.

## Como verificar
Liste os testes de uma categoria, execute o filtro correspondente e confirme que o conjunto selecionado coincide com o definido pelo time.

## Conexões
- [[mstest-timeout-and-retry]] — Veja também: MSTest: limitar tempo e tratar repetição.
- [[mstest-runsettings-vs-testconfig]] — Veja também: MSTest: escolher o arquivo de configuração.

## Fontes
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
- [MSTest — Configure](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure) — runsettings, testconfig.json, paralelização, timeouts e retries; consultado em 2026-10-02.
