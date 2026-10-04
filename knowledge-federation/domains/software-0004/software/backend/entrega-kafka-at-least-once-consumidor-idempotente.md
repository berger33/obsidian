---
id: software.backend.kafka-entrega-at-least-once.000001
tipo: conceito
dominio: software
subdominio: backend
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://docs.confluent.io/kafka/design/delivery-semantics.html", "https://kafka.apache.org/documentation/#semantics"]
tags: [dominio/software, subdominio/backend, qualidade/candidata]
aliases: [At-least-once, Entrega pelo menos uma vez, Consumidor idempotente Kafka]
lote: software-dados-distribuidos-0004
---

# Entrega at-least-once e consumidor idempotente

## Em uma frase
Com entrega at-least-once, um evento não processado pode ser reenviado após uma falha, então o consumidor precisa tolerar o mesmo evento mais de uma vez.

## Por que importa
Uma aplicação pode concluir um efeito e falhar antes de registrar sua posição no fluxo. Ao reiniciar, recebe o evento novamente. Isso é uma troca comum: reduzir risco de perder trabalho aceitando a possibilidade de duplicação. Se cada repetição criar uma cobrança, enviar uma notificação ou aplicar uma alteração adicional, a duplicação vira erro de negócio.

## Como funciona
No modelo de consumo do Kafka, processar a mensagem e depois confirmar o offset favorece at-least-once: uma queda entre essas etapas pode fazer o novo consumidor repetir o registro. Confirmar primeiro pode evitar a repetição, mas uma queda antes do efeito pode perder processamento. Uma chave idempotente e uma gravação deduplicada na mesma transação local do efeito ajudam o consumidor a transformar repetições em resultado equivalente. A idempotência do produtor Kafka pode suprimir duplicatas de retries do próprio produtor no log, mas não torna automaticamente idempotente um efeito externo executado pelo consumidor. Transações Kafka coordenam certos fluxos entre tópicos e offsets Kafka; uma gravação em banco externo requer cooperação adicional.

## Exemplo
Um consumidor de `PedidoCriado` registra o `event_id` em uma tabela com restrição única e atualiza a projeção na mesma transação. Se o offset for reprocessado, a restrição identifica que aquele evento já foi aplicado e o consumidor pode confirmar a posição sem duplicar a projeção. O efeito e o registro de deduplicação não devem ficar em transações separadas.

## Limites e trade-offs
Uma tabela de deduplicação cresce e precisa de retenção coerente com o período possível de replay. Uma chave idempotente deve representar a identidade estável do evento, não apenas o conteúdo que pode coincidir entre eventos diferentes. “Exactly-once” é sempre uma garantia com escopo: não a estenda além dos componentes que participam do protocolo transacional. Efeitos externos como e-mail ou pagamentos precisam de controles próprios.

## Como verificar
Force uma falha após o efeito local e antes da confirmação do offset, depois reprocese a mensagem e verifique que o efeito de negócio ocorre uma vez. Teste eventos repetidos, concorrência entre consumidores, replay histórico e expiração de IDs de deduplicação. Documente se o contrato promete at-most-once, at-least-once ou outro escopo.

## Conexões
- [[outbox-transacional-publicacao-eventos]] — um relay outbox pode publicar mais de uma vez e exige consumidores idempotentes.
- [[idempotencia-http-api]] — idempotência é uma propriedade de efeitos, embora os mecanismos variem entre HTTP e mensageria.
- [[evolucao-esquemas-eventos-avro-registry]] — consumidores também dependem de compatibilidade de esquemas ao reprocessar eventos antigos.

## Fontes
- [Confluent — Kafka Message Delivery Guarantees](https://docs.confluent.io/kafka/design/delivery-semantics.html) — comportamento de produtores, offsets e consumidores; acesso em 2026-10-01.
- [Apache Kafka — Documentation, Message Delivery Semantics](https://kafka.apache.org/documentation/#semantics) — semântica de entrega e limites das garantias; acesso em 2026-10-01.
