---
id: software.devops.tranche12.001179
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

# Botkube: Operação Multi-Cluster em Discord, Mattermost, Elasticsearch e Webhooks

## Em uma frase
O Botkube suporta operação multi-cluster nas integrações de bots com Discord e Mattermost e nos sinks de Elasticsearch e Webhook, identificando claramente o `clusterName` em cada evento emitido e permitindo direcionar comandos de executor ao cluster desejado via flag `--cluster-name`.

## Por que importa
Organizações que operam clusters separados para `dev`, `staging` e `prod` precisam saber instantaneamente de qual cluster partiu uma notificação de erro e impedir que um comando de debugging pensado para `staging` seja executado em `prod`.

## Como funciona
Configurando `settings.clusterName` nos valores de instalação de cada cluster (por exemplo, `eks-prod-sa-east-1`), todas as mensagens e payloads JSON enviados pelo Botkube passam a incluir o identificador do cluster, e os executores validam se o `--cluster-name` informado no comando corresponde àquela instância antes de agir.

## Exemplo
```yaml
settings:
  clusterName: eks-prod-sa-east-1
```

## Limites e trade-offs
Deixar `settings.clusterName` com o valor genérico `default` ou `not-configured` em vários clusters que publicam no mesmo canal de Discord/Mattermost ou no mesmo índice do Elasticsearch torna impossível distinguir a origem dos alertas.

## Como verificar
Defina sempre um `settings.clusterName` único e descritivo em cada cluster e valide sua presença nos cabeçalhos das notificações.

## Conexões
- [[botkube-slack-socket-mode-seguranca-sem-ingress-publico]] — Veja também: Botkube: Conexão Segura com Slack via Socket Mode sem Expor Webhook Público.
- [[botkube-alias-comandos-atalhos-chatops-produtividade-oncall]] — Veja também: Botkube: Configuração de Aliases de Comandos (aliases) para Produtividade no ChatOps.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://github.com/kubeshop/botkube) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://docs.botkube.io/plugins/) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
