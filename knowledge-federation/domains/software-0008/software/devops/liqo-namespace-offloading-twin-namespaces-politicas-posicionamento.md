---
id: software.devops.tranche17.001623
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

# Liqo: *Namespace Offloading* (`liqoctl offload namespace`), namespaces gêmeos e estratégias de mapeamento

## Em uma frase
No Liqo, o offloading de cargas de trabalho é habilitado por namespace (`liqoctl offload namespace <ns>` ou CRD `NamespaceOffloading`), criando automaticamente um namespace gêmeo (*remote twin namespace*) nos clusters provedores selecionados.

## Por que importa
Se todos os namespaces do cluster consumidor fossem exportados indiscriminadamente para os clusters remotos, namespaces de sistema (`kube-system`) ou cargas sensíveis com restrições regulatórias poderiam vazar para infraestruturas externas.

## Como funciona
Ao habilitar o offloading em um namespace, o usuário configura: 1) `podOffloadingStrategy` (`LocalAndRemote` padrão, `Remote` apenas nos clusters remotos, ou `Local`); 2) `namespaceMappingStrategy` (`EnforceSameName` ou `DefaultName` que adiciona um sufixo com o ID do cluster consumidor para evitar colisões no provedor); e 3) `clusterSelector` para filtrar quais clusters remotos podem hospedar recursos daquele namespace.

## Exemplo
```bash
liqoctl offload namespace demo-app \
  --namespace-mapping-strategy EnforceSameName \
  --pod-offloading-strategy LocalAndRemote
kubectl get namespaceoffloadings -n demo-app
```

## Limites e trade-offs
A estratégia `EnforceSameName` facilita a inspeção humana e políticas que dependem do nome exato do namespace, mas falhará se o cluster provedor já possuir um namespace local com aquele mesmo nome.

## Como verificar
Crie um namespace `demo-app`, execute `liqoctl offload namespace demo-app` e confirme no cluster remoto (`--kubeconfig "$KUBECONFIG_MILAN"`) que o namespace gêmeo foi provisionado automaticamente.

## Conexões
- [[liqo-liqoctl-peer-autenticacao-negociacao-recursos-foreigncluster]] — Veja também: Liqo: estabelecimento de peering entre clusters com `liqoctl peer` e representação `ForeignCluster`.
- [[liqo-pod-offloading-virtual-kubelet-reflexao-status-logs-exec]] — Veja também: Liqo: offloading transparente de Pods via Virtual Kubelet e suporte nativo a `kubectl logs` e `exec`.

## Fontes
- [Liqo GitHub — README.md (Dynamic and Seamless Kubernetes Multi-Cluster Topologies, Peering, Offloading, Network & Storage Fabric)](https://docs.liqo.io/en/stable/examples/quick-start.html) — README oficial do liqotech/liqo detalhando peering P2P, Virtual Nodes via Virtual Kubelet, Network Fabric com NATless/NATting IPAM, reflexão de Services e Storage Fabric; consultado em 2026-10-03.
- [Liqo Official Documentation — Quick Start & Examples (liqoctl peer, liqoctl offload namespace, Virtual Node Scheduling & Service Exposure)](https://raw.githubusercontent.com/liqotech/liqo/master/README.md) — Guia oficial Quick Start do Liqo demonstrando peering entre clusters, extensão de namespaces com liqoctl offload e agendamento transparente de Pods remotos; consultado em 2026-10-03.
- [Liqo — Official GitHub Repository](https://github.com/liqotech/liqo) — Repositório oficial Apache-2.0 do Liqo; consultado em 2026-10-03.
