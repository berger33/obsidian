---
id: software.testes.tranche09.000278
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
fontes: ["https://www.postgresql.org/docs/current/datatype-datetime.html", "https://www.postgresql.org/docs/current/transaction-iso.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: testar timestamptz com timezone explícito

## Em uma frase
Valores timestamp with time zone são normalizados internamente e apresentados segundo a configuração de fuso da sessão.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Testes que dependem do fuso local do executor podem divergir em CI e produzir erros em fronteiras de data.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Grave instantes inequívocos com offset, controle TimeZone da sessão e compare instantes em vez de strings formatadas.

## Exemplo
Uma reserva em horário de verão é inserida com offset explícito e consultada em sessão UTC e em outra zona.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Conversões de horário civil ambíguo exigem regra de produto e não podem ser inferidas somente do tipo SQL.

## Como verificar
Rode a fixture em zonas distintas, teste limites de dia e horário de verão e verifique o instante retornado.

## Conexões
- [[postgresql-sequence-valores-nao-gapless]] — Veja também: PostgreSQL: não testar sequences como contador sem lacunas.
- [[postgresql-sqlstate-assertion-errors]] — Veja também: PostgreSQL: afirmar SQLSTATE em vez de texto de erro.

## Fontes
- [PostgreSQL — Date/time types](https://www.postgresql.org/docs/current/datatype-datetime.html) — semântica dos tipos temporais e fuso horário da sessão; consultado em 2026-10-02.
- [PostgreSQL — Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — níveis de isolamento, snapshots e anomalias concorrentes; consultado em 2026-10-02.
