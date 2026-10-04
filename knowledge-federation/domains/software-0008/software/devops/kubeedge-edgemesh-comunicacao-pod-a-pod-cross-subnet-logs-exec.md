---
id: software.devops.tranche17.001638
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
fontes: ["https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md", "https://kubeedge.io/docs/architecture/cloud/cloudhub/", "https://github.com/kubeedge/kubeedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# KubeEdge: `EdgeMesh` e `CloudStream`/`EdgeStream` para rede Pod-a-Pod entre bordas e `kubectl logs`/`exec`

## Em uma frase
Para habilitar `kubectl logs`, `kubectl exec`, `kubectl metrics` e comunicação direta entre Pods situados em sub-redes de borda distintas (LAN-to-LAN ou Edge-to-Cloud), o ecossistema KubeEdge utiliza os módulos `CloudStream`/`EdgeStream` e o add-on `EdgeMesh`.

## Por que importa
Como o `EdgeCore` substitui a comunicação direta do `kubelet` e os nós de borda estão em redes privadas isoladas atrás de NAT, o `kube-apiserver` não consegue discar diretamente a porta `10250` do nó de borda para buscar logs de containers.

## Como funciona
Os módulos `CloudStream` (no `CloudCore`) e `EdgeStream` (no `EdgeCore`) estabelecem um túnel dedicado para streaming de sessões do `kube-apiserver` (`logs`, `exec`, `attach`, `metrics-server`). Complementarmente, o `EdgeMesh` atua como plano de dados service mesh leve na borda, usando libp2p, relay e hole punching para permitir que um Pod no Nó de Borda A chame um `Service` Kubernetes cujos Pods estão no Nó de Borda B ou na nuvem.

## Exemplo
```bash
kubectl logs -n default edge-sensor-pod
kubectl exec -it -n default edge-sensor-pod -- sh
```

## Limites e trade-offs
Para que `kubectl logs` e `kubectl exec` funcionem em nós de borda, as chaves `cloudStream.enable: true` (em `cloudcore.yaml`) e `edgeStream.enable: true` (em `edgecore.yaml`) devem estar ativadas e os certificados de túnel configurados.

## Como verificar
Execute `kubectl logs` em um Pod agendado em um nó `edge` e confirme o retorno imediato do stdout do container através do túnel `CloudStream`/`EdgeStream`.

## Conexões
- [[kubeedge-servicebus-router-invocacao-http-rest-nuvem-para-borda]] — Veja também: KubeEdge: invocação de serviços HTTP na borda a partir da nuvem via `Router` e `ServiceBus`.
- [[kubeedge-keadm-bootstrap-cloudcore-init-edgecore-join-token]] — Veja também: KubeEdge: provisionamento de plano de controle e nós de borda com o instalador `keadm`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
