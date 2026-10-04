---
id: software.testes.tranche15.000934
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
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests-lifecycle", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: usar TestContext para informações de execução

## Em uma frase
O executor injeta um objeto `TestContext` no teste, oferecendo informações de execução, resultado da linha de dados e saída de diagnóstico associada ao caso.

## Por que importa
Acessar dados por índice ou depender de saída padrão sem contexto dificulta associar mensagem ao caso correto, especialmente em execuções paralelas.

## Como funciona
Declare a propriedade pública de contexto, use-a para ler dados e registre diagnóstico por ela, evitando estado estático compartilhado entre testes.

## Exemplo
`public TestContext Contexto { get; set; }` é preenchida pelo framework, e a saída é associada ao caso mesmo com execução concorrente.

## Limites e trade-offs
O contexto muda de instância conforme o nível e não deve ser guardado em campo estático; o objeto não substitui a asserção que define o resultado.

## Como verificar
Escreva uma mensagem de diagnóstico em um caso aprovado e outra em caso falho e confirme que a saída aparece associada a cada teste no relatório.

## Conexões
- [[mstest-lifecycle-order]] — Veja também: MSTest: respeitar a ordem do ciclo de vida.
- [[mstest-assertions-and-exceptions]] — Veja também: MSTest: afirmar valores e exceções.

## Fontes
- [MSTest — Test lifecycle](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests-lifecycle) — ordem de inicialização e limpeza em nível de assembly, classe e teste; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
