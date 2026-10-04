---
id: software.devops.tranche17.001611
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

# Clusternet: arquitetura CNCF Sandbox (`clusternet-hub`, `clusternet-agent`, `clusternet-scheduler` e `clusternet-controller-manager`)

## Em uma frase
O Clusternet (*Cluster Internet*, projeto CNCF Sandbox) é um add-on leve que permite gerenciar frotas de clusters Kubernetes (em nuvem pública, privada, híbrida ou na borda) e visitá-los através de túneis reversos WebSocket como se estivessem rodando localmente.

## Por que importa
Clusters Kubernetes em VPCs isoladas, ambientes on-premise ou estações de borda não possuem IPs públicos acessíveis pelo cluster central, e gerenciar credenciais e ferramentas distintas para cada cluster inviabiliza operações em larga escala.

## Como funciona
O Clusternet é composto por quatro binários: **`clusternet-agent`** (roda nos clusters filhos, auto-registra o cluster como `ManagedCluster`, envia heartbeats e mantém um túnel WebSocket full-duplex sobre uma única conexão TCP até o pai), **`clusternet-hub`** (roda no cluster pai como *Aggregated APIServer* servindo as Shadow APIs e o servidor WebSocket), **`clusternet-scheduler`** (agenda `Subscriptions` para clusters filhos) e **`clusternet-controller-manager`** (aprova registros, cria namespaces/RBAC dedicados e coordena entregas).

## Exemplo
```bash
kubectl get managedclusters -A
kubectl get pods -n clusternet-system
```

## Limites e trade-offs
Como o `clusternet-hub` opera como um *Aggregated APIServer* (AA), o `kube-apiserver` do cluster pai precisa ter conectividade de rede até o Service do `clusternet-hub` e, em Kubernetes v1.22.14+/v1.26+, exige a flag `--aggregator-reject-forwarding-redirect=false` no `kube-apiserver` pai.

## Como verificar
Verifique que o `APIService` `v1alpha1.shadow.clusternet.io` está com `AVAILABLE: True` executando `kubectl get apiservice | grep clusternet`.

## Conexões
- [[clusternet-shadow-apis-aggregated-apiserver-manifest-encapsulation]] — Veja também: Clusternet: *Shadow APIs* via Aggregated APIServer (`shadow/v1alpha1`) para captura transparente de recursos.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
