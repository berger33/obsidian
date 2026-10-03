---
id: software.devops.tranche17.001618
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

# Clusternet: auto-descoberta de clusters Cluster API (CAPI) e rotulagem automática via Node Feature Discovery

## Em uma frase
O Clusternet integra-se nativamente com o Kubernetes Cluster API (`cluster-api`) para descobrir e registrar automaticamente novos clusters provisionados, além de propagar características de hardware descobertas pelo Node Feature Discovery (NFD) para os labels do `ManagedCluster`.

## Por que importa
Em plataformas elásticas onde clusters de clientes ou filiais são criados sob demanda via Cluster API e possuem hardwares variados (GPUs, AVX-512, SR-IOV, arquiteturas `arm64`/`ppc64le`/`s390x`), registrar e rotular cada cluster manualmente atrasa o agendamento de cargas especializadas.

## Como funciona
O `clusternet-controller-manager` observa objetos do Cluster API para automatizar o bootstrap, enquanto o `clusternet-agent` agrega os labels de nós (incluindo os prefixos gerados pelo `node-feature-discovery`, versão do Kubernetes e plataforma de SO/arquitetura) e os publica automaticamente no objeto `ManagedCluster` do cluster pai, permitindo que `Subscriptions` filtrem clusters por `clusterAffinity` de hardware.

## Exemplo
```bash
kubectl get managedclusters -A --show-labels
```

## Limites e trade-offs
O próprio cluster pai (*parent cluster*) também pode registrar a si mesmo como um cluster filho executando o `clusternet-agent` localmente, permitindo que receba workloads agendados pelas mesmas `Subscriptions`.

## Como verificar
Execute `kubectl get managedclusters -A --show-labels` e confirme a presença automática dos labels de plataforma, arquitetura (`beta.kubernetes.io/arch`, `kubernetes.io/os`) e versão do Kubernetes.

## Conexões
- [[clusternet-resource-predictor-framework-agendamento-capacidade-dinamica]] — Veja também: Clusternet: *Cluster Resource Predictor Framework* para agendamento dinâmico baseado em capacidade.
- [[clusternet-tolerancia-version-skew-multi-arquitetura-mcs-api]] — Veja também: Clusternet: compatibilidade com *Kubernetes Version Skew* amplo e descoberta de serviços via `mcs-api`.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
