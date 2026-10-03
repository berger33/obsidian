---
id: software.devops.tranche17.001631
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

# KubeEdge: arquitetura CNCF Graduated de computação de borda (`CloudCore` na nuvem e `EdgeCore` na borda)

## Em uma frase
O KubeEdge (projeto CNCF Graduated, escrito em Go) estende a orquestração nativa de containers e o gerenciamento declarativo de dispositivos IoT do Kubernetes para nós na borda (*Edge*) submetidos a redes instáveis, alta latência e recursos de hardware restritos.

## Por que importa
O `kubelet` padrão do Kubernetes assume conectividade contínua e de baixa latência com o `kube-apiserver` central, além de não possuir abstração nativa para protocolos industriais e de sensores IoT (como MQTT, Modbus ou Bluetooth).

## Como funciona
O KubeEdge divide-se em duas partes consolidadas: **Cloud Part (`CloudCore`)** — contendo `CloudHub`, `EdgeController` e `DeviceController` — e **Edge Part (`EdgeCore`)** — um agente leve em binário único contendo `EdgeHub`, `Edged`, `MetaManager`, `DeviceTwin`, `EventBus` e `ServiceBus` acompanhado de um banco local SQLite para autonomia offline completa.

## Exemplo
```bash
keadm version
kubectl get nodes -o wide
kubectl get pods -n kubeedge
```

## Limites e trade-offs
Ao contrário de um worker node Kubernetes tradicional, um nó de borda gerenciado pelo `EdgeCore` não executa o binário `kubelet` completo separado: o módulo `Edged` embutido no `EdgeCore` assume o gerenciamento de ciclo de vida dos Pods e containers via CRI.

## Como verificar
Verifique com `kubectl get nodes` que os nós de borda aparecem registrados com a role `agent,edge` e status `Ready` após o bootstrap com `keadm`.

## Conexões
- [[kubeedge-cloudhub-edgehub-websocket-quic-channelq-mensageria]] — Veja também: KubeEdge: comunicação bidirecional resiliente entre `CloudHub` e `EdgeHub` via WebSocket e QUIC.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
