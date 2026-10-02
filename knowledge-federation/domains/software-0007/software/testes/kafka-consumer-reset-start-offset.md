---
id: software.testes.tranche08.000208
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

# Kafka: testar offset inicial e política de reset

## Em uma frase
Torne explícito se o consumidor retoma offset committed ou aplica política de reset ao iniciar sem posição válida.

## Por que importa
Grupo novo, offset expirado ou reset administrativo pode mudar o ponto de leitura e causar replay amplo ou lacuna percebida.

## Como funciona
Crie cenários para grupo existente e inexistente, offset válido e inválido, e observe configuração de auto offset reset junto do comportamento da API.

## Exemplo
Um grupo novo parte da posição esperada para o domínio; outro cenário demonstra recuperação após offset indisponível sem assumir silenciosamente latest ou earliest.

## Limites e trade-offs
Configuração de reset não substitui política de retenção e pode variar pelo estado do grupo; não inferir ponto de leitura apenas pelo código.

## Como verificar
Inspecione offsets committed no broker, reinicie grupo controlado e compare registros consumidos com histórico disponível.

## Conexões
- [[kafka-offset-commit-proximo-registro]] — Veja também: Kafka: verificar semântica de offset committed.
- [[kafka-rebalance-processamento-em-curso]] — Veja também: Kafka: testar rebalance com processamento em andamento.

## Fontes
- [Confluent — Kafka Go client](https://docs.confluent.io/platform/current/clients/confluent-kafka-go/index.html) — offsets, grupos, rebalance e semântica transacional; consultado em 2026-10-02.
- [Confluent — Client configuration](https://docs.confluent.io/platform/current/clients/client-configs.html) — propriedades de produtor e consumidor e protocolos de grupo; consultado em 2026-10-02.
