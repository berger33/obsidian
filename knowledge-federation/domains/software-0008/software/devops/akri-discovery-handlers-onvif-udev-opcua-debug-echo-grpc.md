---
id: software.devops.tranche17.001665
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
fontes: ["https://raw.githubusercontent.com/project-akri/akri/main/README.md", "https://docs.akri.sh/architecture/architecture-overview", "https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Akri Discovery Handlers: descoberta de dispositivos por protocolo (`ONVIF`, `udev`, `OPC UA` e `debugEcho`) via `discovery.proto`

## Em uma frase
Os *Discovery Handlers* do Akri são componentes modulares que implementam o serviço gRPC `DiscoveryHandler` definido em `discovery.proto`, registrando-se no serviço `Registration` do Akri Agent para varrer a rede ou o host em busca de dispositivos.

## Por que importa
Como existem dezenas de protocolos industriais e de IoT (ONVIF para câmeras IP, `udev` para dispositivos locais Linux, OPC UA para automação industrial, Bluetooth, CoAP), embutir todos os SDKs dentro do binário do Agent tornaria o agente pesado e difícil de estender.

## Como funciona
O Akri fornece nativamente handlers para **ONVIF** (descoberta WS-Discovery de câmeras IP na sub-rede), **udev** (consulta de regras udev no sistema de arquivos Linux local), **OPC UA** (descoberta de servidores e certificados industriais) e **debugEcho** (simulador de dispositivos para testes em qualquer cluster sem hardware físico). Novos handlers podem ser escritos em qualquer linguagem que fale gRPC implementando `discovery.proto`.

## Exemplo
```bash
helm upgrade akri akri-helm-charts/akri \
  --set onvif.discovery.enabled=true \
  --set opcua.discovery.enabled=true
kubectl get pods -l akri.sh/discoveryHandlerName
```

## Limites e trade-offs
Os Discovery Handlers podem rodar como DaemonSets separados (comunicando-se com o Agent via Unix domain socket em `/var/lib/akri`) ou embutidos no próprio container do Agent quando compilado com as features correspondentes.

## Como verificar
Inspecione os logs do Pod do Discovery Handler (`kubectl logs -l akri.sh/discoveryHandlerName=udev`) para auditar as varreduras e os dispositivos reportados ao Agent.

## Conexões
- [[akri-agent-kubernetes-device-plugin-injecao-broker-properties-env]] — Veja também: Akri Agent: implementação dinâmica de Kubernetes Device Plugin e injeção de `brokerProperties` no container.
- [[akri-controller-reconciliacao-broker-pods-instance-configuration-services]] — Veja também: Akri Controller: orquestração automática de Broker Pods, Services por instância e Services por configuração.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://docs.akri.sh/architecture/architecture-overview) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
