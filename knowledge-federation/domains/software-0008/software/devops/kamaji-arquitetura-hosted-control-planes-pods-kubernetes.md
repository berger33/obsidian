---
id: software.devops.tranche15.001471
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/clastix/kamaji/master/README.md", "https://kamaji.clastix.io/reference/api/", "https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Clastix Kamaji: gerenciamento de Hosted Control Planes Kubernetes rodando como Pods

## Em uma frase
O Kamaji (mantido pela Clastix sob licença Apache-2.0) é um gerenciador de Control Planes Kubernetes baseado no paradigma de *Hosted Control Plane*, executando os componentes do plano de controle dos clusters tenants como Pods regulares dentro de um cluster de gerenciamento.

## Por que importa
Provisionar três máquinas virtuais dedicadas para o control plane de cada cluster Kubernetes de cliente ou equipe gera enorme desperdício de hardware e sobrecarga operacional; ao rodar `kube-apiserver`, `kube-controller-manager` e `kube-scheduler` como Pods, o Kamaji provisiona um novo control plane em cerca de 16 segundos e reduz o consumo de hardware em até 60%.

## Como funciona
O Kamaji estende a API do Kubernetes com dois recursos principais: o `TenantControlPlane` (abreviado como `tcp`, escopo de namespace, que define o estado desejado stateless do control plane) e o `Datastore` (escopo de cluster, que armazena o estado de um ou mais clusters tenants).

## Exemplo
```bash
kubectl get tenantcontrolplanes -A
kubectl get datastores
```

## Limites e trade-offs
O Kamaji não é uma distribuição Kubernetes modificada: todos os clusters criados utilizam binários upstream oficiais (`registry.k8s.io`), resultando em clusters 100% compatíveis com a certificação de conformidade da CNCF.

## Como verificar
Execute `kubectl get tcp -A` no cluster de gerenciamento para inspecionar a versão, o endpoint e o status dos planos de controle hospedados.

## Conexões
- [[kamaji-crd-tenantcontrolplane-replicas-network-kubelet-version]] — Veja também: Kamaji: especificação do CRD `TenantControlPlane` (`version`, `replicas`, `network` e `kubelet`).

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
