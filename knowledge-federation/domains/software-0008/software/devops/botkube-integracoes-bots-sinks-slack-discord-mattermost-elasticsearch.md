---
id: software.devops.tranche12.001175
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
fontes: ["https://github.com/kubeshop/botkube", "https://raw.githubusercontent.com/kubeshop/botkube/main/README.md", "https://docs.botkube.io/plugins/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Botkube: Comparação de Integrações Bidirecionais (Bots) e Unidirecionais (Sinks)

## Em uma frase
A arquitetura de comunicação do Botkube divide as integrações em dois grupos: **Bots** bidirecionais (Slack, Discord e Mattermost), que suportam tanto Source plugins quanto Executor plugins e RBAC por canal, e **Sinks** unidirecionais (Elasticsearch e Webhook), voltados à exportação contínua de eventos multi-cluster.

## Por que importa
Equipes frequentemente precisam enviar alertas interativos e permitir comandos de diagnóstico no Slack ou Mattermost e, simultaneamente, arquivar todos os eventos estruturados do cluster no Elasticsearch ou disparar sistemas externos via Webhook usando o mesmo agente.

## Como funciona
Um único agente Botkube instalado no cluster pode habilitar múltiplas plataformas simultaneamente na seção `communications`. As integrações Slack oferecem suporte adicional a mensagens interativas e notificações acionáveis com botões, enquanto Discord, Mattermost, Elasticsearch e Webhook suportam roteamento multi-cluster.

## Exemplo
```yaml
communications:
  'default-group':
    socketSlack:
      enabled: true
      appToken: "{{ .Values.slack.appToken }}"
      botToken: "{{ .Values.slack.botToken }}"
      channels:
        'sre-alerts':
          name: 'k8s-sre-alerts'
          bindings:
            sources: ['k8s-err-events']
            executors: ['k8s-read-only']
    elasitcsearch:
      enabled: false
```

## Limites e trade-offs
Tentar vincular `executors` a uma integração do tipo Sink (como `elasticsearch` ou `webhook`) é inválido, pois Sinks são estritamente unidirecionais e processam apenas `sources`.

## Como verificar
Associe `executors` apenas a integrações de Bots (`socketSlack`, `discord`, `mattermost`) e utilize Sinks para retenção e auditoria de eventos.

## Conexões
- [[botkube-rbac-por-canal-channel-mapping-least-privilege]] — Veja também: Botkube: Políticas de RBAC por Canal de Chat e Isolamento Multi-Tenant.
- [[botkube-repositorios-plugins-index-extensoes-customizadas]] — Veja também: Botkube: Repositórios de Plugins (botkube e botkubeExtra) e Desenvolvimento de Plugins Customizados.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://github.com/kubeshop/botkube) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://docs.botkube.io/plugins/) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
