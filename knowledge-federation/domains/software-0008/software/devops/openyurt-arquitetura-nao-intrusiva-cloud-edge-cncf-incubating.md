---
id: software.devops.tranche17.001641
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

# OpenYurt: arquitetura cloud-edge não intrusiva CNCF Incubating (`YurtHub`, `Yurt-Manager`, `Raven` e `YurtIoTDock`)

## Em uma frase
O OpenYurt (projeto CNCF Incubating, certificado até Kubernetes v1.34+) estende clusters Kubernetes upstream para cenários de computação de borda de forma 100% não intrusiva, preservando o `kubelet` original nos nós de borda e adicionando componentes modulares (`YurtHub`, `Yurt-Manager`, `Raven-Agent` e `YurtIoTDock`).

## Por que importa
Diferentemente de soluções que substituem o `kubelet` por um agente reescrito (o que pode introduzir incompatibilidades com novos recursos de CSI, CNI ou Device Plugins do Kubernetes upstream), o OpenYurt mantém os binários oficiais do Kubernetes intocados no nó de borda.

## Como funciona
No OpenYurt, os nós na nuvem recebem o label `openyurt.io/is-edge-worker: false` e os nós na borda recebem `openyurt.io/is-edge-worker: true`. O **YurtHub** roda como static pod em cada nó atuando como proxy/cache local para o `kube-apiserver`; o **Yurt-Manager** roda na nuvem executando os controladores e webhooks de borda; o **Raven-Agent** provê rede L3 e proxy reverso L7 entre regiões; e o **YurtIoTDock** integra dispositivos IoT via EdgeX Foundry.

## Exemplo
```bash
kubectl get nodes -L openyurt.io/is-edge-worker
kubectl get pods -n kube-system | grep -E "yurt|raven"
```

## Limites e trade-offs
Como o `Yurt-Manager` é implantado como um `Deployment` (tipicamente com 2 instâncias: líder e backup), recomenda-se alocá-lo nos nós na nuvem (`Cloud Nodes`) junto aos componentes do control plane do Kubernetes.

## Como verificar
Verifique nos nós de borda a presença do label `openyurt.io/is-edge-worker=true` e do Static Pod `yurt-hub` rodando em `kube-system`.

## Conexões
- [[openyurt-yurthub-proxy-local-cache-disco-autonomia-borda]] — Veja também: OpenYurt `YurtHub`: proxy sidecar de nó e cache em disco local para autonomia de borda em desconexões.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
