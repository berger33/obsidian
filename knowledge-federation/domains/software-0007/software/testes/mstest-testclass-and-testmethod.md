---
id: software.testes.tranche15.000930
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
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests", "https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=visualstudio"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: reconhecer a estrutura de um teste

## Em uma frase
Métodos de teste são marcados com `[TestMethod]` dentro de classes anotadas com `[TestClass]`, e precisam ser públicos, de instância e sem parâmetros fora de casos com dados.

## Por que importa
A forma declarada define o que o executor descobre; método estático, privado ou com retorno inválido simplesmente não roda e costuma gerar confusão silenciosa.

## Como funciona
Declare a classe e o método com os atributos correspondentes, mantendo o retorno como `void`, `Task` ou `ValueTask` conforme a operação.

## Exemplo
`[TestClass] public class CalculadoraTests { [TestMethod] public void Soma_RetornaTotal() { Assert.AreEqual(4, Calculadora.Soma(2, 2)); } }` mostra a estrutura aceita.

## Limites e trade-offs
Regras de assinatura mudam entre versões do framework, e a mensagem de descoberta vazia é o sintoma típico de um método fora do formato esperado.

## Como verificar
Compile a suíte e confirme a contagem de testes descobertos; torne um método estático e observe que ele deixa de ser executado.

## Conexões
- [[mstest-datarow-inline]] — Veja também: MSTest: fornecer casos inline com DataRow.

## Fontes
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
- [MSTest — Assert API](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.assert?view=visualstudio) — asserções de igualdade, coleções, exceções e mensagens; consultado em 2026-10-02.
