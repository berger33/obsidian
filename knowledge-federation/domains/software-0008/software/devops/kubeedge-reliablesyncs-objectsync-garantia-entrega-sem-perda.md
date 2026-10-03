---
id: software.devops.tranche17.001640
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

# KubeEdge: entrega confiável de mensagens sem perda sobre redes instáveis via `ObjectSync` (`reliablesyncs`)

## Em uma frase
Para garantir que nenhuma atualização de estado seja perdida durante quedas intermitentes do link WAN entre nuvem e borda, o KubeEdge utiliza os CRDs `ObjectSync` e `ClusterObjectSync` (`reliablesyncs.kubeedge.io/v1alpha1`) gerenciados pelo `SyncController`.

## Por que importa
Se o controlador na nuvem simplesmente enviasse um evento "atualizar ConfigMap" pela rede no exato segundo em que a conexão celular do nó de borda oscilou, a mensagem se perderia e o nó de borda ficaria permanentemente defasado sem saber que perdeu uma revisão.

## Como funciona
Cada objeto sincronizado para um nó de borda tem seu `resourceVersion` confirmado rastreado em um recurso `ObjectSync`. O `EdgeHub` envia confirmações (`ACK`) após o `MetaManager` gravar a mudança no SQLite local; enquanto o `ObjectSync` mostrar divergência entre o `resourceVersion` atual no `etcd` da nuvem e o último `objectResourceVersion` confirmado pelo nó de borda, o `SyncController` reenvia a atualização de forma idempotente.

## Exemplo
```bash
kubectl get objectsyncs -A
kubectl get clusterobjectsyncs
```

## Limites e trade-offs
Objetos `ObjectSync` são gerenciados internamente pelos controladores do `CloudCore` para rastrear o cursor de sincronização de cada nó; apagá-los manualmente força uma ressincronização completa de metadados para o respectivo nó.

## Como verificar
Inspecione `kubectl get objectsyncs -n kubeedge -o yaml` e verifique que `status.objectResourceVersion` acompanha a revisão mais recente dos Pods e ConfigMaps alocados nos nós de borda.

## Conexões
- [[kubeedge-keadm-bootstrap-cloudcore-init-edgecore-join-token]] — Veja também: KubeEdge: provisionamento de plano de controle e nós de borda com o instalador `keadm`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
