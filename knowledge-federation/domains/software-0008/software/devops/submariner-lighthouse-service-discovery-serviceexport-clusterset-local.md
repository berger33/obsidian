---
id: software.devops.tranche14.001315
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
fontes: ["https://submariner.io/getting-started/architecture/", "https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md", "https://github.com/submariner-io/submariner"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Submariner: Descoberta de Serviços Multi-Cluster (Lighthouse, ServiceExport, ServiceImport e clusterset.local)

## Em uma frase
O componente **Lighthouse** implementa a especificação **Kubernetes Multi-Cluster Services (MCS — KEP-1645)** no Submariner, permitindo exportar seletivamente um `Service` via CRD `ServiceExport` para torná-lo acessível em todo o `ClusterSet` pelo domínio DNS `<service>.<ns>.svc.clusterset.local`.

## Por que importa
Compartilhar automaticamente 100% dos Services internos de todos os clusters causaria colisões indesejadas e exporia serviços que deveriam permanecer privados ao seu cluster de origem.

## Como funciona
Quando o usuário cria um `ServiceExport` (manualmente ou via `subctl export service`), o Lighthouse cria e sincroniza objetos `ServiceImport` através do Broker para todos os clusters do `ClusterSet`. Se múltiplos clusters exportarem um `Service` com o mesmo nome e no mesmo namespace (mesma identidade lógica de namespace no `ClusterSet`), o Lighthouse os agrega em um único serviço lógico multi-cluster.

## Exemplo
```bash
subctl export service --namespace default backend-api
kubectl get serviceexport -n default
kubectl get serviceimport -A
```

## Limites e trade-offs
Tentar resolver `<service>.<ns>.svc.clusterset.local` antes de criar o `ServiceExport` no mesmo namespace do `Service` de origem retorna `NXDOMAIN`, pois a exportação é estritamente opt-in.

## Como verificar
Use `subctl export service -n <ns> <nome>` e verifique a propagação com `kubectl get serviceimport -A` e `dig <service>.<ns>.svc.clusterset.local`.

## Conexões
- [[submariner-broker-sincronizacao-crds-endpoint-clusterset]] — Veja também: Submariner: O Papel do Broker na Troca de Metadados (Endpoints e ServiceImports) entre Clusters.
- [[submariner-headless-services-statefulsets-dns-pod-clusterid]] — Veja também: Submariner: Resolução DNS de Headless Services por Pod e cluster-id no ClusterSet.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://submariner.io/getting-started/architecture/) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
