---
id: software.devops.tranche17.001628
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
fontes: ["https://docs.liqo.io/en/stable/examples/quick-start.html", "https://raw.githubusercontent.com/liqotech/liqo/master/README.md", "https://github.com/liqotech/liqo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liqo: sincronização de Custom Resources entre clusters via `liqo-crd-replicator` e modos de peering

## Em uma frase
O componente `liqo-crd-replicator` gerencia a replicação bidirecional dos Custom Resources internos de negociação e rede do Liqo entre clusters emparelhados, suportando conectividade de controle *in-band* (pelo próprio túnel da Network Fabric) e *out-of-band*.

## Por que importa
Em topologias onde dois clusters estão em redes privadas distintas e a única rota mútua passa pelo gateway de rede do Liqo, o plano de controle também precisa trafegar de forma segura por dentro do túnel estabelecido.

## Como funciona
Durante o peering, o `liqo-crd-replicator` observa recursos de coordenação no namespace de tenant dedicado ao cluster par e os espelha no `kube-apiserver` remoto usando as credenciais de escopo restrito negociadas na fase de autenticação.

## Exemplo
```bash
kubectl get pods -n liqo -l app.kubernetes.io/name=crd-replicator
kubectl logs -n liqo -l app.kubernetes.io/name=crd-replicator --tail=30
```

## Limites e trade-offs
Se as políticas de rede (`NetworkPolicy`) administrativas bloquearem a saída do `liqo-crd-replicator` para o endpoint do `kube-apiserver` remoto (no modo out-of-band) ou para o gateway (no modo in-band), a renovação de estado do peering ficará estagnada.

## Como verificar
Verifique em `liqoctl info` o status de saúde do peering ativo e a ausência de erros de sincronização nos logs do `liqo-crd-replicator`.

## Conexões
- [[liqo-storage-fabric-virtual-storageclass-data-gravity-stateful]] — Veja também: Liqo: *Storage Fabric* e `StorageClass` virtual (`liqo`) para aplicações stateful com gravidade de dados.
- [[liqo-compatibilidade-multi-cloud-eks-gke-aks-openshift-k3s]] — Veja também: Liqo: operação multi-cloud heterogênea entre AWS EKS, Google GKE, Azure AKS, OpenShift e K3s.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://docs.liqo.io/en/stable/examples/quick-start.html) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
