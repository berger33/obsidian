---
id: software.devops.tranche17.001662
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

# Akri CRD `Configuration`: definição de protocolo de descoberta, `capacity`, `brokerPodSpec` e `Services` automáticos

## Em uma frase
O Custom Resource `Configuration` (`akri.sh/v0`) é onde o operador declara qual tipo de dispositivo o Akri deve procurar (`discoveryHandler`), quantos nós podem utilizá-lo simultaneamente (`capacity`) e qual Pod (`brokerPodSpec`) e `Services` devem ser implantados automaticamente.

## Por que importa
Sem o `Configuration` do Akri, a cada nova câmera IP ou sensor USB conectado em campo o operador precisaria descobrir o endereço/caminho do dispositivo manualmente, escrever um manifesto de Pod dedicado com `nodeSelector` e criar um `Service` para expô-lo.

## Como funciona
Todo `Configuration` especifica: 1) `discoveryHandler` (ex.: `onvif`, `udev`, `opcua` e seus `discoveryDetails`); 2) `capacity` (número máximo de nós que podem agendar um broker para o mesmo dispositivo); 3) `brokerPodSpec` (o template do Pod que sabe falar com o dispositivo); 4) `instanceServiceSpec` (Service individual para cada dispositivo encontrado); e 5) `configurationServiceSpec` (Service agregado para todos os dispositivos daquela classe).

## Exemplo
```yaml
apiVersion: akri.sh/v0
kind: Configuration
metadata:
  name: akri-udev-video
spec:
  capacity: 1
  discoveryHandler:
    name: udev
    discoveryDetails: |
      udevRules:
        - 'KERNEL=="video[0-9]*"'
  brokerPodSpec:
    containers:
      - name: udev-video-broker
        image: ghcr.io/project-akri/akri/udev-video-broker:latest
        resources:
          limits:
            "{{PLACEHOLDER}}": "1"
```

## Limites e trade-offs
No `brokerPodSpec`, a string literal `"{{PLACEHOLDER}}"` dentro de `resources.limits` (e `requests`) é substituída automaticamente pelo Akri pelo nome do recurso estendido registrado no `kubelet` para aquele dispositivo.

## Como verificar
Aplique a `Configuration` com `kubectl apply -f` e execute `kubectl get akric` (atalho para Akri Configurations) para confirmar o registro.

## Conexões
- [[akri-arquitetura-leaf-devices-cncf-sandbox-rust-device-plugin]] — Veja também: Akri: arquitetura CNCF Sandbox em Rust para descoberta e exposição de dispositivos folha (*Leaf Devices*) no Kubernetes.
- [[akri-crd-instance-rastreamento-estado-compartilhamento-deviceusage]] — Veja também: Akri CRD `Instance`: representação de dispositivos individuais e coordenação de compartilhamento (`deviceUsage`).

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
