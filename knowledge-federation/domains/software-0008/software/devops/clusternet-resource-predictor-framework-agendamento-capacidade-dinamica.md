---
id: software.devops.tranche17.001617
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

# Clusternet: *Cluster Resource Predictor Framework* para agendamento dinâmico baseado em capacidade

## Em uma frase
Para suportar `schedulingStrategy: Dividing` com divisão dinâmica (`Dynamic`), o Clusternet implementa um *Resource Predictor Framework* extensível (`in-tree` e `out-of-tree`) que calcula quantas réplicas de um dado `PodSpec` cabem realmente em cada cluster filho.

## Por que importa
Simplesmente subtrair a soma de `requests` da capacidade bruta de todos os nós de um cluster filho superestima grosseiramente o número de réplicas agendáveis, pois ignora fragmentação por nó, `nodeSelector`, `affinity`, `taints` e topologias de zona.

## Como funciona
No modo `in-tree`, o `clusternet-agent` executa um preditor embutido dentro de cada cluster filho que simula o algoritmo de filtragem e pontuação do scheduler contra os nós locais e reporta ao `clusternet-scheduler` o máximo exato de réplicas suportadas por topologia. Também é possível conectar preditores `out-of-tree` externos para políticas customizadas.

## Exemplo
```yaml
apiVersion: apps.clusternet.io/v1alpha1
kind: Subscription
metadata:
  name: dynamic-capacity-sub
  namespace: default
spec:
  schedulingStrategy: Dividing
  dividingScheduling:
    type: Dynamic
    dynamicDividing:
      strategy: Spread
  subscribers:
    - clusterAffinity:
        matchLabels:
          tier: compute
  feeds:
    - apiVersion: apps/v1
      kind: Deployment
      name: batch-inference
      namespace: default
```

## Limites e trade-offs
Para que o agendamento dinâmico funcione com precisão, o `clusternet-agent` nos clusters filhos precisa estar com o servidor preditor habilitado e acessível pelo `clusternet-scheduler` (diretamente ou via túnel `clusternet-hub`).

## Como verificar
Inspecione o `FeedInventory` gerado (`kubectl get feedinventory batch-inference-sub -o yaml`) para ver os requisitos de recursos extraídos de cada réplica e a alocação calculada.

## Conexões
- [[clusternet-helm-charts-oci-registries-distribuicao-multi-cluster]] — Veja também: Clusternet: distribuição nativa de Helm Charts e artefatos OCI via CRD `HelmChart` e `HelmRelease`.
- [[clusternet-auto-descoberta-cluster-api-node-feature-discovery-labels]] — Veja também: Clusternet: auto-descoberta de clusters Cluster API (CAPI) e rotulagem automática via Node Feature Discovery.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
