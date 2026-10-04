---
id: software.devops.tranche17.001619
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

# Clusternet: compatibilidade com *Kubernetes Version Skew* amplo e descoberta de serviços via `mcs-api`

## Em uma frase
O Clusternet foi projetado para suportar amplo desvio de versão (*Version Skew*) entre o cluster pai e os clusters filhos (gerenciando desde clusters legados v1.18+ até versões atuais >= v1.30), além de integrar descoberta de serviços multi-cluster baseada na especificação `mcs-api` (`ServiceExport` / `ServiceImport`).

## Por que importa
Na prática corporativa, é impossível atualizar simultaneamente centenas de clusters de borda (`k3s`), clusters on-premise e clusters gerenciados em nuvem pública para a mesma versão minor do Kubernetes.

## Como funciona
Por desacoplar o armazenamento dos manifestos (`Manifest` / `Description`) da versão interna da API do cluster pai e usar o túnel WebSocket do `clusternet-agent`, o plano de controle pode rodar em uma versão recente do Kubernetes enquanto coordena clusters filhos em versões distintas e em 6 arquiteturas (`linux/amd64`, `arm64`, `ppc64le`, `s390x`, `386`, `arm`).

## Exemplo
```yaml
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  name: payment-backend
  namespace: prod
```

## Limites e trade-offs
Para clusters rodando Kubernetes `>= v1.30`, utilize Clusternet `v0.18.x` ou superior conforme a matriz oficial de compatibilidade do projeto.

## Como verificar
Verifique a coluna `KUBERNETES VERSION` em `kubectl get managedclusters -A` para auditar a frota heterogênea de versões gerenciadas pelo mesmo `clusternet-hub`.

## Conexões
- [[clusternet-auto-descoberta-cluster-api-node-feature-discovery-labels]] — Veja também: Clusternet: auto-descoberta de clusters Cluster API (CAPI) e rotulagem automática via Node Feature Discovery.
- [[clusternet-client-go-wrapper-kubectl-plugin-integracao-programatica]] — Veja também: Clusternet: integração programática com `client-go` wrapper e operação via plugin `kubectl-clusternet`.

## Fontes
- [Clusternet GitHub — README.md (Managing Kubernetes Clusters as Easily as Visiting the Internet, Hub/Agent/Scheduler Architecture)](https://raw.githubusercontent.com/clusternet/clusternet/main/README.md) — README oficial do clusternet/clusternet detalhando descoberta automática, conexão Dual Sockets, coordenação multi-cluster e roteamento multi-estágio; consultado em 2026-10-03.
- [Clusternet Official Documentation — Introduction (Cluster Registration, App Delivery via Subscription/Localization/Globalization & Shadow APIs)](https://clusternet.io/docs/introduction/) — Introdução oficial do Clusternet cobrindo registro de clusters, entrega de aplicações multi-cluster, Localization, Globalization e APIs shadow; consultado em 2026-10-03.
- [Clusternet — Official GitHub Repository](https://github.com/clusternet/clusternet) — Repositório oficial Apache-2.0 do Clusternet; consultado em 2026-10-03.
