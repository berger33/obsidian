---
id: software.devops.tranche17.001614
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/clusternet/clusternet/main/README.md", "https://clusternet.io/docs/introduction/", "https://github.com/clusternet/clusternet"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clusternet: agendamento multi-cluster via CRD `Subscription` (`Replication`, `Static` e `Dynamic` Dividing)

## Em uma frase
O CRD `Subscription` (`apps.clusternet.io/v1alpha1`) vincula um conjunto de `feeds` (recursos Kubernetes, CRDs ou `HelmChart` inclusive em registries OCI) aos clusters filhos selecionados (`subscribers`), suportando as estratégias de agendamento `Replication` e `Dividing` (estática por peso ou dinâmica por capacidade).

## Por que importa
Permite declarar em um único manifesto quais aplicações e charts Helm compõem uma pilha e como suas réplicas devem ser replicadas ou fatiadas entre subgrupos de clusters.

## Como funciona
Quando uma `Subscription` é criada, o `clusternet-scheduler` avalia os seletores de cluster em `spec.subscribers`, calcula a distribuição de réplicas (consultando preditores `in-tree` ou `out-of-tree` no modo `Dynamic`) e gera um objeto `Base` no namespace dedicado de cada cluster filho selecionado, de onde os manifestos finais (`Description`) são sincronizados.

## Exemplo
```yaml
apiVersion: apps.clusternet.io/v1alpha1
kind: Subscription
metadata:
  name: web-stack-sub
  namespace: default
spec:
  schedulingStrategy: Replication
  subscribers:
    - clusterAffinity:
        matchLabels:
          clusters.clusternet.io/Nothing: ""
          env: prod
  feeds:
    - apiVersion: apps/v1
      kind: Deployment
      name: web-frontend
      namespace: default
```

## Limites e trade-offs
O Clusternet cria um namespace dedicado `clusternet-<id>` no cluster pai para cada cluster filho registrado, onde residem os objetos `Base` e `Description` específicos daquele destino.

## Como verificar
Inspecione `kubectl get subscription web-stack-sub -o yaml` e verifique em `status.bindingClusters` a lista de namespaces de clusters filhos vinculados pelo `clusternet-scheduler`.

## Conexões
- [[clusternet-sockets-websocket-tunnel-acesso-clusters-filhos-rbac]] — Veja também: Clusternet: túnel reverso WebSocket e visitação direta de clusters filhos com regras RBAC dinâmicas.
- [[clusternet-globalization-localization-overrides-duas-etapas-canary]] — Veja também: Clusternet: overrides em dois estágios (`Globalization` e `Localization`) com prioridades e rollback.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
