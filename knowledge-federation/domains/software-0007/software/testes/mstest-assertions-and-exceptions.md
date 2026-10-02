---
id: software.testes.tranche15.000935
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
fontes: ["https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=visualstudio", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: afirmar valores e exceções

## Em uma frase
O tipo `Assert` reúne comparações de igualdade, verificações de coleção e asserções de exceção que falham com mensagem específica.

## Por que importa
Asserções genéricas escondem o motivo da falha, e verificar exceção de forma incorreta aceita tipos derivados ou deixa passar ausência de erro.

## Como funciona
Escolha o método adequado ao valor, informe mensagem quando o diagnóstico precisar de contexto e use a asserção de exceção exata para o tipo esperado.

## Exemplo
`Assert.ThrowsExactly<DivideByZeroException>(() => Calculadora.Divide(1, 0))` confirma o tipo exato, e `Assert.AreEqual` verifica o valor previsto.

## Limites e trade-offs
Capturar exceção manualmente com bloco genérico permite que o teste passe quando nenhuma exceção é lançada, e igualdade de ponto flutuante exige tolerância.

## Como verificar
Substitua uma exceção por uma classe derivada e confirme que a asserção exata falha, enquanto a verificação de tipo base continuaria aceitando.

## Conexões
- [[mstest-testcontext]] — Veja também: MSTest: usar TestContext para informações de execução.
- [[mstest-parallelization]] — Veja também: MSTest: configurar paralelização.

## Fontes
- [MSTest — Assert API](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=visualstudio) — asserções de igualdade, coleções, exceções e mensagens; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
