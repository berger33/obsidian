---
id: software.devops.tranche12.001172
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.botkube.io/plugins/", "https://raw.githubusercontent.com/kubeshop/botkube/main/README.md", "https://github.com/kubeshop/botkube"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Botkube: Source Plugins para Eventos Kubernetes e Alertas Prometheus

## Em uma frase
Os Source plugins do Botkube atuam como observadores assíncronos dentro do cluster que capturam eventos de recursos Kubernetes, alertas Prometheus ou diagnósticos customizados, aplicam filtros de namespace, tipo de evento, labels e anotações e publicam notificações contextualizadas nos canais vinculados.

## Por que importa
Receber todos os eventos `Normal` do Kubernetes (como `Scheduled`, `Pulled`, `Created`) em um canal de Slack gera centenas de mensagens irrelevantes por hora, fazendo a equipe silenciar o canal e perder eventos críticos de erro.

## Como funciona
Na configuração de `sources`, a equipe define instâncias nomeadas do plugin `botkube/kubernetes` especificando `event.types` (por exemplo, apenas `error` ou `warning`), `namespaces.include` e lista de `resources` (`v1/pods`, `apps/v1/deployments`, `batch/v1/jobs`), garantindo que apenas anomalias reais cheguem ao canal da squad responsável.

## Exemplo
```yaml
sources:
  'k8s-err-events':
    botkube/kubernetes:
      enabled: true
      config:
        event:
          types:
            - error
        namespaces:
          include:
            - "^payments-.*"
        resources:
          - type: v1/pods
          - type: apps/v1/deployments
```

## Limites e trade-offs
Incluir eventos de `create` e `update` sem filtro de erro para recursos de alta rotatividade (como `v1/events`, `v1/endpoints` ou `coordination.k8s.io/v1/leases`) esgota os limites de rate limit da API do Slack ou Discord.

## Como verificar
Restrinja os Source plugins a eventos de erro (`types: [error]`) e namespaces de negócio, verificando o status dos sources no canal com `@Botkube list sources`.

## Conexões
- [[botkube-arquitetura-chatops-monitoramento-debugging-kubernetes]] — Veja também: Botkube: Arquitetura ChatOps para Monitoramento e Debugging Colaborativo de Clusters Kubernetes.
- [[botkube-executor-plugins-kubectl-helm-comandos-chat]] — Veja também: Botkube: Executor Plugins para Execução Controlada de kubectl e helm via Chat.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://docs.botkube.io/plugins/) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
