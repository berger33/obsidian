---
id: software.devops.tranche19.001815
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
fontes: ["https://fission.io/docs/concepts/", "https://raw.githubusercontent.com/fission/fission/main/README.md", "https://github.com/fission/fission"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fission `Triggers`: vinculação de eventos HTTP, Cron (`TimeTrigger`), Filas (`MessageQueueTrigger`/KEDA) e Kubernetes Watch

## Em uma frase
No Fission, as funções são agnósticas ao canal de invocação: os recursos **`Trigger`** vinculam fontes de eventos externas (**HTTP**, **Timer/Cron**, **Message Queues** como Kafka/NATS/SQS/RabbitMQ via KEDA e **Kubernetes Watch**) a chamadas HTTP internas para a `Function`.

## Por que importa
Escrever a mesma lógica de negócio separadamente para uma rota REST, um job agendado e um consumidor Kafka duplica código; no Fission, a mesma `Function` pode ser acionada por múltiplos `Triggers` simultaneamente.

## Como funciona
Com `fission route create` (`HTTPTrigger`), o componente `router` expõe o caminho URL/método/host configurado; com `fission timer create` (`TimeTrigger`), o agendador dispara a função segundo uma expressão cron; e com `fission mqt create` (`MessageQueueTrigger`), o Fission consome mensagens de um tópico de entrada, envia para a função e publica a resposta em um tópico de saída ou de erro.

## Exemplo
```bash
# Expondo a função hello via HTTP GET /hello e agendando a cada 5 minutos:
fission route create --name hello-http --function hello --url /hello --method GET
fission timer create --name hello-cron --function hello --cron "0 */5 * * * *"
```

## Limites e trade-offs
Ao configurar um `MessageQueueTrigger` com `--mqtkind keda`, o Fission pode escalar os Pods consumidores baseados no tamanho da fila (*queue lag*) e enviar mensagens que excederem `--maxretries` para o `--errortopic`.

## Como verificar
Liste todos os gatilhos ativos no cluster com `fission route list`, `fission timer list` e `fission mqt list`.

## Conexões
- [[fission-packages-source-archive-deployment-archive-buildermgr]] — Veja também: Fission `Package` e Build Pipeline: gerenciamento de `source` archives, `deployment` archives e `buildermgr`.
- [[fission-specs-declarativos-fission-spec-init-apply-gitops]] — Veja também: Fission Declarative Specs (`fission spec`): gerenciamento GitOps idempotente de funções e arquivos em `specs/`.

## Fontes
- [Fission GitHub — README.md (Serverless Functions for Kubernetes, 100msec Warm Pool Cold Start & CLI Quickstart)](https://fission.io/docs/concepts/) — README oficial do fission/fission detalhando o modelo de pools de containers aquecidos (~100 ms cold start) e comandos fission env/function; consultado em 2026-10-03.
- [Fission Official Documentation — Concepts (Functions, Environments, Executors, Triggers, Packages & Declarative Specs)](https://raw.githubusercontent.com/fission/fission/main/README.md) — Documentação oficial de conceitos do Fission explicando a relação entre Trigger, Function, Environment e Package e os executores poolmgr/newdeploy/container; consultado em 2026-10-03.
- [Fission — Official GitHub Repository](https://github.com/fission/fission) — Repositório oficial Apache-2.0 do Fission para Kubernetes; consultado em 2026-10-03.
