---
id: software.devops.tranche12.001178
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

# Botkube: Conexão Segura com Slack via Socket Mode sem Expor Webhook Público

## Em uma frase
A integração moderna do Botkube com o Slack (`socketSlack`) utiliza o **Slack Socket Mode** via WebSockets de saída iniciados de dentro do cluster, eliminando a necessidade de expor um `Ingress` ou `LoadBalancer` público na internet para receber comandos do chat.

## Por que importa
Expor um endpoint HTTP do agente de cluster na internet pública apenas para receber callbacks interativos do Slack exige gerenciar certificados TLS públicos, WAF e validação de assinatura na borda de cada cluster privado.

## Como funciona
Com `socketSlack`, o pod do Botkube estabelece uma conexão WebSocket autenticada de saída para a API do Slack usando um App-Level Token (`xapp-...`) e um Bot Token (`xoxb-...`). Assim, mesmo clusters em sub-redes privadas ou atrás de NAT recebem comandos `@Botkube` e interações de botões de forma bidirecional.

## Exemplo
```bash
# Verificar nos logs do Botkube a conexao ativa do SocketSlack:
kubectl logs -n botkube deployment/botkube | grep -i "slack"
```

## Limites e trade-offs
Reutilizar o mesmo App-Level Token (`xapp-...`) do Slack Socket Mode simultaneamente em múltiplos clusters sem designar o nome do cluster nos comandos faz com que as mensagens sejam distribuídas de forma imprevisível entre os agentes conectados.

## Como verificar
Configure um App/Token dedicado por cluster (ou utilize o roteamento multi-cluster explícito suportado pela plataforma escolhida) e armazene `appToken` e `botToken` em `Secrets` Kubernetes protegidos.

## Conexões
- [[botkube-automated-actions-autodiagnostico-eventos-kubectl]] — Veja também: Botkube: Ações Automatizadas (Actions) Disparadas por Eventos de Source Plugins.
- [[botkube-multi-cluster-discord-mattermost-webhooks-identificacao]] — Veja também: Botkube: Operação Multi-Cluster em Discord, Mattermost, Elasticsearch e Webhooks.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://github.com/kubeshop/botkube) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://docs.botkube.io/plugins/) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
