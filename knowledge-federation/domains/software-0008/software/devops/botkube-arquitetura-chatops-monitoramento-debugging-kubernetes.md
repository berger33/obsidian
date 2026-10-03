---
id: software.devops.tranche12.001171
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
fontes: ["https://raw.githubusercontent.com/kubeshop/botkube/main/README.md", "https://docs.botkube.io/plugins/", "https://github.com/kubeshop/botkube"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Botkube: Arquitetura ChatOps para Monitoramento e Debugging Colaborativo de Clusters Kubernetes

## Em uma frase
Botkube é um assistente de mensagens open-source (licença MIT, criado pela Kubeshop) para monitoramento e troubleshooting de clusters Kubernetes que conecta eventos do cluster e execução segura de comandos (`kubectl`, `helm`) a plataformas de colaboração como Slack, Discord e Mattermost, além de sinks como Elasticsearch e Webhook.

## Por que importa
Quando desenvolvedores precisam diagnosticar falhas de suas aplicações em ambientes de staging ou produção, conceder acesso direto ao `kubeconfig` do cluster amplia a superfície de risco, enquanto depender exclusivamente da equipe de SRE para rodar `kubectl logs` cria gargalos operacionais.

## Como funciona
O agente do Botkube roda dentro do cluster Kubernetes e opera com dois tipos de extensões modulares: **Source plugins** (que observam eventos de Kubernetes, Prometheus e outras fontes e emitem notificações) e **Executor plugins** (que processam comandos enviados pelos usuários nos canais de chat sob políticas estritas de RBAC por canal).

## Exemplo
```bash
helm repo add botkube https://charts.botkube.io
helm repo update
kubectl get pods -n botkube
kubectl logs -n botkube -l app=botkube --tail=50
```

## Limites e trade-offs
Habilitar um executor `kubectl` em um canal público de chat sem restringir os verbos permitidos e o RBAC por canal permite que qualquer membro do canal execute ações destrutivas no cluster a partir do chat.

## Como verificar
Vincule cada canal de chat a políticas explícitas de RBAC somente leitura (`get`, ` list`, `logs`, `describe`) e valide os plugins ativos com `@Botkube list executors` e `@Botkube list sources`.

## Conexões
- [[botkube-source-plugins-eventos-kubernetes-prometheus-filtros]] — Veja também: Botkube: Source Plugins para Eventos Kubernetes e Alertas Prometheus.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://docs.botkube.io/plugins/) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
