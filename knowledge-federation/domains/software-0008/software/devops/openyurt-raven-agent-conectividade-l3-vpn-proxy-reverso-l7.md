---
id: software.devops.tranche17.001645
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

# OpenYurt `Raven-Agent`: conectividade de rede L3 cross-region e proxy reverso L7 para `kubectl exec`/`logs`

## Em uma frase
O `Raven-Agent` (implantado como DaemonSet em todos os nós e coordenado pelo CRD `Gateway`) unifica a comunicação de plano de dados e de manutenção no OpenYurt, fornecendo túneis VPN de Camada 3 entre regiões físicas distintas e proxy reverso de Camada 7 (substituindo o antigo `Yurt-Tunnel`).

## Por que importa
Em cenários cloud-edge, os nós de borda estão em sub-redes locais privadas sem IP público exposto; por isso, nem os Pods da nuvem conseguem alcançar os IPs de Pods da borda (Camada 3), nem o `kube-apiserver` consegue conectar-se à porta `10250` do `kubelet` da borda para `kubectl logs`/`exec` (Camada 7).

## Como funciona
O OpenYurt agrupa os nós de cada domínio de rede física em um recurso `Gateway` (`raven.openyurt.io/v1beta1`). O `Raven-Agent` elege um nó gateway por região para estabelecer túneis VPN seguros (IPsec/WireGuard) entre os gateways de diferentes `NodePools`/nuvem (habilitando roteamento L3 nativo Pod-a-Pod) e túneis de proxy reverso L7 para encaminhar comandos `kubectl exec`, `logs` e coleta de métricas da nuvem até qualquer nó de borda.

## Exemplo
```yaml
apiVersion: raven.openyurt.io/v1beta1
kind: Gateway
metadata:
  name: gw-factory-sp
spec:
  nodeSelector:
    matchLabels:
      apps.openyurt.io/nodepool: factory-sp-pool
  exposeType: PublicIP
```

## Limites e trade-offs
Enquanto o `YurtHub` cuida do tráfego **borda -> nuvem** (para o `kube-apiserver`), o `Raven-Agent` cuida do tráfego **nuvem -> borda** e **borda -> borda** no plano de dados e de O&M.

## Como verificar
Inspecione `kubectl get gateways.raven.openyurt.io` e verifique os endpoints eleitos e o funcionamento de `kubectl logs <pod-na-borda>` a partir da nuvem.

## Conexões
- [[openyurt-yurtappset-yurtappdaemon-orquestracao-multi-pool-workloads]] — Veja também: OpenYurt: orquestração regional de cargas de trabalho com `YurtAppSet` e `YurtAppDaemon`.
- [[openyurt-yurtiotdock-edgex-foundry-platformadmin-crds-iot]] — Veja também: OpenYurt `YurtIoTDock`: fusão cloud-native com EdgeX Foundry via CRD `PlatformAdmin`.

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://openyurt.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
