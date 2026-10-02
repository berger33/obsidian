# MOC — Dados distribuídos e eventos

Notas autorais do lote editorial `software-dados-distribuidos-0004`. O mapa é navegação, não validação factual.

## Persistência e consultas
- [[mvcc-isolamento-transacoes-postgresql]] — snapshots e níveis de isolamento no PostgreSQL.
- [[explain-analyze-planos-consulta-postgresql]] — estimativas e execução observada de consultas.
- [[indice-btree-multicolunas-postgresql]] — ordem das chaves e padrões de consulta.
- [[sql-parametrizacao-consultas]] — separação entre valores e código SQL.

## Eventos e compatibilidade
- [[outbox-transacional-publicacao-eventos]] — coordenação entre commit local e publicação.
- [[entrega-kafka-at-least-once-consumidor-idempotente]] — offsets, reprocessamento e duplicatas.
- [[evolucao-esquemas-eventos-avro-registry]] — compatibilidade entre produtores e consumidores.

## Contratos de API
- [[concorrencia-otimista-etag-if-match]] — precondições para evitar sobrescritas concorrentes.
- [[paginacao-por-cursor-api]] — percorrer coleções por token de continuação.
- [[contrato-openapi-http]] — documentação de interfaces HTTP.

## Revisão
As 8 notas do lote 0004 tiveram revisão factual humana confirmada pelo usuário em 2026-10-02 e contam como válidas; o passe automático, isoladamente, não substitui essa revisão.
