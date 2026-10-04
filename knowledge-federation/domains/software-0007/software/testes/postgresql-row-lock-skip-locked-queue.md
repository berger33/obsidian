---
id: software.testes.tranche09.000274
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
fontes: ["https://www.postgresql.org/docs/current/explicit-locking.html", "https://www.postgresql.org/docs/current/transaction-iso.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED

## Em uma frase
Locks explícitos em linhas permitem que consumidores concorrentes reivindiquem trabalho sem processar o mesmo item simultaneamente.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. Uma suíte sequencial não revela se dois workers selecionam o mesmo item ou ficam bloqueados indefinidamente.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Coordene transações paralelas e valide a seleção com a cláusula de lock adequada ao desenho da fila.

## Exemplo
Worker A bloqueia a primeira tarefa, worker B usa SKIP LOCKED e recebe outra tarefa ainda disponível.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. SKIP LOCKED pula linhas bloqueadas e pode afetar justiça e ordenação; não equivale a uma fila globalmente ordenada.

## Como verificar
Rode vários workers com carga determinística e verifique ausência de processamento duplicado, bloqueio inesperado e starvation não tolerada.

## Conexões
- [[postgresql-unique-constraint-concorrencia]] — Veja também: PostgreSQL: validar unicidade sob inserções concorrentes.
- [[postgresql-deadlock-sqlstate-retry]] — Veja também: PostgreSQL: reproduzir deadlock e repetir operação inteira.

## Fontes
- [PostgreSQL — Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — locks de tabela/linha, conflitos, deadlocks e SKIP LOCKED; consultado em 2026-10-02.
- [PostgreSQL — Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — níveis de isolamento, snapshots e anomalias concorrentes; consultado em 2026-10-02.
