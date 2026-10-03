---
id: software.devops.tranche19.001825
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio `nuctl` CLI e Builder Kaniko: construção segura de imagens de função in-cluster e deploy declarativo

## Em uma frase
A CLI **`nuctl`** (`nuctl build`, `nuctl deploy`, `nuctl invoke`, `nuctl get`) permite empacotar código-fonte e configurações (`function.yaml`) em imagens de container OCI e implantá-las no Kubernetes, integrando-se nativamente ao **Kaniko** para construir imagens dentro do cluster sem exigir daemon Docker privilegiado.

## Por que importa
Montar `/var/run/docker.sock` dentro de Pods de plataforma em um cluster Kubernetes de produção viola políticas de segurança e não funciona em nós baseados puramente em `containerd`.

## Como funciona
Quando o desenvolvedor executa `nuctl deploy` (ou cria uma `NuclioFunction` pela UI/API), o componente builder do Nuclio gera a imagem contendo o handler do usuário e o binário `processor` utilizando Kaniko, envia a imagem para o container registry configurado e o deployer reconcilia o `Deployment`, `Service`, `HPA` e `Ingress` no Kubernetes.

## Exemplo
```bash
nuctl deploy FraudDetector \
  --namespace nuclio \
  --path ./fraud_detector.py \
  --runtime python:3.11 \
  --handler fraud_detector:handler \
  --registry ghcr.io/org
nuctl invoke FraudDetector --namespace nuclio -m POST -b '{"tx_id": 42}'
```

## Limites e trade-offs
É possível separar a etapa de construção (`nuctl build`) da etapa de implantação (`nuctl deploy --run-image ...`) para construir a imagem uma única vez no pipeline de CI e promovê-la entre homologação e produção.

## Como verificar
Execute `nuctl get function --namespace nuclio` para verificar o estado `ready` e a porta HTTP atribuída à função.

## Conexões
- [[nuclio-auth-proxy-sidecar-reverse-proxy-auth-only-dlx-scale-zero]] — Veja também: Nuclio no Kubernetes: autenticação de funções com `auth-proxy` sidecar (`reverse-proxy` vs `auth-only` no DLX).
- [[nuclio-triggers-streaming-kafka-kinesis-rabbit-mqtt-cron-http]] — Veja também: Nuclio Triggers de Tempo Real: ingestão paralela de streams (`Kafka`, `Kinesis`, `RabbitMQ`, `MQTT`, `NATS`, `Cron` e `HTTP`).

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
