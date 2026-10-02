---
id: software.testes.tranche09.000275
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
fontes: ["https://www.postgresql.org/docs/current/explicit-locking.html", "https://www.postgresql.org/docs/current/errcodes-appendix.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PostgreSQL: reproduzir deadlock e repetir operação inteira

## Em uma frase
Locks obtidos em ordens incompatíveis podem formar deadlock; PostgreSQL aborta uma transação para permitir progresso da outra.

## Por que importa
Testes de banco precisam validar semântica de transações e constraints sob concorrência, não somente o resultado de uma execução sequencial. O teste só de timeout não distingue deadlock detectado de bloqueio prolongado, e retentar dentro da transação abortada não a recupera.

## Como funciona
Use conexões independentes e barreiras explícitas para reproduzir races; examine SQLSTATE e estado final em vez de depender apenas de texto de erro. Use duas conexões e barreiras para inverter ordem de locks; após rollback, a aplicação inicia novamente a transação completa quando apropriado.

## Exemplo
Transação A bloqueia linha 1 e espera 2, B bloqueia 2 e tenta 1; a aplicação reconhece SQLSTATE 40P01.

## Limites e trade-offs
Concorrência depende de versão, nível de isolamento, plano e timing; testes de carga e testes de propriedades complementam casos determinísticos. Retry precisa ter limite e considerar efeitos não transacionais, carga e idempotência da operação.

## Como verificar
Confirme qual transação foi abortada, libere as conexões e valide invariante final após nova tentativa com instrumentação de lock.

## Conexões
- [[postgresql-row-lock-skip-locked-queue]] — Veja também: PostgreSQL: testar filas com FOR UPDATE SKIP LOCKED.
- [[postgresql-explain-analyze-execucao-side-effects]] — Veja também: PostgreSQL: tratar EXPLAIN ANALYZE como execução.

## Fontes
- [PostgreSQL — Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — locks de tabela/linha, conflitos, deadlocks e SKIP LOCKED; consultado em 2026-10-02.
- [PostgreSQL — Error codes](https://www.postgresql.org/docs/current/errcodes-appendix.html) — SQLSTATEs estáveis para classificar erros do servidor; consultado em 2026-10-02.
