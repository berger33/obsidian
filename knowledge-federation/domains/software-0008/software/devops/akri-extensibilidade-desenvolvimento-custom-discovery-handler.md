---
id: software.devops.tranche17.001670
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
fontes: ["https://docs.akri.sh/architecture/architecture-overview", "https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md", "https://raw.githubusercontent.com/project-akri/akri/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Akri: desenvolvimento de Custom Discovery Handlers via contrato gRPC `discovery.proto`

## Em uma frase
A arquitetura extensível do Akri permite que qualquer engenheiro crie um *Custom Discovery Handler* para protocolos proprietários ou novos barramentos implementando os serviços `Registration` e `DiscoveryHandler` definidos em `discovery-utils/proto/discovery.proto`.

## Por que importa
Ambientes industriais, médicos ou agrícolas frequentemente usam sensores com protocolos seriais ou de rádio específicos (LoRaWAN, Zigbee, CAN bus, DICOM) que não fazem parte dos 4 handlers nativos do Akri.

## Como funciona
Na inicialização, o novo Discovery Handler conecta-se ao socket Unix do Akri Agent (`/var/lib/akri/agent-registration.sock`) e chama `RegisterDiscoveryHandler` informando seu nome, endpoint de socket e se os dispositivos descobertos são locais ou compartilhados (`shared`). Quando uma `Configuration` com aquele `discoveryHandler.name` é aplicada no cluster, o Agent abre um stream gRPC `Discover` passando `discoveryDetails` e recebe o fluxo contínuo de dispositivos encontrados.

## Exemplo
```protobuf
// Contrato central em discovery.proto do Akri:
service DiscoveryHandler {
  rpc Discover (DiscoverRequest) returns (stream DiscoverResponse);
}
```

## Limites e trade-offs
O nome informado no registro gRPC (`RegisterDiscoveryHandlerRequest.name`) deve coincidir exatamente com o campo `spec.discoveryHandler.name` declarado nos manifestos `Configuration`.

## Como verificar
Implante o DaemonSet do handler customizado montando `/var/lib/akri` via `hostPath` e verifique nos logs do `akri-agent` o evento de registro bem-sucedido do handler.

## Conexões
- [[akri-broker-jobs-vs-pods-processamento-batch-dispositivos-borda]] — Veja também: Akri: execução de `brokerJobSpec` vs `brokerPodSpec` para tarefas batch disparadas por dispositivos.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
