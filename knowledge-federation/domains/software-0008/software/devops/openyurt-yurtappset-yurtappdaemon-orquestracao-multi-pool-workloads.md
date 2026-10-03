---
id: software.devops.tranche17.001644
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

# OpenYurt: orquestração regional de cargas de trabalho com `YurtAppSet` e `YurtAppDaemon`

## Em uma frase
Dentro do `Yurt-Manager`, os controladores `YurtAppSet` e `YurtAppDaemon` (`apps.openyurt.io`) automatizam a criação e customização de `Deployments` ou `StatefulSets` independentes para cada `NodePool` a partir de um único template central.

## Por que importa
Se uma empresa possui 200 lojas (`NodePools`), manter manualmente 200 objetos `Deployment` separados para a mesma aplicação de caixa registradora — cada um com seu `nodeSelector`, contagem de réplicas e imagem — é operacionalmente inviável.

## Como funciona
O `YurtAppSet` recebe um `workloadTemplate` (`DeploymentTemplate` ou `StatefulSetTemplate`) e uma lista de `pools` (com réplicas e patches específicos por pool), enquanto o `YurtAppDaemon` observa dinamicamente os `NodePools` que casam com um `nodepoolSelector` e provisiona automaticamente um workload dedicado sempre que uma nova filial (`NodePool`) é adicionada ao cluster.

## Exemplo
```yaml
apiVersion: apps.openyurt.io/v1alpha1
kind: YurtAppSet
metadata:
  name: pos-terminal-app
  namespace: default
spec:
  selector:
    matchLabels:
      app: pos-terminal
  workloadTemplate:
    deploymentTemplate:
      metadata:
        labels:
          app: pos-terminal
      spec:
        template:
          metadata:
            labels:
              app: pos-terminal
          spec:
            containers:
              - name: pos
                image: ghcr.io/org/pos:v1.4
  topology:
    pools:
      - name: factory-sp-pool
        replicas: 3
```

## Limites e trade-offs
Como cada `NodePool` recebe seu próprio `Deployment` filho gerenciado pelo `YurtAppSet`, a falha de nós em uma filial jamais faz o `ReplicaSet` tentar recriar os Pods daquela filial dentro de outra filial distante.

## Como verificar
Crie o `YurtAppSet` acima e execute `kubectl get deploy -l app=pos-terminal` para confirmar a criação automática do Deployment específico para `factory-sp-pool`.

## Conexões
- [[openyurt-nodepool-gerenciamento-regioes-fisicas-isolamento-trafego]] — Veja também: OpenYurt `NodePool`: agrupamento declarativo de nós por região física e fechamento de tráfego intra-pool.
- [[openyurt-raven-agent-conectividade-l3-vpn-proxy-reverso-l7]] — Veja também: OpenYurt `Raven-Agent`: conectividade de rede L3 cross-region e proxy reverso L7 para `kubectl exec`/`logs`.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
