---
id: software.devops.tranche19.001832
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md", "https://raw.githubusercontent.com/temporalio/temporal/main/README.md", "https://github.com/temporalio/temporal"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Temporal Server Internals: papel dos 4 serviços (`Frontend`, `History`, `Matching` e `Worker`)

## Em uma frase
Um cluster Temporal de produção é formado por quatro serviços stateless/sharded que podem ser escalados independentemente no Kubernetes (ou executados em um único binário no desenvolvimento): **Frontend Service**, **History Service**, **Matching Service** e **Internal Workers Service**.

## Por que importa
Em cargas de dezenas de milhares de transições de estado por segundo, o gargalo de roteamento de filas (*Matching*) é diferente do gargalo de transações de máquina de estado por shard (*History*) e do rate-limiting de borda (*Frontend*).

## Como funciona
Cada serviço tem uma responsabilidade bem delimitada: 1) **Frontend Service**: gateway gRPC stateless sem estado que autentica chamadas, aplica rate-limiting e roteia requisições dos SDKs/CLI para os demais serviços; 2) **History Service**: dividido em `numHistoryShards` (shards que detêm a propriedade exclusiva de cada *Workflow Execution*, gravam eventos no banco e avançam a máquina de estado); 3) **Matching Service**: gerencia as **Task Queues** em memória e faz o *match* síncrono ou persistido com os Workers em polling; e 4) **Internal Workers Service**: executa workflows internos de sistema do próprio Temporal (como *Archival* e scanners).

## Exemplo
```bash
# Inspecionando a saúde e os membros do anel de serviços do cluster Temporal:
temporal operator cluster health
temporal operator cluster describe
```

## Limites e trade-offs
O parâmetro `numHistoryShards` do History Service é definido na criação inicial do cluster Temporal e **não pode ser alterado** posteriormente sem migrar para um novo cluster; dimensione o número de shards adequadamente para a escala futura.

## Como verificar
Execute `temporal operator cluster describe` para verificar a configuração do cluster, versão de persistência e número de shards de história.

## Conexões
- [[temporal-arquitetura-durable-execution-event-sourcing-cluster-workers]] — Veja também: Temporal: arquitetura de *Durable Execution* baseada em Event Sourcing separando Temporal Cluster e User Workers.
- [[temporal-workflows-determinismo-replay-history-vs-activities-idempotentes]] — Veja também: Temporal: segregação entre `Workflows` determinísticos (Replay de Histórico) e `Activities` idempotentes.

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
