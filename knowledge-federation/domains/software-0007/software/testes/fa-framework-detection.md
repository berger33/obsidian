---
id: software.testes.tranche22.001595
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://www.fluentassertions.com/introduction", "https://fluentassertions.com/extensibility/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FluentAssertions: detecta o framework de teste por baixo

## Em uma frase
O FluentAssertions não exige configuração de framework: você adiciona a referência do seu test framework ao projeto e a biblioteca encontra a assembly, usando-a para lançar a exceção específica daquele executor.

## Por que importa
Trocar de NUnit para xUnit não deveria riscar asserções; a detecção mantém a biblioteca acoplada ao erro certo de cada runner sem linha de setup.

## Como funciona
Se a detecção falhar por setup exótico, especifique manualmente GlobalConfiguration.TestFramework — os valores citados incluem XUnit2, XUnit3, TUnit, MsTest, NUnit, MSpec e MsTest4 — e sem nenhum framework encontrado ele recorre a um AssertionFailedException próprio.

## Exemplo
A própria página manda instalar o NuGet "FluentAssertions" no test project e só: nenhuma outra ligação de asserção é documentada como obrigatória.

## Limites e trade-offs
A lista de frameworks suportados é do site atual; releases antigas da biblioteca tinham outro conjunto — cheque a versão que sua suíte consome antes de copiar o snippet.

## Como verificar
Comente a referência do seu executor, rode um teste com asserção quebrada e veja o fallback AssertionFailedException substituir o formato nativo.

## Conexões
- [[fa-assertion-scope]] — Veja também: FluentAssertions: AssertionScope acumula falhas.
- [[fa-subject-identification]] — Veja também: FluentAssertions: o nome da variável no erro.

## Fontes
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
- [FluentAssertions — Extensibility](https://fluentassertions.com/extensibility/) — página para onde a Introduction delega GlobalConfiguration.TestFramework; consultado em 2026-10-03.
