---
id: software.devops.tranche15.001473
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

# Kamaji: desacoplamento e multi-tenancy do `Datastore` com etcd ou Kine (PostgreSQL, MySQL e NATS)

## Em uma frase
A API cluster-scoped `Datastore` do Kamaji desacopla o armazenamento de estado do plano de controle, permitindo que múltiplos `TenantControlPlanes` compartilhem o mesmo banco subjacente (`etcd`, ou PostgreSQL, MySQL e NATS via `kine`).

## Por que importa
No modelo tradicional, cada cluster exige seu próprio cluster `etcd` de 3 ou 5 nós com consenso Raft; ao consolidar dezenas de control planes sobre um único `Datastore` multi-tenant isolado por prefixo de chave ou schema SQL, elimina-se o principal gargalo operacional do Kubernetes em escala.

## Como funciona
O recurso `TenantControlPlane` referencia o banco via `dataStoreName`, podendo customizar `dataStoreSchema` (nome do banco SQL ou prefixo de chave no etcd), `dataStoreUsername` (imutável após a criação) e até `dataStoreOverrides` para armazenar recursos específicos de alto volume (como `events`) em um datastore separado.

## Exemplo
```bash
kubectl get datastores.kamaji.clastix.io
kubectl describe datastore default
```

## Limites e trade-offs
A documentação da API alerta que o campo `dataStoreUsername` é imutável e que o Kamaji não valida automaticamente colisões caso o usuário defina manualmente o mesmo `dataStoreUsername` em dois `TenantControlPlanes` diferentes; quando omitido, o Kamaji gera um nome único concatenando namespace e nome do recurso.

## Como verificar
Verifique os schemas e conexões ativas no `Datastore` com `kubectl get datastore -o yaml`.

## Conexões
- [[kamaji-crd-tenantcontrolplane-replicas-network-kubelet-version]] — Veja também: Kamaji: especificação do CRD `TenantControlPlane` (`version`, `replicas`, `network` e `kubelet`).
- [[kamaji-addons-gerenciados-coredns-kubeproxy-konnectivity]] — Veja também: Kamaji: gerenciamento automático e auto-healing dos addons `coreDNS`, `kubeProxy` e `konnectivity`.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://kamaji.clastix.io/reference/api/) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
