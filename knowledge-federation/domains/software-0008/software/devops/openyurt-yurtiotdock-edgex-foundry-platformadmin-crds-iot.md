---
id: software.devops.tranche17.001646
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

# OpenYurt `YurtIoTDock`: fusão cloud-native com EdgeX Foundry via CRD `PlatformAdmin`

## Em uma frase
O `YurtIoTDock` (evolução integrada do antigo `YurtDeviceController` no repositório principal do OpenYurt) implanta uma instância por `NodePool` de borda para fazer a ponte bidirecional entre a plataforma de IoT industrial **EdgeX Foundry** e CRDs nativos do Kubernetes (`Device`, `DeviceService`, `DeviceProfile`).

## Por que importa
O EdgeX Foundry é um padrão industrial consolidado para aquisição de dados de sensores OT (Modbus, BACnet, OPC-UA, MQTT), mas opera tradicionalmente como microsserviços isolados em cada site sem visibilidade nem controle declarativo na API do Kubernetes.

## Como funciona
Por meio do Custom Resource `PlatformAdmin` (`iot.openyurt.io`), o operador provisiona automaticamente a pilha do EdgeX Foundry e o `YurtIoTDock` no `NodePool` de borda. Assim que sobe, o `YurtIoTDock` sincroniza continuamente os dispositivos registrados no EdgeX local com os CRDs `Device`, `DeviceService` e `DeviceProfile` no Kubernetes, permitindo gerenciar dispositivos IoT via `kubectl` e GitOps.

## Exemplo
```yaml
apiVersion: iot.openyurt.io/v1alpha2
kind: PlatformAdmin
metadata:
  name: edgex-factory-sp
  namespace: default
spec:
  version: Minnesota
  poolName: factory-sp-pool
```

## Limites e trade-offs
Desde a integração no repositório principal do OpenYurt, não é mais necessário instalar um `yurt-device-controller` separado fora do OpenYurt; o ciclo de vida é orquestrado diretamente via `PlatformAdmin` e `Yurt-Manager`.

## Como verificar
Aplique o manifesto `PlatformAdmin` para um `NodePool` e verifique a criação automática dos recursos `devices.iot.openyurt.io` e `deviceservices.iot.openyurt.io` sincronizados.

## Conexões
- [[openyurt-raven-agent-conectividade-l3-vpn-proxy-reverso-l7]] — Veja também: OpenYurt `Raven-Agent`: conectividade de rede L3 cross-region e proxy reverso L7 para `kubectl exec`/`logs`.
- [[openyurt-autonomia-no-prevencao-eviccao-pods-desconexao-wan]] — Veja também: OpenYurt: prevenção de evicção indevida de Pods durante desconexão nuvem-borda (`node-autonomy`).

## Fontes
- [OpenYurt GitHub — README.md (CNCF Incubating Extending Native Kubernetes to Edge, Non-Intrusive Architecture & Edge Autonomy)](https://openyurt.io/docs/core-concepts/architecture/) — README oficial do openyurtio/openyurt (CNCF Incubating) apresentando a filosofia não intrusiva, autonomia de borda, NodePool e operação cloud-edge; consultado em 2026-10-03.
- [OpenYurt Official Documentation — Core Concepts: Architecture (YurtHub Local Cache, Yurt-Tunnel Reverse Proxy, Yurt-Manager & Raven)](https://raw.githubusercontent.com/openyurtio/openyurt/master/README.md) — Documentação oficial de arquitetura do OpenYurt detalhando YurtHub, Yurt-Tunnel-Server/Agent, controladores do Yurt-Manager e topologia por NodePool; consultado em 2026-10-03.
- [OpenYurt — Official GitHub Repository](https://github.com/openyurtio/openyurt) — Repositório oficial Apache-2.0 do OpenYurt na CNCF; consultado em 2026-10-03.
