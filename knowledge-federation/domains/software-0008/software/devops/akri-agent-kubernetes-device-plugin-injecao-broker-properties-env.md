---
id: software.devops.tranche17.001664
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

# Akri Agent: implementação dinâmica de Kubernetes Device Plugin e injeção de `brokerProperties` no container

## Em uma frase
O `Akri Agent` roda como DaemonSet em cada nó do cluster e implementa a interface gRPC de *Device Plugin* do Kubernetes dinamicamente para cada dispositivo folha descoberto, anunciando o recurso ao `kubelet` e injetando as variáveis de conexão (`brokerProperties`) nos containers agendados.

## Por que importa
Um container de aplicação genérico (`broker`) não sabe de antemão se a câmera USB foi montada em `/dev/video0` ou `/dev/video2`, nem qual é a URL RTSP da câmera IP recém-descoberta na rede.

## Como funciona
Ao receber um dispositivo de um Discovery Handler, o Akri Agent instancia um Device Plugin virtual para aquela `Instance` e registra-o no socket do `kubelet`. Quando o `kubelet` aloca o container do broker Pod para aquele recurso (`Allocate` RPC), o Agent instrui o `kubelet` a montar os device nodes necessários e a definir todas as entradas de `brokerProperties` (como `UDEV_DEVNODE=/dev/video0` ou `ONVIF_DEVICE_SERVICE_URL=...`) como variáveis de ambiente dentro do container.

## Exemplo
```bash
kubectl exec -it <broker-pod-name> -- env | grep -E "UDEV_|ONVIF_|OPCUA_"
```

## Limites e trade-offs
Se o dispositivo folha for desconectado (por exemplo, alguém puxar o cabo USB da câmera), o Akri Agent reporta imediatamente ao `kubelet` que o recurso ficou `Unhealthy` e remove/atualiza a `Instance`, fazendo o Akri Controller encerrar o broker Pod correspondente.

## Como verificar
Conecte um dispositivo (ou ative o handler `debugEcho`), aguarde o broker Pod subir e verifique com `kubectl exec ... -- env` as variáveis de ambiente injetadas pelo Akri Agent.

## Conexões
- [[akri-crd-instance-rastreamento-estado-compartilhamento-deviceusage]] — Veja também: Akri CRD `Instance`: representação de dispositivos individuais e coordenação de compartilhamento (`deviceUsage`).
- [[akri-discovery-handlers-onvif-udev-opcua-debug-echo-grpc]] — Veja também: Akri Discovery Handlers: descoberta de dispositivos por protocolo (`ONVIF`, `udev`, `OPC UA` e `debugEcho`) via `discovery.proto`.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
