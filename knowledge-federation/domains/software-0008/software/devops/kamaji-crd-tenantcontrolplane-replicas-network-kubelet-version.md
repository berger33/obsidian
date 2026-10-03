---
id: software.devops.tranche15.001472
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
fontes: ["https://kamaji.clastix.io/reference/api/", "https://raw.githubusercontent.com/clastix/kamaji/master/README.md", "https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kamaji: especificação do CRD `TenantControlPlane` (`version`, `replicas`, `network` e `kubelet`)

## Em uma frase
O recurso `TenantControlPlane` (e seu equivalente `KamajiControlPlane` no Cluster API) declara de forma stateless todos os parâmetros do plano de controle de um cluster tenant, incluindo versão do Kubernetes, número de réplicas, tipo de exposição de rede e opções do Kubelet.

## Por que importa
Permite escalar horizontalmente o control plane (inclusive de zero a dezenas de réplicas durante picos de tráfego) e realizar upgrades de versão do Kubernetes em cerca de 10 segundos com estratégia Blue/Green sem servir versões mistas da API.

## Como funciona
No `spec` do recurso, o administrador define `version` (obrigatório), `replicas` (padrão `2`), `network` (padrão `serviceType: LoadBalancer`, suportando também `NodePort` ou `ClusterIP`), `registry` (padrão `registry.k8s.io`, customizável para ambientes air-gapped) e `kubelet` (padrão `cgroupfs: systemd` e `preferredAddressTypes: [InternalIP, ExternalIP, Hostname]`).

## Exemplo
```yaml
apiVersion: controlplane.cluster.x-k8s.io/v1alpha1
kind: KamajiControlPlane
metadata:
  name: tenant-prod-cp
  namespace: tenants
spec:
  version: v1.31.0
  replicas: 2
  dataStoreName: default
  network:
    serviceType: LoadBalancer
```

## Limites e trade-offs
Por padrão, no recurso `KamajiControlPlane`, a lista `admissionControllers` vem vazia se não for especificada; consulte os controladores de admissão recomendados para a versão desejada do Kubernetes (como `NodeRestriction`, `PodSecurity`, `ServiceAccount` e `ValidatingAdmissionWebhook`).

## Como verificar
Inspecione o Service e o Deployment gerados pelo Kamaji no namespace do tenant com `kubectl get deploy,svc -n tenants`.

## Conexões
- [[kamaji-arquitetura-hosted-control-planes-pods-kubernetes]] — Veja também: Clastix Kamaji: gerenciamento de Hosted Control Planes Kubernetes rodando como Pods.
- [[kamaji-datastore-multitenancy-etcd-kine-postgresql-mysql-nats]] — Veja também: Kamaji: desacoplamento e multi-tenancy do `Datastore` com etcd ou Kine (PostgreSQL, MySQL e NATS).

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://kamaji.clastix.io/reference/api/) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
