---
id: software.testes.tranche08.000205
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

# Kafka: testar rebalance com processamento em andamento

## Em uma frase
Inclua rebalance enquanto há mensagens em processamento para verificar propriedade de partição e política de commit.

## Por que importa
Mudança de membros pode revogar partição no meio de trabalho e expor duplicação, commit inválido ou atraso de retomada.

## Como funciona
Adicione e remova consumidor durante carga, observe callbacks e atribuições, e verifique que mensagem não é perdida quando ownership muda.

## Exemplo
Um worker pausa após ler, outro entra no grupo, e o teste verifica que o efeito aparece uma vez logicamente após reassignment e retry.

## Limites e trade-offs
Rebalance depende de protocolo, configuração e versão do cliente; um teste unitário de callback não representa coordenação real do broker.

## Como verificar
Registre geração, partições e offsets antes/depois, injete interrupção e confirme política de commit e tratamento de mensagens em voo.

## Conexões
- [[kafka-at-least-once-consumidor-idempotente]] — Veja também: Kafka: tornar efeitos do consumidor seguros contra redelivery.
- [[kafka-offset-commit-proximo-registro]] — Veja também: Kafka: verificar semântica de offset committed.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
