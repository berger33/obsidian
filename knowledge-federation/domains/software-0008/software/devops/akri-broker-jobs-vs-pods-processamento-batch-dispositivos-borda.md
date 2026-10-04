---
id: software.devops.tranche17.001669
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

# Akri: execução de `brokerJobSpec` vs `brokerPodSpec` para tarefas batch disparadas por dispositivos

## Em uma frase
Além de implantar Daemons contínuos via `brokerPodSpec`, o CRD `Configuration` do Akri permite definir um `brokerJobSpec` (`batch/v1 JobSpec`) para disparar um `Job` Kubernetes finito sempre que um dispositivo folha é conectado.

## Por que importa
Nem todo dispositivo conectado na borda exige um servidor de streaming rodando 24x7: quando um operador de campo conecta um pendrive/cartão de dados USB ou um coletor móvel em um gateway, o objetivo é apenas executar um Job único de extração/calibração, fazer upload dos dados e encerrar.

## Como funciona
Ao preencher `spec.brokerJobSpec` em vez de `spec.brokerPodSpec` na `Configuration`, o Akri Controller cria um `Job` Kubernetes (com políticas de `backoffLimit` e `parallelism`) assim que a `Instance` do dispositivo é detectada pelo Agent.

## Exemplo
```yaml
apiVersion: akri.sh/v0
kind: Configuration
metadata:
  name: usb-calibration-job
spec:
  capacity: 1
  discoveryHandler:
    name: udev
    discoveryDetails: |
      udevRules:
        - 'SUBSYSTEM=="tty", ATTRS{idVendor}=="10c4"'
  brokerJobSpec:
    backoffLimit: 2
    template:
      spec:
        restartPolicy: OnFailure
        containers:
          - name: calibrator
            image: ghcr.io/org/calibrator:v1.0
            resources:
              limits:
                "{{PLACEHOLDER}}": "1"
```

## Limites e trade-offs
Em uma `Configuration`, os campos `brokerPodSpec` e `brokerJobSpec` são mutuamente exclusivos (cada `Configuration` gerencia ou Pods de longa duração ou Jobs finitos).

## Como verificar
Aplique uma `Configuration` com `brokerJobSpec` e verifique com `kubectl get jobs -l akri.sh/configuration=usb-calibration-job` o disparo automático do Job.

## Conexões
- [[akri-debug-echo-discovery-handler-simulacao-testes-ci]] — Veja também: Akri: simulação de dispositivos folha intermitentes em CI/CD com o handler `debugEcho`.
- [[akri-extensibilidade-desenvolvimento-custom-discovery-handler]] — Veja também: Akri: desenvolvimento de Custom Discovery Handlers via contrato gRPC `discovery.proto`.

## Fontes
- [Akri GitHub — README.md (CNCF Sandbox Kubernetes Resource Interface for the Edge, ONVIF, udev, OPC UA & Dynamic Leaf Device Discovery)](https://docs.akri.sh/architecture/architecture-overview) — README oficial do project-akri/akri (CNCF Sandbox) explicando a exposição dinâmica de dispositivos folha como recursos nativos de Kubernetes; consultado em 2026-10-03.
- [Akri Official Documentation — Architecture Overview (Configuration & Instance CRDs, Discovery Handlers, Akri Agent Device Plugin & Controller)](https://raw.githubusercontent.com/project-akri/akri-docs/main/docs/architecture/architecture-overview.md) — Visão geral oficial da arquitetura do Akri detalhando os 5 componentes, slots deviceUsage, brokerPodSpec/brokerJobSpec e injeção de brokerProperties; consultado em 2026-10-03.
- [Akri Documentation Repository — architecture-overview.md](https://raw.githubusercontent.com/project-akri/akri/main/README.md) — Fonte oficial em Markdown da documentação de arquitetura do projeto Akri; consultado em 2026-10-03.
