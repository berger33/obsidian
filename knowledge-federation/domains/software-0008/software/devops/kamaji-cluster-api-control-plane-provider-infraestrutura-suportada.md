---
id: software.devops.tranche15.001477
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
fontes: ["https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md", "https://kamaji.clastix.io/reference/api/", "https://raw.githubusercontent.com/clastix/kamaji/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kamaji: provedor de Control Plane para Cluster API (CAPI) e matriz de provedores de infraestrutura

## Em uma frase
O `cluster-api-control-plane-provider-kamaji` integra o Kamaji ao ecossistema Cluster API (`controlplane.cluster.x-k8s.io/v1alpha1`), unindo planos de controle em Pods com o provisionamento declarativo de máquinas de trabalho em 14 provedores de infraestrutura.

## Por que importa
O Kamaji foca exclusivamente no Control Plane; ao combiná-lo com o Cluster API, a plataforma provisiona automaticamente tanto o control plane em Pods quanto os worker nodes em AWS, Azure, vSphere, OpenStack, Metal3, KubeVirt, Proxmox, Hetzner, Nutanix ou Tinkerbell.

## Como funciona
O administrador instala o Cluster API com `clusterctl`, instala o Kamaji via Helm e aplica os recursos `Cluster`, `KamajiControlPlane` e `MachineDeployment` (ou `KamajiControlPlaneTemplate` para `ClusterClass`), delegando ao provedor CAPI a junção automática dos nós ao endpoint do `TenantControlPlane`.

## Exemplo
```bash
kubectl get clusters,kamajicontrolplanes,machinedeployments -A
```

## Limites e trade-offs
A partir de julho de 2024 (e da versão `v0.12.0` do provedor CAPI), a organização Clastix Labs passou a publicar artefatos comunitários no modelo de *edge releases* em vez de pinning fixo de versões estáveis, recomendando alinhamento cuidadoso de versões em produção.

## Como verificar
Verifique a prontidão conjunta do `Cluster` e do `KamajiControlPlane` com `clusterctl describe cluster <nome>`.

## Conexões
- [[kamaji-gestao-automatica-certificados-kubeadm-rotacao-autohealing]] — Veja também: Kamaji: ciclo de vida automatizado de certificados X.509 (`kubeadm`), rotação e auto-healing de estado.
- [[kamaji-datastore-overrides-separacao-eventos-etcd-escalabilidade]] — Veja também: Kamaji: separação de recursos de alto volume com `dataStoreOverrides` no `TenantControlPlane`.

## Fontes
- [Kamaji GitHub — README.md (Hosted Control Planes in Pods, TenantControlPlane & Datastore CRDs, Konnectivity, Auto-Healing & Use Cases)](https://raw.githubusercontent.com/clastix/cluster-api-control-plane-provider-kamaji/master/README.md) — README oficial do clastix/kamaji explicando a arquitetura de planos de controle em Pods, provisionamento em 16s, upgrades Blue/Green em 10s e multi-tenancy de Datastore; consultado em 2026-10-03.
- [Kamaji Official Documentation — API Reference (KamajiControlPlane, TenantControlPlane, Datastore, Addons & DataStoreOverrides)](https://kamaji.clastix.io/reference/api/) — Referência oficial da API do Kamaji especificando os campos de KamajiControlPlane, TenantControlPlane, addons (coreDNS, kubeProxy, konnectivity) e dataStoreOverrides; consultado em 2026-10-03.
- [Kamaji Cluster API Control Plane Provider — Official README.md](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do provedor Cluster API do Kamaji listando os 14 provedores de infraestrutura suportados; consultado em 2026-10-03.
