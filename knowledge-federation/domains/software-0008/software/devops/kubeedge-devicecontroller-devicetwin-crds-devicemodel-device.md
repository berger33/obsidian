---
id: software.devops.tranche17.001635
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

# KubeEdge: gerenciamento nativo de dispositivos IoT com `DeviceController`, `DeviceTwin` e CRDs `DeviceModel`/`Device`

## Em uma frase
O KubeEdge gerencia sensores e atuadores físicos por meio de Custom Resource Definitions nativas do Kubernetes (`DeviceModel` e `Device` em `devices.kubeedge.io`), sincronizando o estado desejado (*desired state*) e o estado reportado (*reported state*) entre o `DeviceController` na nuvem e o `DeviceTwin` na borda.

## Por que importa
Dispositivos de chão de fábrica (sensores de temperatura, PLCs, válvulas, câmeras) não executam containers; representá-los como CRDs Kubernetes permite aplicar GitOps, RBAC e observabilidade unificada tanto às aplicações quanto ao hardware físico.

## Como funciona
O `DeviceModel` define o esquema reutilizável de propriedades de um tipo de hardware (ex.: `temperature-sensor` com propriedade `temperature` do tipo `int`/`double` e modo `ReadOnly`). O `Device` instancia um sensor físico vinculado a um nó de borda específico (`nodeSelector`). O `DeviceController` sincroniza alterações do `spec` (desired) para o módulo `DeviceTwin` no `EdgeCore`, que armazena o estado no SQLite e publica de volta no `status` (reported) do CRD na nuvem.

## Exemplo
```yaml
apiVersion: devices.kubeedge.io/v1beta1
kind: DeviceModel
metadata:
  name: industrial-thermostat-model
  namespace: default
spec:
  properties:
    - name: target-temp-celsius
      description: "Setpoint de temperatura em graus Celsius"
      type:
        int:
          accessMode: ReadWrite
          defaultValue: 22
```

## Limites e trade-offs
Se o dispositivo físico estiver temporariamente desconectado do nó de borda ou o nó estiver offline da nuvem, o `DeviceTwin` preserva a última intenção (`expected`) no SQLite local e reconcilia o delta assim que a comunicação é restabelecida.

## Como verificar
Crie um `DeviceModel` e um `Device` correspondente e execute `kubectl get device <nome> -o yaml` para inspecionar a sincronização entre os valores desejados e reportados.

## Conexões
- [[kubeedge-edgecontroller-sincronizacao-pods-nodes-configmaps-secrets]] — Veja também: KubeEdge: sincronização bidirecional de metadados Kubernetes pelo `EdgeController`.
- [[kubeedge-eventbus-mqtt-mosquitto-integracao-mappers-iot]] — Veja também: KubeEdge: integração MQTT na borda via `EventBus` e arquitetura de *Device Mappers*.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
