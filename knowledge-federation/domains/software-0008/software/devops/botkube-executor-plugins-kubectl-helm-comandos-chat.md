---
id: software.devops.tranche12.001173
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

# Botkube: Executor Plugins para Execução Controlada de kubectl e helm via Chat

## Em uma frase
Os Executor plugins do Botkube (como `botkube/kubectl`, `botkube/helm` e `botkube/echo`) processam comandos interativos digitados diretamente no Slack, Discord ou Mattermost (por exemplo, `@Botkube kubectl get pods -n checkout`), executam a operação no cluster e devolvem a saída formatada para toda a thread acompanhar em tempo real.

## Por que importa
Durante uma sala de guerra (war room) de incidente, compartilhar trechos de terminal copiando e colando manualmente atrasa a colaboração, enquanto o uso de Executor plugins no canal do incidente registra uma trilha auditável e visível para todos os participantes.

## Como funciona
Na seção `executors` dos valores do Botkube, habilita-se o plugin `botkube/kubectl` ou `botkube/helm` a partir do repositório oficial `plugins-index.yaml` e vincula-se aquela configuração apenas aos canais de comunicação autorizados em `communications`.

## Exemplo
```yaml
executors:
  'k8s-read-only':
    botkube/kubectl:
      enabled: true
      config:
        defaultNamespace: default
  'helm-list-only':
    botkube/helm:
      enabled: true
      config:
        defaultNamespace: default
```

## Limites e trade-offs
Usar comandos interativos que exigem TTY ou bloqueiam indefinidamente (como `kubectl exec -it` ou `kubectl logs -f` sem limite) não é suportado ou trava a resposta do executor no chat.

## Como verificar
Execute apenas comandos não-interativos e finitos via `@Botkube kubectl` (usando `--tail=100` em `logs`) e consulte o help no canal com `@Botkube help`.

## Conexões
- [[botkube-source-plugins-eventos-kubernetes-prometheus-filtros]] — Veja também: Botkube: Source Plugins para Eventos Kubernetes e Alertas Prometheus.
- [[botkube-rbac-por-canal-channel-mapping-least-privilege]] — Veja também: Botkube: Políticas de RBAC por Canal de Chat e Isolamento Multi-Tenant.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://docs.botkube.io/plugins/) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
