---
id: software.testes.tranche11.000499
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
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/TestContext.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/teardown.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: ler TestContext no escopo de execução correto

## Em uma frase
TestContext fornece dados do execution context e distingue contexto de caso em método/setup/teardown de contexto de fixture nos métodos one-time.

## Por que importa
Buscar argumentos de test case em OneTimeSetUp ou compartilhar resultado do fixture como se fosse de um caso pode produzir diagnóstico incorreto.

## Como funciona
Leia properties e argumentos no contexto apropriado e acrescente diagnostics associados ao caso sem transformar saída em assertion oculta.

## Exemplo
O teardown registra identificador do caso que falhou e relatório do fixture registra apenas metadado de inicialização.

## Limites e trade-offs
Somente assertions falhas são armazenadas em certos resultados e APIs podem depender da fase do lifecycle.

## Como verificar
Gere uma falha em setup e outra no teste e compare TestContext e arquivos de saída associados a cada fase.

## Conexões
- [[nunit-order-local-nao-sincroniza-conclusao]] — Veja também: NUnit: usar Order para organização local, nunca como dependência temporal.

## Fontes
- [NUnit — TestContext](https://docs.nunit.org/articles/nunit/writing-tests/TestContext.html) — contexto por caso ou fixture e informações/resultados de execução; consultado em 2026-10-02.
- [NUnit — TearDown attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/teardown.html) — limpeza após o caso, inclusive tratamento após falha de setup/teste; consultado em 2026-10-02.
