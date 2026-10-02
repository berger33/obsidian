---
id: software.testes.tranche08.000209
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
fontes: ["https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html", "https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kafka: escolher broker de teste conforme contrato

## Em uma frase
Use mock para lógica isolada e broker real de teste quando protocolo, offsets ou coordenação forem parte do comportamento.

## Por que importa
Mock de producer/consumer pode validar decisões locais, mas não exercita serialização, broker, commit nem rebalance.

## Como funciona
Defina fronteira contratual, inicialize broker descartável ou ambiente controlado para integração e mantenha tópicos, grupo e cleanup exclusivos.

## Exemplo
Unit test verifica tratamento de evento inválido; integração publica e consome em broker de teste e confirma headers, partition e commit.

## Limites e trade-offs
Broker descartável não representa escala, configuração gerenciada ou falhas regionais de produção; ambiente remoto também precisa de isolamento e cleanup.

## Como verificar
Execute contrato contra versão declarada do broker/client e confirme que nenhuma configuração ou dado de produção é reutilizado.

## Conexões
- [[terraform-validate-vs-test-provisionamento]] — Veja também: Terraform: distinguir validate de terraform test.
- [[terraform-plan-assertions-estado-esperado]] — Veja também: Terraform: verificar plano contra mudança de infraestrutura esperada.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Producer configuration](https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html) — idempotência, retries, acks, ordenação e transações; consultado em 2026-10-02.
