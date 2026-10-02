---
id: software.testes.tranche11.000496
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/fixturelifecycle.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: combinar lifecycle por caso com parallelism sem estado de instância

## Em uma frase
FixtureLifeCycle pode usar instância única por fixture ou instância nova por test case.

## Por que importa
Instância única expõe campos mutáveis compartilhados quando testes executam paralelamente; instância nova reduz essa fonte, mas não protege recursos estáticos.

## Como funciona
Avalie InstancePerTestCase para campos de teste independentes e torne OneTimeSetUp/OneTimeTearDown estáticos quando essa opção exigir.

## Exemplo
Dois casos alteram contador de instância próprio em paralelo, enquanto conexão estática é substituída por fixture controlada.

## Limites e trade-offs
Lifecycle por caso não isola arquivos, singleton, ambiente de processo ou banco compartilhado.

## Como verificar
Execute em paralelo e instrumente identidade da fixture e acesso aos recursos externos para identificar estado realmente compartilhado.

## Conexões
- [[nunit-setupfixture-escopo-namespace]] — Veja também: NUnit: usar SetUpFixture para preparação de namespace conscientemente.
- [[nunit-parallelizable-nao-e-limite-de-workers]] — Veja também: NUnit: distinguir Parallelizable de LevelOfParallelism.

## Fontes
- [NUnit — FixtureLifeCycle attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/fixturelifecycle.html) — instância compartilhada ou por test case e requisitos do lifecycle; consultado em 2026-10-02.
- [NUnit — Parallelizable attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html) — marcação de testes paralelizáveis e separação da configuração máxima de workers; consultado em 2026-10-02.
