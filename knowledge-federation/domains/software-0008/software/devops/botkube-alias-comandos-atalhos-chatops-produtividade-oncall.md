---
id: software.devops.tranche12.001180
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

# Botkube: Configuração de Aliases de Comandos (aliases) para Produtividade no ChatOps

## Em uma frase
O Botkube permite definir `aliases` customizados na configuração do agente (como `k` para `kubectl`, `kgp` para `kubectl get pods` ou `hl` para `helm list`), reduzindo a digitação manual ao executar comandos pelo Slack, Discord ou Mattermost, inclusive em dispositivos móveis.

## Por que importa
Digitar comandos longos como `@Botkube kubectl get pods --all-namespaces` em um teclado de celular durante um acionamento de sobreaviso é lento e propenso a erros de autocorreção.

## Como funciona
Na seção `aliases` dos valores do Botkube, cada atalho mapeia um prefixo curto (por exemplo, `p`) para o comando completo do executor (`kubectl get pods`) e exibe um `displayName` amigável, funcionando de forma transparente com as mesmas regras de RBAC do executor subjacente.

## Exemplo
```yaml
aliases:
  k:
    command: kubectl
    displayName: "Kubectl alias"
  kgp:
    command: kubectl get pods
    displayName: "Get pods"
  kdp:
    command: kubectl describe pod
    displayName: "Describe pod"
```

## Limites e trade-offs
Criar aliases curtos para subcomandos destrutivos (como `kd` para `kubectl delete`) aumenta drasticamente o risco de exclusão acidental por erro de digitação no chat.

## Como verificar
Crie aliases apenas para comandos de leitura e inspeção (`get`, `describe`, `logs`, `top`) e liste os atalhos configurados no canal com `@Botkube list aliases`.

## Conexões
- [[botkube-multi-cluster-discord-mattermost-webhooks-identificacao]] — Veja também: Botkube: Operação Multi-Cluster em Discord, Mattermost, Elasticsearch e Webhooks.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://docs.botkube.io/plugins/) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
