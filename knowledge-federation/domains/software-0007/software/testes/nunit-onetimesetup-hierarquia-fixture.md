---
id: software.testes.tranche11.000494
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/setup.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: delimitar OneTimeSetUp à fixture e à hierarquia

## Em uma frase
OneTimeSetUp executa uma vez antes dos testes filhos da fixture; classes base e derivadas seguem ordem de herança documentada.

## Por que importa
Confundir setup único com setup por teste pode compartilhar estado que uma assertion altera e tornar a suite não determinística.

## Como funciona
Use OneTimeSetUp apenas para recurso caro e realmente imutável durante os casos; crie/limpe dados mutáveis em SetUp/TearDown.

## Exemplo
A fixture conecta ao container uma vez e cada teste cria schema ou linha própria antes de exercitar o repository.

## Limites e trade-offs
Múltiplos métodos OneTimeSetUp na mesma classe têm ordem não definida; não use isso para sincronizar dependências.

## Como verificar
Registre número de chamadas por fixture e rode casos isolados para confirmar o limite de compartilhamento.

## Conexões
- [[nunit-setup-teardown-por-caso]] — Veja também: NUnit: reservar SetUp e TearDown para estado de cada caso.
- [[nunit-setupfixture-escopo-namespace]] — Veja também: NUnit: usar SetUpFixture para preparação de namespace conscientemente.

## Fontes
- [NUnit — OneTimeSetUp attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/onetimesetup.html) — setup único da fixture, herança e escopo de SetUpFixture; consultado em 2026-10-02.
- [NUnit — SetUp attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/setup.html) — preparação de fixture por caso de teste; consultado em 2026-10-02.
