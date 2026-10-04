---
id: software.testes.tranche08.000204
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

# Kafka: tornar efeitos do consumidor seguros contra redelivery

## Em uma frase
Projete efeitos de consumo para tolerar redelivery quando o offset só é confirmado após o processamento.

## Por que importa
Falha entre persistir efeito e commitar offset permite que a mesma mensagem seja entregue de novo após retomada.

## Como funciona
Escolha chave de deduplicação estável e faça escrita idempotente ou transacional na fronteira disponível. Teste repetição do mesmo evento e conflito com versão atual.

## Exemplo
Evento de pagamento repetido mantém um único lançamento lógico porque operação usa identificador de evento com restrição de unicidade.

## Limites e trade-offs
Deduplicação precisa de retenção e escopo compatíveis com replay; chave mal escolhida pode colidir eventos distintos ou aceitar atualização fora de ordem.

## Como verificar
Force crash após escrita e antes do commit, reinicie consumidor e confirme que estado de negócio permanece correto com evento reprocessado.

## Conexões
- [[kafka-offset-commit-proximo-registro]] — Veja também: Kafka: verificar semântica de offset committed.
- [[kafka-retry-dlq-erro-transitorio-permanente]] — Veja também: Kafka: separar erro transitório de erro permanente.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
