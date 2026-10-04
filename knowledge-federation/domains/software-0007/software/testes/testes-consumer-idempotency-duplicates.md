---
id: software.testes.tranche07.000147
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html", "https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/idempotent-consumer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de consumidor idempotente com mensagens duplicadas", "Teste: Teste de consumidor idempotente com mensagens duplicadas"]
lote: software-testes-2000-0001
---

# Teste de consumidor idempotente com mensagens duplicadas

## Em uma frase
Entregue a mesma mensagem mais de uma vez e confirme que consumidor produz no máximo o efeito de negócio definido para aquele identificador.

## Por que importa
Sistemas de mensageria podem entregar novamente uma mensagem, por exemplo após falha entre persistência do efeito e confirmação de recebimento.

## Como funciona
Crie fixture com ID de mensagem estável, processe uma vez, repita após sucesso e em cenários de falha antes/depois do commit. Teste mensagens distintas com conteúdo semelhante e concorrência; mantenha deduplicação durável conforme janela de reentrega.

## Exemplo
Publique duas vezes evento de pagamento de teste com mesmo event ID e confirme uma única baixa; depois publique evento novo com ID diferente e valide que produz o segundo efeito previsto.

## Limites e trade-offs
Deduplicação por hash de conteúdo pode conflitar com eventos legítimos idênticos; retenção de chaves tem custo e requer política. Exatamente uma entrega ponta a ponta não deve ser presumida.

## Como verificar
Interrompa consumidor em pontos distintos do processamento, reinicie e reentregue a mensagem; compare estado, efeitos externos e registros de deduplicação sob concorrência.

## Conexões
- [[entrega-kafka-at-least-once-consumidor-idempotente]] — aprofundamento relacionado.
- [[testes-retry-backoff-jitter-cascata]] — aprofundamento relacionado.

## Fontes
- [AWS SQS — At-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html) — entrega duplicada pode ocorrer e consumidores devem ser idempotentes; consultado em 2026-10-01.
- [AWS Prescriptive Guidance — Idempotent consumer](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/idempotent-consumer.html) — deduplicação durável e idempotência em consumidores de mensagens; consultado em 2026-10-01.
