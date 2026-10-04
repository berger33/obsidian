---
id: software.devops.tranche12.001174
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
fontes: ["https://github.com/kubeshop/botkube", "https://docs.botkube.io/plugins/", "https://raw.githubusercontent.com/kubeshop/botkube/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Botkube: Políticas de RBAC por Canal de Chat e Isolamento Multi-Tenant

## Em uma frase
O Botkube suporta configuração granular de RBAC por plugin e por canal (`context.rbac`), permitindo que o canal `#squad-checkout` execute `kubectl` e receba eventos apenas do namespace `checkout` usando uma `Role` restrita, enquanto o canal `#sre-ops` opera com visibilidade em todo o cluster.

## Por que importa
Se o agente do Botkube utilizasse uma única `ClusterRole` global para todos os canais sem impersonation ou mapeamento de RBAC por canal, um desenvolvedor em um canal de testes poderia inspecionar `Secrets` de produção digitando `-n prod`.

## Como funciona
Ao configurar a política de RBAC de uma instância de source ou executor, o Botkube pode mapear a execução para um `ServiceAccount`, `Group` ou `User` específico do Kubernetes (via impersonation) ou restringir estaticamente os namespaces e recursos acessíveis àquele canal específico.

## Exemplo
```yaml
rbac:
  groups:
    'checkout-devs-group':
      create: true
      rules:
        - apiGroups: ["", "apps"]
          resources: ["pods", "pods/log", "deployments"]
          Namespaces: ["checkout"]
          verbs: ["get", "list"]
```

## Limites e trade-offs
Conceder o verbo `get` no recurso `secrets` ao perfil de RBAC vinculado a um canal de chat faz com que qualquer participante possa imprimir segredos codificados em base64 no histórico permanente de mensagens do Slack ou Discord.

## Como verificar
Nunca inclua `secrets` nas regras de RBAC associadas a canais de chat e verifique o isolamento tentando executar `@Botkube kubectl get secrets -A` no canal para confirmar que o comando é negado.

## Conexões
- [[botkube-executor-plugins-kubectl-helm-comandos-chat]] — Veja também: Botkube: Executor Plugins para Execução Controlada de kubectl e helm via Chat.
- [[botkube-integracoes-bots-sinks-slack-discord-mattermost-elasticsearch]] — Veja também: Botkube: Comparação de Integrações Bidirecionais (Bots) e Unidirecionais (Sinks).

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://github.com/kubeshop/botkube) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://docs.botkube.io/plugins/) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
