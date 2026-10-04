---
id: software.testes.tranche08.000206
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html", "https://docs.confluent.io/platform/current/clients/client-configs.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kafka: separar erro transitório de erro permanente

## Em uma frase
Defina quais falhas serão repetidas e quais irão para tratamento terminal, mantendo observável a origem e a contagem de tentativas.

## Por que importa
Retry infinito em payload inválido pode bloquear progresso; descarte silencioso transforma erro conhecido em perda de informação.

## Como funciona
Classifique falhas, imponha política de backoff e limite, preserve identificador e motivo ao encaminhar para DLQ, e torne reprocessamento controlado.

## Exemplo
Timeout do serviço externo entra em retry limitado; schema impossível de interpretar vai para fila de erro com contexto seguro e alerta.

## Limites e trade-offs
DLQ não corrige causa nem garante ordem com fluxo principal; política de retenção e replay pode afetar duplicidade e consistência.

## Como verificar
Injete falha temporária e permanente, confira tentativas, progresso de partição, evento terminal e possibilidade de replay sem vazar segredo.

## Conexões
- [[kafka-producer-callback-delivery-failure]] — Veja também: Kafka: observar falhas de entrega no produtor.
- [[kafka-at-least-once-consumidor-idempotente]] — Veja também: Kafka: tornar efeitos do consumidor seguros contra redelivery.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
