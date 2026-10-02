---
id: software.testes.tranche09.000277
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://www.postgresql.org/docs/current/functions-sequence.html", "https://www.postgresql.org/docs/current/ddl-constraints.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: não testar sequences como contador sem lacunas

## Em uma frase
Valores retornados por sequences podem ser consumidos mesmo quando a transação que pediu o valor é abortada.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Assumir IDs contíguos depois de rollback torna teste frágil e confunde identificador técnico com regra de negócio.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Afirme apenas unicidade e associação correta do identificador; teste numeração sem lacunas por mecanismo de domínio separado.

## Exemplo
Uma transação insere e faz rollback, a seguinte recebe outro ID e o teste valida existência e referência sem exigir sequência adjacente.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. A semântica depende da sequence usada; não transforme seu valor em ordem temporal nem comprovante de commit.

## Como verificar
Execute rollback intencional, inspecione o próximo valor e confirme que as assertions funcionais não dependem de gaplessness.

## Conexões
- [[postgresql-explain-analyze-execucao-side-effects]] — Veja também: PostgreSQL: tratar EXPLAIN ANALYZE como execução.
- [[postgresql-timestamptz-session-timezone]] — Veja também: PostgreSQL: testar timestamptz com timezone explícito.

## Fontes
- [PostgreSQL — Sequence functions](https://www.postgresql.org/docs/current/functions-sequence.html) — alocação de valores de sequência e efeitos fora do rollback transacional; consultado em 2026-10-02.
- [PostgreSQL — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — constraints de integridade declaradas no banco; consultado em 2026-10-02.
