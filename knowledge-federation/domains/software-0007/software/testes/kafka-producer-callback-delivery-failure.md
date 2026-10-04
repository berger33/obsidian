---
id: software.testes.tranche08.000207
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

# Kafka: observar falhas de entrega no produtor

## Em uma frase
Verifique resultado assíncrono de entrega e erros retornados, em vez de considerar uma chamada de produce como confirmação do broker.

## Por que importa
Enfileirar localmente pode anteceder falha de rede, rejeição ou timeout; a aplicação precisa tornar o resultado visível ao chamador.

## Como funciona
Aguarde ou processe callback/evento de delivery conforme cliente, trate erros retriable e fatais de forma distinta e aplique timeout de forma explícita.

## Exemplo
O teste faz broker ficar indisponível, publica registro e confirma que erro alcança métrica e resposta, não apenas log de debug.

## Limites e trade-offs
API específica do client determina callback, flush e lifecycle; não copie comportamento entre linguagens sem verificar documentação da versão.

## Como verificar
Force entrega bem-sucedida e falha, encerre producer com pendências e confirme que nenhum erro fica sem observação.

## Conexões
- [[kafka-producer-idempotencia-retries-acks]] — Veja também: Kafka: testar produtor idempotente e confirmação.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Veja também: Kafka: separar erro transitório de erro permanente.

## Fontes
- [Confluent — Producer configuration](https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html) — idempotência, retries, acks, ordenação e transações; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
