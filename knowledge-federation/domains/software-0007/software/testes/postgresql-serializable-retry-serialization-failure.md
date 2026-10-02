---
id: software.testes.tranche09.000271
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
fontes: ["https://www.postgresql.org/docs/current/transaction-iso.html", "https://www.postgresql.org/docs/current/errcodes-appendix.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: repetir transação após serialization failure

## Em uma frase
Uma transação SERIALIZABLE pode abortar quando concorrência produzir uma execução que não possa ser serializada.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Tratar esse aborto como erro permanente ou repetir somente o statement final pode deixar a operação incompleta.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Detecte SQLSTATE 40001 e repita a unidade transacional inteira com limite e política de espera apropriados ao serviço.

## Exemplo
Duas reservas competem por uma regra de capacidade; uma tentativa é refeita e a asserção final confirma que o limite continua respeitado.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Retry excessivo mascara contenda e não substitui idempotência de efeitos fora do banco.

## Como verificar
Force interleaving concorrente, registre tentativas e verifique que commits finais respeitam a invariante sem repetir efeitos externos.

## Conexões
- [[postgresql-read-committed-snapshot-por-statement]] — Veja também: PostgreSQL: testar snapshots no READ COMMITTED.
- [[postgresql-mvcc-concurrent-read-write]] — Veja também: PostgreSQL: testar visibilidade MVCC entre conexões.

## Fontes
- [PostgreSQL — Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — níveis de isolamento, snapshots e anomalias concorrentes; consultado em 2026-10-02.
- [PostgreSQL — Error codes](https://www.postgresql.org/docs/current/errcodes-appendix.html) — SQLSTATEs estáveis para classificar erros do servidor; consultado em 2026-10-02.
