---
id: software.devops.tranche17.001637
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

# KubeEdge: invocação de serviços HTTP na borda a partir da nuvem via `Router` e `ServiceBus`

## Em uma frase
A combinação do módulo `Router` (no `CloudCore`) com o módulo `ServiceBus` (no `EdgeCore`) permite que componentes ou aplicações na nuvem façam requisições HTTP/REST diretas para servidores HTTP que rodam no nó de borda, atravessando o túnel existente do `CloudHub`/`EdgeHub`.

## Por que importa
Normalmente, um servidor HTTP legado ou webhook rodando dentro de uma fábrica sem IP público não pode receber chamadas REST iniciadas por um sistema central na nuvem.

## Como funciona
Com os CRDs `Rule` e `RuleEndpoint` (`rules.kubeedge.io/v1`, suportando endpoints `rest` e `eventbus`/`servicebus`), o administrador define uma rota lógica no `CloudCore`. Quando uma aplicação na nuvem faz uma chamada HTTP para o endpoint do `Router` do `CloudCore`, a mensagem é encapsulada pelo `CloudHub`, entregue ao `EdgeHub` do nó alvo e executada pelo cliente HTTP `ServiceBus` contra a porta local no nó de borda, retornando a resposta HTTP de volta para a nuvem.

## Exemplo
```yaml
apiVersion: rules.kubeedge.io/v1
kind: RuleEndpoint
metadata:
  name: cloud-rest-source
spec:
  ruleEndpointType: rest
---
apiVersion: rules.kubeedge.io/v1
kind: RuleEndpoint
metadata:
  name: edge-servicebus-target
spec:
  ruleEndpointType: servicebus
  properties:
    service_port: "8080"
```

## Limites e trade-offs
O `ServiceBus` vem desabilitado por padrão no arquivo `/etc/kubeedge/config/edgecore.yaml`; é necessário definir `modules.serviceBus.enable: true` no nó de borda antes de rotear chamadas HTTP para ele.

## Como verificar
Habilite `serviceBus` no `edgecore.yaml`, crie a `Rule` conectando os dois `RuleEndpoints` e faça um `curl` na porta REST do `CloudCore` para validar a resposta do serviço local da borda.

## Conexões
- [[kubeedge-eventbus-mqtt-mosquitto-integracao-mappers-iot]] — Veja também: KubeEdge: integração MQTT na borda via `EventBus` e arquitetura de *Device Mappers*.
- [[kubeedge-edgemesh-comunicacao-pod-a-pod-cross-subnet-logs-exec]] — Veja também: KubeEdge: `EdgeMesh` e `CloudStream`/`EdgeStream` para rede Pod-a-Pod entre bordas e `kubectl logs`/`exec`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
