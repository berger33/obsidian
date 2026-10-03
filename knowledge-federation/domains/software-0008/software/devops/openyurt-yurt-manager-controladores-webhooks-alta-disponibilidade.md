---
id: software.devops.tranche17.001649
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
fontes: ["https://openyurt.io/docs/core-concepts/architecture/", "https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md", "https://github.com/openyurtio/openyurt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenYurt `Yurt-Manager`: consolidação de controladores e webhooks cloud-edge em alta disponibilidade

## Em uma frase
O `Yurt-Manager` consolida em um único binário e `Deployment` (normalmente com 2 réplicas em esquema líder/backup nos nós de nuvem) todos os controladores de ciclo de vida e admission webhooks do OpenYurt (`NodePool`, `YurtAppSet`, `YurtAppDaemon`, `YurtStaticSet`, `PlatformAdmin`, `Gateway`, `PodBinding`).

## Por que importa
Nas versões iniciais de arquiteturas de borda, rodar meia dúzia de deployments separados para cada controlador customizado aumentava o consumo de memória na nuvem e multiplicava as conexões de `Watch` e certificados de webhook.

## Como funciona
No OpenYurt v1.7+, o `Yurt-Manager` centraliza a liderança (`leader election`) e o servidor de webhooks, coordenando desde a governança de `NodePools` e upgrades de Static Pods (`YurtStaticSet` para atualizar o próprio `YurtHub` nos nós de borda) até a topologia de rede do `Raven`.

## Exemplo
```bash
kubectl get deploy yurt-manager -n kube-system
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations | grep yurt
```

## Limites e trade-offs
Como o `Yurt-Manager` hospeda webhooks de validação e mutação para recursos do cluster, nunca o escale para `0` nem o agende em nós de borda com link WAN instável; mantenha sempre `nodeSelector` / `affinity` restrito aos nós de nuvem (`openyurt.io/is-edge-worker: false`).

## Como verificar
Verifique com `kubectl get pods -n kube-system -l app.kubernetes.io/name=yurt-manager -o wide` que ambas as réplicas estão alocadas em nós de nuvem e com probes de saúde aprovadas.

## Conexões
- [[openyurt-node-resource-manager-lvm-quotapath-pmem-armazenamento-borda]] — Veja também: OpenYurt `Node Resource Manager`: gerenciamento de armazenamento local de borda (LVM, QuotaPath e PMEM).
- [[openyurt-conversao-cluster-kubernetes-instalacao-control-plane-join-nodes]] — Veja também: OpenYurt: instalação de componentes de control plane e ingresso de nós de borda (`yurtadm join`).

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://openyurt.io/docs/core-concepts/architecture/) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
