---
id: software.testes.tranche08.000203
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

# Kafka: verificar semântica de offset committed

## Em uma frase
Interprete offset comprometido como posição de retomada no grupo e teste o que ocorre entre processamento e commit.

## Por que importa
Commit prematuro pode perder processamento após crash; commit tardio pode repetir registros, portanto a ordem afeta a semântica entregue.

## Como funciona
Registre qual mensagem foi processada e qual offset foi commitado, simule interrupção em cada fronteira e confira retomada após restart.

## Exemplo
O consumidor processa offset n e confirma o próximo offset; ao reiniciar, teste que não pula o registro seguinte nem assume que commit representa o último já consumido.

## Limites e trade-offs
Semântica concreta depende da API e do método de commit; transações ou offsets automáticos alteram o fluxo e precisam ser examinados separadamente.

## Como verificar
Use tópico de teste com offsets observáveis, interrompa antes e depois do commit e compare mensagens reproduzidas e resultado persistido.

## Conexões
- [[kafka-rebalance-processamento-em-curso]] — Veja também: Kafka: testar rebalance com processamento em andamento.
- [[kafka-consumer-reset-start-offset]] — Veja também: Kafka: testar offset inicial e política de reset.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
