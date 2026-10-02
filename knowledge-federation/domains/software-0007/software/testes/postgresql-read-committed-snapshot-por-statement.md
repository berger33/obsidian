---
id: software.testes.tranche09.000270
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
fontes: ["https://www.postgresql.org/docs/current/transaction-iso.html", "https://www.postgresql.org/docs/current/mvcc.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: testar snapshots no READ COMMITTED

## Em uma frase
No READ COMMITTED do PostgreSQL, cada comando de uma transação vê um snapshot iniciado para aquele comando, não necessariamente o mesmo do comando anterior.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Um teste que presume snapshot estável em toda a transação pode aprovar lógica de leitura-modificação que observa concorrência entre statements.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Use duas conexões coordenadas para atualizar uma linha entre a primeira e a segunda leitura da transação observadora.

## Exemplo
A conexão A lê saldo, B confirma uma atualização e A consulta novamente; o teste registra o valor visto em cada statement.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Esse comportamento é específico do nível de isolamento e não deve ser generalizado a REPEATABLE READ ou SERIALIZABLE.

## Como verificar
Fixe explicitamente o isolamento, coordene as barreiras e confirme tanto os snapshots quanto a ordem de commit registrada.

## Conexões
- [[postgresql-serializable-retry-serialization-failure]] — Veja também: PostgreSQL: repetir transação após serialization failure.

## Fontes
- [PostgreSQL — Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — níveis de isolamento, snapshots e anomalias concorrentes; consultado em 2026-10-02.
- [PostgreSQL — MVCC](https://www.postgresql.org/docs/current/mvcc.html) — controle de concorrência multiversão e visibilidade de linhas; consultado em 2026-10-02.
