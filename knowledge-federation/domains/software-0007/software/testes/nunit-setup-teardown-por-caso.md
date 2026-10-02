---
id: software.testes.tranche11.000493
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/setup.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/teardown.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: reservar SetUp e TearDown para estado de cada caso

## Em uma frase
SetUp é chamado antes de cada test method e TearDown logo depois de cada test case na fixture.

## Por que importa
NUnit transforma attributes e fontes de dados em test cases e controla setup, teardown, fixtures e paralelismo; confundir esse lifecycle gera dependência entre casos. Setup compartilhado mutável pode deixar o resultado de um caso depender de qual método executou antes.

## Como funciona
Escolha dados e lifecycle pelo custo e isolamento desejados, verifique assinaturas async, configure concorrência de forma explícita e trate ordem como organização local, não como mecanismo de sincronização. Crie estado novo por teste e faça teardown idempotente que possa limpar recursos parcialmente alocados sem esconder falha.

## Exemplo
Cada caso cria arquivo temporário com nome único e remove-o no teardown mesmo se assertion falhar.

## Limites e trade-offs
Versão de NUnit, runner e configuração da assembly podem alterar APIs e execução. Parallelizable não torna recursos estáticos ou externos thread-safe, e um teste verde não prova todas as combinações de dados. Setup/teardown não limpam automaticamente servidor, banco externo ou processo iniciado fora da fixture.

## Como verificar
Provoque falha na preparação e no teste e observe se cleanup ainda libera recurso e se causa original permanece no resultado.

## Conexões
- [[nunit-testcasesource-fonte-enumeravel]] — Veja também: NUnit: separar conjunto de dados com TestCaseSource.
- [[nunit-onetimesetup-hierarquia-fixture]] — Veja também: NUnit: delimitar OneTimeSetUp à fixture e à hierarquia.

## Fontes
- [NUnit — SetUp attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/setup.html) — preparação de fixture por caso de teste; consultado em 2026-10-02.
- [NUnit — TearDown attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/teardown.html) — limpeza após o caso, inclusive tratamento após falha de setup/teste; consultado em 2026-10-02.
