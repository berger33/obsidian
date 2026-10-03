---
id: software.devops.tranche19.001823
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
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio: alocação de EventProcessors em dois níveis (`Blocking Allocator` vs `Non-blocking Allocator`) para modos Sync e Async

## Em uma frase
No pipeline interno do Function Processor do Nuclio, cada evento atravessa dois níveis de abstração `EventProcessor` (primeiro no nível do **Trigger** e depois no nível do **Runtime**), gerenciados por um **Blocking Allocator** (para processamento síncrono FIFO) ou por um **Non-blocking Allocator** (para processamento assíncrono concorrente).

## Por que importa
Enquanto handlers síncronos tradicionais processam 1 evento por vez por worker (bloqueando o worker até o retorno), handlers assíncronos modernos (como `async def` em `asyncio` do Python) permitem que um único worker processe dezenas de eventos concorrentemente enquanto aguarda I/O externo.

## Como funciona
No modo **Synchronous** (padrão), o Nuclio usa um *Blocking Pool Allocator* no nível do trigger que garante que cada worker processe apenas 1 evento por vez em ordem FIFO. Já no modo **Asynchronous**, o nível do trigger usa um *Singleton Non-blocking Allocator* (permitindo alocar múltiplos eventos simultaneamente ao mesmo worker), enquanto o nível de conexão/runtime garante o isolamento de cada chamada.

## Exemplo
```yaml
# Trecho de function.yaml configurando múltiplos workers no trigger HTTP:
spec:
  runtime: python:3.11
  handler: main:handler
  triggers:
    myHttpTrigger:
      kind: http
      numWorkers: 8
```

## Limites e trade-offs
Mesmo no fluxo assíncrono (*async processing flow*), o Nuclio utiliza *Blocking Allocator* para a alocação de conexões individuais no nível de runtime a fim de preservar a integridade de protocolo.

## Como verificar
Ajuste `numWorkers` no trigger da função e monitore a utilização de workers pelas métricas Prometheus expostas pelo processor.

## Conexões
- [[nuclio-function-processor-event-listeners-runtimes-native-shmem-shell]] — Veja também: Nuclio Function Processor: arquitetura interna de Event Listeners e motores de Runtime (`Native`, `SHMEM` e `Shell`).
- [[nuclio-auth-proxy-sidecar-reverse-proxy-auth-only-dlx-scale-zero]] — Veja também: Nuclio no Kubernetes: autenticação de funções com `auth-proxy` sidecar (`reverse-proxy` vs `auth-only` no DLX).

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
