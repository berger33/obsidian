---
id: software.devops.tranche10.000980
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md", "https://www.vcluster.com/docs/vcluster/introduction/architecture/", "https://github.com/loft-sh/vcluster"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# vCluster: integrações nativas com a pilha do cluster hospedeiro (cert-manager, External Secrets, Istio, KubeVirt e Gateway API)

## Em uma frase
Nos modos Shared e Dedicated Nodes, o vCluster possui integrações nativas para sincronizar recursos de **cert-manager**, **External Secrets Operator (ESO)**, **KubeVirt**, **Istio**, **metrics-server** e **Gateway API** (`v0.36+`) com uma única instalação compartilhada no Control Plane Cluster.

## Por que importa
Se uma plataforma possui 50 Tenant Clusters rodando dentro de um único Control Plane Cluster, instalar 50 cópias separadas do `cert-manager`, 50 cópias do `external-secrets` e 50 controladores de Ingress/Gateway dentro de cada vCluster multiplicaria por 50 o consumo de memória RAM dos operadores de plataforma.

## Como funciona
Em vez de instalar o operador dentro de cada Tenant Cluster, o administrador instala o operador (como `cert-manager`, `external-secrets` ou o controlador de `Gateway API`) **apenas uma vez** no Control Plane Cluster e habilita a integração correspondente no `vcluster.yaml`. O syncer do vCluster copia a definição dos CRDs (`Certificate`, `Issuer`, `ExternalSecret`, `HTTPRoute`, `Gateway`) para dentro do Tenant Cluster: quando o desenvolvedor cria um `ExternalSecret` ou `Certificate` dentro do seu vCluster, o syncer o encaminha para o namespace hospedeiro, o operador global do Control Plane Cluster processa o recurso e gera o `Secret` nativo, e o syncer devolve o `Secret` pronto para dentro do vCluster!

## Exemplo
```yaml
# Exemplo de vcluster.yaml reutilizando o cert-manager e o External Secrets Operator instalados no cluster hospedeiro
integrations:
  certManager:
    enabled: true
  externalSecrets:
    enabled: true
  metricsServer:
    enabled: true
```

## Limites e trade-offs
Para que as integrações compartilhadas (`integrations.certManager`, `integrations.externalSecrets` ou sincronização de `Gateway API`) funcionem, os respectivos operadores e CRDs **já devem estar instalados no Control Plane Cluster** hospedeiro; se um tenant precisar de uma versão customizada incompatível do operador que não existe no host, ele ainda pode desativar a integração e instalar o operador diretamente dentro do seu próprio vCluster.

## Como verificar
Com `integrations.metricsServer.enabled: true` no `vcluster.yaml`, conecte-se ao vCluster e execute `kubectl top pods` e `kubectl top nodes` para confirmar o consumo das métricas a partir do `metrics-server` do cluster hospedeiro.

## Conexões
- [[vcluster-auto-nodes-karpenter-gpu-ai-factories-slurm-ray]] — Veja também: vCluster: Auto Nodes (Karpenter-powered), Node VPN e clusters especializados para IA (Inference, Ray, Run:ai e Slurm).
- [[vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura]] — Referência cruzada direta com vcluster-clusters-kubernetes-virtuais-multitenancy-arquitetura.
- [[vcluster-componente-syncer-sincronizacao-recursos-tohost-fromhost]] — Referência cruzada direta com vcluster-componente-syncer-sincronizacao-recursos-tohost-fromhost.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.

## Fontes
- [vCluster GitHub — README.md (CNCF Certified Kubernetes & AI Conformant, Architecture Comparison, vind, Auto Nodes, Snapshots & Sleep Mode)](https://raw.githubusercontent.com/loft-sh/vcluster/main/README.md) — README oficial do loft-sh/vcluster detalhando Tenant Clusters, comparação entre Shared/Dedicated/Private Nodes/Standalone, driver Docker vind, Auto Nodes (Karpenter), Node VPN, Snapshots e Sleep Mode; consultado em 2026-10-03.
- [vCluster Official Documentation — Architecture (v0.37 Control Plane, API Server, Data Store, Syncer, Virtual Scheduler & vind vs KinD)](https://www.vcluster.com/docs/vcluster/introduction/architecture/) — Documentação oficial de arquitetura do vCluster (v0.37) explicando o processo unificado do control plane (API server, controller manager, datastore SQLite/etcd/SQL, syncer), virtual scheduler e tabela comparativa vind vs KinD; consultado em 2026-10-03.
- [Loft Labs vCluster — Official GitHub Repository](https://github.com/loft-sh/vcluster) — Repositório oficial do vCluster; consultado em 2026-10-03.
