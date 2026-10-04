---
id: software.devops.tranche19.001809
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
fontes: ["https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS Event Connectors e Cron: disparo de funções por tópicos (`topic` annotation) e agendamentos `cron-connector`

## Em uma frase
O OpenFaaS desacopla as fontes de eventos das funções por meio do padrão **connector-sdk**: conectores dedicados (`cron-connector`, `kafka-connector`, `sqs-connector`, `nats-connector`, `postgres-connector`) observam as anotações `topic` e `schedule` nas funções implantadas e encaminham eventos automaticamente.

## Por que importa
Em vez de embutir consumidores Kafka ou agendadores cron dentro do código de cada função, basta anotar a função existente para que ela responda tanto a chamadas HTTP quanto a mensagens de fila ou horários programados.

## Como funciona
Para agendar uma função periodicamente com o `cron-connector`, basta adicionar as anotações `topic: cron-function` e `schedule: "*/5 * * * *"` na definição da função. Para consumir tópicos Kafka ou filas SQS, basta anotar `topic: "orders.created,payments.processed"`.

## Exemplo
```yaml
functions:
  nightly-cleanup:
    lang: golang-middleware
    handler: ./nightly-cleanup
    image: ghcr.io/org/nightly-cleanup:0.1.0
    annotations:
      topic: cron-function
      schedule: "0 2 * * *"
```

## Limites e trade-offs
Os conectores de eventos consultam periodicamente a API do Gateway para descobrir quais funções assinaram cada `topic`, não exigindo reiniciar o conector quando novas funções são implantadas.

## Como verificar
Implante o `cron-connector`, anote uma função com `topic: cron-function` e `schedule: "*/1 * * * *"` e confirme nas métricas do Gateway que a função é invocada a cada minuto.

## Conexões
- [[openfaas-profiles-crd-afinidadade-tolerations-pod-security-context]] — Veja também: OpenFaaS `Profile` CRD: aplicação reutilizável de `affinity`, `tolerations`, `runtimeClassName` e `podSecurityContext`.
- [[openfaas-dimensionamento-recursos-helm-chart-gateway-faasnetes-prometheus]] — Veja também: OpenFaaS no Kubernetes: dimensionamento de requests/limits dos componentes core no Helm chart e boas práticas de produção.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
