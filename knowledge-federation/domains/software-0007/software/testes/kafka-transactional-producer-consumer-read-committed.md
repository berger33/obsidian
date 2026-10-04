---
id: software.testes.tranche08.000202
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

# Kafka: testar transações com consumidor read-committed

## Em uma frase
Valide transações Kafka exercitando produtor transacional e consumidor configurado para observar apenas dados comprometidos.

## Por que importa
Um teste que só lê registros pode não distinguir lote abortado de transação comprometida se isolamento do consumidor não corresponder ao cenário.

## Como funciona
Use transactional.id, inicialização e commit/abort conforme API do cliente; configure consumidor com isolamento documentado e observe offsets e registros após cada resultado.

## Exemplo
Produza um lote e aborte a transação; consumidor read-committed não apresenta os registros abortados, enquanto o cenário comprometido os torna visíveis.

## Limites e trade-offs
A garantia cobre operações Kafka participantes da transação; gravar em banco externo ou chamar API exige coordenação adicional ou idempotência.

## Como verificar
Teste commit, abort e reinício do producer, confirme configuração do consumidor e assegure que resultados respeitam fronteira transacional.

## Conexões
- [[kafka-offset-commit-proximo-registro]] — Veja também: Kafka: verificar semântica de offset committed.
- [[kafka-at-least-once-consumidor-idempotente]] — Veja também: Kafka: tornar efeitos do consumidor seguros contra redelivery.

## Fontes
- [Confluent — Producer configuration](https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html) — idempotência, retries, acks, ordenação e transações; consultado em 2026-10-02.
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
