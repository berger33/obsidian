---
id: software.devops.tranche19.001831
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
fontes: ["https://raw.githubusercontent.com/temporalio/temporal/main/README.md", "https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md", "https://github.com/temporalio/temporal"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Temporal: arquitetura de *Durable Execution* baseada em Event Sourcing separando Temporal Cluster e User Workers

## Em uma frase
O **Temporal** (evolução direta do Cadence da Uber criada pelos mesmos fundadores, licenciada sob MIT) é uma plataforma de **execução durável (*Durable Execution*)** onde fluxos de aplicação (*Workflows*) são escritos como código em linguagens de programação padrão e executam de forma resiliente através de falhas de processos, rede ou servidores por meio de **Event Sourcing**.

## Por que importa
Em sistemas distribuídos tradicionais, coordenar transações de múltiplos passos que duram minutos, dias ou meses exige espalhar filas, tabelas de estado no banco de dados, cronjobs de retentativa e máquinas de estado frágeis por todo o código.

## Como funciona
A arquitetura do Temporal separa estritamente: 1) os **Processos Hospedados pelo Usuário** (a aplicação cliente gRPC e os processos **Workers** que executam o código de *Workflows* e *Activities* dentro da infraestrutura do próprio usuário); e 2) o **Temporal Cluster** (composto por 4 serviços escaláveis independentes: **Frontend**, **History**, **Matching** e **Internal Workers**, persistindo um histórico append-only de eventos para cada execução).

## Exemplo
```bash
# Iniciando um servidor Temporal completo de desenvolvimento com Web UI na porta 8233:
temporal server start-dev --ui-port 8233
temporal operator namespace list
```

## Limites e trade-offs
Como o código do usuário roda exclusivamente nos **Workers** hospedados pelo usuário (que fazem long-polling gRPC de saída nas *Task Queues* do servidor), o servidor Temporal nunca executa código arbitrário da aplicação nem precisa abrir conexões de entrada para a rede dos Workers.

## Como verificar
Inicie `temporal server start-dev` e execute `temporal workflow list` (ou acesse `http://localhost:8233`) para validar o cluster local.

## Conexões
- [[temporal-quatro-servicos-internos-frontend-history-matching-worker]] — Veja também: Temporal Server Internals: papel dos 4 serviços (`Frontend`, `History`, `Matching` e `Worker`).

## Fontes
- [Temporal GitHub — README.md (Durable Execution Platform, Local Dev Server, Temporal CLI & Web UI)](https://raw.githubusercontent.com/temporalio/temporal/main/README.md) — README oficial do temporalio/temporal apresentando o servidor de execução durável, CLI temporal e inicialização start-dev; consultado em 2026-10-03.
- [Temporal Server Architecture Documentation — High-Level Architecture (Frontend, History, Matching, Internal Workers, Event Sourcing & Tasks)](https://raw.githubusercontent.com/temporalio/temporal/main/docs/architecture/README.md) — Documentação oficial de arquitetura interna do Temporal detalhando processos do usuário vs cluster Temporal, shards do History Service, Task Queues e tipos de Tasks; consultado em 2026-10-03.
- [Temporal — Official GitHub Repository](https://github.com/temporalio/temporal) — Repositório oficial MIT do Temporal Server; consultado em 2026-10-03.
