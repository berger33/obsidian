---
id: software.devops.tranche19.001810
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
fontes: ["https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md", "https://raw.githubusercontent.com/openfaas/faas/master/README.md", "https://github.com/openfaas/faas-netes"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenFaaS no Kubernetes: dimensionamento de requests/limits dos componentes core no Helm chart e boas práticas de produção

## Em uma frase
A documentação operacional do `faas-netes` especifica os valores de referência de `requests` e `limits` de CPU e memória para cada componente da pilha (`gateway`, `faasnetes`/`operator`, `queueWorker`, `prometheus`, `alertmanager`, `nats` e `basicAuthPlugin`) além de boas práticas de isolamento.

## Por que importa
Subdimensionar a memória do `prometheus` embutido (padrão `512Mi`) ou não definir `requests`/`limits` nas próprias funções em `openfaas-fn` pode causar `OOMKilled` no controlador de auto-scaling ou contenção de CPU nos worker nodes.

## Como funciona
Na tabela oficial do `faas-netes`, os componentes leves de controle (`gateway`, `faasnetes`, `operator`, `queueWorker`, `nats`) iniciam com requests enxutos (`memory: 120Mi`, `cpu: 50m`), o `prometheus` com `512Mi`, o `alertmanager` com `25Mi` e o `basicAuthPlugin` com `50Mi`/`20m`. Em produção, configure também TLS no Gateway/Ingress e defina `limits`/`requests` explícitos para cada função no `stack.yaml`.

## Exemplo
```yaml
# Definindo requests e limits explícitos para uma função no stack.yaml:
functions:
  pdf-generator:
    lang: python3-http
    handler: ./pdf-generator
    image: ghcr.io/org/pdf-generator:1.2.0
    limits:
      memory: 256Mi
      cpu: 500m
    requests:
      memory: 128Mi
      cpu: 100m
```

## Limites e trade-offs
Por padrão, o `faas-netes` aplica `imagePullPolicy: Always` nas funções implantadas para garantir que tags atualizadas sejam recarregadas; em produção, prefira tags SemVer imutáveis em cada release.

## Como verificar
Execute `kubectl top pods -n openfaas` e `kubectl top pods -n openfaas-fn` para auditar o consumo real frente aos limites configurados.

## Conexões
- [[openfaas-event-connectors-cron-connector-kafka-sqs-annotations]] — Veja também: OpenFaaS Event Connectors e Cron: disparo de funções por tópicos (`topic` annotation) e agendamentos `cron-connector`.

## Fontes
- [OpenFaaS GitHub — README.md (Serverless Functions Made Simple, Stack Architecture, Code Samples & Template Store)](https://raw.githubusercontent.com/openfaas/faas-netes/master/README.md) — README oficial do openfaas/faas apresentando a arquitetura conceitual, uso da CLI faas-cli, templates de linguagem e auto-scaling; consultado em 2026-10-03.
- [OpenFaaS faas-netes GitHub — README.md (Kubernetes Provider, Controller vs Operator Function CRD, Readiness Lock & Helm Resources)](https://raw.githubusercontent.com/openfaas/faas/master/README.md) — Documentação oficial do provedor faas-netes cobrindo modos controller e operator (Function CRD), readiness probe com arquivo .lock e dimensionamento; consultado em 2026-10-03.
- [OpenFaaS faas-netes — Official GitHub Repository](https://github.com/openfaas/faas-netes) — Repositório oficial do provedor Kubernetes faas-netes do OpenFaaS; consultado em 2026-10-03.
