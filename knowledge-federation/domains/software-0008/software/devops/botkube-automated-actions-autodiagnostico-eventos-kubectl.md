---
id: software.devops.tranche12.001177
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

# Botkube: Ações Automatizadas (Actions) Disparadas por Eventos de Source Plugins

## Em uma frase
O recurso de `actions` do Botkube conecta automaticamente a emissão de um evento por um Source plugin à execução imediata de um Executor plugin, anexando o diagnóstico (como `kubectl describe` ou `kubectl logs`) junto ao alerta publicado no canal de chat.

## Por que importa
Mesmo com o comando `@Botkube kubectl` disponível no chat, exigir que um humano digite `kubectl logs` toda vez que um Pod falha desperdiça tempo se o próprio bot pode rodar esse comando automaticamente no instante do erro.

## Como funciona
Na seção `actions`, define-se uma regra vinculando `bindings.sources` (por exemplo, `k8s-err-events`) a um template de comando em `command` (como `"kubectl describe {{ .Event.TypeMeta.Kind | lower }} {{ .Event.Name }} -n {{ .Event.Namespace }}"`) usando `bindings.executors`, de modo que todo erro já chega ao canal acompanhado da saída do comando.

## Exemplo
```yaml
actions:
  'describe-created-resource':
    enabled: true
    displayName: "Describe failed resource"
    command: "kubectl describe {{ .Event.TypeMeta.Kind | lower }} {{ .Event.Name }} -n {{ .Event.Namespace }}"
    bindings:
      sources:
        - k8s-err-events
      executors:
        - k8s-read-only
```

## Limites e trade-offs
Vincular uma `action` automatizada que executa comandos mutáveis (como `kubectl delete pod`) a um source de eventos amplo pode criar loops infinitos de deleção e recriação de Pods no cluster.

## Como verificar
Restrinja `actions` automatizadas a comandos puramente de diagnóstico somente leitura (`describe`, `logs`, `get`, `top`) e valide o template Go antes de ativar em produção.

## Conexões
- [[botkube-repositorios-plugins-index-extensoes-customizadas]] — Veja também: Botkube: Repositórios de Plugins (botkube e botkubeExtra) e Desenvolvimento de Plugins Customizados.
- [[botkube-slack-socket-mode-seguranca-sem-ingress-publico]] — Veja também: Botkube: Conexão Segura com Slack via Socket Mode sem Expor Webhook Público.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://docs.botkube.io/plugins/) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
