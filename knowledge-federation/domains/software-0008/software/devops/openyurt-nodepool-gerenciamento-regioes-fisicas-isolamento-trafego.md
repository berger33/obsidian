---
id: software.devops.tranche17.001643
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
fontes: ["https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md", "https://openyurt.io/docs/core-concepts/architecture/", "https://github.com/openyurtio/openyurt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenYurt `NodePool`: agrupamento declarativo de nós por região física e fechamento de tráfego intra-pool

## Em uma frase
O OpenYurt introduz a abstração de `NodePool` (`apps.openyurt.io/v1beta1`) para agrupar nós de borda localizados na mesma região física, filial ou site de rede, aplicando governança de metadados e isolamento de tráfego de serviços no nível de pool.

## Por que importa
Em um cluster Kubernetes padrão, o `kube-proxy` balanceia requisições de um `Service` aleatoriamente entre todos os Pods do cluster inteiro; na borda, isso faria um Pod na fábrica de São Paulo chamar um Pod na fábrica de Manaus pela internet pública ou falhar por falta de rota direta entre sites.

## Como funciona
Cada `NodePool` agrega nós da mesma localidade e propaga automaticamente labels, annotations e taints definidos no pool para seus nós membros. Combinado com a filtragem de topologia de endpoints do `YurtHub`, o tráfego de `Services` consumido dentro de um `NodePool` permanece fechado (*closed-loop*) apenas entre os endpoints saudáveis daquele mesmo `NodePool`.

## Exemplo
```yaml
apiVersion: apps.openyurt.io/v1beta1
kind: NodePool
metadata:
  name: factory-sp-pool
spec:
  type: Edge
  labels:
    region.openyurt.io/site: sao-paulo
  taints:
    - key: edge.openyurt.io/dedicated
      value: factory
      effect: NoSchedule
```

## Limites e trade-offs
O campo `spec.type` de um `NodePool` (`Edge` ou `Cloud`) é imutável após a criação do pool; para migrar um nó para um `NodePool`, basta rotular o nó com `apps.openyurt.io/desired-nodepool=<nome-do-pool>`.

## Como verificar
Execute `kubectl get nodepools` para verificar a contagem de nós prontos (`READYNODES`), não prontos (`NOTREADYNODES`) e a propagação dos labels para os nós membros.

## Conexões
- [[openyurt-yurthub-proxy-local-cache-disco-autonomia-borda]] — Veja também: OpenYurt `YurtHub`: proxy sidecar de nó e cache em disco local para autonomia de borda em desconexões.
- [[openyurt-yurtappset-yurtappdaemon-orquestracao-multi-pool-workloads]] — Veja também: OpenYurt: orquestração regional de cargas de trabalho com `YurtAppSet` e `YurtAppDaemon`.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
