---
id: software.testes.tranche11.000497
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/fixturelifecycle.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: distinguir Parallelizable de LevelOfParallelism

## Em uma frase
Parallelizable marca testes ou descendentes elegíveis para concorrência; LevelOfParallelism define o teto de workers da assembly.

## Por que importa
NUnit transforma attributes e fontes de dados em test cases e controla setup, teardown, fixtures e paralelismo; confundir esse lifecycle gera dependência entre casos. Configurar muitos workers não significa que testes sem marcação serão executados juntos nem que seus recursos são seguros.

## Como funciona
Escolha dados e lifecycle pelo custo e isolamento desejados, verifique assinaturas async, configure concorrência de forma explícita e trate ordem como organização local, não como mecanismo de sincronização. Marque apenas fixtures sem conflitos e limite worker count com base em banco, CPU e capacidade do ambiente.

## Exemplo
Uma fixture sem state compartilhado é marcada parallelizable; integração contra schema único usa NonParallelizable ou dados isolados.

## Limites e trade-offs
Versão de NUnit, runner e configuração da assembly podem alterar APIs e execução. Parallelizable não torna recursos estáticos ou externos thread-safe, e um teste verde não prova todas as combinações de dados. Configuração real depende do runner e pode reduzir concorrência além do teto declarado.

## Como verificar
Observe execução em log e verifique colisões com diferentes worker counts, não apenas a configuração textual.

## Conexões
- [[nunit-fixturelifecycle-instance-per-case]] — Veja também: NUnit: combinar lifecycle por caso com parallelism sem estado de instância.
- [[nunit-order-local-nao-sincroniza-conclusao]] — Veja também: NUnit: usar Order para organização local, nunca como dependência temporal.

## Fontes
- [NUnit — Parallelizable attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html) — marcação de testes paralelizáveis e separação da configuração máxima de workers; consultado em 2026-10-02.
- [NUnit — FixtureLifeCycle attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/fixturelifecycle.html) — instância compartilhada ou por test case e requisitos do lifecycle; consultado em 2026-10-02.
