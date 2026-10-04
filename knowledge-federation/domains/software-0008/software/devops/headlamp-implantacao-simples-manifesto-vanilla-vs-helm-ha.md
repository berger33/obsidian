---
id: software.devops.tranche14.001329
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
fontes: ["https://headlamp.dev/docs/latest/installation/in-cluster/", "https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Implantação Vanilla (kubernetes-headlamp.yaml) vs Alta Disponibilidade via Helm Chart

## Em uma frase
O projeto Headlamp mantém tanto um manifesto simplificado (`kubernetes-headlamp.yaml`) para testes rápidos em qualquer cluster quanto um Helm chart oficial completo (`charts/headlamp`) com suporte a múltiplas réplicas (`replicaCount`), afinidade de nós, `securityContext` e gerenciamento de plugins.

## Por que importa
Usar o manifesto estático `kubernetes-headlamp.yaml` em produção sem revisar réplicas, limites de recursos e configurações de Ingress/OIDC deixa apenas uma réplica básica rodando sem alta disponibilidade.

## Como funciona
Para ambientes de avaliação ou clusters locais (`kind`, `minikube`), aplica-se `kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/kubernetes-headlamp.yaml`; para produção, utiliza-se `helm install my-headlamp headlamp/headlamp --namespace kube-system -f values.yaml --set replicaCount=2`.

## Exemplo
```bash
helm upgrade --install my-headlamp headlamp/headlamp \
  --namespace kube-system \
  --set replicaCount=2 \
  --wait
kubectl -n kube-system rollout status deployment/my-headlamp
```

## Limites e trade-offs
Escalar `replicaCount: 2` ou mais usando um `PersistentVolumeClaim` `ReadWriteOnce` compartilhado entre os Pods para o diretório de plugins pode impedir o agendamento das réplicas em nós diferentes.

## Como verificar
Use um InitContainer/sidecar `pluginsManager` com `emptyDir` por Pod (ou storage `ReadWriteMany`) para que múltiplas réplicas do Headlamp rodem distribuídas entre diferentes worker nodes.

## Conexões
- [[headlamp-desenvolvimento-plugins-frontend-sdk-typescript-react]] — Veja também: Headlamp: Desenvolvimento de Plugins Customizados para Plataformas Internas (IDPs).
- [[headlamp-desktop-app-linux-macos-windows-kubeconfig-local]] — Veja também: Headlamp: Operação Segura como Aplicativo Desktop Local (Linux, macOS e Windows).

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://headlamp.dev/docs/latest/installation/in-cluster/) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
