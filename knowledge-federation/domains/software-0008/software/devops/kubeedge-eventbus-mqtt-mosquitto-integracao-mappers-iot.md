---
id: software.devops.tranche17.001636
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

# KubeEdge: integração MQTT na borda via `EventBus` e arquitetura de *Device Mappers*

## Em uma frase
O módulo `EventBus` do `EdgeCore` atua como cliente MQTT local que se conecta a um broker MQTT no nó de borda (como Eclipse Mosquitto) para fornecer capacidades de publicação e assinatura (*pub/sub*) entre o `DeviceTwin` e os *Device Mappers* dos dispositivos IoT.

## Por que importa
Sensores industriais falam protocolos heterogêneos (MQTT, Modbus RTU/TCP, OPC-UA, Bluetooth, ONVIF); o `EdgeCore` mantém seu núcleo enxuto padronizando a troca de mensagens de telemetria e comando via tópicos MQTT bem definidos no `EventBus` ou gRPC via Mapper Framework.

## Como funciona
Quando um sensor publica sua telemetria em um tópico `$hw/events/device/<id>/twin/update` no broker MQTT local, o `EventBus` recebe a mensagem e a entrega ao `DeviceTwin`, que atualiza o SQLite local e sincroniza o estado com o `DeviceController` na nuvem. Inversamente, mudanças de configuração feitas via `kubectl patch device` na nuvem descem até o `DeviceTwin` e são publicadas pelo `EventBus` para o dispositivo.

## Exemplo
```bash
mosquitto_pub -h 127.0.0.1 -p 1883 \
  -t '$hw/events/device/thermostat-01/twin/update' \
  -m '{"event_id":"1","timestamp":1727950000,"twin":{"target-temp-celsius":{"actual":{"value":"24"}}}}'
```

## Limites e trade-offs
Em versões recentes do KubeEdge (`Mapper-Framework`), além do modo MQTT via `EventBus`, mappers customizados podem comunicar-se diretamente com o `EdgeCore` via sockets gRPC de baixa latência sem exigir um broker Mosquitto externo.

## Como verificar
Publique uma mensagem de teste no tópico `$hw/events/device/.../twin/update` no nó de borda e verifique que o campo `status.twins` do objeto `Device` no Kubernetes é atualizado na nuvem.

## Conexões
- [[kubeedge-devicecontroller-devicetwin-crds-devicemodel-device]] — Veja também: KubeEdge: gerenciamento nativo de dispositivos IoT com `DeviceController`, `DeviceTwin` e CRDs `DeviceModel`/`Device`.
- [[kubeedge-servicebus-router-invocacao-http-rest-nuvem-para-borda]] — Veja também: KubeEdge: invocação de serviços HTTP na borda a partir da nuvem via `Router` e `ServiceBus`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
