---
id: software.devops.tranche14.001321
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://headlamp.dev/docs/latest/installation/in-cluster/", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Arquitetura da Interface Web Kubernetes Extensível (SIG UI) In-Cluster e Desktop

## Em uma frase
O **Headlamp** (`kubernetes-sigs/headlamp`, projeto sob o **Kubernetes SIG UI** e CNCF Sandbox) é uma interface gráfica web e desktop moderna, agnóstica de fornecedor e extensível por plugins para visualização e operação de clusters Kubernetes.

## Por que importa
Dashboards Kubernetes antigos frequentemente sofrem com falta de suporte multi-cluster nativo, controles de tela que não refletem as permissões reais de RBAC do usuário logado ou ausência de extensibilidade para CRDs modernas.

## Como funciona
O Headlamp pode ser executado de duas formas: **in-cluster** (implantado via Helm chart `headlamp/headlamp` ou manifesto YAML e exposto por Ingress/port-forward) ou localmente como **aplicação Desktop** (Linux, macOS e Windows) que lê diretamente os arquivos `kubeconfig` da máquina do usuário.

## Exemplo
```bash
helm repo add headlamp https://kubernetes-sigs.github.io/headlamp/
helm install my-headlamp headlamp/headlamp --namespace kube-system
kubectl port-forward -n kube-system service/my-headlamp 8080:80
```

## Limites e trade-offs
Expor o serviço do Headlamp em um Ingress público sem configurar TLS ou usando um ServiceAccount com `cluster-admin` compartilhado compromete a segurança do cluster.

## Como verificar
Exponha o Headlamp exclusivamente sob HTTPS e autentique cada operador individualmente via OIDC ou token de ServiceAccount com RBAC mínimo.

## Conexões
- [[headlamp-rbac-ui-dinamica-serviceaccount-tokens-permissoes]] — Veja também: Headlamp: Controles de UI Orientados por RBAC e Acesso via ServiceAccount Tokens.

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://headlamp.dev/docs/latest/installation/in-cluster/) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
