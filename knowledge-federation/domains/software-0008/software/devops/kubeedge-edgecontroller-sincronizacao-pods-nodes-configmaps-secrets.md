---
id: software.devops.tranche17.001634
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

# KubeEdge: sincronização bidirecional de metadados Kubernetes pelo `EdgeController`

## Em uma frase
O `EdgeController` (parte do `CloudCore`) é o controlador Kubernetes estendido que faz a ponte entre o `kube-apiserver` central e os nós de borda, roteando eventos de Pods, ConfigMaps, Secrets, Endpoints e Nodes especificamente para o `nodeID` de destino via `CloudHub`.

## Por que importa
Se cada um dos 5.000 nós de borda abrisse `Watch` lists globais diretamente contra o `kube-apiserver` para todos os recursos do cluster, a banda WAN seria saturada e o `kube-apiserver` sofreria sobrecarga de memória.

## Como funciona
O `EdgeController` divide-se em *Upstream Controller* (que recebe relatórios de status de nós e Pods vindos do `EdgeHub`/`CloudHub` e atualiza o `kube-apiserver`) e *Downstream Controller* (que observa o `kube-apiserver`, filtra apenas os objetos vinculados a cada nó de borda específico e envia os deltas enxutos pelo canal daquele nó no `CloudHub`).

## Exemplo
```bash
kubectl get pods -A --field-selector spec.nodeName=edge-node-01
kubectl describe node edge-node-01
```

## Limites e trade-offs
Diferentemente de nós de nuvem comuns, os Pods enviados a nós do KubeEdge não montam por padrão o token de `ServiceAccount` para falar diretamente com o `kube-apiserver` remoto, a menos que o recurso de proxy de API na borda (`metaServer` no `EdgeCore`) esteja habilitado.

## Como verificar
Agende um Pod com `nodeName: edge-node-01` montando um `ConfigMap`, atualize uma chave do `ConfigMap` na nuvem e verifique a propagação seletiva para o nó `edge-node-01`.

## Conexões
- [[kubeedge-metamanager-sqlite-autonomia-offline-edged-recuperacao]] — Veja também: KubeEdge: autonomia de borda offline e recuperação pós-reboot via `MetaManager`, SQLite e `Edged`.
- [[kubeedge-devicecontroller-devicetwin-crds-devicemodel-device]] — Veja também: KubeEdge: gerenciamento nativo de dispositivos IoT com `DeviceController`, `DeviceTwin` e CRDs `DeviceModel`/`Device`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
