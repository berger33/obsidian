---
id: software.backend.outbox-transacional.000001
tipo: tecnica
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
fontes: ["https://microservices.io/patterns/data/transactional-outbox.html", "https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html"]
tags: [dominio/software, subdominio/backend, qualidade/candidata]
aliases: [Transactional outbox, Outbox transacional, Dual write]
lote: software-dados-distribuidos-0004
---

# Outbox transacional para publicação de eventos

## Em uma frase
O padrão outbox grava a mudança de negócio e a intenção de publicar um evento na mesma transação local, deixando um relay entregar esse evento ao broker depois.

## Por que importa
Se um serviço grava no banco e publica no broker em duas operações independentes, uma falha entre elas pode deixar os sistemas divergentes: a alteração existe sem evento, ou o evento anuncia uma alteração que foi revertida. Uma transação distribuída entre banco e broker pode não estar disponível ou ser indesejável; o outbox reduz a janela de dual write usando a atomicidade do banco local.

## Como funciona
A transação grava as entidades de negócio e uma linha de outbox contendo, por exemplo, identificador do evento, tipo, chave da entidade e payload. Um processo separado lê linhas pendentes e publica mensagens. O relay pode consultar a tabela periodicamente ou capturar mudanças no log de transações; Debezium oferece uma transformação Outbox Event Router para mapear linhas a mensagens. Se o relay publicar e falhar antes de registrar que concluiu, pode publicar novamente após reiniciar. Portanto, consumidores devem ser idempotentes, e o desenho deve definir ordenação, retenção, limpeza e monitoramento da outbox.

## Exemplo
Ao confirmar um pedido, o serviço atualiza o pedido e insere `PedidoCriado` na outbox dentro do mesmo commit. Um relay envia o evento ao tópico depois. Se a transação falhar, nenhuma das duas gravações fica visível; se o relay repetir a publicação, o consumidor reconhece o ID do evento já processado.

## Limites e trade-offs
Outbox não oferece entrega exactly-once de ponta a ponta por si só. Duplicatas, atraso do relay, crescimento da tabela, ordem entre eventos e evolução do payload continuam sendo responsabilidades operacionais. CDC pode exigir slots de replicação, permissões e capacidade para reter logs; polling tem suas próprias questões de contenção e escala. A transação atômica cobre o banco local, não efeitos em serviços externos.

## Como verificar
Simule falha antes do commit, depois do commit e após a publicação mas antes da confirmação do relay. Confirme que o evento não antecede uma alteração revertida, que a recuperação não perde registros e que consumidores toleram duplicatas. Meça atraso e volume pendente, valide ordenação por agregado e teste a política de retenção da tabela.

## Conexões
- [[entrega-kafka-at-least-once-consumidor-idempotente]] — entrega repetida exige processamento idempotente no consumidor.
- [[evolucao-esquemas-eventos-avro-registry]] — o payload do evento precisa evoluir sem quebrar produtores e consumidores.
- [[migracoes-expand-contract]] — mudanças no esquema da outbox também podem exigir implantação compatível em etapas.

## Fontes
- [Microservices.io — Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) — problema dual write, participantes, benefícios e risco de duplicação; acesso em 2026-10-01.
- [Debezium — Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — configuração e transformação de eventos de outbox; acesso em 2026-10-01.
