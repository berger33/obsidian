---
id: software.testes.tranche11.000492
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcasesource.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcase.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: separar conjunto de dados com TestCaseSource

## Em uma frase
TestCaseSource identifica campo, propriedade ou método que fornece argumentos para casos parametrizados.

## Por que importa
Fonte explícita permite compartilhar dados de domínio sem entupir assinatura do teste ou duplicar matrizes.

## Como funciona
Use source que retorna IEnumerable e mantenha seus dados determinísticos; confira requisito de membro static para as formas documentadas.

## Exemplo
Um source fornece entradas de moeda e arredondamento com resultado esperado para dois testes que compartilham o mesmo conjunto.

## Limites e trade-offs
Fontes async e IAsyncEnumerable têm suporte dependente de versão NUnit; não presuma compatibilidade com versões antigas.

## Como verificar
Execute discovery com a versão do runner do projeto e confirme nomes, contagem e argumentos dos casos gerados.

## Conexões
- [[nunit-testcase-cada-argumento-caso]] — Veja também: NUnit: interpretar cada TestCase como caso parametrizado separado.
- [[nunit-setup-teardown-por-caso]] — Veja também: NUnit: reservar SetUp e TearDown para estado de cada caso.

## Fontes
- [NUnit — TestCaseSource attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcasesource.html) — fontes estáticas de casos, sequências e versões com dados assíncronos; consultado em 2026-10-02.
- [NUnit — TestCase attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/testcase.html) — argumentos inline e criação de casos parametrizados; consultado em 2026-10-02.
