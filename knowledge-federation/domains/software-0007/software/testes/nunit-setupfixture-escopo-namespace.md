---
id: software.testes.tranche11.000495
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html", "https://docs.nunit.org/articles/nunit/writing-tests/TestContext.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: usar SetUpFixture para preparação de namespace conscientemente

## Em uma frase
SetUpFixture oferece setup e teardown únicos para fixtures pertencentes a namespace e subnamespaces na assembly.

## Por que importa
Preparação de ambiente repetida por fixture pode ser cara, mas ampliá-la à assembly inteira sem intenção afeta testes sem relação.

## Como funciona
Coloque SetUpFixture dentro do namespace adequado, limite seu efeito e mantenha no máximo setup e teardown únicos do nível.

## Exemplo
Vários fixtures de integração sob namespace database-test usam servidor local iniciado uma vez e recebem teardown após concluírem.

## Limites e trade-offs
Fixtures no mesmo nível podem ter ordem indeterminada; dependência em sequência entre namespaces deve ser removida ou modelada fora do runner.

## Como verificar
Execute fixture de outro namespace e confirme que não herda o recurso; observe início e descarte da configuração compartilhada.

## Conexões
- [[nunit-onetimesetup-hierarquia-fixture]] — Veja também: NUnit: delimitar OneTimeSetUp à fixture e à hierarquia.
- [[nunit-fixturelifecycle-instance-per-case]] — Veja também: NUnit: combinar lifecycle por caso com parallelism sem estado de instância.

## Fontes
- [NUnit — OneTimeSetUp attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html) — setup único da fixture, herança e escopo de SetUpFixture; consultado em 2026-10-02.
- [NUnit — TestContext](https://docs.nunit.org/articles/nunit/writing-tests/TestContext.html) — contexto por caso ou fixture e informações/resultados de execução; consultado em 2026-10-02.
