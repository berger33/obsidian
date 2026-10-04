---
id: software.devops.tranche17.001666
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

# Akri Controller: orquestração automática de Broker Pods, Services por instância e Services por configuração

## Em uma frase
O `Akri Controller` observa continuamente as mudanças nos CRDs `Instance` e `Nodes` para criar ou remover os Pods *brokers* (ou `Jobs`) e provisionar dois níveis de `Service` Kubernetes: um `Service` dedicado para cada dispositivo individual (`instanceServiceSpec`) e um `Service` global para todos os dispositivos daquela configuração (`configurationServiceSpec`).

## Por que importa
Uma aplicação de monitoramento de vídeo pode querer tanto acessar o stream de uma câmera específica (Câmera #3 do corredor norte) quanto agregar os quadros de todas as câmeras descobertas na loja através de um único endpoint de balanceamento.

## Como funciona
Quando uma `Instance` aparece, o Akri Controller agenda até `Configuration.capacity` broker Pods solicitando o recurso estendido daquela instância e cria o Service individual `<instance-name>-svc` (selecionando apenas os brokers daquela câmera) e o Service agregado `<configuration-name>-svc` (selecionando todos os brokers de todas as câmeras daquela `Configuration`).

## Exemplo
```bash
kubectl get pods,svc -l akri.sh/configuration=akri-udev-video
```

## Limites e trade-offs
Se um nó que estava hospedando o broker Pod de um dispositivo de rede compartilhado (`shared: true`, como uma câmera IP ONVIF com `capacity: 1`) ficar `NotReady` ou falhar, o Akri Controller limpa o slot em `deviceUsage` da `Instance` e agenda imediatamente um novo broker Pod em outro nó saudável que enxergue a mesma câmera.

## Como verificar
Liste os Services gerados com `kubectl get svc -l akri.sh/configuration` e confirme a presença tanto do serviço agregado da configuração quanto dos serviços individuais por `Instance`.

## Conexões
- [[akri-discovery-handlers-onvif-udev-opcua-debug-echo-grpc]] — Veja também: Akri Discovery Handlers: descoberta de dispositivos por protocolo (`ONVIF`, `udev`, `OPC UA` e `debugEcho`) via `discovery.proto`.
- [[akri-alta-disponibilidade-compartilhamento-dispositivos-rede-capacity]] — Veja também: Akri: compartilhamento multi-nó e alta disponibilidade de dispositivos de rede com `spec.capacity`.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
