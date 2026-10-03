---
id: software.devops.tranche17.001661
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

# Akri: arquitetura CNCF Sandbox em Rust para descoberta e exposição de dispositivos folha (*Leaf Devices*) no Kubernetes

## Em uma frase
O Akri (projeto CNCF Sandbox, escrito em Rust) expõe dispositivos folha heterogêneos — como câmeras IP ONVIF, sensores USB via `udev`, controladores industriais OPC UA e GPUs/FPGAs — como recursos nativos de um cluster Kubernetes, detectando dinamicamente o aparecimento e desaparecimento desses dispositivos e agendando Pods *brokers* automaticamente.

## Por que importa
Dispositivos folha na borda (microcontroladores, sensores USB, câmeras RTSP) são pequenos demais para rodar o Kubernetes por conta própria, e o *Device Plugin Framework* original do Kubernetes foi desenhado para hardware estático de servidor (como GPUs em data center), não para periféricos intermitentes ou compartilhados na rede.

## Como funciona
A arquitetura do Akri resume-se no lema *"you name it, Akri finds it, you use it"* e é formada por 5 componentes: dois CRDs (`Configuration` e `Instance`), **Discovery Handlers** (que varrem protocolos de rede ou barramentos locais), o **Akri Agent** (DaemonSet que implementa o Kubernetes Device Plugin para anunciar os recursos encontrados ao `kubelet`) e o **Akri Controller** (que cria e remove automaticamente os Pods *brokers* e `Services` para cada dispositivo descoberto).

## Exemplo
```bash
helm repo add akri-helm-charts https://project-akri.github.io/akri/
helm install akri akri-helm-charts/akri --set udev.discovery.enabled=true
kubectl get pods -o wide
```

## Limites e trade-offs
O código do Akri requer Kubernetes compatível e é testado continuamente contra distribuições leves de borda como K3s, MicroK8s e Kubernetes upstream.

## Como verificar
Após instalar via Helm, verifique que o `akri-controller-deployment`, o `akri-agent-daemonset` e os Pods de Discovery Handler habilitados estão `Running`.

## Conexões
- [[akri-crd-configuration-brokerpodspec-capacity-servicespecs]] — Veja também: Akri CRD `Configuration`: definição de protocolo de descoberta, `capacity`, `brokerPodSpec` e `Services` automáticos.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://docs.akri.sh/architecture/architecture-overview) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
