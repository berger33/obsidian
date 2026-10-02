---
id: software.testes.tranche08.000200
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
fontes: ["https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html", "https://docs.confluent.io/platform/current/clients/client-configs.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kafka: testar produtor idempotente e confirmação

## Em uma frase
Teste retries, acknowledgements e idempotência como configuração conjunta, não como três flags independentes.

## Por que importa
Retries podem duplicar ou reordenar efeitos se produtor, broker e limites de requests não satisfizerem as condições exigidas.

## Como funciona
Verifique configuração efetiva do producer, falha transitória e confirmação do broker. Confirme se idempotência está habilitada e se combinações de acks e requests são compatíveis.

## Exemplo
Interrompa temporariamente broker durante publicação, restaure serviço e valide que consumidor recebe o evento esperado sem duplicação produzida pelo retry.

## Limites e trade-offs
Idempotência do produtor trata duplicatas de envio sob escopo documentado; ela não torna idempotentes efeitos do consumidor nem transações externas.

## Como verificar
Leia a configuração final, injete falha transitória e compare sequência/contagem no tópico; verifique logs e callbacks de entrega.

## Conexões
- [[kafka-at-least-once-consumidor-idempotente]] — Veja também: Kafka: tornar efeitos do consumidor seguros contra redelivery.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Veja também: Kafka: separar erro transitório de erro permanente.

## Fontes
- [Confluent — Producer configuration](https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html) — idempotência, retries, acks, ordenação e transações; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
