---
id: software.devops.tranche17.001647
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

# OpenYurt: prevenção de evicção indevida de Pods durante desconexão nuvem-borda (`node-autonomy`)

## Em uma frase
Quando um nó de borda marcado como autônomo perde a comunicação com a nuvem e seu status no `kube-apiserver` passa para `NotReady`/`Unknown`, os controladores do OpenYurt impedem que o plano de controle evicte e reagende os Pods daquele nó.

## Por que importa
No Kubernetes padrão, após `pod-eviction-timeout` (ou a toleration padrão de 300 segundos para `node.kubernetes.io/unreachable`), os Pods de um nó sem heartbeat são marcados para deleção/evicção. Na borda, o nó frequentemente continua ligado e processando dados localmente — apenas o link de internet caiu; evictar os Pods causaria disrupção assim que o link voltasse.

## Como funciona
Combinando o cache em disco local do `YurtHub` no nó com a lógica de autonomia de nó no `Yurt-Manager` (ativada pela anotação de autonomia no nó de borda), o plano de controle preserva os Pods vinculados ao nó desconectado enquanto o `kubelet` local continua mantendo os containers vivos.

## Exemplo
```bash
kubectl annotate node edge-worker-01 node.beta.openyurt.io/autonomy="true" --overwrite
kubectl get node edge-worker-01 -o jsonpath='{.metadata.annotations.node\.beta\.openyurt\.io/autonomy}'
```

## Limites e trade-offs
A anotação de autonomia impede a evicção motivada por perda de heartbeat de rede, mas o administrador deve estar ciente de que, se o servidor físico de borda realmente queimar de vez, os Pods daquele nó não serão migrados automaticamente para outros nós até intervenção ou política explícita.

## Como verificar
Anote o nó de borda com `node.beta.openyurt.io/autonomy="true"`, bloqueie temporariamente o tráfego para o `kube-apiserver` por mais de 6 minutos e confirme que os Pods permanecem `Running` sem serem evictados.

## Conexões
- [[openyurt-yurtiotdock-edgex-foundry-platformadmin-crds-iot]] — Veja também: OpenYurt `YurtIoTDock`: fusão cloud-native com EdgeX Foundry via CRD `PlatformAdmin`.
- [[openyurt-node-resource-manager-lvm-quotapath-pmem-armazenamento-borda]] — Veja também: OpenYurt `Node Resource Manager`: gerenciamento de armazenamento local de borda (LVM, QuotaPath e PMEM).

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://openyurt.io/docs/core-concepts/architecture/) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
