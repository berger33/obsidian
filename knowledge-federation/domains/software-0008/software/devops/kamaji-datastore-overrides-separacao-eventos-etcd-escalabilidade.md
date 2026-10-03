---
id: software.devops.tranche15.001478
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

# Kamaji: separação de recursos de alto volume com `dataStoreOverrides` no `TenantControlPlane`

## Em uma frase
O campo `spec.dataStoreOverrides` do `KamajiControlPlane` / `TenantControlPlane` permite direcionar recursos específicos da API do Kubernetes (como `/events`) para um `Datastore` separado do banco principal do cluster.

## Por que importa
Em clusters Kubernetes sob forte carga ou falhas em cascata, tempestades de objetos `Event` geram intenso tráfego de escrita e compactação no `etcd`, degradando a latência de leitura/escrita de objetos críticos como `Pods`, `Secrets` e `Leases`.

## Como funciona
Ao configurar `dataStoreOverrides` mapeando o recurso `events` para um `Datastore` secundário dedicado, o Kamaji configura a flag `--etcd-servers-overrides` no `kube-apiserver` do tenant, isolando a pressão de I/O de eventos do estado principal do cluster.

## Exemplo
```yaml
spec:
  dataStoreName: primary-etcd
  dataStoreOverrides:
    - resource: "/events"
      dataStoreName: events-etcd
```

## Limites e trade-offs
Todos os `Datastores` referenciados em `dataStoreName` e em `dataStoreOverrides` devem utilizar drivers compatíveis e estar previamente saudáveis no cluster de gerenciamento.

## Como verificar
Inspecione os argumentos do Pod `kube-apiserver` do tenant e confirme a presença de `--etcd-servers-overrides` apontando para o datastore de eventos.

## Conexões
- [[kamaji-cluster-api-control-plane-provider-infraestrutura-suportada]] — Veja também: Kamaji: provedor de Control Plane para Cluster API (CAPI) e matriz de provedores de infraestrutura.
- [[kamaji-upgrades-blue-green-10s-scale-to-zero-otimizacao]] — Veja também: Kamaji: upgrades Blue/Green de versão Kubernetes em 10 segundos e escalonamento elástico de Control Planes.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://kamaji.clastix.io/reference/api/) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
