---
id: software.testes.tranche08.000201
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
fontes: ["https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html", "https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kafka: delimitar ordenação por partição

## Em uma frase
Especifique a ordem exigida por chave e partição antes de afirmar que o produtor preserva a ordem global dos eventos.

## Por que importa
Kafka ordena registros dentro de uma partição, enquanto chaves diferentes podem seguir partições distintas e não têm ordem total entre si.

## Como funciona
Escolha chave de partição coerente com a entidade cuja sequência importa. Teste retries, número de requests em voo e comportamento de consumidor por partição.

## Exemplo
Atualizações do mesmo pedido usam chave estável e consumidor confere versão monotônica; eventos de pedidos diferentes não são comparados por ordem global.

## Limites e trade-offs
Ordem de partição não resolve eventos atrasados na origem, mudança de estratégia de partição ou efeitos assíncronos downstream.

## Como verificar
Publique eventos sequenciais para mesma chave e chaves diferentes; compare offsets por partição após retry e rebalance.

## Conexões
- [[kafka-rebalance-processamento-em-curso]] — Veja também: Kafka: testar rebalance com processamento em andamento.
- [[kafka-offset-commit-proximo-registro]] — Veja também: Kafka: verificar semântica de offset committed.

## Fontes
- [Confluent — Producer configuration](https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html) — idempotência, retries, acks, ordenação e transações; consultado em 2026-10-02.
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
